# Data hierarchy filter model

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/data_hierarchy_filter_model.html

**Documentation path:** `api/core/models/data_hierarchy/data_hierarchy_filter_model.html`

---

# Data hierarchy filter model

`DataHierarchyFilterModel` filters and sorts a source data-hierarchy model for presentation in a Qt item view.

class DataHierarchyFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Data hierarchy filter model class.

    A class for filtering and sorting the data hierarchy model

    **Author**
    :   Thomas Kroes

    Public Functions

    DataHierarchyFilterModel(QObject \*parent = nullptr)
    :   Constructor.

        Parameters:
        :   **parent** – Pointer to parent object

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether a given row with give parent is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index
