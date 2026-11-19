# Workflow execution notifier

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_notifier.html

**Documentation path:** `api/core/workflow/execution/workflow_execution_notifier.html`

---

# Workflow execution notifier

A Qt notifier that bridges aggregate workflow progress to observers such as ManiVault tasks.

class WorkflowExecutionNotifier : public QObject
:   QObject notifier for workflow execution UI updates.

    [WorkflowExecutionNotifier](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_notifier.html#classmv_1_1workflow_1_1WorkflowExecutionNotifier) exposes workflow progress and status changes as Qt signals so UI components can observe execution without coupling to the executor internals.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Functions

    explicit WorkflowExecutionNotifier(QObject \*parent = nullptr)
    :   Constructs a workflow execution notifier.

        Parameters:
        :   **parent** – Optional parent object.

    void setTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
    :   Sets the task whose progress is observed.

        Parameters:
        :   **task** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) to observe, or nullptr.

    void progressChanged(double overallProgress)
    :   Emitted when the overall workflow progress changes.

        Parameters:
        :   **overallProgress** – Normalized workflow progress.

    void messagesChanged()
    :   Emitted when workflow messages change.

    void statusChanged()
    :   Emitted when workflow execution status changes.
