# ModalTask

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/types/modal_task.html

**Documentation path:** `api/core/task/types/modal_task.html`

---

# ModalTask

**Qualified name:** `mv::ModalTask`

Use `ModalTask` only when continuing to interact with the application while the operation runs would be invalid. Its handler presents a modal task dialog.

For selection, lifecycle, and cancellation guidance, see [Tasks and progress reporting](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/index.html).

class ModalTask : public mv::[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")
:   Modal task class.

    Modal tasks are foreground tasks that show their progress in a modal progress dialog.

    **Author**
    :   Thomas Kroes

    Public Functions

    ModalTask(QObject \*parent, const QString &name, const Status &status = Status::Undefined, bool mayKill = false)
    :   Construct task with `parent` object, `name` and initial `status`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **name** – Name of the task
            - **status** – Initial status of the task
            - **mayKill** – Boolean determining whether the task may be killed or not

    Public Static Functions

    static void createHandler(QObject \*parent)
    :   Creates singleton modal task handler.

        Parameters:
        :   **parent** – Pointer to parent object

    static inline [ModalTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/modal_task_handler.html#_CPPv4N2mv16ModalTaskHandlerE "mv::ModalTaskHandler") \*getGlobalHandler()
    :   Get global handler.

        Returns:
        :   Pointer to global modal task handler
