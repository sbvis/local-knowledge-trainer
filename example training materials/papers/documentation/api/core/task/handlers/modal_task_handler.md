# ModalTaskHandler

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/handlers/modal_task_handler.html

**Documentation path:** `api/core/task/handlers/modal_task_handler.html`

---

# ModalTaskHandler

**Qualified name:** `mv::ModalTaskHandler`

class ModalTaskHandler : public mv::[AbstractTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html#_CPPv4N2mv19AbstractTaskHandlerE "mv::AbstractTaskHandler")
:   Modal task handler class.

    Takes care of handling modal tasks (i.e. shows them in a modal tasks dialog).

    **Author**
    :   Thomas Kroes

    Public Functions

    ModalTaskHandler(QObject \*parent)
    :   Construct task handler with `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    [TasksTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_tree_model.html#_CPPv4N2mv14TasksTreeModelE "mv::TasksTreeModel") &getModel()
    :   Get the tasks model.

        Returns:
        :   Reference to the tasks tree model

    [TasksFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_filter_model.html#_CPPv4N2mv16TasksFilterModelE "mv::TasksFilterModel") &getFilterModel()
    :   Get the tasks filter model.

        Returns:
        :   Reference to the tasks filter model

    class ModalTasksDialog : public QDialog
    :   Dialog for interaction with modal tasks.

        Public Functions

        ModalTasksDialog([ModalTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/modal_task_handler.html#_CPPv4N2mv16ModalTaskHandlerE "mv::ModalTaskHandler") \*modalTaskHandler, QWidget \*parent = nullptr)
        :   Construct with `parent` widget.

            Parameters:
            :   - **modalTaskHandler** – Pointer to owning modal task handler
                - **parent** – Pointer to parent widget
