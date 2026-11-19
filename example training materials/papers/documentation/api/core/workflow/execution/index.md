# Execution

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/index.html

**Documentation path:** `api/core/workflow/execution/index.html`

---

# Execution

Execution types consume workflow plans, schedule their jobs, maintain root execution state, and expose synchronous or asynchronous completion. Callers should use the abstract executor contract rather than depend on the internal scheduling backend.

For the end-to-end lifecycle, see [Execution model](https://manivault.readthedocs.io/en/latest/development/workflows/execution_model.html).

- [Abstract workflow plan executor](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/abstract_workflow_plan_executor.html)
- [Workflow execution state](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_state.html)
- [Workflow result future](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html)
- [Workflow execution notifier](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_execution_notifier.html)
