# User-facing channels

Green 1 belongs to the user; agents send decisions/outcomes through Green 2 or the configured fallback. Mention actual colour/worker number, assigned issue and clickable thread where supported.

Name every item for the user. Replies, catch-ups, questions and relayed status give each issue, pull request, decision question, review and helper a plain name plus one or two specific sentences on first mention, never a bare number or code. Identifiers go last in parentheses, only when the user needs them to find or answer something. Take the name from the item's own title or what it changes; for an unnamed item propose one and record it in the owning record. Restate the name and meaning when asking for an answer to an earlier item. A generalisation such as "the settings work" is not a name. Agent-to-agent messages and records keep identifiers.

Lead with answer/choice, use short numbered steps, suppress tangents and show changed state only when useful. Use [ADHD output](../skills/adhd-output/SKILL.md) and [unslop](../skills/unslop/SKILL.md). No invented timings or repetitive plans.

Before asking, inspect requirements, previous answers and evidence. Use [grill-with-docs](../skills/grill-with-docs/SKILL.md) with stable IDs and useful choices. Do not ask the user to interpret Git graphs or verify agent-checkable safety.

Keep the tracker's Needs user column in step with the questions you ask ([tracking](tracking.md)). Keep interim user-led investigation findings here; relay one concluded actionable result when needed. Do not wake/steer/dispatch to acknowledge updates. Record exact decisions with their owning writer; a decision is not implemented behavior.

The user-facing thread writes the plan in the user's terms: what the user will see and decide. Root writes the technical plan. Neither replaces the other, and workers' threads only execute and suggest. Sign anything you post under the records guide.

<!-- swarm:start -->
For /swarm controls, load [the core skill](../skills/swarm/SKILL.md). Use the original user-message ID, validated project/Root binding and existing grants. Relay allowed queue/steer requests once; read status locally and retain the latest deferred direction. No routine progress depends on the user sending another command.
<!-- swarm:end -->
