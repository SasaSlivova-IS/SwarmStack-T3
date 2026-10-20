---
name: can-settle
description: Answers two questions about the lead threads in the project sidebar: which need the user or others (and what each needs), and how much of the sidebar can be cleared by settling. Shows a checklist; the user ticks, copies the selection, pastes it back, and the orchestrator settles those threads itself. Reads only until the user pastes a selection.
disable-model-invocation: true
---

# Can settle (T3 Code)

T3 Code only: it needs T3's thread tools and the inline page tool `html_render`. Other harnesses lack these, so this skill stays out of the generic toolkit.

Settling is organisation and bloat removal, and it is reversible: any thread can be unsettled when related work returns. So lean towards listing finished work, and keep only what is clearly live.

## 1. Read (no changes)

Scope: only the **lead threads** the user sees in the project sidebar: top-level threads (`parentThreadId` empty) that are unsettled and not archived. Subagents (child threads) are displayed differently in T3 and do not clutter the sidebar, so ignore them completely and never list them. Use `t3_thread_list` on the confirmed project (50 per page, newest update first) and keep paging until unsettled top-level threads stop appearing, then read each one. Reading may be split across a few read-only helpers; keep their results out of the final text. For each lead thread read the end of it (its last messages), plus `t3_pending_request_list`, `t3_queue_list` and whether it has running subagents.

Settling is reversible organisation, so the user decides. The report answers two things:

1. **Which threads need the user or someone else, and what each needs.** For every thread that cannot be settled, say what it is waiting on and from whom (the user, the orchestrator, another lead, a decision, a hold, a running job). Never leave a blocked thread without its reason.
2. **How much of the sidebar can be cleared.** Open with one sentence: how many of the sidebar's lead threads can be settled now, how many are your call, and how many stay.

Sort each lead thread into one group:

- **Can settle (Done):** its last run finished, nothing is running, queued or pending, and it is not waiting on the user. Say plainly in the reason what is still open, for example that its issue or pull request is unfinished, so the user can judge.
- **Maybe, your call:** finished-looking but waiting on someone else's decision, hold or hand-off, or with a running subagent.
- **Needs attention (not settleable):** running or working, a pending request or queued message, waiting on the user, or a standing role (the orchestrator, the user-facing chats). Give what it needs and from whom.

A missing pull request is not a reason to settle. Take each reason from what the thread says; never invent one.

## 2. Show the page

Check it once with `html_preview`, then `html_render` with `page-template.html`. The page has a one-sentence summary, then:

- **Can settle:** thread title, a reason of two or three short sentences (what it delivered, what is still open, whether anything waits on it), last update. Checkboxes, unchecked.
- **Maybe, your call:** same shape, reason of two short sentences, unchecked.
- **Needs attention:** thread title, what it needs and from whom in one or two short sentences, no checkbox.

No list of deviations or open questions on the page. After the page write at most two short lines: the counts and how many sidebar threads were covered. Put any problem with the skill itself in one line, only if it changed the result. If `html_render` is unavailable, give the same three tables as Markdown.

## 3. Relay the selection

Do nothing until the user pastes a selection that starts "Please settle these threads (chosen in /can-settle)". That paste is the approval. Send it unchanged to the orchestrator with `t3_thread_send`, using a stable `clientRequestId`, and ask it to settle those threads itself and record which ones it settled. Do not settle anything yourself. After the orchestrator answers, read the list once to confirm, and tell the user in plain words which were settled. If a selected thread has meanwhile started running or has new work, say so before relaying.
