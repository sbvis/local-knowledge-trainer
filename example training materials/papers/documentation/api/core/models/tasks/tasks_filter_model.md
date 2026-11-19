# TasksFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_filter_model.html

**Documentation path:** `api/core/models/tasks/tasks_filter_model.html`

---

# TasksFilterModel

**Qualified name:** `mv::TasksFilterModel`

class TasksFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Tasks filter class.

    Proxy model for filtering tasks

    **Author**
    :   Thomas Kroes

    Public Functions

    TasksFilterModel(QObject \*parent = nullptr)
    :   Construct with parent `parent` object.

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
    :   Compares two cluster items.

        Parameters:
        :   - **lhs** – Left cluster
            - **rhs** – Right cluster

    bool hasKillableTasks() const
    :   Determines whether one (or more) tasks are killable.

        Returns:
        :   Boolean determining whether there are any killable tasks
