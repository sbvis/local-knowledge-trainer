# Workflow reporting options

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_reporting_options.html

**Documentation path:** `api/core/workflow/planning/workflow_reporting_options.html`

---

# Workflow reporting options

Configuration controlling lifecycle reports, notifications, console output, and result presentation.

struct WorkflowReportingOptions
:   Configures workflow progress and reporting behavior.

    These options control whether workflow execution creates visible progress, emits completion notifications, produces live console output, and customizes the result dialog copy.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Members

    bool progress = false
    :   Whether to show workflow progress through a task.

    bool finishedNotification = false
    :   Whether to add a notification when execution finishes.

    bool enableConsoleDashboard = false
    :   Whether to enable live console dashboard output.

    std::uint32\_t maxLoggingDepth = std::numeric\_limits<std::uint32\_t>::max()
    :   Maximum nested detail depth for workflow logging.

    [WorkflowResultDetailsOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_result_details_options.html#_CPPv4N2mv8workflow28WorkflowResultDetailsOptionsE "mv::workflow::WorkflowResultDetailsOptions") resultDetails
    :   Result dialog title and message options.
