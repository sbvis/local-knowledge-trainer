# Parallel execution

**Source:** https://manivault.readthedocs.io/en/latest/development/parallel_execution/index.html

**Documentation path:** `development/parallel_execution/index.html`

---

# Parallel execution

Parallel execution is an optional API for scheduling work and running independent operations concurrently. You do not have to use it to build a ManiVault plugin or application. Ordinary synchronous functions, standard action serialization, and other existing Core APIs continue to work without calling `mv::Parallel` or defining a custom workflow.

Use these pages when an operation is substantial enough that moving work to worker threads, processing independent items concurrently, reporting progress, supporting cancellation, or preserving a structured result would improve the implementation or user experience.

## Common recipes

Start with the outcome you need. These links lead to concise recipes with the appropriate API and a small example.

- [Run one substantial operation on a worker and wait for its result](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-run-one-operation)
- [Process independent items concurrently](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-process-items)
- [Transform a collection and preserve input order](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-map-results)
- [Combine preparation, parallel work, and finalization](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-stage-pipeline)
- [Limit concurrency or force serial execution](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-limit-workers)
- [Keep the interface responsive and show live progress](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-live-progress)
- [Make a long-running operation cancellable](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-cancellation)
- [Report intermediate progress and diagnostics](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-report-progress)
- [Prepare on workers and commit on the GUI thread](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-gui-commit)
- [Process a very large collection in bounded batches](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-batched-work)
- [Parallelize expensive or staged serialization](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-workflow-serialization)
- [Show progress for work scheduled by another executor](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html#recipe-external-task)

Simple action state still uses [ordinary action serialization](https://manivault.readthedocs.io/en/latest/development/building_plugins/actions/serialization.html); no parallel API is needed. For tight numerical loops or an already internally threaded kernel, first read [Intended scope and granularity](https://manivault.readthedocs.io/en/latest/development/parallel_execution/scope_and_granularity.html).

## Choose the smallest suitable level

- **Direct synchronous code:** use it when the work is short, bounded, and does not need execution progress or cancellation.
- **High-level `mv::Parallel` utilities:** use them when the caller may wait and the work fits one operation, a collection, a mapping, or a straightforward sequence of stages.
- **Advanced workflow framework:** use it when the operation needs asynchronous lifetime, task-backed progress, cancellation, GUI-thread phases, nesting, custom weights, or detailed reporting.

`mv::Parallel` is the concise entry point when the middle level fits. It builds on the workflow engine without requiring developers to construct workflow plans themselves. Its terminal calls are blocking: the work can run on workflow workers, but the call returns only after the operation finishes. Do not use a blocking helper from a context that must remain responsive.

## Explore the built-in examples

On Windows, ManiVault includes a hidden **Dev** menu with workflow test scenarios. Press `Ctrl+Alt+Shift+D` to reveal the menu, then open **Dev → Workflow testing**. You can run an individual scenario or execute the complete scenario set sequentially.

These scenarios provide a quick way to observe workflow scheduling, progress, reporting, and results in the application. They are demonstrations and integration tests, not setup steps or APIs that plugin code must call.

![Revealing the Dev menu and running workflow test scenarios](https://manivault.readthedocs.io/en/latest/_images/parallel_workflow_examples.gif)

## Start using the high-level API

Begin with [Getting started](https://manivault.readthedocs.io/en/latest/development/parallel_execution/getting_started.html), then continue with the guide matching the shape of the operation.

- [Getting started](https://manivault.readthedocs.io/en/latest/development/parallel_execution/getting_started.html)
- [Running an operation](https://manivault.readthedocs.io/en/latest/development/parallel_execution/running_operations.html)
- [Processing collections](https://manivault.readthedocs.io/en/latest/development/parallel_execution/processing_collections.html)
- [Mapping collections](https://manivault.readthedocs.io/en/latest/development/parallel_execution/mapping_collections.html)
- [Building execution chains](https://manivault.readthedocs.io/en/latest/development/parallel_execution/execution_chains.html)
- [Examples and recipes](https://manivault.readthedocs.io/en/latest/development/parallel_execution/examples.html)

## Advanced decisions and controls

The following pages explain configuration, safety, granularity, and the point at which a custom workflow becomes appropriate. They are important when the basic utilities fit only partially, but they are not prerequisites for understanding what the API is for.

- [Options, reporting, and cancellation](https://manivault.readthedocs.io/en/latest/development/parallel_execution/options_and_cancellation.html)
- [Thread safety and lifetime](https://manivault.readthedocs.io/en/latest/development/parallel_execution/thread_safety.html)
- [Intended scope and granularity](https://manivault.readthedocs.io/en/latest/development/parallel_execution/scope_and_granularity.html)
- [Advanced workflow framework](https://manivault.readthedocs.io/en/latest/development/workflows/index.html)

## API reference

For exact signatures, see the [parallel API reference](https://manivault.readthedocs.io/en/latest/api/core/parallel/index.html). The underlying types are documented in the [workflow API reference](https://manivault.readthedocs.io/en/latest/api/core/workflow/index.html).
