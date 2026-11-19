# ProjectsListModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_list_model.html

**Documentation path:** `api/core/models/projects/projects_list_model.html`

---

# ProjectsListModel

**Qualified name:** `mv::ProjectsListModel`

class ProjectsListModel : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")
:   Projects list model class.

    Contains projects in a list.

    **Author**
    :   Thomas Kroes

    Public Functions

    ProjectsListModel(const PopulationMode &mode = PopulationMode::Automatic, QObject \*parent = nullptr)
    :   Construct with population `mode` and pointer to `parent` object.

        Parameters:
        :   - **mode** – Mode of the model (automatic/manual)
            - **parent** – Pointer to parent object

    Protected Functions

    virtual void populate(util::ProjectsModelProjectSharedPtrs projects) override
    :   Populate the model with the given projects.

        Parameters:
        :   **projects** – Shared pointers to projects to populate the model with
