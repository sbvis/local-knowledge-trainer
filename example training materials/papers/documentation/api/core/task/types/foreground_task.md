# ForegroundTask

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/types/foreground_task.html

**Documentation path:** `api/core/task/types/foreground_task.html`

---

# ForegroundTask

**Qualified name:** `mv::ForegroundTask`

Use `ForegroundTask` for user-initiated work whose live state should appear automatically in the foreground task popup.

For selection, lifecycle, and cancellation guidance, see [Tasks and progress reporting](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/index.html).

class ForegroundTask : public mv::[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")
:   Foreground task class.

    Foreground tasks appear in a main window status bar popup window.

    **Author**
    :   Thomas Kroes

    Public Functions

    ForegroundTask(QObject \*parent, const QString &name, const Status &status = Status::Undefined, bool mayKill = false)
    :   Construct task with `parent` object, `name` and some optional parameters.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **name** – Name of the task
            - **status** – Initial status of the task
            - **mayKill** – Boolean determining whether the task may be killed or not

    Public Static Functions

    static void createHandler(QObject \*parent)
    :   Creates singleton foreground task handler.

        Parameters:
        :   **parent** – Pointer to parent object

    static inline [ForegroundTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/foreground_task_handler.html#_CPPv4N2mv21ForegroundTaskHandlerE "mv::ForegroundTaskHandler") \*getGlobalHandler()
    :   Get global handler.

        Returns:
        :   Pointer to global foreground task handler
