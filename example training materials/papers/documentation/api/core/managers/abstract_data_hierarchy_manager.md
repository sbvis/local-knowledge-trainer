# AbstractDataHierarchyManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_hierarchy_manager.html

**Documentation path:** `api/core/managers/abstract_data_hierarchy_manager.html`

---

# AbstractDataHierarchyManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the data hierarchy manager
mv::dataHierarchy().getItems();
```

## Related

- [Working with data and datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/index.html)
- [Interacting with the data hierarchy](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/index.html)
- Core [data API](https://manivault.readthedocs.io/en/latest/api/core/data/index.html)
- Data hierarchy [models](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/index.html)
- Data hierarchy [`item`](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem")

**Qualified name:** `mv::AbstractDataHierarchyManager`

class AbstractDataHierarchyManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract data hierarchy manager.

    Base abstract data hierarchy manager class for organizing the dataset hierarchy.

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractDataHierarchyManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual const [DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*getItem(const QString &datasetId) const = 0
    :   Get hierarchy item by `datasetId`.

        Parameters:
        :   **datasetId** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) GUID

        Returns:
        :   Pointer to data hierarchy item, nullptr if not found

    virtual [DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*getItem(const QString &datasetId) = 0
    :   Get hierarchy item by `datasetId`.

        Parameters:
        :   **datasetId** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) GUID

        Returns:
        :   Pointer to data hierarchy item, nullptr if not found

    virtual DataHierarchyItems getItems() const = 0
    :   Get all items.

        Returns:
        :   List of items

    virtual DataHierarchyItems getChildren([DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") &dataHierarchyItem, const bool &recursive = true) = 0
    :   Get dataset children.

        Parameters:
        :   - **dataHierarchyItem** – Reference to data hierarchy item
            - **recursive** – Whether to get all children in a recursive manner

        Returns:
        :   Children

    virtual DataHierarchyItems getTopLevelItems() = 0
    :   Get top-level items.

        Returns:
        :   Top-level items

    virtual void select(DataHierarchyItems items, bool clear = true) = 0
    :   Select data hierarchy `items`.

        Parameters:
        :   - **items** – List of pointers to data hierarchy items to select
            - **clear** – Clear the current selections before selection

    virtual void selectAll() = 0
    :   Select all items.

    virtual void clearSelection() = 0
    :   Clear the item selection.

    virtual DataHierarchyItems getSelectedItems() const = 0
    :   Get selected items.

        Returns:
        :   List of selected items

    void itemAdded([DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*dataHierarchyItem)
    :   Signals that `dataHierarchyItem` is added to the hierarchy manager.

        Parameters:
        :   **dataHierarchyItem** – Pointer to added data hierarchy item

    void itemAboutToBeRemoved([DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*dataHierarchyItem)
    :   Signals that `dataHierarchyItem` is about to be removed from the hierarchy manager.

        Parameters:
        :   **dataHierarchyItem** – Pointer to data hierarchy item which is about to be removed

    void itemRemoved(const QString &datasetId)
    :   Signals that hierarchy item `datasetId` is removed from the hierarchy manager.

        Parameters:
        :   **datasetId** – GUID of the removed dataset

    void itemParentChanged([DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*dataHierarchyItem)
    :   Signals that the parent of `dataHierarchyItem` changed.

        Parameters:
        :   **dataHierarchyItem** – Pointer to data hierarchy item of which the parent changed

    void selectedItemsChanged(DataHierarchyItems selectedItems)
    :   Signals that the selected items changed.

        Parameters:
        :   **selectedItems** – Pointers to selected data hierarchy items

    Protected Functions

    virtual void addItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> parentDataset, const bool &visible = true) = 0
    :   Add a dataset to the hierarchy.

        Parameters:
        :   - **dataset** – Smart pointer to dataset
            - **parentDataset** – Smart pointer to parent dataset (if any)
            - **visible** – Whether the dataset is visible in the gui

    virtual void removeItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset) = 0
    :   Removes data hierarchy for `dataset` from the data hierarchy.

        Parameters:
        :   **dataset** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) to remove the data hierarchy item for

    virtual void removeAllItems() = 0
    :   Removes all items from the data hierarchy manager in a top-down manner.
