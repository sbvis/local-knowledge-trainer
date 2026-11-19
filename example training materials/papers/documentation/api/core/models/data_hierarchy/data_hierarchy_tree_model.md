# Data hierarchy tree model

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/data_hierarchy_tree_model.html

**Documentation path:** `api/core/models/data_hierarchy/data_hierarchy_tree_model.html`

---

# Data hierarchy tree model

`DataHierarchyTreeModel` represents `DataHierarchyItem` parent-child relationships as a Qt tree model.

class DataHierarchyTreeModel : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")
:   Data hierarchy tree model class.

    Standard item model for managing the data hierarchy in tree form

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit DataHierarchyTreeModel(QObject \*parent = nullptr)
    :   Construct with `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    Qt::DropActions supportedDragActions() const override
    :   Get supported drag actions.

    void populateFromDataHierarchyManager()
    :   Populate the model with data hierarchy items from the data hierarchy manager.
