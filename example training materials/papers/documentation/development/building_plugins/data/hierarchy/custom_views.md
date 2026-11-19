# Building a custom hierarchy view

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/custom_views.html

**Documentation path:** `development/building_plugins/data/hierarchy/custom_views.html`

---

# Building a custom hierarchy view

Most plugins should consume datasets and hierarchy-manager signals rather than recreate the application’s data hierarchy. When a specialized tree view is genuinely useful, ManiVault provides models that mirror hierarchy state.

- `AbstractDataHierarchyModel` defines shared hierarchy roles and item access.
- `DataHierarchyTreeModel` presents the hierarchy as a tree.
- `DataHierarchyFilterModel` filters and sorts a source hierarchy model.

Use the tree model as the source and place the filter model between it and a Qt item view. Map indexes through the proxy before retrieving source-model items.

```cpp
auto sourceIndex = filterModel.mapToSource(proxyIndex);
auto* item = treeModel.getItem(sourceIndex);

if (!item)
    return;

auto dataset = item->getDataset();
```

Consult the concrete model API for the exact item accessor and roles supported by the current version.

## Do not duplicate hierarchy state

The manager and items remain authoritative. React to model changes or manager signals instead of maintaining a parallel tree of raw `DataHierarchyItem*` pointers. If a view caches dataset identity, cache IDs or `Dataset<T>` handles and resolve hierarchy items when needed.

Use item methods for selection, visibility, expansion, and locking so the manager and all hierarchy views stay synchronized. Directly modifying `QStandardItem` state can update one view without updating the underlying hierarchy.

See the [data hierarchy models API](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/index.html) for the model classes.
