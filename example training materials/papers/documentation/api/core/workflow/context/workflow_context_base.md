# Workflow context base

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_context_base.html

**Documentation path:** `api/core/workflow/context/workflow_context_base.html`

---

# Workflow context base

The polymorphic base for operation-specific data shared through a workflow.

class WorkflowContextBase
:   Optional workflow-specific context shared by all stages and jobs.

    The context is the intended mechanism for sharing input, output, and intermediate data across a workflow. Implementations should use a typed context class when workflow stages need to communicate.

    Thread safety is the responsibility of the context implementation. For parallel stages, prefer per-job output storage followed by a sequential merge stage, or protect shared mutable state with appropriate locking.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Subclassed by [mv::workflow::WorkflowContextVariantMap](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_context_variant_map.html#classmv_1_1workflow_1_1WorkflowContextVariantMap)

    Public Functions

    virtual ~WorkflowContextBase() = default
    :   Destroys the workflow context.
