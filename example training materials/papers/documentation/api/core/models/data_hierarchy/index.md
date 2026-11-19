# Data hierarchy models

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/index.html

**Documentation path:** `api/core/models/data_hierarchy/index.html`

---

# Data hierarchy models

These models present and filter the project data hierarchy for specialized Qt item views. Most plugin code should use `Dataset<T>`, `DataHierarchyItem`, and `mv::dataHierarchy()` directly.

For guidance on when to use a model and how to avoid duplicating hierarchy state, see [Building a custom hierarchy view](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/custom_views.html).

- [Abstract data hierarchy model](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html)
- [Data hierarchy tree model](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/data_hierarchy_tree_model.html)
- [Data hierarchy filter model](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/data_hierarchy_filter_model.html)

`ActionsListModel` is an actions model and is documented separately from the hierarchy model family.
