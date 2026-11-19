# Long-running operations and task progress

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/index.html

**Documentation path:** `development/building_plugins/tasks/index.html`

---

# Long-running operations and task progress

For new long-running operations, prefer ManiVault’s workflow-backed execution facilities. Start with the high-level `Parallel` utilities for common operation shapes and move to a custom workflow plan when you need explicit stages, dependencies, thread affinity, structured results, or detailed reporting.

A `Task` is the presentation layer for progress and abort requests; it does not schedule or execute work. Manage one directly when execution already belongs to an external, legacy, or otherwise independently managed operation. A workflow can instead drive a task while remaining the authoritative owner of execution and outcome.

- [Choosing an execution model](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/choosing_an_execution_model.html)
- [Tasks and workflows](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/tasks_and_workflows.html)
- [Lifecycle and progress](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/lifecycle_and_progress.html)
- [Cancellation and abort behavior](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/cancellation.html)
- [Task hierarchies](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/task_hierarchies.html)
- [Threading and integration](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/threading_and_integration.html)
- [Recipes and pitfalls](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/recipes_and_pitfalls.html)

Start with [Choosing an execution model](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/choosing_an_execution_model.html). If the work is workflow-backed, continue with [Tasks and workflows](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/tasks_and_workflows.html); otherwise use the remaining pages to manage task reporting directly. For exact signatures and all signals, see the [Task API](https://manivault.readthedocs.io/en/latest/api/core/task/index.html).
