---
name: can-settle
description: Show which threads can be settled (moved out of the active list) as one glanceable table with checkboxes. The user ticks, copies the selection, pastes it back, and the orchestrator settles those threads itself. "/can-settle" only reads until the user pastes a selection.
disable-model-invocation: true
---

# Can settle (T3 Code)

T3 Code only: it needs T3's thread tools and the inline page tool `html_render`. Other harnesses lack these, so this skill stays out of the generic toolkit.

Settling is organisation and bloat removal, and it is reversible: any thread can be unsettled when related work returns. So lean towards listing finished work, and keep only what is clearly live.

## 1. Read (no changes)

Use `t3_thread_list` on the confirmed project (50 per page, newest update first). Filter to `settled=false` and statuses that are not running, starting or waiting, then cover all of them or about 300 threads, whichever comes first. Reading the candidates may be split across a few read-only helpers; keep their results out of the final text. For each candidate read the end of the thread (its last messages), plus `t3_pending_request_list` and `t3_queue_list`.

Put a thread in **Can settle now** when all of these hold:

1. Not running, waiting, queued or starting, and not snoozed.
2. No pending request, no queued message and no running child.
3. Its last message is a finished result, hand-off or superseded round, not a question or offer waiting on the user.
4. No open decision, hold or unfinished check belongs to it. A finished child counts as done when its parent has shown later activity or recorded the result. An idle helper with no named hold counts as not running.
5. It is not a standing role thread: the orchestrator, a user-facing chat, or a lead whose issue is still open.

Put a thread in **Maybe, your call** when it is finished-looking but one thing is unclear, for example whether the parent took in the result. Everything else is **Kept**. A missing pull request is not a reason to settle. Take each reason from what the thread says; never invent one.

## 2. Show the page

Check it once with `html_preview`, then `html_render` with `page-template.html`. The page is the main table plus a short maybe list, nothing else:

- **Can settle now:** thread title, a reason of at most 12 words, last update. Checkboxes, unchecked.
- **Maybe, your call:** same shape, reason of at most 8 words, unchecked.
- **Kept:** only a closed line with the count and the groups.

No long sentences, no per-thread reasons for kept threads, no list of deviations or open questions on the page. After the page write at most two short lines: the counts, and how many threads you covered. Put any problem with the skill itself in one line, only if it changed the result. If `html_render` is unavailable, give the same two tables as Markdown.

## 3. Relay the selection

Do nothing until the user pastes a selection that starts "Please settle these threads (chosen in /can-settle)". That paste is the approval. Send it unchanged to the orchestrator with `t3_thread_send`, using a stable `clientRequestId`, and ask it to settle those threads itself and record which ones it settled. Do not settle anything yourself. After the orchestrator answers, read the list once to confirm, and tell the user in plain words which were settled. If a selected thread has meanwhile started running or has new work, say so before relaying.
