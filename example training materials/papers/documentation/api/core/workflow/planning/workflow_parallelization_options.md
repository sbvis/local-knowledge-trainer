# Workflow parallelization options

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_parallelization_options.html

**Documentation path:** `api/core/workflow/planning/workflow_parallelization_options.html`

---

# Workflow parallelization options

Configuration controlling parallel workflow execution.

struct WorkflowParallelizationOptions
:   Configures workflow job parallelization.

    These options decide whether jobs may run concurrently and limit the maximum number of worker threads used by the workflow executor.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Members

    bool parallel = true
    :   Whether parallel execution is enabled.

    MaxWorkerThreadCount maxWorkerThreadCount = 63
    :   Maximum number of worker threads for parallel execution.
