---
name: can-settle
description: Show which threads can be settled (moved out of the active list) as one glanceable table with checkboxes. The user ticks, copies the selection, pastes it back, and the orchestrator settles those threads itself. "/can-settle" only reads until the user pastes a selection.
disable-model-invocation: true
---

# Can settle (T3 Code)

T3 Code only: it needs T3's thread tools and the inline page tool `html_render`. Other harnesses lack these, so this skill stays out of the generic toolkit.

Settling is organisation and bloat removal, and it is reversible: any thread can be unsettled when related work returns. So lean towards listing finished work, and keep only what is clearly live.

## 1. Read (no changes)

Scope: only **top-level threads of the project** (`parentThreadId` empty) that are unsettled and not archived. These are the threads in the user's sidebar. Helper, reviewer and other child threads never appear there, so never list them. Use `t3_thread_list` on the confirmed project (50 per page, newest update first) and keep paging until the unsettled top-level threads stop appearing, then read each one. Reading may be split across a few read-only helpers; keep their results out of the final text. For each thread read the end of it (its last messages), plus `t3_pending_request_list`, `t3_queue_list` and its children.

Settling is reversible organisation, so the user decides. Sort each thread into one group:

- **Looks finished (Done):** its last run finished, nothing is running, queued or pending, and it is not waiting on the user. Say plainly in the reason what is still open, for example that its issue or pull request is unfinished, so the user can judge. A lead whose issue is still open can sit here; the reason must say so.
- **Maybe, your call:** finished-looking but waiting on someone else's decision, hold or hand-off, or with a running child.
- **Kept:** running or working, queued messages or a pending request, waiting on the user, or a standing role (the orchestrator and the user-facing chats).

A missing pull request is not a reason to settle. Take each reason from what the thread says; never invent one.

## 2. Show the page

Check it once with `html_preview`, then `html_render` with `page-template.html`. The page is the main table plus a short maybe list, nothing else:

- **Looks finished:** thread title, a reason of two or three short sentences (what it delivered, what is still open on it, whether anything is waiting on it), last update. Checkboxes, unchecked.
- **Maybe, your call:** same shape, reason of two short sentences (what is finished and what it waits on), unchecked.
- **Kept:** only a closed line with the count and the groups.

No long sentences, no per-thread reasons for kept threads, no list of deviations or open questions on the page. After the page write at most two short lines: the counts, and how many threads you covered. Put any problem with the skill itself in one line, only if it changed the result. If `html_render` is unavailable, give the same two tables as Markdown.

## 3. Relay the selection

Do nothing until the user pastes a selection that starts "Please settle these threads (chosen in /can-settle)". That paste is the approval. Send it unchanged to the orchestrator with `t3_thread_send`, using a stable `clientRequestId`, and ask it to settle those threads itself and record which ones it settled. Do not settle anything yourself. After the orchestrator answers, read the list once to confirm, and tell the user in plain words which were settled. If a selected thread has meanwhile started running or has new work, say so before relaying.
