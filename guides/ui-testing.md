# Independent frontend UI and UX review

Load [verification](verification.md). Frontend leads own one complete automated affected-flow pass before submission, including corrections and affected retests. Use existing assertions and automated interaction tools with an allocated test session. The orchestrator's independent reviewer verifies that proof and the required automated workflow behaviour under [review](review.md); do not add a separate manual agent walkthrough. The user performs the final manual and visual pass before any merge or release. Models follow the project's configured policy.

## Brief and environment

- Give the reviewer the accepted requirements, Done criteria, affected flows, known failures, exact candidate pin and source location. Expected results come from requirements, not the current implementation's output.
- Identify the actual loaded build before testing. Use an allocated synthetic session and representative fixtures built from genuine application objects and role or state data. Mock external effects explicitly.
- Keep source fixed during checks. Use one driver per session. Never drive a live user session or personal data; use a separate allocated session or wait for the owner to release it.
- Reuse existing launchers, automation tools and end-to-end assertions. If the fixture or driver cannot reach the flow, report the concrete blocker; do not weaken the requirement or substitute a screenshot pass.

## Exercise affected behaviour

1. Complete the user flow and assert the resulting state, including persistence or reopen where affected. Check relevant denied roles, failures, cancellation, retries and duplicate effects.
2. Check relevant keyboard and focus behaviour, labels, navigation, dropdowns, scrolling, narrow layouts and themes. Look for clipping, overlap, missing controls and confusing or duplicate terminology against accepted design references. Skip exhaustive matrices for unaffected states.
3. Use screenshots for visual observations and assertions for behaviour. Corroborate blank or black captures through other observations. Browser checks do not qualify native-only behaviour or other platforms.
4. Report the requirement, steps, expected and observed result, tested pin, evidence and PASS, FAIL or BLOCKED. Mark synthetic, native and platform scope. Never change a test expectation merely to match a defect.

## Correction and handoff

The lead checks findings, fixes product defects and reruns affected checks on the final candidate. Reuse unchanged qualified evidence and retest changed production dependencies. Preserve failures and one-shot or effect limits. Send the orchestrator only Done, genuine blockers or required decisions.

Done for agent UI review means the affected required checks pass, findings are resolved, agreed coverage is accounted for and remaining gates are explicit. It does not complete the issue while required human, native or platform acceptance remains. Give the user a short final visual and UX list after functional defects are addressed.

## Pass criteria

A UI test passes only when the expected interaction reaches its required resulting state on the identified loaded candidate. Visual observation alone cannot prove persistence, permission enforcement or money-moving effects. Required blocked or unrun flows prevent UI review Done. Human quality acceptance remains the user's decision.
