# Parallel execution chain

**Source:** https://manivault.readthedocs.io/en/latest/api/core/parallel/parallel_execution_chain.html

**Documentation path:** `api/core/parallel/parallel_execution_chain.html`

---

# Parallel execution chain

`ParallelExecutionChain` is a move-only, single-use builder that combines sequential `run()` stages and parallel `forEach()` stages before executing the resulting workflow plan.

class ParallelExecutionChain
