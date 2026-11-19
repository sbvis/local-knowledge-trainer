# Workflow plan

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html

**Documentation path:** `api/core/workflow/planning/workflow_plan.html`

---

# Workflow plan

The central planning type containing stages, jobs, lifecycle branches, weights, and scheduling policies.

class WorkflowPlan
:   Describes an executable workflow.

    [WorkflowPlan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan) is a declarative description consumed by an [AbstractWorkflowPlanExecutor](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/abstract_workflow_plan_executor.html#classmv_1_1workflow_1_1AbstractWorkflowPlanExecutor). It contains main stages, optional success/failure/finalization stages, shared workflow context, and relative progress weight information. Stages may execute sequentially, in parallel, or in batches, and individual jobs can run normal functions or create nested workflow plans.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Types

    enum class ConcurrencyMode
    :   Defines how jobs inside a stage are scheduled.

        *Values:*

        enumerator Sequential
        :   Jobs run one after another.

        enumerator Parallel
        :   Jobs may run concurrently.

    enum class StageExecutionPolicy
    :   Defines the workflow phase in which a stage participates.

        *Values:*

        enumerator Main
        :   Main workflow execution.

        enumerator OnSuccess
        :   Runs after successful main execution.

        enumerator OnFailure
        :   Runs after failed main execution.

        enumerator Finally
        :   Runs after main and success/failure stages.

    enum class JobThreadAffinity
    :   Defines which thread a job should run on.

        *Values:*

        enumerator CurrentWorkerThread
        :   Run on the current worker thread.

        enumerator GuiThread
        :   Dispatch to the GUI thread.

    enum class JobCompletionPolicy
    :   Defines how job completion is determined.

        *Values:*

        enumerator Auto
        :   Completion is inferred by the executor.

        enumerator ManualOrNested
        :   Completion is controlled manually or by nested workflow progress.

    enum class JobProgressMode
    :   Defines how job progress contributes to parent progress.

        *Values:*

        enumerator Automatic
        :   Leaf jobs auto-complete when they have no children.

        enumerator Atomic
        :   Nested workflow progress is treated as one job unit.

        enumerator Nested
        :   Nested workflows contribute fine-grained progress.

    using SharedState = std::shared\_ptr<QVariantMap>
    :   Shared mutable variant-map context used by workflow plans and jobs.

    using JobFunction = std::function<void(const [Job](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan3JobE "mv::workflow::WorkflowPlan::Job")&, const SharedWorkflowExecutionContext&)>
    :   Callable job body.

    using JobFunctions = std::vector<[JobFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan11JobFunctionE "mv::workflow::WorkflowPlan::JobFunction")>
    :   Collection of callable job bodies.

    using NestedWorkflowFunction = std::function<UniqueWorkflowPlan(const [Job](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan3JobE "mv::workflow::WorkflowPlan::Job")&, const SharedWorkflowExecutionContext&)>
    :   Function that creates a nested workflow plan for a job.

    using WorkflowBatchSizeFunction = std::function<std::size\_t(const SharedWorkflowExecutionContext&)>
    :   Function that resolves a batched stage size from an execution context.

    using OptionalWorkflowBatchSizeFunction = std::optional<[WorkflowBatchSizeFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan25WorkflowBatchSizeFunctionE "mv::workflow::WorkflowPlan::WorkflowBatchSizeFunction")>
    :   Optional batched stage size resolver.

    using Jobs = std::vector<[Job](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan3JobE "mv::workflow::WorkflowPlan::Job")>
    :   Collection of workflow jobs.

    Public Functions

    WorkflowPlan(const QString &title, SharedWorkflowContext context = SharedWorkflowContext())
    :   Constructs a workflow plan.

        Parameters:
        :   - **title** – Human-readable workflow name.
            - **context** – Optional shared workflow context passed to jobs.

    [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addStage([Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan5StageE "mv::workflow::WorkflowPlan::Stage") stage)
    :   Adds a fully constructed stage to the main workflow stage list.

        Parameters:
        :   **stage** – [Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Stage) to add.

        Returns:
        :   Handle for the added stage.

    template<typename Function> inline [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addSequentialStage(QString name, [Function](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4I0EN2mv8workflow12WorkflowPlan18addSequentialStageE14WorkflowHandle7QStringRR8Function17JobThreadAffinityd "mv::workflow::WorkflowPlan::addSequentialStage::Function") &&function, [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") threadAffinity = [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity")::[CurrentWorkerThread](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinity19CurrentWorkerThreadE "mv::workflow::WorkflowPlan::JobThreadAffinity::CurrentWorkerThread"), double weight = 1.0)
    :   Adds a single-function sequential stage.

        Parameters:
        :   - **name** – [Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Stage) and job name.
            - **function** – Function to execute.
            - **threadAffinity** – Thread affinity for the generated job.
            - **weight** – Relative progress weight.

        Returns:
        :   Handle for the added stage.

    QString getName() const
    :   Returns:
        :   Human-readable workflow plan name.

    [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addSequentialStage(QString name, [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") jobs, double weight = 1.0)
    :   Adds a sequential stage to the main workflow stage list.

        Parameters:
        :   - **name** – Human-readable stage name.
            - **jobs** – Jobs contained by the stage.
            - **weight** – Relative progress weight.

        Returns:
        :   Handle for the added stage.

    [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addParallelStage(QString name, [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") jobs, double weight = 1.0)
    :   Adds a parallel stage to the main workflow stage list.

        Parameters:
        :   - **name** – Human-readable stage name.
            - **jobs** – Jobs contained by the stage.
            - **weight** – Relative progress weight.

        Returns:
        :   Handle for the added stage.

    [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addParallelNestedWorkflowStage(QString name, [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") jobs, double weight = 1.0)
    :   Adds a parallel stage containing only nested workflow jobs.

        Parameters:
        :   - **name** – Human-readable stage name.
            - **jobs** – Nested workflow jobs contained by the stage.
            - **weight** – Relative progress weight.

        Returns:
        :   Handle for the added stage.

    [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addBatchedParallelStage(const QString &name, [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") jobs, std::size\_t batchSize)
    :   Adds a batched parallel stage with a fixed batch size.

        Parameters:
        :   - **name** – [Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Stage) name.
            - **jobs** – Jobs to execute in batches.
            - **batchSize** – Fixed batch size.

        Returns:
        :   Handle for the added stage.

    [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addBatchedParallelStage(const QString &name, [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") jobs, [WorkflowBatchSizeFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan25WorkflowBatchSizeFunctionE "mv::workflow::WorkflowPlan::WorkflowBatchSizeFunction") batchSizeFunction)
    :   Adds a batched parallel stage with a dynamic batch-size resolver.

        Parameters:
        :   - **name** – [Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Stage) name.
            - **jobs** – Jobs to execute in batches.
            - **batchSizeFunction** – Function that resolves the batch size.

        Returns:
        :   Handle for the added stage.

    [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addStage(QString name, [ConcurrencyMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15ConcurrencyModeE "mv::workflow::WorkflowPlan::ConcurrencyMode") mode, [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") jobs, double weight = 1.0)
    :   Adds a stage using an explicit concurrency mode.

        Parameters:
        :   - **name** – Human-readable stage name.
            - **mode** – [Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Stage) concurrency mode.
            - **jobs** – Jobs contained by the stage.
            - **weight** – Relative progress weight.

        Returns:
        :   Handle for the added stage.

    template<typename Function> inline void addOnSuccessStage(QString name, [Function](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4I0EN2mv8workflow12WorkflowPlan17addOnSuccessStageEv7QStringRR8Function17JobThreadAffinityd "mv::workflow::WorkflowPlan::addOnSuccessStage::Function") &&function, [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") threadAffinity = [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity")::[CurrentWorkerThread](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinity19CurrentWorkerThreadE "mv::workflow::WorkflowPlan::JobThreadAffinity::CurrentWorkerThread"), double weight = 0.0)
    :   Adds a single-function stage that runs when the main workflow succeeds.

    template<typename Function> inline void addOnFailureStage(QString name, [Function](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4I0EN2mv8workflow12WorkflowPlan17addOnFailureStageEv7QStringRR8Function17JobThreadAffinityd "mv::workflow::WorkflowPlan::addOnFailureStage::Function") &&function, [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") threadAffinity = [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity")::[CurrentWorkerThread](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinity19CurrentWorkerThreadE "mv::workflow::WorkflowPlan::JobThreadAffinity::CurrentWorkerThread"), double weight = 0.0)
    :   Adds a single-function stage that runs when the main workflow fails.

    template<typename Function> inline void addFinalizationStage(QString name, [Function](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4I0EN2mv8workflow12WorkflowPlan20addFinalizationStageEv7QStringRR8Function17JobThreadAffinityd "mv::workflow::WorkflowPlan::addFinalizationStage::Function") &&function, [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") threadAffinity = [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity")::[CurrentWorkerThread](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinity19CurrentWorkerThreadE "mv::workflow::WorkflowPlan::JobThreadAffinity::CurrentWorkerThread"), double weight = 0.0)
    :   Adds a single-function stage that runs during finalization.

    const Stages &getStages() const
    :   Returns:
        :   Const main workflow stages.

    Stages &getStages()
    :   Returns:
        :   Mutable main workflow stages.

    const Stages &getOnSuccessStages() const
    :   Returns:
        :   Stages that execute after successful main execution.

    const Stages &getOnFailureStages() const
    :   Returns:
        :   Stages that execute after failed main execution.

    const Stages &getFinallyStages() const
    :   Returns:
        :   Stages that execute during finalization.

    SharedWorkflowContext getWorkflowContext() const
    :   Gets the shared workflow context.

        The workflow context can store data shared across stages and jobs in this plan.

        Returns:
        :   Shared workflow context.

    template<typename WorkflowContextType> inline std::shared\_ptr<[WorkflowContextType](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4I0ENK2mv8workflow12WorkflowPlan20getWorkflowContextAsENSt10shared_ptrI19WorkflowContextTypeEEv "mv::workflow::WorkflowPlan::getWorkflowContextAs::WorkflowContextType")> getWorkflowContextAs() const
    :   Returns the shared workflow context cast to a specific type.

        WorkflowContextType must derive from [WorkflowContextBase](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_context_base.html#classmv_1_1workflow_1_1WorkflowContextBase). The method returns nullptr when the stored context has a different type.

        Template Parameters:
        :   **WorkflowContextType** – Target workflow context type.

        Returns:
        :   Context cast to WorkflowContextType, or nullptr if the cast fails.

    void setWeight(double weight)
    :   Sets the relative progress weight for this workflow plan.

    double getWeight() const
    :   Returns:
        :   Relative progress weight for this workflow plan.

    [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") addNestedWorkflowStage(const QString &name, [NestedWorkflowFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan22NestedWorkflowFunctionE "mv::workflow::WorkflowPlan::NestedWorkflowFunction") function, [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") threadAffinity = [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity")::[CurrentWorkerThread](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinity19CurrentWorkerThreadE "mv::workflow::WorkflowPlan::JobThreadAffinity::CurrentWorkerThread"), double weight = 1.0)
    :   Adds a sequential stage that executes a nested workflow.

        Parameters:
        :   - **name** – [Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Stage) and nested workflow job name.
            - **function** – Function that creates the nested workflow plan.
            - **threadAffinity** – Thread affinity for the nested workflow job.
            - **weight** – Relative progress weight.

        Returns:
        :   Handle for the added nested workflow stage.

    class Job
    :   Smallest executable unit in a workflow.

        Jobs either wrap a function or a nested workflow factory. Each job has an identifier, output identifier, thread affinity, progress mode, relative weight, optional result/error state, and access to the plan’s shared workflow context.

        Public Types

        enum class JobKind
        :   Defines the concrete kind of work represented by the job.

            *Values:*

            enumerator Function
            :   [Job](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Job) executes a callable directly.

            enumerator NestedWorkflow
            :   [Job](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Job) creates and executes a nested workflow.

        using ErrorString = QString
        :   Error message type stored by jobs.

        Public Functions

        Job(QString name, [JobFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan11JobFunctionE "mv::workflow::WorkflowPlan::JobFunction") function, [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") threadAffinity = [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity")::[CurrentWorkerThread](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinity19CurrentWorkerThreadE "mv::workflow::WorkflowPlan::JobThreadAffinity::CurrentWorkerThread"), [JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"))
        :   Constructs a function job.

            Parameters:
            :   - **name** – Human-readable job name.
                - **function** – Callable executed by this job.
                - **threadAffinity** – Preferred execution thread.
                - **progressMode** – Progress reporting mode for this job.

        Job(QString name, [NestedWorkflowFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan22NestedWorkflowFunctionE "mv::workflow::WorkflowPlan::NestedWorkflowFunction") nestedWorkflowFunction, [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") threadAffinity = [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity")::[CurrentWorkerThread](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinity19CurrentWorkerThreadE "mv::workflow::WorkflowPlan::JobThreadAffinity::CurrentWorkerThread"), [JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode = [JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressMode9AutomaticE "mv::workflow::WorkflowPlan::JobProgressMode::Automatic"), double weight = 1.0)
        :   Constructs a nested workflow job.

            Parameters:
            :   - **name** – Human-readable job name.
                - **nestedWorkflowFunction** – Function that creates the nested workflow.
                - **threadAffinity** – Preferred execution thread.
                - **progressMode** – Progress reporting mode for this job.
                - **weight** – Relative progress weight.

        Job(QString name, [NestedWorkflowJob](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17NestedWorkflowJobE "mv::workflow::WorkflowPlan::NestedWorkflowJob") job, [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") threadAffinity, [JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") progressMode, double weight)
        :   Constructs a nested workflow job from a wrapper.

            Parameters:
            :   - **name** – Human-readable job name.
                - **job** – Nested workflow job descriptor.
                - **threadAffinity** – Preferred execution thread.
                - **progressMode** – Progress reporting mode for this job.
                - **weight** – Relative progress weight.

        inline QUuid getId() const
        :   Returns the unique job identifier.

            Returns:
            :   Unique job identifier.

        void setOutputId(const QUuid &outputId)
        :   Assigns the identifier used for storing this job’s output.

            Parameters:
            :   **outputId** – Output identifier.

        QUuid getOutputId() const
        :   Returns the identifier used for storing this job’s output.

            Returns:
            :   Output identifier.

        [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") getHandle() const
        :   Returns a handle that refers to this job.

            Returns:
            :   Workflow handle for this job.

        QString getName() const
        :   Returns the human-readable job name.

            Returns:
            :   [Job](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Job) name.

        void run(SharedWorkflowExecutionContext context) const
        :   Runs the job function in the supplied execution context.

        void setResult(QVariant result)
        :   Stores a result value on the job.

        const QVariant &getResult() const
        :   Returns:
            :   Current job result value.

        void clearResult()
        :   Clears the stored result value.

        void setError(QString error)
        :   Stores an error message on the job.

        bool hasError() const
        :   Returns:
            :   True when the job has an error message.

        const QString &getError() const
        :   Returns:
            :   Stored error message.

        void clearError()
        :   Clears the stored error message.

        void setException(const std::exception &e)
        :   Stores an exception message on the job.

        void setUnknownException()
        :   Stores a generic unknown-exception message on the job.

        void fail(QString error)
        :   Marks the job as failed with an error message.

        [JobThreadAffinity](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan17JobThreadAffinityE "mv::workflow::WorkflowPlan::JobThreadAffinity") getThreadAffinity() const
        :   Returns:
            :   Thread affinity for this job.

        double getWeight() const
        :   Returns:
            :   Relative progress weight for this job.

        [Job](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan3JobE "mv::workflow::WorkflowPlan::Job") weighted(double weight)
        :   Returns a copy of this job with a different relative progress weight.

        [JobProgressMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15JobProgressModeE "mv::workflow::WorkflowPlan::JobProgressMode") getProgressMode() const
        :   Returns:
            :   Progress aggregation mode for this job.

        inline bool isNestedWorkflow() const
        :   Returns:
            :   True when this job creates a nested workflow.

        inline UniqueWorkflowPlan createNestedWorkflow(const SharedWorkflowExecutionContext &context) const
        :   Creates the nested workflow represented by this job.

            Parameters:
            :   **context** – Workflow execution context used during nested workflow creation.

            Returns:
            :   Newly created nested workflow plan.

        SharedWorkflowContext getWorkflowContext() const
        :   Returns the shared workflow context associated with this job.

            Returns:
            :   Shared workflow context.

        template<typename WorkflowContextType> inline std::shared\_ptr<[WorkflowContextType](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4I0ENK2mv8workflow12WorkflowPlan3Job20getWorkflowContextAsENSt10shared_ptrI19WorkflowContextTypeEEv "mv::workflow::WorkflowPlan::Job::getWorkflowContextAs::WorkflowContextType")> getWorkflowContextAs() const
        :   Returns the shared workflow context cast to a specific type.

            Template Parameters:
            :   **WorkflowContextType** – Target workflow context type.

            Returns:
            :   Context cast to WorkflowContextType, or nullptr if the cast fails.

    struct NestedWorkflowJob
    :   Wrapper used to disambiguate nested workflow jobs.

        Public Members

        [NestedWorkflowFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan22NestedWorkflowFunctionE "mv::workflow::WorkflowPlan::NestedWorkflowFunction") function
        :   Function that creates the nested workflow plan.

    class Stage
    :   Ordered group of jobs with a shared execution mode.

        A stage can run sequentially, in parallel, or in batches when a batch size resolver is configured. Stages also carry their own handle and progress weight so callers can address outputs produced by a stage.

        Public Functions

        Stage(QString name, [ConcurrencyMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15ConcurrencyModeE "mv::workflow::WorkflowPlan::ConcurrencyMode") concurrencyMode, [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") jobs, double weight = 1.0)
        :   Constructs a sequential or parallel stage.

            Parameters:
            :   - **name** – Human-readable stage name.
                - **concurrencyMode** – [Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Stage) concurrency mode.
                - **jobs** – Jobs contained by the stage.
                - **weight** – Relative progress weight.

        Stage(QString name, [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") jobs, [WorkflowBatchSizeFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan25WorkflowBatchSizeFunctionE "mv::workflow::WorkflowPlan::WorkflowBatchSizeFunction") batchSizeFunction, double weight)
        :   Constructs a batched parallel stage.

            Parameters:
            :   - **name** – Human-readable stage name.
                - **jobs** – Jobs executed in batches.
                - **batchSizeFunction** – Function that resolves the batch size.
                - **weight** – Relative progress weight.

        QUuid getId() const
        :   Returns:
            :   Unique stage identifier.

        [WorkflowHandle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html#_CPPv4N2mv8workflow14WorkflowHandleE "mv::workflow::WorkflowHandle") getHandle() const
        :   Returns:
            :   Workflow handle for this stage.

        [ConcurrencyMode](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan15ConcurrencyModeE "mv::workflow::WorkflowPlan::ConcurrencyMode") getConcurrencyMode() const
        :   Returns:
            :   [Stage](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#classmv_1_1workflow_1_1WorkflowPlan_1_1Stage) concurrency mode.

        bool isSequential() const
        :   Returns:
            :   True when the stage runs sequentially.

        bool isParallel() const
        :   Returns:
            :   True when the stage runs in parallel.

        bool isBatchedParallel() const
        :   Returns:
            :   True when this is a batched parallel stage.

        void setBatchSizeFunction([WorkflowBatchSizeFunction](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan25WorkflowBatchSizeFunctionE "mv::workflow::WorkflowPlan::WorkflowBatchSizeFunction") batchSizeFunction)
        :   Sets the batch-size resolver for a parallel stage.

            Parameters:
            :   **batchSizeFunction** – Function that resolves the batch size.

        std::size\_t resolveBatchSize(const SharedWorkflowExecutionContext &executionContext) const
        :   Resolves the batch size for an execution context.

            Parameters:
            :   **executionContext** – Execution context used by the resolver.

            Returns:
            :   Batch size to use for this stage.

        QString getName() const
        :   Returns:
            :   Human-readable stage name.

        const [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") &getJobs() const
        :   Returns:
            :   Const jobs in this stage.

        [Jobs](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html#_CPPv4N2mv8workflow12WorkflowPlan4JobsE "mv::workflow::WorkflowPlan::Jobs") &getJobs()
        :   Returns:
            :   Mutable jobs in this stage.

        void setWeight(double weight)
        :   Sets the relative progress weight for this stage.

        double getWeight() const
        :   Returns:
            :   Relative progress weight for this stage.

        bool containsGuiThreadJobs() const
        :   Returns:
            :   True when the stage contains GUI-thread jobs.

        bool containsWorkerThreadJobs() const
        :   Returns:
            :   True when the stage contains worker-thread jobs.

        bool isThreadAffinityCompatible() const
        :   Returns:
            :   True when the stage’s concurrency mode supports its job thread affinities.
