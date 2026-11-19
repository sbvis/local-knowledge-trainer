# Reporting and metrics

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/index.html

**Documentation path:** `api/core/workflow/reporting/index.html`

---

# Reporting and metrics

Reporting types capture lifecycle events, structured diagnostics, aggregate metrics, and stage summaries. Presentation types render this information for result dialogs and detailed message inspection without owning workflow control flow.

For reporting conventions, see [Reporting, metrics, and profiling](https://manivault.readthedocs.io/en/latest/development/workflows/reporting_and_profiling.html).

Workflow messages are part of a particular execution result. They are distinct from the process-wide [Qt logging pipeline](https://manivault.readthedocs.io/en/latest/api/core/util/logging/index.html): messages preserve workflow context and can be shown with the result, while Qt logs provide general developer diagnostics.

- [Workflow message](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html)
- [AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html)
- [WorkflowMessagesListModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_messages_list_model.html)
- [WorkflowMessagesTreeModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_messages_tree_model.html)
- [WorkflowMessagesFilterModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_messages_filter_model.html)
- [Workflow report node](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_report_node.html)
- [Workflow metric](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_metric.html)
- [Workflow execution metrics](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_execution_metrics.html)
- [Workflow stage summary](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_stage_summary.html)
- [Workflow result details options](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_result_details_options.html)
- [Workflow result dialog](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_result_dialog.html)
