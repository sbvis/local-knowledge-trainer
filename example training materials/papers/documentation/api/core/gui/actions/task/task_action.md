# TaskAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/task_action.html

**Documentation path:** `api/core/gui/actions/task/task_action.html`

---

# TaskAction

**Qualified name:** `mv::gui::TaskAction`

class TaskAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) action class.

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) action class for interacting with a task

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator ProgressBar

        enumerator KillButton
        :   Widget includes a progress bar.

        enumerator Default
        :   Widget includes a button to kill the task.

    Public Functions

    Q\_INVOKABLE TaskAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*getTask()
    :   get task

        Returns:
        :   Pointer to task to keep track of

    void setTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
    :   Set task to `task`.

        Parameters:
        :   **task** – Pointer to task to keep track of

    [ProgressAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/progress_action.html#_CPPv4N2mv3gui14ProgressActionE "mv::gui::ProgressAction") &getProgressAction()
    :   Get progress action.

        Returns:
        :   Reference to built-in progress action

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") &getKillTaskAction()
    :   Get kill task action.

        Returns:
        :   Reference to built-in trigger action for killing the task

    void taskChanged([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*previousTask, [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
    :   Signals that the current task changed to `task`.

        Parameters:
        :   - **previousTask** – Pointer to previous task
            - **task** – Pointer to current task
