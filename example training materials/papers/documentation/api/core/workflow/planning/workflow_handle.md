# Workflow handle

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_handle.html

**Documentation path:** `api/core/workflow/planning/workflow_handle.html`

---

# Workflow handle

A stable identifier and display name for a workflow entity.

class WorkflowHandle
:   Lightweight identifier for workflow entities that can produce outputs.

    Workflow handles allow jobs and contexts to refer to producer outputs without retaining references to the producer object itself.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Functions

    WorkflowHandle()
    :   Constructs an invalid workflow handle.

    explicit WorkflowHandle(QUuid id, QString name = {})
    :   Constructs a workflow handle.

        Parameters:
        :   - **id** – Workflow entity identifier.
            - **name** – Human-readable workflow entity name.

    bool isValid() const
    :   Returns whether the handle is valid.

        Returns:
        :   True if the handle contains a non-null identifier.

    QUuid getId() const
    :   Returns the workflow entity identifier.

        Returns:
        :   Workflow entity identifier.

    QString getName() const
    :   Returns the workflow entity name.

        Returns:
        :   Human-readable workflow entity name.
