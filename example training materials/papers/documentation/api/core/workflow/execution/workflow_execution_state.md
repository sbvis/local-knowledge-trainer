# Workflow execution state

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_state.html

**Documentation path:** `api/core/workflow/execution/workflow_execution_state.html`

---

# Workflow execution state

Shared root state containing progress, reports, options, metrics, status, outputs, and cancellation.

class WorkflowExecutionState
:   Shared mutable state for a workflow execution tree.

    [WorkflowExecutionState](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_state.html#classmv_1_1workflow_1_1WorkflowExecutionState) owns the root report and progress nodes, execution options, aggregate metrics, execution status, published result values, and routed workflow outputs. It is shared by all [WorkflowExecutionContext](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#classmv_1_1workflow_1_1WorkflowExecutionContext) objects that belong to one root workflow execution.

    The state protects mutable maps and status fields because workflow stages and jobs may update them from different worker threads after the execution refactor.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Types

    using Ptr = std::shared\_ptr<[WorkflowExecutionState](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_state.html#_CPPv4N2mv8workflow22WorkflowExecutionStateE "mv::workflow::WorkflowExecutionState")>
    :   Shared pointer type for workflow execution state objects.

    Public Functions

    WorkflowExecutionState(const [WorkflowReportNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_report_node.html#_CPPv4N2mv8workflow18WorkflowReportNodeE "mv::workflow::WorkflowReportNode")::[SharedWorkflowReportNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_report_node.html#_CPPv4N2mv8workflow18WorkflowReportNode24SharedWorkflowReportNodeE "mv::workflow::WorkflowReportNode::SharedWorkflowReportNode") &reportRoot, const [WorkflowProgressNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNodeE "mv::workflow::WorkflowProgressNode")::[Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode3PtrE "mv::workflow::WorkflowProgressNode::Ptr") &progressRoot, [WorkflowOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html#_CPPv4N2mv8workflow15WorkflowOptionsE "mv::workflow::WorkflowOptions") options = {})
    :   Constructs shared workflow execution state.

        Parameters:
        :   - **reportRoot** – Root report node for lifecycle and diagnostic messages.
            - **progressRoot** – Root progress node for progress aggregation.
            - **options** – Workflow execution options.

    [WorkflowReportNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_report_node.html#_CPPv4N2mv8workflow18WorkflowReportNodeE "mv::workflow::WorkflowReportNode")::[SharedWorkflowReportNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_report_node.html#_CPPv4N2mv8workflow18WorkflowReportNode24SharedWorkflowReportNodeE "mv::workflow::WorkflowReportNode::SharedWorkflowReportNode") getReportRoot() const
    :   Returns the root report node.

        Returns:
        :   Root report node for this execution.

    [WorkflowProgressNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNodeE "mv::workflow::WorkflowProgressNode")::[Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode3PtrE "mv::workflow::WorkflowProgressNode::Ptr") getProgressRoot() const
    :   Returns the root progress node.

        Returns:
        :   Root progress node for this execution.

    [WorkflowOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html#_CPPv4N2mv8workflow15WorkflowOptionsE "mv::workflow::WorkflowOptions") getOptions() const
    :   Returns the workflow options.

        Returns:
        :   Options captured for this execution.

    WorkflowExecutionStatus getStatus() const
    :   Returns the workflow execution status.

        Returns:
        :   Current execution status.

    void setStatus(WorkflowExecutionStatus status)
    :   Updates the workflow execution status.

        Parameters:
        :   **status** – New workflow execution status.

    double getOverallProgress() const
    :   Returns overall workflow progress.

        Returns:
        :   Aggregated progress of the root progress node.

    WorkflowMessages collectMessages() const
    :   Collects messages from the report tree.

        Returns:
        :   Messages collected recursively from the report tree.

    [WorkflowExecutionMetrics](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_execution_metrics.html#_CPPv4N2mv8workflow24WorkflowExecutionMetricsE "mv::workflow::WorkflowExecutionMetrics") &metrics()
    :   Returns the mutable execution metrics accumulator.

        Returns:
        :   Execution metrics accumulator.

    const [WorkflowExecutionMetrics](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_execution_metrics.html#_CPPv4N2mv8workflow24WorkflowExecutionMetricsE "mv::workflow::WorkflowExecutionMetrics") &metrics() const
    :   Returns the execution metrics accumulator.

        Returns:
        :   Const execution metrics accumulator.

    void publishResultValue(const QUuid &contextId, const QString &key, const QVariant &value)
    :   Publishes a named result value for an execution context.

        Parameters:
        :   - **contextId** – Identifier of the context that owns the value.
            - **key** – Value key within the context result map.
            - **value** – Value to store.

    QVariantMap takeResultValues(const QUuid &contextId)
    :   Takes and removes all published result values for a context.

        Parameters:
        :   **contextId** – Identifier of the context whose values should be taken.

        Returns:
        :   Result values published for the context.

    inline void setOutput(const QUuid &id, const QVariant &value)
    :   Stores an output value under an output identifier.

        Parameters:
        :   - **id** – Output identifier, typically from a [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#classmv_1_1workflow_1_1WorkflowHandle) or context output id.
            - **value** – Output value to store.

    inline QVariant takeOutput(const QUuid &id)
    :   Takes and removes an output value.

        Parameters:
        :   **id** – Output identifier to read.

        Returns:
        :   Stored output value, or an invalid QVariant when no output exists.
