# Workspace boundaries and effects

Load when briefing a child task, or when a child returns outside-effects findings. Setup chooses which parts below are installed through `workspace_policy` in `.swarmstack/project.json` (defaults: scratch directories on, outside-effects check on, tool-cleanup exception off). A part that is switched off is not installed in a project.

## Always

Every brief names its input list and its output directory. A child reads only the listed inputs, does not scan checkouts or directories it was not given, and writes only to its output directory and any separately authorised source paths. It never deletes, moves over or rewrites a file it did not create. Creating a file grants no authority to clean it up. Where scratch directories are not enabled, temporary helpers go inside the output directory.

<!-- workspace:scratch:start -->
## Per-task scratch directories

Give every child its own named scratch directory, disjoint from its output directory, and bind the task ID to it in the task's receipt. Children use only that directory for temporary helpers and never use shared names such as `/tmp/check.py`. Set the child's temporary-directory environment variable to the scratch directory where the host supports it; where only command environments are supported, set it on each applicable command and report that scope. Do not change the host's own configuration to add this support, and report unsupported temp control honestly.
<!-- workspace:scratch:end -->

<!-- workspace:effects:start -->
## Outside-effects check

After each task, compare the child's own native command and result history with its output and scratch directories. List every file created, removed, moved, overwritten or otherwise written outside them, and separate authorised source edits from deviations. Name the compared path set and the areas not covered. Return the list even when empty, with the evidence and its limits. A no-deletion or no-write claim must match the actual commands; a partial snapshot supports no broad "nothing was lost" conclusion. Preserve original commands, failures and receipts, and never clean up evidence of a deviation to make a report pass.
<!-- workspace:effects:end -->

<!-- workspace:cleanup:start -->
## Tool cleanup exception

Deterministic tools may clean up their own files under the conditions in `guides/tool-cleanup.md`. Everything above still applies.
<!-- workspace:cleanup:end -->
