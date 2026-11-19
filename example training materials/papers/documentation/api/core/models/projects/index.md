# Projects

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/projects/index.html

**Documentation path:** `api/core/models/projects/index.html`

---

# Projects

**ManiVault** manages the lifetime of projects through the [`mv::AbstractProjectManager`](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManagerE "mv::AbstractProjectManager"). Projects are tracked in dedicated **list** and **tree** models, which are primarily used by the UI. The model classes below are for storing and filtering projects.

Note

This API is **stable** and intended for use by **core developers**. Plugin developers typically do not need to interact with it directly, as it is fully wrapped by the projects manager.

- [AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html)
- [ProjectsTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_tree_model.html)
- [ProjectsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_list_model.html)
- [ProjectsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_filter_model.html)
- [ProjectsModelProject](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_model_project.html)
- [ProjectsModelVisibilityController](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_model_visibility_controller.html)
