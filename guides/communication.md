# Communication and tool use

Load when coordinating threads, delegating, resuming work or running a user-led investigation.

Workers message the orchestrator only for:

1. A Done delivery, showing that the assignment's criteria are met, with source and evidence references.
2. A genuine blocker that needs coordination or authority to reach Done.
3. A required decision that blocks Done and stays unanswered after checking the records.

Keep milestones, child completions, review rounds and routine next steps in the issue thread. Continue authorised work until Done or a genuine blocker; do not ask for a new assignment after each step.

## Routing and priority

Choose by the consequence of waiting until the recipient's next safe boundary:

- **P0 / urgent, steer:** a blocker or correction that cannot wait because the recipient's current action would become invalid or unsafe. State that consequence. A delivery or blocker is not urgent by name alone.
- **P1 / decision, queue:** a required decision or coordination blocker that can wait until the current batch finishes. State the blocked outcome and the independent work still available.
- **P2 / delivery, queue:** one consolidated Done delivery per assigned outcome, with evidence and remaining gates. Batch related non-urgent policy updates.
- **Records only:** milestones, routine progress, logs, evidence additions and child completions. Children report to their lead.

Host controls vary, so verify the steer, queue and automatic modes your host actually supports before relying on them. Priority is a label for triage, not queue order; the host schedules queued follow-ups. Queue non-urgent work explicitly instead of using an automatic mode while the recipient is active. If a steer is refused because the thread cannot be steered, make at most one supported automatic fallback with the same request ID, report its actual delivery, and do not restart the recipient or poll. Keep message IDs, run IDs and stable request IDs so a failed delivery does not become duplicate messages.

Send one notification per outcome. If its facts change, update the owning record and mark the superseded revision; steer again only when the correction is urgent. Queue tools can edit or cancel still-queued messages but not delivered history. Before acting on a queued batch, recheck the current owner record, pin, authority and evidence; discard obsolete requests and never silently substitute an unverified successor or rewrite another sender's meaning.

Keep each message to a short fixed budget (six lines by default): priority and issue, event, result, evidence link, required action. Keep prompts, code, logs and routine progress in the worker thread or owning files and link detail. Do not forward verbose instructions, step-by-step updates, acknowledgements or repeated waiting notices.

## Users and investigations

Questions, updates and merge requests for the user go through the user-facing channel; the orchestrator never asks the user in its own output. Batch independent questions and return numbered answers verbatim with the same urgency routing. A user answer steers only when it changes the current action.

During a user-led investigation, keep interim findings, guesses and acknowledgements in the user-facing chat. Do not forward them or dispatch parallel work from them. Send one concise outcome only when the stated goal succeeds or fails; a failed diagnostic step alone does not conclude it. Do not expand diagnosis into implementation or deployment.

Before escalating, check requirements, issue records, decisions and code. Apply accepted rules and make reversible technical choices yourself. Escalate unresolved requirements, authority, spending, ownership conflicts or contradictory records, stating what you checked. Number independent questions and give options and a recommendation for concrete choices.

## Delegation and tools

Use the host's supported asynchronous delegation and keep task IDs. Let completion notify the parent; read status when needed without polling or duplicate watchers. Start each delegated review round as a fresh task with the original brief and unresolved findings. Use the host's supported event notifications; a push alone is not a promised wake. Reuse an authorised scheduled check rather than adding watchers.

API metadata can contain credentials. Request only the fields you need and allowlist them before any retained or model-visible output; never dump whole repository, session or account objects. If sensitive data appears unexpectedly, stop further effects, keep the original in restricted custody, send only a secret-free incident summary, and never forward the value or a reversible encoding. Do not test or change credentials without authority.

Use focused tool output:

- Search by issue, symbol or item before reading whole documents. Read complete files when correctness requires it.
- Select needed response fields where supported. Preserve all findings, errors, pending work, provenance and evidence references; read omitted detail before relying on it.
- Save large logs. Report successful checks with outcome, counts, source pin and log path; show actionable failures with context.
- Reuse verified model catalogues within a run; refresh after settings changes, uncertain availability or a selection failure.
- At the next task boundary after an instruction update, reread the changed rules without interrupting active work.

Leads continue available authorised work through Done or a genuine blocker; when none is left, end the turn and await the owned event. Ending a turn is not pausing a goal or declaring Done. A wake grants no merge, deployment, spending or acceptance authority. Do not pause or resume a goal except at the user's request; if the host lacks the control, report that once and do not work around it.
