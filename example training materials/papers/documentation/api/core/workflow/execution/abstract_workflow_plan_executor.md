# Abstract workflow plan executor

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/abstract_workflow_plan_executor.html

**Documentation path:** `api/core/workflow/execution/abstract_workflow_plan_executor.html`

---

# Abstract workflow plan executor

The public execution contract for root and nested plans, with blocking and asynchronous entry points.

class AbstractWorkflowPlanExecutor : public QObject
:   Abstract base class for workflow plan executors.

    A workflow plan executor is responsible for executing [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan) instances, managing workflow execution contexts, dispatching jobs to the appropriate execution thread, tracking progress, and producing [WorkflowResult](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/workflow_result.html#classmv_1_1workflow_1_1WorkflowResult) objects.

    Workflow plans can be executed either as root workflows or as nested child workflows. Root workflows own their execution lifecycle and optionally create tasks, notifications, and progress reporting infrastructure. Child workflows execute within an existing [WorkflowExecutionContext](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#classmv_1_1workflow_1_1WorkflowExecutionContext) and contribute their results to the parent workflow.

    Concrete implementations define the execution strategy, scheduling model, threading behavior, and workflow compilation process.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    See also

    [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan)

    See also

    [WorkflowExecutionContext](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#classmv_1_1workflow_1_1WorkflowExecutionContext)

    See also

    [WorkflowResult](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/workflow_result.html#classmv_1_1workflow_1_1WorkflowResult)

    Public Functions

    AbstractWorkflowPlanExecutor(QObject \*parent = nullptr)
    :   Constructs a workflow plan executor.

        Parameters:
        :   **parent** – Optional QObject parent.

    virtual [WorkflowResultFuture](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html#_CPPv4N2mv8workflow20WorkflowResultFutureE "mv::workflow::WorkflowResultFuture") execute(UniqueWorkflowPlan workflowPlan, SharedWorkflowExecutionContext parentContext = nullptr, OptionalWorkflowOptions options = std::nullopt) = 0
    :   Executes a workflow asynchronously.

        If no parent execution context is supplied, the workflow is executed as a root workflow. Otherwise it is executed as a child workflow within the supplied execution context.

        The returned future can be used to monitor execution progress and obtain the final [WorkflowResult](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/workflow_result.html#classmv_1_1workflow_1_1WorkflowResult) when execution completes.

        Parameters:
        :   - **workflowPlan** – Workflow plan to execute.
            - **parentContext** – Optional parent workflow execution context.
            - **options** – Optional execution configuration.

        Returns:
        :   Future representing the workflow execution.

    virtual SharedWorkflowResult executeBlocking(UniqueWorkflowPlan workflowPlan, [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task = nullptr, [WorkflowOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html#_CPPv4N2mv8workflow15WorkflowOptionsE "mv::workflow::WorkflowOptions") options = {}) = 0
    :   Executes a workflow synchronously as a root workflow.

        The calling thread is blocked until execution completes.

        Implementations may create a root execution context, progress task, notifications, tracing infrastructure, and other root-level resources.

        Parameters:
        :   - **workflowPlan** – Workflow plan to execute.
            - **task** – Optional task associated with the workflow.
            - **options** – Workflow execution options.

        Returns:
        :   Final workflow result.

    virtual SharedWorkflowResult executeBlocking(UniqueWorkflowPlan workflowPlan, SharedWorkflowExecutionContext parentContext) = 0
    :   Executes a workflow synchronously as a child workflow.

        The workflow executes within the supplied parent execution context and contributes its progress, outputs, and lifecycle events to the parent.

        Parameters:
        :   - **workflowPlan** – Workflow plan to execute.
            - **parentContext** – Parent workflow execution context.

        Returns:
        :   Final workflow result.

    Public Static Functions

    static SharedWorkflowResult waitForAsync([WorkflowResultFuture](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html#_CPPv4N2mv8workflow20WorkflowResultFutureE "mv::workflow::WorkflowResultFuture")::[State](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html#_CPPv4N2mv8workflow20WorkflowResultFuture5StateE "mv::workflow::WorkflowResultFuture::State") &state)
    :   Waits for asynchronous workflow completion.

        This helper blocks until the supplied asynchronous execution state has completed and then returns the resulting workflow result.

        Parameters:
        :   **state** – Asynchronous workflow state.

        Returns:
        :   Final workflow result.

    static void installNotificationLinkHandler()
    :   Installs the workflow notification link handler.

        Implementations use this to register handlers that allow users to open workflow results, logs, traces, or other workflow-related resources from notifications.
