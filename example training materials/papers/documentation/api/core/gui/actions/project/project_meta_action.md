# ProjectMetaAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html

**Documentation path:** `api/core/gui/actions/project/project_meta_action.html`

---

# ProjectMetaAction

**Qualified name:** `mv::ProjectMetaAction`

class ProjectMetaAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) meta class.

    [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) class for preview purposes (contains project meta data).

    **Author**
    :   Thomas Kroes

    Public Functions

    ProjectMetaAction([Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") \*project, QObject \*parent = nullptr)
    :   Construct project with source `project` and `parent` object.

        Parameters:
        :   - **project** – Pointer to source project to get the meta data from
            - **parent** – Pointer to parent object

    ProjectMetaAction(const QString &filePath, QObject \*parent = nullptr)
    :   Construct project from `filePath` and `parent` object.

        Parameters:
        :   - **filePath** – Path of the project meta file
            - **parent** – Pointer to parent object

    [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") \*getProject() const
    :   Get owning project.

        Returns:
        :   Pointer to owning project (might be nullptr if project meta action is used in isolation)

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load project from variant.

        Parameters:
        :   **variantMap** – Variant representation of the project

    virtual workflow::UniqueWorkflowPlan fromVariantMapWorkflow(QVariantMap variantMap) override
    :   Create a workflow that restores the object state.

        This function constructs a workflow but does not execute it.

        The returned workflow must fully restore the object when executed.

        Implementations may use sequential, parallel, nested, or batched stages and may publish progress, warnings, messages, and outputs.

        The default implementation creates a simple workflow that invokes [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#classmv_1_1ProjectMetaAction_1a269a52485ded2f4a6547088622acfc6b).

        Framework code may compose this workflow directly, for example as a nested workflow within a larger serialization workflow.

        Parameters:
        :   **variantMap** – Serialized object state.

        Returns:
        :   Workflow plan that restores the object state.

    virtual QVariantMap toVariantMap() const override
    :   Save project to variant.

        Returns:
        :   Variant representation of the project
