# Models and effort

Load at model intake, delegation or changed capacity. Do not inherit the lead's model/effort automatically.

Use dated primary [Artificial Analysis](https://artificialanalysis.ai/) Intelligence, Coding and Agentic evidence where available. Record exact version, effort, benchmark/version, provider/setup, source and retrieval date. Missing scores remain unknown. Do not transfer scores across versions, context variants, efforts or providers without proof.

Compare model+provider+effort on one comparable task cohort at a time. Maximise relevant quality while minimising measured per-task cost and latency. Include reasoning tokens and actual token usage; identical token prices do not make high effort free. A point is dominated if another is at least as good on every dimension and strictly better on one.

Use [model_frontier.py](../scripts/model_frontier.py) offline. The sample is invented data, not live AA scores or permission to spend. Never rank incomparable benchmark cohorts or silently substitute missing measurements.

Required independent verification follows the project's `model_policy.verification`, a different vendor than the builder by default (see [review](review.md)). Route new work to a provider through the instance the project configures for it, and change a running lead's route only at an authorised task boundary.

Choose using scale, complexity, time/parallel benefit, data sensitivity, consequence and ability to verify. Prefer the cheapest sufficiently reliable allowed configuration. Use the project's normal effort; raise it for a named need. Do not force a weak failed attempt before consequential review gets a stronger model.

Use small representative public/synthetic evaluations within an explicit budget to confirm tool use, correctness and latency. Benchmarks are not proof of host compatibility or safe private-data handling.

Record approved actual host IDs/efforts, data permissions and budget in project configuration. Setup also chooses the other roles (orchestrator, debugging, other), the child tiers (bounded, simple, rote, strong), the verification rule, prohibited models and any further usage rules, in `models` and `model_policy`; guides here name no model. Validation refuses unresolved or prohibited choices; vendor and verification choices are recorded rules that agents follow, since a vendor cannot be derived from a provider string. No silent fallback for user-required models. Capacity failures stop unchanged retries; preserve handoff and continue independent work. No unapproved spending, extra subscription or overage without authority.
