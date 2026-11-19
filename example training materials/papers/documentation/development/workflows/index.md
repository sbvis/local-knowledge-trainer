# Advanced workflow framework

**Source:** https://manivault.readthedocs.io/en/latest/development/workflows/index.html

**Documentation path:** `development/workflows/index.html`

---

# Advanced workflow framework

The ManiVault workflow framework is the primary execution mechanism for substantial new operations. It provides the underlying model for sequential and parallel work, GUI-thread dispatch, nested workflows, progress aggregation, cancellation, diagnostics, metrics, and final results.

Its intended level is application-operation orchestration, not automatic acceleration of tight loops or replacement of OpenMP, oneTBB, SIMD, or optimized numerical libraries. Those facilities can provide kernel-level parallelism inside a workflow job. See [Intended scope and granularity](https://manivault.readthedocs.io/en/latest/development/parallel_execution/scope_and_granularity.html) for the comparison and composition guidance.

Most developers should enter this machinery through the [high-level parallel execution utilities](https://manivault.readthedocs.io/en/latest/development/parallel_execution/index.html). This advanced guide is for developers who need to construct custom workflow plans, integrate task-backed progress, use nested workflows, control execution contexts, or understand the scheduler’s detailed behavior. For individual types and member signatures, use the [workflow API reference](https://manivault.readthedocs.io/en/latest/api/core/workflow/index.html).

A ManiVault `Task` is a presentation adapter for workflow progress, not an alternative execution engine. See [Tasks and workflows](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/tasks_and_workflows.html) for their relationship.

Note

In this section, *workflow* means the C++ execution framework in `mv::workflow`. It does not mean an informal end-user sequence of actions.

## Advanced path

Begin with the overview and concepts, then work through planning, execution, and results. The remaining pages are focused references for concurrency, nesting, cancellation, metrics, and framework supporting types.

- [Overview](https://manivault.readthedocs.io/en/latest/development/workflows/overview.html)
  - [System at a glance](https://manivault.readthedocs.io/en/latest/development/workflows/overview.html#system-at-a-glance)
  - [When to use it](https://manivault.readthedocs.io/en/latest/development/workflows/overview.html#when-to-use-it)
  - [Public and internal pieces](https://manivault.readthedocs.io/en/latest/development/workflows/overview.html#public-and-internal-pieces)
- [Core concepts](https://manivault.readthedocs.io/en/latest/development/workflows/concepts.html)
  - [Plan, stage, and job](https://manivault.readthedocs.io/en/latest/development/workflows/concepts.html#plan-stage-and-job)
  - [Handles and identities](https://manivault.readthedocs.io/en/latest/development/workflows/concepts.html#handles-and-identities)
  - [Execution context](https://manivault.readthedocs.io/en/latest/development/workflows/concepts.html#execution-context)
  - [Progress and reports](https://manivault.readthedocs.io/en/latest/development/workflows/concepts.html#progress-and-reports)
  - [State and result](https://manivault.readthedocs.io/en/latest/development/workflows/concepts.html#state-and-result)
  - [Root and child workflows](https://manivault.readthedocs.io/en/latest/development/workflows/concepts.html#root-and-child-workflows)
- [Defining workflows](https://manivault.readthedocs.io/en/latest/development/workflows/defining_workflows.html)
  - [Choose a stage shape](https://manivault.readthedocs.io/en/latest/development/workflows/defining_workflows.html#choose-a-stage-shape)
  - [Give each unit one responsibility](https://manivault.readthedocs.io/en/latest/development/workflows/defining_workflows.html#give-each-unit-one-responsibility)
  - [Weights](https://manivault.readthedocs.io/en/latest/development/workflows/defining_workflows.html#weights)
  - [Execution policies](https://manivault.readthedocs.io/en/latest/development/workflows/defining_workflows.html#execution-policies)
  - [Capture safely](https://manivault.readthedocs.io/en/latest/development/workflows/defining_workflows.html#capture-safely)
- [Execution model](https://manivault.readthedocs.io/en/latest/development/workflows/execution_model.html)
  - [Root execution lifecycle](https://manivault.readthedocs.io/en/latest/development/workflows/execution_model.html#root-execution-lifecycle)
  - [Blocking and asynchronous execution](https://manivault.readthedocs.io/en/latest/development/workflows/execution_model.html#blocking-and-asynchronous-execution)
  - [Failure boundaries](https://manivault.readthedocs.io/en/latest/development/workflows/execution_model.html#failure-boundaries)
  - [Ownership](https://manivault.readthedocs.io/en/latest/development/workflows/execution_model.html#ownership)
- [Execution context and shared state](https://manivault.readthedocs.io/en/latest/development/workflows/execution_context.html)
  - [Operation data](https://manivault.readthedocs.io/en/latest/development/workflows/execution_context.html#operation-data)
  - [Hierarchy](https://manivault.readthedocs.io/en/latest/development/workflows/execution_context.html#hierarchy)
  - [Outputs](https://manivault.readthedocs.io/en/latest/development/workflows/execution_context.html#outputs)
  - [Thread safety](https://manivault.readthedocs.io/en/latest/development/workflows/execution_context.html#thread-safety)
  - [Lifetime](https://manivault.readthedocs.io/en/latest/development/workflows/execution_context.html#lifetime)
- [Threading and parallelism](https://manivault.readthedocs.io/en/latest/development/workflows/threading_and_parallelism.html)
  - [Thread affinity](https://manivault.readthedocs.io/en/latest/development/workflows/threading_and_parallelism.html#thread-affinity)
  - [Parallel stages](https://manivault.readthedocs.io/en/latest/development/workflows/threading_and_parallelism.html#parallel-stages)
  - [Batching](https://manivault.readthedocs.io/en/latest/development/workflows/threading_and_parallelism.html#batching)
  - [Parallelization options](https://manivault.readthedocs.io/en/latest/development/workflows/threading_and_parallelism.html#parallelization-options)
  - [Deadlock prevention](https://manivault.readthedocs.io/en/latest/development/workflows/threading_and_parallelism.html#deadlock-prevention)
- [Nested workflows](https://manivault.readthedocs.io/en/latest/development/workflows/nested_workflows.html)
  - [Execution under a parent](https://manivault.readthedocs.io/en/latest/development/workflows/nested_workflows.html#execution-under-a-parent)
  - [Progress modes](https://manivault.readthedocs.io/en/latest/development/workflows/nested_workflows.html#progress-modes)
  - [Error and cancellation propagation](https://manivault.readthedocs.io/en/latest/development/workflows/nested_workflows.html#error-and-cancellation-propagation)
  - [Avoid unnecessary nesting](https://manivault.readthedocs.io/en/latest/development/workflows/nested_workflows.html#avoid-unnecessary-nesting)
- [Progress and cancellation](https://manivault.readthedocs.io/en/latest/development/workflows/progress_and_cancellation.html)
  - [Progress tree](https://manivault.readthedocs.io/en/latest/development/workflows/progress_and_cancellation.html#progress-tree)
  - [Cooperative cancellation](https://manivault.readthedocs.io/en/latest/development/workflows/progress_and_cancellation.html#cooperative-cancellation)
  - [Skipped work](https://manivault.readthedocs.io/en/latest/development/workflows/progress_and_cancellation.html#skipped-work)
  - [Cleanup](https://manivault.readthedocs.io/en/latest/development/workflows/progress_and_cancellation.html#cleanup)
- [Results and error handling](https://manivault.readthedocs.io/en/latest/development/workflows/results_and_error_handling.html)
  - [Result hierarchy](https://manivault.readthedocs.io/en/latest/development/workflows/results_and_error_handling.html#result-hierarchy)
  - [Reporting a failure](https://manivault.readthedocs.io/en/latest/development/workflows/results_and_error_handling.html#reporting-a-failure)
  - [Structured messages](https://manivault.readthedocs.io/en/latest/development/workflows/results_and_error_handling.html#structured-messages)
  - [Futures](https://manivault.readthedocs.io/en/latest/development/workflows/results_and_error_handling.html#futures)
  - [Result registry and dialog](https://manivault.readthedocs.io/en/latest/development/workflows/results_and_error_handling.html#result-registry-and-dialog)
- [Reporting, metrics, and profiling](https://manivault.readthedocs.io/en/latest/development/workflows/reporting_and_profiling.html)
  - [Report tree](https://manivault.readthedocs.io/en/latest/development/workflows/reporting_and_profiling.html#report-tree)
  - [Metrics](https://manivault.readthedocs.io/en/latest/development/workflows/reporting_and_profiling.html#metrics)
  - [Stage summaries](https://manivault.readthedocs.io/en/latest/development/workflows/reporting_and_profiling.html#stage-summaries)
  - [Console presentation](https://manivault.readthedocs.io/en/latest/development/workflows/reporting_and_profiling.html#console-presentation)
- [Framework supporting types](https://manivault.readthedocs.io/en/latest/development/workflows/framework_supporting_types.html)
  - [Configuration value types](https://manivault.readthedocs.io/en/latest/development/workflows/framework_supporting_types.html#configuration-value-types)
  - [RAII scopes](https://manivault.readthedocs.io/en/latest/development/workflows/framework_supporting_types.html#raii-scopes)
  - [Nested runtime access](https://manivault.readthedocs.io/en/latest/development/workflows/framework_supporting_types.html#nested-runtime-access)
  - [Identity and type conversion](https://manivault.readthedocs.io/en/latest/development/workflows/framework_supporting_types.html#identity-and-type-conversion)
  - [Formatting and presentation](https://manivault.readthedocs.io/en/latest/development/workflows/framework_supporting_types.html#formatting-and-presentation)
  - [Registry and dispatch](https://manivault.readthedocs.io/en/latest/development/workflows/framework_supporting_types.html#registry-and-dispatch)
  - [Context utility](https://manivault.readthedocs.io/en/latest/development/workflows/framework_supporting_types.html#context-utility)
- [Examples and recipes](https://manivault.readthedocs.io/en/latest/development/workflows/examples_and_recipes.html)
  - [Pipeline with a parallel middle phase](https://manivault.readthedocs.io/en/latest/development/workflows/examples_and_recipes.html#pipeline-with-a-parallel-middle-phase)
  - [GUI hand-off](https://manivault.readthedocs.io/en/latest/development/workflows/examples_and_recipes.html#gui-hand-off)
  - [Reusable child operation](https://manivault.readthedocs.io/en/latest/development/workflows/examples_and_recipes.html#reusable-child-operation)
  - [Failure cleanup](https://manivault.readthedocs.io/en/latest/development/workflows/examples_and_recipes.html#failure-cleanup)
  - [Large homogeneous collections](https://manivault.readthedocs.io/en/latest/development/workflows/examples_and_recipes.html#large-homogeneous-collections)
- [Testing workflows](https://manivault.readthedocs.io/en/latest/development/workflows/testing.html)
  - [Core cases](https://manivault.readthedocs.io/en/latest/development/workflows/testing.html#core-cases)
  - [Determinism](https://manivault.readthedocs.io/en/latest/development/workflows/testing.html#determinism)
  - [Small plans](https://manivault.readthedocs.io/en/latest/development/workflows/testing.html#small-plans)
  - [Context and lifetime checks](https://manivault.readthedocs.io/en/latest/development/workflows/testing.html#context-and-lifetime-checks)
  - [Headless diagnostics](https://manivault.readthedocs.io/en/latest/development/workflows/testing.html#headless-diagnostics)
- [Troubleshooting](https://manivault.readthedocs.io/en/latest/development/workflows/troubleshooting.html)
  - [The workflow never completes](https://manivault.readthedocs.io/en/latest/development/workflows/troubleshooting.html#the-workflow-never-completes)
  - [Progress stalls below completion](https://manivault.readthedocs.io/en/latest/development/workflows/troubleshooting.html#progress-stalls-below-completion)
  - [Cancellation appears ineffective](https://manivault.readthedocs.io/en/latest/development/workflows/troubleshooting.html#cancellation-appears-ineffective)
  - [A later stage sees missing output](https://manivault.readthedocs.io/en/latest/development/workflows/troubleshooting.html#a-later-stage-sees-missing-output)
  - [Intermittent failures in parallel stages](https://manivault.readthedocs.io/en/latest/development/workflows/troubleshooting.html#intermittent-failures-in-parallel-stages)
  - [Messages appear but the workflow succeeds](https://manivault.readthedocs.io/en/latest/development/workflows/troubleshooting.html#messages-appear-but-the-workflow-succeeds)
  - [Result details cannot be opened](https://manivault.readthedocs.io/en/latest/development/workflows/troubleshooting.html#result-details-cannot-be-opened)
