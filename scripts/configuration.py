"""Shared configuration validation. Reads no project files and executes no commands."""
import copy
import math
import re
import unicodedata

MIN_COOLDOWN = 5 * 60 * 60

SKILLS = {"grill-with-docs", "code-review", "delivery", "adhd-output", "unslop", "swarm", "loose-ends", "swarmstack"}
AUTHORITY = {"create_threads", "create_branches", "push_issue_branches", "open_prs", "merge_integration", "promote_production", "deploy"}


def local_path(value):
    return isinstance(value, str) and bool(value) and not value.startswith(("/", "\\")) and not re.match(r"^[A-Za-z]:", value) and ".." not in value.replace("\\", "/").split("/")


def validate(config, *, draft=False):
    if not isinstance(config, dict):
        raise ValueError("configuration must be an object")
    required = {"schema_version", "status", "name", "goal", "success", "github_repository", "primary_branch", "integration_branch", "requirements_path", "glossary_path", "test_environment", "commands", "models", "budget", "authority", "human_ux_acceptance_required", "skills"}
    if not required <= set(config) or set(config) - required - {"swarm", "model_policy"} or config.get("schema_version") != 1 or config.get("status") != ("draft" if draft else "confirmed"):
        raise ValueError("use the exact v1 configuration and confirm setup first")
    for field in ["name", "goal", "success", "github_repository", "primary_branch", "integration_branch", "test_environment"]:
        value = config[field]
        if not isinstance(value, str) or not value.strip() or any(x in value for x in (["\n", "\r"] if draft else ["REPLACE_", "SELECT_", "\n", "\r"])):
            raise ValueError("unresolved or invalid field: " + field)
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", config["github_repository"]):
        raise ValueError("github_repository must be owner/repository")
    if not all(local_path(config[f]) for f in ["requirements_path", "glossary_path"]):
        raise ValueError("requirements/glossary must use project-relative paths")
    if not isinstance(config["commands"], dict) or set(config["commands"]) != {"test", "lint", "typecheck", "build"}:
        raise ValueError("commands must name test/lint/typecheck/build, nullable when inapplicable")
    for name, command in config["commands"].items():
        if command is not None and (not isinstance(command, str) or not command.strip() or (not draft and "REPLACE_" in command)):
            raise ValueError("unresolved command: " + name)
    if not config["commands"]["test"]:
        raise ValueError("an actual test/check command is required")
    if not isinstance(config["authority"], dict) or set(config["authority"]) != AUTHORITY or not all(type(v) is bool for v in config["authority"].values()):
        raise ValueError("authority grants must be explicit booleans")
    if draft and any(config["authority"].values()):
        raise ValueError("draft installation grants no effects")
    if type(config["human_ux_acceptance_required"]) is not bool:
        raise ValueError("human acceptance policy must be explicit")
    budget = config["budget"]
    if not isinstance(budget, dict) or set(budget) != {"spend_limit_usd", "paid_overage", "allowed_data"}:
        raise ValueError("invalid budget fields")
    cost = budget["spend_limit_usd"]
    if type(cost) not in (int, float) or not math.isfinite(cost) or cost < 0 or type(budget["paid_overage"]) is not bool or not isinstance(budget["allowed_data"], str) or not budget["allowed_data"].strip():
        raise ValueError("invalid budget or data permission")
    if not isinstance(config["skills"], list) or not all(isinstance(s, str) for s in config["skills"]) or not config["skills"] or len(set(config["skills"])) != len(config["skills"]) or not set(config["skills"]) <= SKILLS:
        raise ValueError("select known unique skills")
    if not {"grill-with-docs", "code-review", "swarmstack", "delivery", "adhd-output", "unslop"} <= set(config["skills"]):
        raise ValueError("select the core skills, including swarmstack for project setup")
    if "swarm" in config or "swarm" in config["skills"]:
        validate_options(config.get("swarm", {}), draft=draft)
    if not isinstance(config["models"], dict) or set(config["models"]) != {"frontend", "backend", "review"}:
        raise ValueError("select frontend/backend/review models from the live host")
    if not all(valid_model(model, draft) for model in config["models"].values()):
        raise ValueError("model IDs and efforts must be resolved")
    if "model_policy" in config:
        validate_model_policy(config["model_policy"], config["models"], draft=draft)


def valid_model(model, draft):
    return isinstance(model, dict) and set(model) == {"provider", "model", "effort"} and all(isinstance(v, str) and v.strip() and (draft or "SELECT_" not in v) for v in model.values())


def policy_text(value, draft):
    """One short printable line with no control or bidi characters; placeholders only in a draft."""
    return isinstance(value, str) and bool(value.strip()) and len(value) <= 500 and all(unicodedata.category(c) not in {"Cc", "Cf", "Zl", "Zp"} for c in value) and (draft or not re.search(r"REPLACE_|SELECT_", value))


def model_key(text):
    return re.sub(r"[\s_]+", "-", text.strip().lower())


def validate_model_policy(policy, models, *, draft=False):
    """Optional role, child-tier, verification and prohibition choices made during setup."""
    allowed = {"roles", "children", "verification", "prohibited", "rules"}
    if not isinstance(policy, dict) or set(policy) - allowed:
        raise ValueError("model_policy may hold roles, children, verification, prohibited and rules")
    if not isinstance(policy.get("verification", "different_vendor"), str) or policy.get("verification", "different_vendor") not in {"different_vendor", "any"}:
        raise ValueError("model_policy.verification must be different_vendor or any")
    chosen = list(models.values())
    for key, names in [("roles", {"orchestrator", "debugging", "other"}), ("children", {"bounded", "simple", "rote", "strong"})]:
        group = policy.get(key, {})
        if not isinstance(group, dict) or set(group) - names or not all(valid_model(m, draft) for m in group.values()):
            raise ValueError("model_policy." + key + " must name only " + "/".join(sorted(names)) + " with resolved provider, model and effort")
        chosen += list(group.values())
    for key in ("prohibited", "rules"):
        items = policy.get(key, [])
        if not isinstance(items, list) or len(items) > 50 or not all(policy_text(i, draft) for i in items) or len({model_key(i) for i in items}) != len(items):
            raise ValueError("model_policy." + key + " must be at most 50 unique printable single-line strings of at most 500 characters")
    banned = {model_key(i) for i in policy.get("prohibited", [])}
    if any({model_key(m["model"]), model_key(m["provider"] + "/" + m["model"])} & banned for m in chosen):
        raise ValueError("a prohibited model is selected for a role, child tier or review")


def normalise_config(config):
    config = copy.deepcopy(config)
    if not isinstance(config, dict):
        raise ValueError("configuration must be an object")
    skills = config.get("skills")
    if not isinstance(skills, list) or any(not isinstance(s, str) for s in skills):
        raise ValueError("select known unique skills")
    if len(set(skills)) != len(skills):
        raise ValueError("select known unique skills")
    aliases = {"setup-project": "swarmstack", "swarmstack-help": "swarmstack"}
    config["skills"] = list(dict.fromkeys(aliases.get(s, s) for s in skills))
    return config


def validate_options(options, *, draft=False):
    if not isinstance(options, dict) or set(options) != {"host", "orchestrator", "direction_cooldown_seconds", "status_ttl_seconds"}:
        raise ValueError("configure the swarm host, orchestrator and cooldowns first")
    if options["host"] not in {"t3", "codex", "claude", "manual"} or not ((draft and options["orchestrator"] is None) or (isinstance(options["orchestrator"], str) and options["orchestrator"].strip())):
        raise ValueError("verify and configure one actual orchestrator identity")
    for key, minimum, maximum in [("direction_cooldown_seconds", MIN_COOLDOWN, 31536000), ("status_ttl_seconds", 0, 3600)]:
        value = options[key]
        if type(value) is not int or not minimum <= value <= maximum:
            raise ValueError("invalid " + key)
    return options


