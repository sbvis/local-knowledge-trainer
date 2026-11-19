# RecentFilesFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/recent_files_filter_model.html

**Documentation path:** `api/core/models/recent_files/recent_files_filter_model.html`

---

# RecentFilesFilterModel

**Qualified name:** `mv::RecentFilesFilterModel`

class RecentFilesFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Recent files filter model class.

    For filtering recent files model class.

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    RecentFilesFilterModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether `row` with `parent` is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index

        Returns:
        :   Boolean indicating whether the item is filtered in or out

    bool lessThan(const QModelIndex &lhs, const QModelIndex &rhs) const override
    :   Compares two model indices plugin `lhs` with `rhs`.

        Parameters:
        :   - **lhs** – Left-hand model index
            - **rhs** – Right-hand model index

    void setSourceModel(QAbstractItemModel \*sourceModel) override
    :   Set source model to `sourceModel`.

        Parameters:
        :   **sourceModel** – Pointer to source model
