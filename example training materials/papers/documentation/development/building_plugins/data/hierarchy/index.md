# Interacting with the data hierarchy

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/index.html

**Documentation path:** `development/building_plugins/data/hierarchy/index.html`

---

# Interacting with the data hierarchy

The data hierarchy is ManiVault’s project-wide tree of registered datasets. Each dataset has one `DataHierarchyItem` that stores presentation state and connects the dataset to hierarchy views, selection, attached actions, and context menus.

## Choose the right abstraction

| Need | Use |
| --- | --- |
| Read semantic dataset relationships | `Dataset<T>` methods such as `getParent()` and `getChildren()` |
| Find or select rows across the application hierarchy | `mv::dataHierarchy()` |
| Change visibility, expansion, or row selection | `DataHierarchyItem` |
| Offer a dataset-specific operation | Attach a long-lived `WidgetAction` to the item |
| Build a specialized hierarchy view | Hierarchy tree and filter models |

Important

Hierarchy selection selects dataset rows in the application interface. It does not change the elements selected inside any dataset.

- [Finding items and navigating the tree](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/navigating.html)
- [Selection and presentation state](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/selection_and_presentation.html)
- [Parenting, changes, and lifetime](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/parenting_and_lifetime.html)
- [Attached actions and context menus](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/attached_actions.html)
- [Building a custom hierarchy view](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/custom_views.html)

Hierarchy placement describes presentation and navigation. For derived, full, subset, and proxy relationships, continue with [Hierarchy, derived data, and subsets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy_derived_and_subsets.html).

For exact signatures, see the [hierarchy manager API](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_hierarchy_manager.html) and [DataHierarchyItem API](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html).
