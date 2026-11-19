# Task

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/task.html

**Documentation path:** `api/core/task/task.html`

---

# Task

**Qualified name:** `mv::Task`

`Task` is the common state and progress model behind all task presentations. It reports an operation but does not execute it. Prefer workflow-backed execution for substantial new work; use a presentation-specific task directly when another component already owns execution. See the [practical execution and task guide](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/index.html).

Important

`Task::Status` has no failed state. Preserve failures through the operation result, exception, or workflow context, and ensure the task no longer remains running.

class Task : public QObject, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) class.

    Convenience class for managing a task.

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) progress can be determined in three ways (see [Task::setProgressMode()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1ab8351a413af1cda8f352379838e8e0a1) and [Task::getProgressMode()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1af195311d97d0971c0eb827de0d58daa2)):

    - Setting progress directly setProgress(…)
    - Setting sub tasks items via one of the overloads of Task::setSubTasks() and flagging items as finished with [Task::setSubtaskFinished()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1ac1ae2037281bfe874df8d872259249c5), the percentage is then updated automatically
    - Computing the combined progress of child tasks using aggregation (initialize with parent task or use [Task::setParentTask()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1afcedf165c947f1e93761a7c9914c5436))

    Tasks have a scope which defines how the content is presented in the user interface (see Task::setScope() and Task::getScope())

    - All background tasks are aggregated into one overarching task and presented in the status bar
    - Foreground tasks automatically show up in a popup at the right of the status bar
    - Modal tasks show up in a modal tasks dialog which blocks all other user interaction

    There is no need to create a user interface to kill tasks, all scopes have controls to kill a task. Connect to the [Task::requestAbort()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a233f014be89ae47fe080327655380da8) signal to be notified when a task was aborted so that further action can be taken.

    Special notes:

    - Tasks should work cross threads (this has only been tested using QThread though)
    - For a more detail exploration of all tasks in the system, a tasks view system plugin is available
    - In case of a tasks hierarchy, all task objects should be in the same QThread context

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::ApplicationStartupTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/application_startup_task.html#classmv_1_1ApplicationStartupTask), [mv::BackgroundTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/background_task.html#classmv_1_1BackgroundTask), [mv::DatasetTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/dataset_task.html#classmv_1_1DatasetTask), [mv::ForegroundTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/foreground_task.html#classmv_1_1ForegroundTask), [mv::ModalTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/modal_task.html#classmv_1_1ModalTask)

    Public Types

    enum class ConfigurationFlag
    :   Describes the configuration options.

        *Values:*

        enumerator OverrideAggregateStatus

        enumerator Default
        :   Status is not automatically based on child tasks but will be set manually.

    enum class Status
    :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task):

        *Values:*

        enumerator Undefined

        enumerator Idle
        :   …status is undefined

        enumerator Running
        :   …is idle

        enumerator RunningIndeterminate
        :   …is currently running

        enumerator Finished
        :   …is currently running, but it’s operating time is not known

        enumerator AboutToBeAborted
        :   …has finished successfully

        enumerator Aborting
        :   …is about to be aborted

        enumerator Aborted
        :   …is in the process of being aborted

            …has been aborted

    enum class ProgressMode
    :   Progress is tracked by:

        *Values:*

        enumerator Manual

        enumerator Subtasks
        :   …setting progress percentage manually

        enumerator Aggregate
        :   …setting a number of subtasks and flagging subtasks as finished (progress percentage is computed automatically)

            …combining the progress of child tasks

    enum class GuiScope
    :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task):

        *Values:*

        enumerator None

        enumerator Background
        :   …has no explicit GUI handlers that show it in the gui (the task can still be observed in the tasks plugin)

        enumerator Foreground
        :   …will run in the background (not visible by default but can be revealed in the tasks view plugin)

        enumerator Modal
        :   …will run in the foreground (tasks with this scope will automatically appear in a tasks popup when running)

        enumerator DataHierarchy
        :   …will run modally (tasks with this scope will automatically appear in a modal tasks dialog when the needed)

    Public Functions

    Task(QObject \*parent, const QString &name, const GuiScopes &guiScopes = {[GuiScope](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task8GuiScopeE "mv::Task::GuiScope")::[None](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task8GuiScope4NoneE "mv::Task::GuiScope::None")}, const [Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status") &status = [Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status")::[Undefined](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6Status9UndefinedE "mv::Task::Status::Undefined"), bool mayKill = false, [AbstractTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html#_CPPv4N2mv19AbstractTaskHandlerE "mv::AbstractTaskHandler") \*handler = nullptr)
    :   Construct task with `parent` object, `name`, initial `status`, whether the task may be killed `mayKill` and possibly a `taskHandler`.

        Parameters:
        :   - **parent** – Pointer to parent object (simply denotes the position of the task in the QObject hierarchy and has nothing to do with the task hierarchy)
            - **name** – Name of the task
            - **guiScopes** – GUI scopes of the task
            - **status** – Initial status of the task
            - **mayKill** – Boolean determining whether the task may be killed or not
            - **handler** – Pointer to task handler

    ~Task()
    :   Remove from task manager when destructed.

    QString getTypeName(bool humanFriendly = true) const
    :   Get type (class) name (using QMetaObject)

        Parameters:
        :   **humanFriendly** – Whether to include the task namespace or not

        Returns:
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) type name

    std::int32\_t getConfiguration() const
    :   Get configuration.

        Returns:
        :   Configuration

    bool isConfigurationFlagSet([ConfigurationFlag](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task17ConfigurationFlagE "mv::Task::ConfigurationFlag") configurationFlag) const
    :   Check whether `configurationFlag` is set or not.

        Parameters:
        :   **configurationFlag** – Configuration flag

        Returns:
        :   Boolean determining whether `configurationFlag` is set or not

    void setConfigurationFlag([ConfigurationFlag](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task17ConfigurationFlagE "mv::Task::ConfigurationFlag") configurationFlag, bool unset = false, bool recursive = false)
    :   Set configuration flag.

        Parameters:
        :   - **configurationFlag** – Configuration flag to set
            - **unset** – Whether to unset the `configurationFlag` flag
            - **recursive** – Whether to recursively set child configuration flag

    void setConfiguration(std::int32\_t configuration, bool recursive = false)
    :   Set configuration.

        Parameters:
        :   - **configuration** – Configuration value
            - **recursive** – Whether to recursively set child configuration flag

    virtual float getWeight() const
    :   Get weight.

        Returns:
        :   Get relative size of the progress interval this task occupies when it is a child task

    virtual void setWeight(float weight)
    :   Set weight.

        Parameters:
        :   **weight** – Relative size of the progress interval this task occupies when it is a child task

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*getParentTask()
    :   Get parent task (if it has one)

        Returns:
        :   Pointer to parent task if it has, nullptr otherwise

    void setParentTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*parentTask)
    :   Set parent task to `parentTask`.

        Parameters:
        :   **parentTask** – Pointer to parent task

    bool hasParentTask()
    :   Determine whether the task has a parent task.

        Returns:
        :   Boolean determining whether the task has a parent task

    TasksPtrs getChildTasks(bool recursively = false, bool enabledOnly = true) const
    :   Get child tasks.

        Parameters:
        :   - **recursively** – Whether to get child tasks recursively
            - **enabledOnly** – Filter out tasks which are disabled

        Returns:
        :   Vector of pointers to child tasks

    TasksPtrs getChildTasksForStatuses(bool recursively = false, bool enabledOnly = true, const Statuses &statuses = Statuses()) const
    :   Get child tasks for `statuses`.

        Parameters:
        :   - **recursively** – Whether to get child tasks recursively
            - **enabledOnly** – Filter out tasks which are disabled
            - **status** – Filter on task status

        Returns:
        :   Vector of pointer to child tasks

    TasksPtrs getChildTasksForGuiScopes(bool recursively = false, bool enabledOnly = true, const GuiScopes &guiScopes = GuiScopes()) const
    :   Get child tasks for `guiScopes`.

        Parameters:
        :   - **recursively** – Whether to get child tasks recursively
            - **enabledOnly** – Filter out tasks which are disabled
            - **guiScopes** – Filter on task GUI scope

        Returns:
        :   Vector of pointer to child tasks

    TasksPtrs getChildTasksForGuiScopesAndStatuses(bool recursively = false, bool enabledOnly = true, const GuiScopes &guiScopes = GuiScopes(), const Statuses &statuses = Statuses()) const
    :   Get child tasks for `guiScopes` and `statuses`.

        Parameters:
        :   - **recursively** – Whether to get child tasks recursively
            - **enabledOnly** – Filter out tasks which are disabled
            - **guiScopes** – Filter on task GUI scope
            - **statuses** – Filter on task status

        Returns:
        :   Vector of pointer to child tasks

    QString getName() const
    :   Get task name.

        Returns:
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) name

    void setName(const QString &name)
    :   Set task name to `name`.

        Parameters:
        :   **name** – Name of the task

    QString getDescription() const
    :   Gets the task description.

    void setDescription(const QString &description)
    :   Sets the task description to `description`.

        Parameters:
        :   **description** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) description

    QIcon getIcon() const
    :   Gets the task icon.

    void setIcon(const QIcon &icon)
    :   Sets the task icon to `icon`.

        Parameters:
        :   **icon** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) icon

    bool getEnabled() const
    :   Get whether the task is enabled or not.

        Returns:
        :   Boolean determining whether the task is enabled or not

    void setEnabled(bool enabled, bool recursive = false)
    :   Sets whether the task is enabled or not.

        Parameters:
        :   - **enabled** – Boolean determining whether the task is enabled or not
            - **recursive** – Whether to set all descendants to `enabled` as well

    bool getVisible() const
    :   Get whether the task is visible or not.

        Returns:
        :   Boolean determining whether the task is visible or not

    void setVisible(bool visible)
    :   Sets whether the task is visible or not.

        Parameters:
        :   **visible** – Boolean determining whether the task is visible or not

    bool getMayKill() const
    :   Get whether the task may be killed or not.

        Returns:
        :   Whether the task may be killed or not

    void setMayKill(bool mayKill, bool recursive = false)
    :   Sets whether the task may be killed or not.

        Parameters:
        :   - **mayKill** – Boolean determining whether the task may be killed or not
            - **recursive** – Whether to set all descendants to `mayKill` as well

    bool isKillable() const
    :   Get whether the task is killable Return true when the following two criteria are met:

        - Task::\_status is either [Task::Status::Running](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a646b3a1ec8736860202a56133c424476a5bda814c4aedb126839228f1a3d92f09) or [Task::Status::RunningIndeterminate](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a646b3a1ec8736860202a56133c424476a07628dd82ebed81948fc0f6f9916cd71)
        - Task::\_mayKill is true

        Returns:
        :   Whether the task is killable

    void reset(bool recursive = false)
    :   Resets the task internals.

        Parameters:
        :   **recursive** – Whether to reset all descendants as well

    void setAlwaysProcessEvents(bool alwaysProcessEvents)
    :   Envoke Qt’s processEvents on updates.

        Parameters:
        :   **alwaysProcessEvents** – Whether to invoke Qt’s processEvents on updates

    bool getAlwaysProcessEvents() const
    :   Get whether the task envokes Qt processEvents on updates.

        Returns:
        :   Whether the task envokes Qt’s processEvents on updates

    [Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status") getStatus() const
    :   Get task status.

    bool isIdle() const
    :   Check if task is idle.

    bool isRunning() const
    :   Check if task is running.

    bool isRunningIndeterminate() const
    :   Check if task is running indeterminate.

    bool isFinished() const
    :   Check if task is finished.

    bool isAboutToBeAborted() const
    :   Check if task is about to be aborted.

    bool isAborting() const
    :   Check if task is being aborted.

    bool isAborted() const
    :   Check if task is aborted.

    void setStatus(const [Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status") &status, bool recursive = false)
    :   Set task status to `status`, possibly `recursive`.

        Parameters:
        :   - **status** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) status
            - **recursive** – Whether to set all descendants statuses as well

    void setStatusDeferred(const [Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status") &status, bool recursive = false, std::uint32\_t delay = DEFERRED\_TASK\_STATUS\_INTERVAL)
    :   Set task status deferred to `status`, possibly `recursively` and after `delay`.

        Parameters:
        :   - **status** – Deferred task status
            - **recursive** – Whether to set all descendants statuses as well
            - **delay** – Delay after which the deferred task status is set

    void setUndefined()
    :   Convenience method to set task status to undefined.

    void setIdle()
    :   Convenience method to set task status to idle.

    void setRunning()
    :   Convenience method to set task status to running.

    void setRunningIndeterminate()
    :   Convenience method to set task status to running indeterminate.

    void setFinished()
    :   Convenience method to set task status to finished and use a custom progress description.

    void setAboutToBeAborted()
    :   Convenience method to set task status to about to be aborted.

    void setAborting()
    :   Convenience method to set task status to aborting.

    void setAborted()
    :   Convenience method to set task status to aborted.

    void kill(bool recursive = true)
    :   Kill the task and trigger Task::abort() signal.

        Parameters:
        :   **recursive** – Boolean determining whether to also kill chill tasks recursively

    [AbstractTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html#_CPPv4N2mv19AbstractTaskHandlerE "mv::AbstractTaskHandler") \*getHandler()
    :   Get task handler.

        Returns:
        :   Pointer to task handler

    void setHandler([AbstractTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html#_CPPv4N2mv19AbstractTaskHandlerE "mv::AbstractTaskHandler") \*handler)
    :   Set task handler to `handler`.

        Parameters:
        :   **handler** – Pointer to task handler

    [ProgressMode](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task12ProgressModeE "mv::Task::ProgressMode") getProgressMode() const
    :   Get progress mode.

        Returns:
        :   Progress mode enum

    void setProgressMode(const [ProgressMode](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task12ProgressModeE "mv::Task::ProgressMode") &progressMode)
    :   Sets progress mode to to `progressMode`.

        Parameters:
        :   **progressMode** – Progress mode

    GuiScopes getGuiScopes() const
    :   Get GUI scopes.

        Returns:
        :   GUI scopes

    void setGuiScopes(const GuiScopes &guiScopes)
    :   Sets GUI scopes to `guiScopes`.

        Parameters:
        :   **guiScopes** – GUI scope enum

    void addGuiScope(const [GuiScope](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task8GuiScopeE "mv::Task::GuiScope") &guiScope)
    :   Add `guiScope` to the GUI scopes set.

        Parameters:
        :   **guiScope** – GUI scope to add

    void removeGuiScope(const [GuiScope](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task8GuiScopeE "mv::Task::GuiScope") &guiScope)
    :   Remove `guiScope` from the GUI scopes set.

        Parameters:
        :   **guiScope** – GUI scope to remove

    bool doGuiScopesOverlap(const GuiScopes &guiScopesA, const GuiScopes &guiScopesB) const
    :   Function to establish whether at lease one GUI scope is present in both `guiScopesA` and `guiScopesB`.

        Parameters:
        :   - **guiScopesA** – GUI scopes A
            - **guiScopesB** – GUI scopes B

    float getProgress() const
    :   Gets the task progress [0, 1].

    virtual void setProgress(float progress, const QString &subtaskDescription = "")
    :   Sets the task progress percentage to `progress` This method only has an effect when Task::\_progressMode is set to [ProgressMode::Manual](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61ae1ba155a9f2e8c3be94020eef32a0301).

        Parameters:
        :   - **progress** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) progress, clamped to [0, 1]
            - **subtaskDescription** – Subtask description associated with the progress update

    virtual void resetProgress(bool recursive = false)
    :   Re-sets the task progress percentage to zero.

        Parameters:
        :   **recursive** – Boolean determining whether to also set the descendant tasks

    QTimer &getTimer(const TimerType &timerType)
    :   Get timer by `timerType`.

        Returns:
        :   [Timer](https://manivault.readthedocs.io/en/latest/api/core/util/timer/timer.html#classTimer) for `timerType`

    void setTimerInterval(const TimerType &timerType, std::uint32\_t interval)
    :   Set timer `interval` for `timerType`.

        Parameters:
        :   - **timerType** – Type of timer to set `interval` for
            - **interval** – Interval for `timerType`

    void setSubtasks(std::uint32\_t numberOfSubtasks)
    :   Initializes the subtasks with `numberOfSubtasks` This method sets the Task::\_progressMode to [ProgressMode::Subtasks](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61a024e2c2f409b3f3932f59ebedf891a39).

        Parameters:
        :   **numberOfSubtasks** – Number of subtasks

    void setSubtasks(const QStringList &subtasksNames)
    :   Initializes the subtasks with `subtasksNames` This method sets the Task::\_progressMode to [ProgressMode::Subtasks](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61a024e2c2f409b3f3932f59ebedf891a39).

        Parameters:
        :   **subtasksNames** – Subtasks names

    void setSubtaskStarted(std::uint32\_t subtaskIndex, const QString &progressDescription = QString())
    :   Flag item with `subtaskIndex` as started Assumes the number of tasks has been set prior with [Task::setSubtasks()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1adde0b238ccc96c6a33485d9533c3559f) This method only has an effect when Task::\_progressMode is set to [ProgressMode::Subtasks](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61a024e2c2f409b3f3932f59ebedf891a39).

        Parameters:
        :   - **subtaskIndex** – Index of the subtask
            - **progressDescription** – Override the default progress description when set to a non-empty string

    void setSubtaskStarted(const QString &subtaskName, const QString &progressDescription = QString())
    :   Flag item with `subtaskName` as started Assumes the number of tasks has been set prior with [Task::setSubtasks()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1adde0b238ccc96c6a33485d9533c3559f) This method only has an effect when Task::\_progressMode is set to [ProgressMode::Subtasks](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61a024e2c2f409b3f3932f59ebedf891a39).

        Parameters:
        :   - **subtaskName** – Name of the subtask
            - **progressDescription** – Override the default progress description when set to a non-empty string

    void setSubtaskFinished(std::uint32\_t subtaskIndex, const QString &progressDescription = QString())
    :   Flag item with `subtaskIndex` as finished, the progress percentage will be computed automatically Assumes the number of tasks has been set prior with [Task::setSubtasks()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1adde0b238ccc96c6a33485d9533c3559f) This method only has an effect when Task::\_progressMode is set to [ProgressMode::Subtasks](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61a024e2c2f409b3f3932f59ebedf891a39).

        Parameters:
        :   - **subtaskIndex** – Index of the subtask
            - **progressDescription** – Override the default progress description when set to a non-empty string

    void setSubtaskFinished(const QString &subtaskName, const QString &progressDescription = QString())
    :   Flag item with `subtaskName` as finished, the progress percentage will be computed automatically Assumes the number of tasks has been set prior with [Task::setSubtasks()](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1adde0b238ccc96c6a33485d9533c3559f) If `subtaskName` is not found, the progress will not be updated (ensure that subtasks names are set with Task::setSubtasksNames() or Task::setSubtasksName()) This method only has an effect when Task::\_progressMode is set to [ProgressMode::Subtasks](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61a024e2c2f409b3f3932f59ebedf891a39).

        Parameters:
        :   - **subtaskName** – Name of the subtask
            - **progressDescription** – Override the default progress description when set to a non-empty string

    void setSubtaskName(std::uint32\_t subtaskIndex, const QString &subtaskName)
    :   Set subtask name to `subtaskName` for `subtaskIndex` This method only has an effect when Task::\_progressMode is set to [ProgressMode::Subtasks](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61a024e2c2f409b3f3932f59ebedf891a39).

        Parameters:
        :   - **subtaskIndex** – Subtask index to set the description for
            - **subtaskName** – Name of the subtask

    QStringList getSubtasksNames() const
    :   Get subtask names.

        Returns:
        :   Subtasks names

    QString getSubtasksName(std::uint32\_t subtaskIndex) const
    :   Get subtask name for `subtaskIndex`.

        Parameters:
        :   **subtaskIndex** – Index of the subtask

        Returns:
        :   Subtasks name for `subtaskIndex`, empty string if not found

    std::int32\_t getSubtaskIndex(const QString &subtaskName) const
    :   Get subtask index for `subtaskName` Returns -1 when `subtaskName` is not found or Task::\_progressMode is set to [ProgressMode::Manual](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task_1a4476ad9cb2e2740039affed5f7503e61ae1ba155a9f2e8c3be94020eef32a0301).

        Parameters:
        :   **subtaskName** – Name of the subtask

    QString getSubtaskNamePrefix() const
    :   Get subtask name prefix.

        Returns:
        :   String to prefix unnamed subtasks with

    void setSubtaskNamePrefix(const QString &subtaskNamePrefix)
    :   Set subtask name prefix to `subtaskNamePrefix`.

        Parameters:
        :   **subtaskNamePrefix** – String to prefix unnamed subtasks with

    QString getProgressDescription() const
    :   Get progress description.

        Returns:
        :   Progress description

    void setProgressDescription(const QString &progressDescription, std::uint32\_t clearDelay = 0)
    :   Set progress description to `progressDescription`.

        Parameters:
        :   - **progressDescription** – Progress description
            - **clearDelay** – Progress description will be cleared after this delay (do not clear if zero)

    QString getProgressText() const
    :   Gets the task progress text.

    void setProgressTextFormatter(const ProgressTextFormatter &progressTextFormatter)
    :   Set progress text formatter to `progressTextFormatter`.

        Parameters:
        :   **progressTextFormatter** – Progress formatter function

    void addToTaskManager()
    :   Adds this task to the task manager Under normal circumstances, tasks are automatically added to the task manager during construction.

        In some cases, the task manager is not yet present then and therefore this method allows to manually add this task to the task manager at a later point in time. Only use this in edge cases!

    void nameChanged(const QString &name)
    :   Signals that the task name changed to `name`.

        Parameters:
        :   **name** – Modified name

    void configurationFlagToggled(const [ConfigurationFlag](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task17ConfigurationFlagE "mv::Task::ConfigurationFlag") &configurationFlag, bool set)
    :   Signals that `configurationFlag` is `set`.

        Parameters:
        :   - **configurationFlag** – Toggled configuration flag
            - **set** – Whether the flag was set or unset

    void configurationChanged(std::int32\_t configuration)
    :   Signals that the configuration changed.

        Parameters:
        :   **configuration** – New configuration

    void descriptionChanged(const QString &description)
    :   Signals that the task description changed to `description`.

        Parameters:
        :   **description** – Modified description

    void iconChanged(const QIcon &icon)
    :   Signals that the task icon changed to `icon`.

        Parameters:
        :   **icon** – Modified icon

    void enabledChanged(bool enabled)
    :   Signals that the task enabled state changed to `enabled`.

        Parameters:
        :   **enabled** – Whether the task is enabled

    void visibileChanged(bool visible)
    :   Signals that the task visibility changed to `visible`.

        Parameters:
        :   **visible** – Whether the task is visible in the user interface

    void handlerChanged([AbstractTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html#_CPPv4N2mv19AbstractTaskHandlerE "mv::AbstractTaskHandler") \*handler)
    :   Signals that the task handler changed to `handler`.

        Parameters:
        :   **handler** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) handler

    void statusChanged(const [Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status") &previousStatus, const [Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status") &status)
    :   Signals that the task status changed from `previousStatus` to `status`.

        Parameters:
        :   - **previousStatus** – Status before the modification
            - **status** – Modified name

    void mayKillChanged(bool mayKill)
    :   Signals that may kill changed to `mayKill`.

        Parameters:
        :   **mayKill** – Boolean determining whether the task may be killed or not

    void isKillableChanged(bool killable)
    :   Signals that killable changed to `killable`.

        Parameters:
        :   **killable** – Boolean determining whether the task is killable or not

    void statusChangedToUndefined()
    :   Signals that the task status changed to undefined.

    void statusChangedToIdle()
    :   Signals that the task became idle.

    void statusChangedToRunning()
    :   Signals that the task started running.

    void statusChangedToRunningIndeterminate()
    :   Signals that the task started running indeterminately.

    void statusChangedToFinished()
    :   Signals that the task finished.

    void statusChangedToAboutToBeAborted()
    :   Signals that the task is about to be aborted.

    void statusChangedToAborting()
    :   Signals that the task is aborting.

    void statusChangedToAborted()
    :   Signals that the task is aborted.

    void requestAbort()
    :   Requests the involved task algorithms to abort their work.

    void progressModeChanged(const [ProgressMode](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task12ProgressModeE "mv::Task::ProgressMode") &progressMode)
    :   Signals that the task progress mode changed to `progressMode`.

        Parameters:
        :   **progressMode** – Modified progress mode

    void guiScopesChanged(const GuiScopes &guiScopes)
    :   Signals that the task GUI scopes changed to `guiScopes`.

        Parameters:
        :   **guiScopes** – Modified GUI scopes

    void progressChanged(float progress)
    :   Signals that the task progress changed to `progress`.

        Parameters:
        :   **progress** – Modified progress

    void subtasksAdded(const QStringList &subtasksNames)
    :   Signals that subtasks with `subtasksNames` have been added.

        Parameters:
        :   **subtasksNames** – Added subtasks names

    void subtasksChanged(const QBitArray &subtasks, const QStringList &subtasksNames)
    :   Signals that subtasks changed to `subtasks`.

        Parameters:
        :   - **subtasks** – Modified subtasks
            - **subtasksNames** – Modified subtasks names

    void subtaskStarted(const QString &subTaskName)
    :   Signals that subtask with `name` started.

        Parameters:
        :   **subTaskName** – Name of the subtask that started

    void subtaskFinished(std::uint32\_t subtaskIndex, const QString &subtaskName = "")
    :   Signals that subtask with `subtaskIndex` finished.

        Parameters:
        :   - **subtaskIndex** – Index of the subtask that finished
            - **subtaskName** – Name of the subtask that finished (set when Task::\_subtasksNames is set)

    void subtaskNamePrefixChanged(const QString &previousSubtaskNamePrefix, const QString &currentSubtaskNamePrefix)
    :   Signals that subtask name prefix changed from `previousSubtaskNamePrefix` to `currentSubtaskNamePrefix`.

        Parameters:
        :   - **previousSubtaskNamePrefix** – Previous subtask name prefix
            - **currentSubtaskNamePrefix** – Current subtask name prefix

    void progressDescriptionChanged(const QString &progressDescription)
    :   Signals that the progress description changed to `progressDescription`.

        Parameters:
        :   **progressDescription** – Modified progress description

    void progressTextChanged(const QString &progressText)
    :   Signals that the progress text changed to `progressText`.

        Parameters:
        :   **progressText** – Current progress text

    void parentTaskChanged([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*previousParentTask, [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*currentParentTask)
    :   Signals that the parent task changed from `previousParentTask` to `currentParentTask`.

        Parameters:
        :   - **previousParentTask** – Pointer to previous parent task (maybe nullptr)
            - **currentParentTask** – Pointer to previous parent task (maybe nullptr)

    void childTaskAdded([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*childTask)
    :   Signals that `childTask` has been added.

        Parameters:
        :   **childTask** – Pointer to child task that was added

    void childTaskAboutToBeRemoved([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*childTask)
    :   Signals that `childTask` is about to be removed from the list of children.

        Parameters:
        :   **childTask** – Pointer to child task that is about to be removed from the list of children

    void childTaskRemoved([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*childTask)
    :   Signals that `childTask` has been removed from the list of children.

        Parameters:
        :   **childTask** – Pointer to child task that has been removed from the list of children

    Public Static Functions

    static QStringList guiScopesToStringlist(const GuiScopes &guiScopes)
    :   Convert `guiScopes` to string list.

        Returns:
        :   String list of gui scopes

    Public Static Attributes

    static QMap<[Status](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task6StatusE "mv::Task::Status"), QString> statusNames
    :   Couples status enum value to status name string.

    static QMap<[ProgressMode](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task12ProgressModeE "mv::Task::ProgressMode"), QString> progressModeNames
    :   Couples scope enum value to scope name string.

    static QMap<[GuiScope](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4Task8GuiScopeE "mv::Task::GuiScope"), QString> guiScopeNames
    :   Couples scope enum value to scope name string.

    Protected Functions

    virtual void addChildTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*childTask)
    :   Adds `childTask` to children.

        Parameters:
        :   **childTask** – Pointer to child task to add

    virtual void removeChildTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*childTask)
    :   Removes `childTask` from children.

        Parameters:
        :   **childTask** – Pointer to child task to remove
