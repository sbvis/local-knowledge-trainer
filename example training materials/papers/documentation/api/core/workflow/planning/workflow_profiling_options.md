# Workflow profiling options

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_profiling_options.html

**Documentation path:** `api/core/workflow/planning/workflow_profiling_options.html`

---

# Workflow profiling options

Configuration controlling timing and profiling collection.

struct WorkflowProfilingOptions
:   Configures workflow profiling and tracing.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Types

    enum class SinkType
    :   Defines the profiling output sink.

        *Values:*

        enumerator None
        :   No profiling or tracing.

        enumerator ChromeTracing
        :   Chrome tracing-compatible output.

    Public Members

    [SinkType](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_profiling_options.html#_CPPv4N2mv8workflow24WorkflowProfilingOptions8SinkTypeE "mv::workflow::WorkflowProfilingOptions::SinkType") sinkType = [SinkType](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_profiling_options.html#_CPPv4N2mv8workflow24WorkflowProfilingOptions8SinkTypeE "mv::workflow::WorkflowProfilingOptions::SinkType")::[None](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_profiling_options.html#_CPPv4N2mv8workflow24WorkflowProfilingOptions8SinkType4NoneE "mv::workflow::WorkflowProfilingOptions::SinkType::None")
    :   Profiling sink used for execution.
