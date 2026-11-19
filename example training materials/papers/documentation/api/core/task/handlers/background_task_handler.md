# BackgroundTaskHandler

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/handlers/background_task_handler.html

**Documentation path:** `api/core/task/handlers/background_task_handler.html`

---

# BackgroundTaskHandler

**Qualified name:** `mv::BackgroundTaskHandler`

class BackgroundTaskHandler : public mv::[AbstractTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html#_CPPv4N2mv19AbstractTaskHandlerE "mv::AbstractTaskHandler")
:   Background task handler class.

    Interact with tasks in a main window status bar pop up window.

    **Author**
    :   Thomas Kroes

    Public Functions

    BackgroundTaskHandler(QObject \*parent)
    :   Construct task handler with `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    [BackgroundTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/background_task.html#_CPPv4N2mv14BackgroundTaskE "mv::BackgroundTask") &getOverallBackgroundTask()
    :   Get overall background task.

        Returns:
        :   Aggregate background task to which all other background tasks are (in)directly parented
