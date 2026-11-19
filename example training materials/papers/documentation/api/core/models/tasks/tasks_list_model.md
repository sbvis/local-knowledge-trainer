# TasksListModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_list_model.html

**Documentation path:** `api/core/models/tasks/tasks_list_model.html`

---

# TasksListModel

**Qualified name:** `mv::TasksListModel`

class TasksListModel : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")
:   Tasks model class.

    Standard item model class for tasks

    **Author**
    :   Thomas Kroes

    Public Functions

    TasksListModel(QObject \*parent = nullptr)
    :   Construct with `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    QPointer<[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")> getTask(const std::int32\_t &rowIndex) const
    :   Get task by `rowIndex`.

        Parameters:
        :   **rowIndex** – Row index of the task to get

        Returns:
        :   Pointer to task at `rowIndex`, or nullptr if no task is found
