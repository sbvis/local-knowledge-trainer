# Workflow options

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html

**Documentation path:** `api/core/workflow/planning/workflow_options.html`

---

# Workflow options

The root option bundle for cancellation, parallelization, profiling, and reporting.

struct WorkflowOptions
:   Configures workflow execution behavior.

    [WorkflowOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html#structmv_1_1workflow_1_1WorkflowOptions) groups execution, batching, reporting, and profiling settings passed to workflow executors.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Members

    [WorkflowParallelizationOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_parallelization_options.html#_CPPv4N2mv8workflow30WorkflowParallelizationOptionsE "mv::workflow::WorkflowParallelizationOptions") execution
    :   Parallelization options for workflow jobs.

    [WorkflowBatchingOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_batching_options.html#_CPPv4N2mv8workflow23WorkflowBatchingOptionsE "mv::workflow::WorkflowBatchingOptions") batching
    :   Batch-size options for serialization work.

    [WorkflowCancellationOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_cancellation_options.html#_CPPv4N2mv8workflow27WorkflowCancellationOptionsE "mv::workflow::WorkflowCancellationOptions") cancellation
    :   Cooperative cancellation options.

    [WorkflowReportingOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_reporting_options.html#_CPPv4N2mv8workflow24WorkflowReportingOptionsE "mv::workflow::WorkflowReportingOptions") reporting
    :   Reporting, notification, and result-dialog options.

    [WorkflowProfilingOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_profiling_options.html#_CPPv4N2mv8workflow24WorkflowProfilingOptionsE "mv::workflow::WorkflowProfilingOptions") profiling
    :   Profiling and trace sink options.
