# Workflow

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/index.html

**Documentation path:** `api/core/workflow/index.html`

---

# Workflow

The workflow API provides ManiVault’s advanced execution framework for structured, observable operations. A workflow plan describes sequential or parallel stages containing jobs; an executor runs that plan using hierarchical contexts, progress and reporting nodes, cooperative cancellation, and configurable threading behavior. Completed executions produce structured results containing status, diagnostics, metrics, and published values.

Most developers should begin with the [parallel API](https://manivault.readthedocs.io/en/latest/api/core/parallel/index.html) and the [Parallel execution](https://manivault.readthedocs.io/en/latest/development/parallel_execution/index.html) guide. The pages below are the curated class-level reference for custom workflow plans and deeper framework integration. For architectural guidance, see the [Advanced workflow framework](https://manivault.readthedocs.io/en/latest/development/workflows/index.html) guide.

## API areas

- [Planning](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/index.html)
  - [Workflow plan](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_plan.html)
  - [Workflow handle](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html)
  - [Workflow options](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html)
  - [Workflow batching options](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_batching_options.html)
  - [Workflow cancellation options](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_cancellation_options.html)
  - [Workflow parallelization options](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_parallelization_options.html)
  - [Workflow profiling options](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_profiling_options.html)
  - [Workflow reporting options](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_reporting_options.html)
- [Execution](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/index.html)
  - [Abstract workflow plan executor](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/abstract_workflow_plan_executor.html)
  - [Workflow execution state](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_state.html)
  - [Workflow result future](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html)
  - [Workflow execution notifier](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_notifier.html)
- [Context](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/index.html)
  - [Workflow context base](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_context_base.html)
  - [Workflow context variant map](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_context_variant_map.html)
  - [Workflow execution context](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html)
- [Progress](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/index.html)
  - [Workflow progress node](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html)
- [Results](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/index.html)
  - [Workflow result base](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/workflow_result_base.html)
  - [Workflow result](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/workflow_result.html)
  - [Workflow stage result](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/workflow_stage_result.html)
  - [Workflow job result](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/workflow_job_result.html)
  - [Workflow result registry](https://manivault.readthedocs.io/en/latest/api/core/workflow/results/workflow_result_registry.html)
- [Reporting and metrics](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/index.html)
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
- [Utilities](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/index.html)
  - [Workflow execution node type](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/workflow_execution_node_type.html)
  - [Workflow execution lifecycle scope](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/workflow_execution_lifecycle_scope.html)
  - [Workflow runtime scope](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/workflow_runtime_scoped.html)
  - [Workflow console formatter](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/workflow_console_formatter.html)
  - [Workflow console dashboard](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/workflow_console_dashboard.html)
  - [Workflow console dashboard scope](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/workflow_console_dashboard_scope.html)
