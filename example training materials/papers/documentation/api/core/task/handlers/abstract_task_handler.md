# AbstractTaskHandler

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html

**Documentation path:** `api/core/task/handlers/abstract_task_handler.html`

---

# AbstractTaskHandler

**Qualified name:** `mv::AbstractTaskHandler`

class AbstractTaskHandler : public QObject
:   Abstract task handler class.

    Base handler class for interacting with a task.

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::BackgroundTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/background_task_handler.html#classmv_1_1BackgroundTaskHandler), [mv::DatasetTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/dataset_task_handler.html#classmv_1_1DatasetTaskHandler), [mv::ForegroundTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/foreground_task_handler.html#classmv_1_1ForegroundTaskHandler), [mv::ModalTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/modal_task_handler.html#classmv_1_1ModalTaskHandler)

    Public Functions

    AbstractTaskHandler(QObject \*parent, [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
    :   Construct task handler with `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **task** – Pointer to task to handle

    virtual [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*getTask() final
    :   Get task.

        Returns:
        :   Pointer to task

    std::uint32\_t getMinimumDuration() const
    :   Get the minimum duration.

        Returns:
        :   Minimum duration before the handler displays a tasks UI

    void setMinimumDuration(std::uint32\_t minimumDuration)
    :   Set the minimum duration.

        Parameters:
        :   **minimumDuration** – Minimum duration before the handler displays a tasks UI

    bool getEnabled() const
    :   Get enabled.

        Returns:
        :   Boolean determining whether the task handler is enabled or not

    void setEnabled(bool enabled)
    :   Set enabled to `enabled`.

        Parameters:
        :   **enabled** – Minimum duration before the handler displays a tasks UI

    void taskChanged([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*previousTask, [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*currentTask)
    :   Signals that the current task has changed from `previousTask` to `currentTask`.

        Parameters:
        :   - **previousTask** – Pointer to previous task (if any)
            - **currentTask** – Pointer to current task

    void minimumDurationChanged(std::uint32\_t previousMinimumDuration, std::uint32\_t currentMinimumDuration)
    :   Signals that the minimum duration changed from `previousMinimumDuration` to `currentMinimumDuration`.

        Parameters:
        :   - **previousMinimumDuration** – Previous minimum duration
            - **currentMinimumDuration** – Current minimum duration

    void enabledChanged(bool enabled)
    :   Signals that enabled changed to `enabled`.

        Parameters:
        :   **enabled** – Boolean determining whether the task handler is enabled or not

    Protected Functions

    virtual void setTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task) final
    :   Set handle `task`.

        Parameters:
        :   **task** – Pointer to task to handle
