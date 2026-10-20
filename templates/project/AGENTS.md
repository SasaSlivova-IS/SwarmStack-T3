# Working on {{PROJECT_NAME}}

Shared development instructions, not the runtime prompt. Follow the user and higher-priority host instructions. Read this file, your role guide and applicable nested AGENTS.md before edits.

Read [.swarmstack/project.json](.swarmstack/project.json) for scope, models, commands, branches and effects. Inspect status and preserve WIP. Keep secrets/real data out of synthetic fixtures. Never dump the process environment (`env`, `printenv`, `set`, `export -p`, process or session dumps): agent environments carry access tokens. Check a named variable's presence instead of printing it, read only the names you need, and never print a value. Only the grants recorded there or given by the user allow outside effects such as pushing, merging, spending, deploying, deleting or touching real data. Finishing a step, passing a check or review, or loading a guide or skill never adds a grant.

One purple orchestrator coordinates. Each issue has one dedicated lead thread, reused only for that issue. Names use `<colour> <worker ordinal> | #<GitHub issue> <issue name>`, for example `🟡 4 | #17 Export invoices as CSV`. Blue/yellow require issues; red/green and general black work may omit them. Preserve worker identity and explicit workspace binding.

Load only your role: [orchestrator](.swarmstack/guides/orchestrator.md), [frontend](.swarmstack/guides/frontend.md), [backend](.swarmstack/guides/backend.md), [debugging](.swarmstack/guides/debugging.md), [other](.swarmstack/guides/other.md) or [user-facing](.swarmstack/guides/user-facing.md). Issue leads also load [lead](.swarmstack/guides/lead.md). Children receive bounded assignments, not every role's instructions.

When talking to the user, name each thing by what it is, never by a number or code alone. On first mention give a short plain name plus one or two sentences saying specifically what it covers, not a generalisation; identifiers such as issue, pull request or question numbers may follow in parentheses. Use the project's standard terms and propose a plain name for anything unnamed. Agent-to-agent messages keep identifiers. See the [user-facing guide](.swarmstack/guides/user-facing.md).

Continue complete authorised outcomes through checks, review and corrections. A child PASS, source review or merged slice is not issue Done. Required checks, resolved findings, agreed integration and required human acceptance determine closure. Escalate real blockers, not routine next steps.

Read [models](.swarmstack/guides/models.md) only for intake/delegation and [review](.swarmstack/guides/review.md) at submission. Load [communication](.swarmstack/guides/communication.md) when coordinating or delegating, [verification](.swarmstack/guides/verification.md) when checking work, [records](.swarmstack/guides/records.md) before changing shared records, and [workspace](.swarmstack/guides/workspace.md) when briefing children, [implementation](.swarmstack/guides/implementation.md), [integration](.swarmstack/guides/integration.md) or [UI testing](.swarmstack/guides/ui-testing.md) for those subagent tasks. Keep temporary limits in the task and requirements/terminology in their owning project files.

<!-- swarm:start -->
Use [swarm](.agents/skills/swarm/SKILL.md) only for user-facing commands and normal pending-command checkpoints.
<!-- swarm:end -->

Current state: [.swarmstack/state.md](.swarmstack/state.md). Accepted setup: [.swarmstack/decisions.md](.swarmstack/decisions.md). Issue workflow: [docs/agents/issue-tracker.md](docs/agents/issue-tracker.md).
