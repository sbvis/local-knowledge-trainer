# BackgroundTask

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/types/background_task.html

**Documentation path:** `api/core/task/types/background_task.html`

---

# BackgroundTask

**Qualified name:** `mv::BackgroundTask`

Use `BackgroundTask` for work that can continue without demanding the user’s attention. It participates in the application’s aggregated background-task presentation by default.

For selection, lifecycle, and cancellation guidance, see [Tasks and progress reporting](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/index.html).

class BackgroundTask : public mv::[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")
:   Background task class.

    Background tasks are shown in a main window status bar popup window.

    **Author**
    :   Thomas Kroes

    Public Functions

    BackgroundTask(QObject \*parent, const QString &name, bool parentToOverallBackgroundTask = true, const Status &status = Status::Undefined, bool mayKill = false)
    :   Construct task with `parent` object, `name` and initial `status`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **name** – Name of the task
            - **parentToOverallBackgroundTask** – Boolean determining whether the task will be automatically parented to the global overall background task
            - **status** – Initial status of the task
            - **mayKill** – Boolean determining whether the task may be killed or not

    Public Static Functions

    static [BackgroundTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/background_task.html#_CPPv4N2mv14BackgroundTaskE "mv::BackgroundTask") &getOverallBackgroundTask()
    :   Get overall background task.

        Returns:
        :   Aggregate background task to which all other background tasks are (in)directly parented

    static void createHandler(QObject \*parent)
    :   Creates singleton background task handler.

        Parameters:
        :   **parent** – Pointer to parent object

    static inline [BackgroundTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/background_task_handler.html#_CPPv4N2mv21BackgroundTaskHandlerE "mv::BackgroundTaskHandler") \*getGlobalHandler()
    :   Get global handler.

        Returns:
        :   Pointer to background task handler
