---
name: can-settle
description: Show which threads can be settled (moved out of the active list) as a table with a real reason each and checkboxes. The user ticks, copies the selection, pastes it back, and the orchestrator settles those threads itself. "/can-settle" only reads until the user pastes a selection.
disable-model-invocation: true
---

# Can settle (T3 Code)

T3 Code only: it needs T3's thread tools and the inline page tool `html_render`. Other harnesses lack these, so this skill stays out of the generic toolkit.

## 1. Read (no changes)

Use `t3_thread_list` on the confirmed project. Pages are 50 threads, newest update first. Page until unsettled threads stop being recent or until about 300 threads are covered, and say how many you covered. Candidates are unsettled, unsnoozed threads that are not running, starting or waiting. For each candidate use `t3_thread_read` for its last messages, `t3_pending_request_list` and `t3_queue_list` for requests and queued messages, and the list itself for children (`parentThreadId`).

A thread can be settled only when all of these hold. Check each against the thread itself, never the title:

1. Not running, waiting, queued or starting, and not snoozed.
2. No pending request, no queued message and no running or unfinished child.
3. Its last message is a finished result or hand-off, not a question or offer waiting on the user.
4. No open decision, hold, unfinished check or required next step belongs to it. A finished delegated child whose parent has taken in the result, with no later child turn, queue, request or owned next step, counts as done. An idle name such as `/root/...` proves nothing.
5. It is not a standing role thread: the orchestrator, a user-facing chat, or a lead whose issue is still open. If unsure, keep it.

A missing pull request is not a reason to settle. A finished turn is not completion. Take the reason from what the thread says, never invent one.

## 2. Show the page

Call `html_preview` once to check the page, then `html_render` with `page-template.html` filled in. Put each thread's plain title on screen, never its id; the id goes only in `data-id`. Fill three groups:

- **Can settle now:** a few plain words on why it is finished, with the time of its last update.
- **Keep, and why:** threads that look finished but fail a check, naming the failing check.
- **Not sure:** one line each on what could not be read.

After the page add at most two lines: the count, how many threads you covered, and that settled threads stay recoverable only if asked. Do not repeat the table. If `html_render` is unavailable, give the same three groups as a Markdown table.

## 3. Relay the selection

Do nothing until the user pastes a selection that starts "Please settle these threads (chosen in /can-settle)". That paste is the approval. Send it unchanged to the orchestrator with `t3_thread_send`, using a stable `clientRequestId`, and ask it to settle those threads itself and record which ones it settled. Do not settle anything yourself. After the orchestrator answers, read the list once to confirm the threads show as settled, and tell the user in plain words which were and which were not. If a selected thread turns out to be running or to have new work, tell the user before relaying.
