# Deterministic tool cleanup inside child scratch

Installed only when setup enables `tool_cleanup_exception`, which requires the scratch-directory and outside-effects parts of [workspace](workspace.md). It refines that guide and changes no other rule. Independent review stays mandatory for anything that deletes data ([verification](verification.md)).

The default no-deletion rule limits models. A model never deletes, moves over, truncates or rewrites a file it did not create, whether or not the exception is on. This exception lets a deterministic tool (an installer, build, test runner or named script) remove or replace objects that tool itself created during the same run, inside the child's own named scratch directory (a work or environment folder named in the brief).

Conditions:

1. The brief names the directory, says it is empty or fresh at the start, and keeps it disjoint from the output directory. Record its state before the run.
2. The tool or script is named and deterministic. A model's ad hoc `rm`, `rmdir`, `unlink`, `mv`-over or `sed -i` is not covered, even inside scratch. A cleanup script that a model runs counts only if the brief pre-approves its exact path list, and that list is still limited by condition 3.
3. Only objects the tool created in this run are covered. Never pre-existing files, source, user data, evidence, originals or any path outside the named directory. If a name collides with a pre-existing object, skip it and report the collision.
4. Original inputs, such as downloaded packages, manifests and logs, are retained. The effects receipt lists the tool, command, directory, the path of every object created and removed, and any collision.
5. A model never deletes its own reports or outputs. Reports go to the output directory and stay.

Reporting follows [workspace](workspace.md). This exception grants no product, network, provider or native authority and does not reinterpret earlier failures.
