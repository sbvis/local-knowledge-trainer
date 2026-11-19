# Overview

**Source:** https://manivault.readthedocs.io/en/latest/development/workflows/overview.html

**Documentation path:** `development/workflows/overview.html`

---

# Overview

The workflow framework separates an operation’s **description** from its **execution**. A `WorkflowPlan` describes stages and jobs. An `AbstractWorkflowPlanExecutor` runs that plan while a `WorkflowExecutionContext` exposes the current node’s shared state, progress, reporting, outputs, and cancellation status. Execution produces a `WorkflowResult`, synchronously or through a `WorkflowResultFuture`.

This separation is useful when an operation must do more than invoke a function. A workflow can:

- run independent jobs concurrently while preserving stage ordering;
- move selected jobs to the GUI thread;
- embed another workflow and include its progress;
- aggregate progress using relative weights;
- propagate cancellation through the execution hierarchy;
- collect structured messages, metrics, outputs, and timing information;
- run cleanup regardless of whether the main stages succeeded.

## System at a glance

```text
Caller -> WorkflowPlan -> Workflow plan executor -> Execution contexts
                    ^                                |-- Progress tree
                    |                                |-- Report tree
              WorkflowOptions                       `-- Metrics and outputs

Workflow plan executor -> WorkflowResult / WorkflowResultFuture
```

The executor owns the scheduling details. Workflow code should express dependencies through stages and use the context for runtime interaction instead of coordinating threads directly.

## When to use it

Prefer workflow-backed execution for a new long-running operation. Begin with the [high-level Parallel utilities](https://manivault.readthedocs.io/en/latest/development/parallel_execution/index.html) when the work fits a common operation, collection, mapping, or pipeline shape. Define a custom workflow plan when it has multiple observable steps, needs task-backed progress, crosses thread boundaries, contains independent work, or must return structured diagnostics. A direct function call remains preferable for small synchronous work that needs none of those facilities.

“Long-running operation” refers to an application-level unit that benefits from managed lifecycle and observability. It does not imply that every expensive inner loop should become a workflow stage or job. Keep fine-grained numerical parallelism in a suitable kernel-level API and let the workflow coordinate the surrounding operation. See [Intended scope and granularity](https://manivault.readthedocs.io/en/latest/development/parallel_execution/scope_and_granularity.html).

Use a directly managed ManiVault task only when execution is already owned elsewhere and needs progress presentation. A task does not schedule work, preserve structured failure, or replace the workflow result. See [Choosing an execution model](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/choosing_an_execution_model.html).

## Public and internal pieces

The types in `mv::workflow` form the reusable framework API. The current concrete executor is an internal Taskflow-based implementation. Callers should depend on `AbstractWorkflowPlanExecutor` and the public plan/context/result contracts rather than on Taskflow details.

See [Defining workflows](https://manivault.readthedocs.io/en/latest/development/workflows/defining_workflows.html) for plan construction and the [API reference](https://manivault.readthedocs.io/en/latest/api/core/workflow/index.html) for individual types.
