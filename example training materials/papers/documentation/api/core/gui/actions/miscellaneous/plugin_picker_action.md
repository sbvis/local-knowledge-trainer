# PluginPickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_picker_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/plugin_picker_action.html`

---

# PluginPickerAction

**Qualified name:** `mv::gui::PluginPickerAction`

class PluginPickerAction : public mv::gui::[OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction")
:   Plugin picker action class.

    Action class for picking a plugin from a list.

    Note: This class is not fully production yet, it needs some thorough testing

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE PluginPickerAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    plugin::Plugins getPlugins() const
    :   Get plugins.

        Returns:
        :   Vector of plugins

    void setPlugins(const plugin::Plugins &plugins, bool silent = false)
    :   Set the `plugins` from which can be picked (mode is set to StorageMode::Manual)

        Parameters:
        :   - **plugins** – Plugins from which can be picked
            - **silent** – Whether the signal pluginsChanged is emitted

    void setFilterFunction(const [PluginsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_filter_model.html#_CPPv4N2mv18PluginsFilterModelE "mv::PluginsFilterModel")::[FilterFunction](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_filter_model.html#_CPPv4N2mv18PluginsFilterModel14FilterFunctionE "mv::PluginsFilterModel::FilterFunction") &filterFunction)
    :   Set plugins filter function to `filterFunction`.

        Parameters:
        :   **filterFunction** – Filter lambda (triggered when plugins are added and/or removed)

    plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*getCurrentPlugin() const
    :   Get selected plugin.

        Returns:
        :   Pointer to selected plugin (maybe nullptr)

    template<typename PluginType> inline [PluginType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_picker_action.html#_CPPv4I0ENK2mv3gui18PluginPickerAction16getCurrentPluginEP10PluginTypev "mv::gui::PluginPickerAction::getCurrentPlugin::PluginType") \*getCurrentPlugin() const
    :   Get selected plugin of `PluginType`.

        Returns:
        :   Pointer to selected plugin of `PluginType` (maybe nullptr)

    void setCurrentPlugin(const plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*currentPlugin)
    :   Set current plugin to `currentPlugin`.

        Parameters:
        :   **currentPlugin** – Pointer to current plugin (maybe nullptr)

    void setCurrentPlugin(const QString &pluginId)
    :   Set current plugin by `pluginId`.

        Parameters:
        :   **pluginId** – Current plugin globally unique identifier

    QString getCurrentPluginId() const
    :   Get current plugin globally unique identifier.

        Returns:
        :   The globally unique identifier of the currently selected plugin (if any)

    [AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")::[PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationModeE "mv::AbstractPluginsModel::PopulationMode") getPopulationMode() const
    :   Get current population mode.

        Returns:
        :   Population mode

    void setPopulationMode([AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")::[PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationModeE "mv::AbstractPluginsModel::PopulationMode") populationMode)
    :   Set population mode to `populationMode`.

        Parameters:
        :   **populationMode** – Population mode

    plugin::Types getFilterPluginTypes() const
    :   Get plugin types to filter.

        Returns:
        :   Plugin types

    void setFilterPluginTypes(const plugin::Types &filterPluginTypes)
    :   Set plugin filter types to `filterPluginTypes`.

        Parameters:
        :   **filterPluginTypes** – Plugin filter types

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void pluginPicked(plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*pickedPlugin)
    :   Signals that `pickedPlugin` is picked.

        Parameters:
        :   **pickedPlugin** – Pointer to picked plugin

    void pluginsChanged(const plugin::Plugins &plugins)
    :   Signals that selectable plugins changed.

        Parameters:
        :   **plugins** – Selectable plugins

    void populationModeChanged([AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")::[PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationModeE "mv::AbstractPluginsModel::PopulationMode") previousPopulationMode, [AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")::[PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationModeE "mv::AbstractPluginsModel::PopulationMode") currentPopulationMode)
    :   Signals that the population mode changed from `previousPopulationMode` to `currentPopulationMode`.

        Parameters:
        :   - **previousPopulationMode** – Previous population mode
            - **currentPopulationMode** – Current population mode

    void filterPluginTypesChanged(const plugin::Types &previousFilterPluginTypes, const plugin::Types &currentFilterPluginTypes)
    :   Signals that the filter plugin types changed from `previousPopulationMode` to `currentPopulationMode`.

        Parameters:
        :   - **previousFilterPluginTypes** – Previous filter plugin types
            - **currentFilterPluginTypes** – Current filter plugin types

    Protected Functions

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive) override
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions
