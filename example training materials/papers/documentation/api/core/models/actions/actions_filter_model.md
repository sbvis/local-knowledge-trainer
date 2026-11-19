# ActionsFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_filter_model.html

**Documentation path:** `api/core/models/actions/actions_filter_model.html`

---

# ActionsFilterModel

**Qualified name:** `mv::ActionsFilterModel`

class ActionsFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Actions filter class.

    Proxy model for filtering concrete actions model classes (derived from [AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel))

    **Author**
    :   Thomas Kroes

    Public Functions

    ActionsFilterModel(QObject \*parent = nullptr)
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

    gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction(std::int32\_t rowIndex)
    :   Get action for filter model `index`.

        Parameters:
        :   **rowIndex** – Row index to retrieve the action for

        Returns:
        :   Pointer to action (nullptr if not found)
