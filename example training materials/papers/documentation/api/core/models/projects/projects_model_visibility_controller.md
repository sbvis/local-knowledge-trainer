# ProjectsModelVisibilityController

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_model_visibility_controller.html

**Documentation path:** `api/core/models/projects/projects_model_visibility_controller.html`

---

# ProjectsModelVisibilityController

**Qualified name:** `mv::ProjectsModelVisibilityController`

class ProjectsModelVisibilityController : public QObject
:   Projects model visibility controller class.

    Controls the visibility of projects in a projects model, ensuring that among duplicate projects (with the same UUID) only one is visible based on a user-defined criterion

    **Author**
    :   Thomas Kroes

    Public Types

    using VisibilityRuleFunction = std::function<QModelIndex(const QModelIndexList&, QStandardItemModel\*)>
    :   Function type to assign visibility among duplicates.

    Public Functions

    ProjectsModelVisibilityController([AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel") \*projectsModel, [VisibilityRuleFunction](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_model_visibility_controller.html#_CPPv4N2mv33ProjectsModelVisibilityController22VisibilityRuleFunctionE "mv::ProjectsModelVisibilityController::VisibilityRuleFunction") visibilityRuleFunction = {}, QObject \*parent = nullptr)
    :   Construct a visibility controller for the given projects model.

        Parameters:
        :   - **projectsModel** – Pointer to the projects model to control
            - **visibilityRuleFunction** – Function to assign visibility among duplicates
            - **parent** – Pointer to parent QObject

    void recomputeAll()
    :   Recompute visibility for all rows in the model.
