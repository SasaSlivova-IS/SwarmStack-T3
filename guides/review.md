# Completed-issue review

Load only at completed implementation submission. The orchestrator owns acceptance/integration; original leads fix product defects.

Under the project's `model_policy.verification` (default `different_vendor`), reviewers come from a different vendor than the builder; with `any`, any independent reviewer is accepted. The project maps which models fill each side. Each reads the original requirements and exact artifact itself; self-review or acceptance on the lead's conclusion alone does not count. The reason is a policy judgement about correlated blind spots between a builder and a reviewer from the same vendor, not a proven benchmark fact. The orchestrator then relies on lead-owned checks, evidence summaries and targeted spot-checks rather than routine full replay; no required check is waived.

Use two independent roles at a fixed candidate:

1. Code/edge cases: bugs, lifecycle/error/permission paths, affected callers, scope and altered tests. Reuse the project's code-review Standards/Spec specialists; preserve separate verdicts rather than spawn duplicate generic reviewers.
2. Original claim/end-to-end: compare accepted requirements and independently exercise the actual workflow in an authorised fixture. Inspect resulting state and meaningful refusal cases. Source inspection or green counts do not replace execution.

Add [code-review](../skills/code-review/SKILL.md)'s Security specialist for changed security boundaries. Reviewers are read-only on delivered source/index/branches. Approved execution uses isolated fixtures.

Frontend leads already perform an automated affected-flow pass. Verify necessary independent workflow proof; final manual visual acceptance belongs to the user, not another manual agent round.

Return full severity-labelled reports: location, rule, trigger, consequence, evidence. The lead validates claims, fixes material findings or rebuts with evidence; reviewer checks rebuttals before closure. Retest changed/affected parts without repeating unchanged checks absent a reason.

Missing required proof or unresolved material findings prevent Done. Do not confuse unrelated project release gates with the issue's own criteria.
