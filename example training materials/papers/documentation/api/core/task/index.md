# Task

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/index.html

**Documentation path:** `api/core/task/index.html`

---

# Task

Tasks report the progress and state of long-running operations to the user. They do not schedule or execute those operations. For substantial new work, prefer the workflow-backed execution facilities and use a task as their GUI progress projection; manage a task directly when execution is owned elsewhere.

In the current design, tasks focus on progress reporting rather than execution itself. Future versions will extend this concept to optionally manage and run worker logic directly, allowing tasks to encapsulate both execution and reporting.

Tasks are closely integrated with the task models, which manage their lifecycle and visibility within the application.

For guidance on choosing between high-level parallel execution, custom workflows, and direct task management, see [Long-running operations and task progress](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/index.html).

## Related

- Task [models](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/index.html)

## Base type

- [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html)

## Types

The task classes below are derived from the [task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html) base class.

- [BackgroundTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/background_task.html)
- [DatasetTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/dataset_task.html)
- [ForegroundTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/foreground_task.html)
- [ModalTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/modal_task.html)
- [ApplicationStartupTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/application_startup_task.html)

## Handlers

Task handlers are responsible for presenting task-related information to the user. For example, they may display progress using a modal dialog, a progress bar in the status bar, or similar UI elements.

- [AbstractTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html)
- [BackgroundTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/background_task_handler.html)
- [DatasetTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/dataset_task_handler.html)
- [ForegroundTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/foreground_task_handler.html)
- [ModalTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/modal_task_handler.html)

## Testing

Below are some auxilliary classes for testing various task types

- [AbstractTaskTester](https://manivault.readthedocs.io/en/latest/api/core/task/testing/abstract_task_tester.html)
- [BackgroundTaskTester](https://manivault.readthedocs.io/en/latest/api/core/task/testing/background_task_tester.html)
- [ForegroundTaskTester](https://manivault.readthedocs.io/en/latest/api/core/task/testing/foreground_task_tester.html)
- [ModalTaskTester](https://manivault.readthedocs.io/en/latest/api/core/task/testing/modal_task_tester.html)
- [TaskTesterRunner](https://manivault.readthedocs.io/en/latest/api/core/task/testing/task_tester_runner.html)
