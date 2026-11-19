# Parallel execution

**Source:** https://manivault.readthedocs.io/en/latest/api/core/parallel/index.html

**Documentation path:** `api/core/parallel/index.html`

---

# Parallel execution

The parallel API is ManiVault’s preferred high-level interface for scheduled and concurrent work. `Parallel` runs individual operations, processes or maps collections in parallel, and starts staged execution chains. `ParallelExecutionChain` combines sequential and parallel phases while leaving plan construction and executor integration to the underlying workflow framework.

Start with the [Parallel execution developer guide](https://manivault.readthedocs.io/en/latest/development/parallel_execution/index.html) for examples, ownership rules, result handling, and thread-safety guidance. Use the [advanced workflow API](https://manivault.readthedocs.io/en/latest/api/core/workflow/index.html) only when these high-level operations do not express the required execution model.

- [Parallel](https://manivault.readthedocs.io/en/latest/api/core/parallel/parallel.html)
- [Parallel execution chain](https://manivault.readthedocs.io/en/latest/api/core/parallel/parallel_execution_chain.html)
