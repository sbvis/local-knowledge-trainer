# AbstractTaskManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_task_manager.html

**Documentation path:** `api/core/managers/abstract_task_manager.html`

---

# AbstractTaskManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the tasks manager
mv::tasks()->...
```

## Related

- Tasks [models](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/index.html)

**Qualified name:** `mv::AbstractTaskManager`

class AbstractTaskManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract task manager class.

    Base abstract task manager class for global task management.

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractTaskManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    inline virtual void initialize() override
    :   Perform manager startup initialization.

    virtual Tasks getTasks() = 0
    :   Get all tasks.

        Returns:
        :   Vector of tasks

    template<typename TaskHandlerType> inline Tasks getTasksByHandlerTypeAndStatus(const [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")::[Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status") &status)
    :   Get tasks by handler type and `status`.

        Returns:
        :   Vector of tasks

    void taskAdded([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
    :   Signals that `task` is added.

        Parameters:
        :   **task** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) which is added

    void taskAboutToBeRemoved([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
    :   Signals that `task` is about to be removed.

        Parameters:
        :   **task** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) which is about to be removed

    void taskRemoved(const QString &taskId)
    :   Signals that task with `taskId` is removed.

        Parameters:
        :   **taskId** – Globally unique identifier of the task which is removed

    Protected Functions

    virtual void addTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task) = 0
    :   Adds `task` to the task manager.

        Parameters:
        :   **task** – Pointer to task to add

    virtual void removeTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task) = 0
    :   Removes `task` from the task manager.

        Parameters:
        :   **task** – Pointer to task to remove
