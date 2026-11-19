# Workflow execution context

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html

**Documentation path:** `api/core/workflow/context/workflow_execution_context.html`

---

# Workflow execution context

The node-local runtime interface to shared state, progress, reporting, outputs, and cancellation.

class WorkflowExecutionContext : public std::enable\_shared\_from\_this<[WorkflowExecutionContext](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContextE "mv::workflow::WorkflowExecutionContext")>
:   Runtime context for one workflow execution node.

    [WorkflowExecutionContext](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#classmv_1_1workflow_1_1WorkflowExecutionContext) binds together the report node, progress node, shared execution state, optional task, and hierarchy metadata for a workflow, stage, or job. Contexts form a tree that mirrors the workflow plan during execution.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Types

    using ReportNodePtr = [WorkflowReportNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_report_node.html#_CPPv4N2mv8workflow18WorkflowReportNodeE "mv::workflow::WorkflowReportNode")::[SharedWorkflowReportNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_report_node.html#_CPPv4N2mv8workflow18WorkflowReportNode24SharedWorkflowReportNodeE "mv::workflow::WorkflowReportNode::SharedWorkflowReportNode")
    :   Shared report node pointer type used by execution contexts.

    using ProgressNodePtr = [WorkflowProgressNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNodeE "mv::workflow::WorkflowProgressNode")::[Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode3PtrE "mv::workflow::WorkflowProgressNode::Ptr")
    :   Shared progress node pointer type used by execution contexts.

    using StatePtr = [WorkflowExecutionState](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_state.html#_CPPv4N2mv8workflow22WorkflowExecutionStateE "mv::workflow::WorkflowExecutionState")::[Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_state.html#_CPPv4N2mv8workflow22WorkflowExecutionState3PtrE "mv::workflow::WorkflowExecutionState::Ptr")
    :   Shared execution state pointer type used by execution contexts.

    using Type = [WorkflowExecutionNodeType](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/workflow_execution_node_type.html#_CPPv4N2mv8workflow25WorkflowExecutionNodeTypeE "mv::workflow::WorkflowExecutionNodeType")
    :   Semantic execution node type.

    Public Functions

    WorkflowExecutionContext()
    :   Constructs an empty workflow execution context.

    WorkflowExecutionContext(QString name, [ReportNodePtr](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext13ReportNodePtrE "mv::workflow::WorkflowExecutionContext::ReportNodePtr") reportNode, [ProgressNodePtr](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext15ProgressNodePtrE "mv::workflow::WorkflowExecutionContext::ProgressNodePtr") progressNode, [StatePtr](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext8StatePtrE "mv::workflow::WorkflowExecutionContext::StatePtr") state, [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task = nullptr, [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"))
    :   Constructs a workflow execution context.

        Parameters:
        :   - **name** – Human-readable context name.
            - **reportNode** – Report node associated with this context.
            - **progressNode** – Progress node associated with this context.
            - **state** – Shared execution state.
            - **task** – Optional task used for GUI progress reporting.
            - **progressMode** – Progress aggregation mode for this context.

    inline [Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext4TypeE "mv::workflow::WorkflowExecutionContext::Type") getType() const
    :   Returns the semantic execution node type.

        Returns:
        :   Semantic execution node type for this context.

    inline void setType([Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext4TypeE "mv::workflow::WorkflowExecutionContext::Type") type)
    :   Sets the semantic execution node type.

        Parameters:
        :   **type** – New semantic execution node type.

    SharedWorkflowExecutionContext createChild([Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext4TypeE "mv::workflow::WorkflowExecutionContext::Type") type, const QString &name, double weight = 1.0, [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"))
    :   Creates a child context of the requested semantic type.

        Parameters:
        :   - **type** – Semantic type of the child context.
            - **name** – Child context name.
            - **weight** – Relative progress contribution of the child.
            - **progressMode** – Progress aggregation mode for the child.

        Returns:
        :   Child execution context, or nullptr if this context is invalid.

    SharedWorkflowExecutionContext createWorkflowChild(const QString &name, double weight = 1.0, [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"))
    :   Creates a workflow child context.

        This function creates a new workflow execution context that inherits execution state, reporting infrastructure, progress tracking infrastructure, and task association from the current context while establishing a new execution hierarchy level for a child workflow.

        The created child context:

        - Shares the same workflow execution state
        - Shares the same task association
        - Extends the execution path hierarchy
        - Creates child report and progress nodes
        - Establishes a unique result scope
        - Receives its own unique execution identifier
        - Is classified as a Workflow execution context

        Parameters:
        :   - **name** – Human-readable name of the child workflow context.
            - **weight** – Relative progress contribution weight of the child workflow.
            - **progressMode** – Progress reporting mode used by the child workflow.

        Returns:
        :   Shared pointer to the newly created workflow execution context.

    SharedWorkflowExecutionContext createNestedWorkflowChild(const QString &name, double weight = 1.0, [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"))
    :   Creates a nested workflow child context.

        Parameters:
        :   - **name** – Human-readable child context name.
            - **weight** – Relative progress contribution of the child.
            - **progressMode** – Progress aggregation mode for the child.

        Returns:
        :   Nested workflow child context.

    SharedWorkflowExecutionContext createSequentialStageChild(const QString &name, double weight = 1.0, [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"))
    :   Creates a sequential stage child context.

        Parameters:
        :   - **name** – Human-readable child context name.
            - **weight** – Relative progress contribution of the child.
            - **progressMode** – Progress aggregation mode for the child.

        Returns:
        :   Sequential stage child context.

    SharedWorkflowExecutionContext createParallelStageChild(const QString &name, double weight = 1.0, [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"))
    :   Creates a parallel stage child context.

        Parameters:
        :   - **name** – Human-readable child context name.
            - **weight** – Relative progress contribution of the child.
            - **progressMode** – Progress aggregation mode for the child.

        Returns:
        :   [Parallel](https://manivault.readthedocs.io/en/latest/api/core/parallel/parallel.html#classmv_1_1Parallel) stage child context.

    SharedWorkflowExecutionContext createJobChild(const QString &name, double weight = 1.0, [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"))
    :   Creates a job child context.

        Parameters:
        :   - **name** – Human-readable child context name.
            - **weight** – Relative progress contribution of the child.
            - **progressMode** – Progress aggregation mode for the child.

        Returns:
        :   Job child context.

    SharedWorkflowExecutionContext createTypedChild([Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext4TypeE "mv::workflow::WorkflowExecutionContext::Type") type, const QString &name, double weight, [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode)
    :   Creates a typed child context.

        Parameters:
        :   - **type** – Semantic child context type.
            - **name** – Human-readable child context name.
            - **weight** – Relative progress contribution of the child.
            - **progressMode** – Progress aggregation mode for the child.

        Returns:
        :   Typed child execution context.

    bool isRootExecution() const
    :   Returns whether this context has no parent.

        Returns:
        :   True for root execution contexts.

    void reportStarted() const
    :   Reports this context as started.

    void reportFinished(std::uint64\_t durationMs = 0)
    :   Reports this context as finished.

    void reportFailed(util::[SeverityLevel](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv4util13SeverityLevelE "mv::util::SeverityLevel") severity, const QString &errorMessage, QVariantMap extraDetails = {})
    :   Reports this context as failed.

    void reportSkipped(const QString &reason)
    :   Reports this context as skipped.

    void reportStageSummary(const [WorkflowStageSummary](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_stage_summary.html#_CPPv4N2mv8workflow20WorkflowStageSummaryE "mv::workflow::WorkflowStageSummary") &summary) const
    :   Reports a stage summary on this context.

    QVariantMap makeLifecycleDetails(const QString &event, std::uint64\_t durationMs = 0) const
    :   Builds standard lifecycle details for report messages.

        Parameters:
        :   - **event** – Lifecycle event name.
            - **durationMs** – Optional event duration in milliseconds.

        Returns:
        :   Variant map with context identity, hierarchy, and timing details.

    bool hasProgressChildren() const
    :   Returns:
        :   True when the progress node has child progress nodes.

    bool isValid() const
    :   Returns:
        :   True when this context has report, progress, and state objects.

    QString getName() const
    :   Returns:
        :   Human-readable context name.

    void message(util::[SeverityLevel](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv4util13SeverityLevelE "mv::util::SeverityLevel") severity, QString text, QString location, QVariantMap details) const
    :   Adds a message with an explicit severity to the report node and console output.

    void info(QString text, QString location = {}, QVariantMap details = {}, [MessageKind](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKindE "mv::workflow::MessageKind") kind = [MessageKind](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKindE "mv::workflow::MessageKind")::[Diagnostic](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKind10DiagnosticE "mv::workflow::MessageKind::Diagnostic")) const
    :   Adds an informational message.

        Parameters:
        :   - **text** – Message text.
            - **location** – Source or workflow location associated with the message.
            - **details** – Additional structured details.
            - **kind** – Message category.

    void warning(QString text, QString location = {}, QVariantMap details = {}, [MessageKind](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKindE "mv::workflow::MessageKind") kind = [MessageKind](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKindE "mv::workflow::MessageKind")::[Diagnostic](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKind10DiagnosticE "mv::workflow::MessageKind::Diagnostic")) const
    :   Adds a warning message.

        Parameters:
        :   - **text** – Message text.
            - **location** – Source or workflow location associated with the message.
            - **details** – Additional structured details.
            - **kind** – Message category.

    void error(QString text, QString location = {}, QVariantMap details = {}, [MessageKind](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKindE "mv::workflow::MessageKind") kind = [MessageKind](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKindE "mv::workflow::MessageKind")::[Diagnostic](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow11MessageKind10DiagnosticE "mv::workflow::MessageKind::Diagnostic")) const
    :   Adds an error message.

        Parameters:
        :   - **text** – Message text.
            - **location** – Source or workflow location associated with the message.
            - **details** – Additional structured details.
            - **kind** – Message category.

    void markFailed()
    :   Marks this context as failed in the progress node and synchronizes task progress.

    void setProgress(double value) const
    :   Sets this context progress and synchronizes task progress.

    double getProgress() const
    :   Returns:
        :   Current progress value for this context.

    [ReportNodePtr](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext13ReportNodePtrE "mv::workflow::WorkflowExecutionContext::ReportNodePtr") getReportNode() const
    :   Returns:
        :   Report node associated with this context.

    [ProgressNodePtr](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext15ProgressNodePtrE "mv::workflow::WorkflowExecutionContext::ProgressNodePtr") getProgressNode() const
    :   Returns:
        :   Progress node associated with this context.

    [StatePtr](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#_CPPv4N2mv8workflow24WorkflowExecutionContext8StatePtrE "mv::workflow::WorkflowExecutionContext::StatePtr") getState() const
    :   Returns:
        :   Shared execution state associated with this context.

    [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlanE "mv::workflow::WorkflowPlan")::[JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") getProgressMode() const
    :   Returns:
        :   Progress aggregation mode for this context.

    QString getExecutionPath(const QString &separator = "/") const
    :   Returns the execution path.

        The path is built from this context and its ancestors, starting at the root context.

        Parameters:
        :   **separator** – Separator inserted between path elements.

        Returns:
        :   Execution path string.

    std::int32\_t getDepth() const
    :   Returns the hierarchical depth.

        Returns:
        :   Depth relative to the root context.

    [WorkflowOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html#_CPPv4N2mv8workflow15WorkflowOptionsE "mv::workflow::WorkflowOptions") getOptions() const
    :   Returns:
        :   Workflow options from the shared execution state, or defaults if unavailable.

    QUuid getId() const
    :   Returns the unique context identifier.

        Returns:
        :   Unique identifier of this workflow execution context.

    void setOutputId(const QUuid &outputId)
    :   Sets the output identifier used by [setOutput()](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#classmv_1_1workflow_1_1WorkflowExecutionContext_1a3bec51e8ccb516f45c709ef2e347adc0) and [takeOutput()](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#classmv_1_1workflow_1_1WorkflowExecutionContext_1a712bc72fe8096e1b37a98900bbfb01a8).

        Parameters:
        :   **outputId** – Output identifier to route values through shared state.

    QUuid getOutputId() const
    :   Returns:
        :   Output identifier used by this context.

    QUuid getParentId() const
    :   Returns the parent context identifier.

        Returns:
        :   Parent context identifier, or a null QUuid for root contexts.

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*getTask() const
    :   Returns:
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) associated with this context, or nullptr.

    void registerChildContext(const QString &name, const SharedWorkflowExecutionContext &child)
    :   Registers a named child context.

        Parameters:
        :   - **name** – Child context lookup name.
            - **child** – Child context to register.

    SharedWorkflowExecutionContext getChildContext(const QString &name) const
    :   Retrieves a named child context.

        Parameters:
        :   **name** – Child context lookup name.

        Returns:
        :   Registered child context, or nullptr.

    void setOutput(const QVariant &value)
    :   Stores an output value for this context output id.

        Parameters:
        :   **value** – Output value to publish through the shared execution state.

    QVariant takeOutput()
    :   Returns:
        :   Output value for this context output id, removed from shared state.

    QVariant takeOutput(const [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") &handle)
    :   Takes an output produced for a workflow handle.

        Parameters:
        :   **handle** – Workflow handle whose id identifies the output.

        Returns:
        :   Output value, or an invalid QVariant when unavailable.

    SharedWorkflowExecutionContext getParent() const
    :   Returns:
        :   Parent execution context, or nullptr for root contexts.

    QStringList getChildNames() const
    :   Returns:
        :   Names of registered child contexts.

    bool hasExplicitOutputId() const
    :   Returns:
        :   True when the output id differs from this context id.

    Public Static Functions

    static SharedWorkflowExecutionContext makeRoot(const QString &name, [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task, [WorkflowOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html#_CPPv4N2mv8workflow15WorkflowOptionsE "mv::workflow::WorkflowOptions") options = {})
    :   Creates a root workflow execution context.

        Parameters:
        :   - **name** – Root workflow name.
            - **task** – Optional task used for progress reporting.
            - **options** – Workflow execution options.

        Returns:
        :   Root execution context.
