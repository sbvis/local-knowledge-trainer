# PluginsFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_filter_model.html

**Documentation path:** `api/core/models/plugins/plugins_filter_model.html`

---

# PluginsFilterModel

**Qualified name:** `mv::PluginsFilterModel`

class PluginsFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Plugin filter model class.

    Sorting and filtering model for plugins models

    **Author**
    :   Thomas Kroes

    Public Types

    using FilterFunction = std::function<bool(plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")\*)>
    :   Filter function signature, the input are all datasets in the core and it returns the filtered datasets.

    Public Functions

    PluginsFilterModel(QObject \*parent = nullptr)
    :   Construct the filter model with `parent`.

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

    void setFilterFunction(const [FilterFunction](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_filter_model.html#_CPPv4N2mv18PluginsFilterModel14FilterFunctionE "mv::PluginsFilterModel::FilterFunction") &filterFunction)
    :   Set plugins filter function to `filterFunction`.

        Parameters:
        :   **filterFunction** – Filter lambda (triggered when plugins are added and/or removed)

    plugin::Types getFilterPluginTypes() const
    :   Get plugin types to filter.

        Returns:
        :   Plugin types

    void setFilterPluginTypes(const plugin::Types &filterPluginTypes)
    :   Set plugin filter types to `filterPluginTypes`.

        Parameters:
        :   **filterPluginTypes** – Plugin filter types
