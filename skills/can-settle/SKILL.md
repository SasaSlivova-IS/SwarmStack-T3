---
name: can-settle
description: List which threads can be settled (moved out of the active list) and which should stay, with a one-line reason each. "/can-settle" reports only; it never settles, messages or changes anything.
disable-model-invocation: true
---

# Can settle

Read-only. Use the host's thread tools (in T3 Code: `t3_thread_list`, `t3_thread_read`, `t3_pending_request_list`, `t3_queue_list`) on the confirmed project. Do not settle, message, interrupt or edit anything.

A thread can be settled only when all of these hold. Check each against the thread itself, not its title:

1. Not running, waiting, queued or starting, and not snoozed.
2. No pending request, no queued message and no running child.
3. Its last message is a finished result or hand-off, not a question or offer still waiting on the user.
4. No open decision or required next step belongs to it. A finished delegated child whose parent has taken in the result counts as done.
5. It is not a standing role thread: the orchestrator, the user-facing chat, or a lead whose issue is still open. If unsure, keep it.

Report in plain words, no hashes or run numbers:

- **Can settle now:** each thread as a link, with a few words on why it is finished.
- **Keep, and why:** threads that look finished but fail a check above, with the failing check.
- **Not sure:** one line each, saying what you could not read.

Open with the count. Settled threads stay recoverable, but say so only if asked. Offer to settle the first group only after the report, and do it only on a clear yes from the user.
