# PluginsTreeModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_tree_model.html

**Documentation path:** `api/core/models/plugins/plugins_tree_model.html`

---

# PluginsTreeModel

**Qualified name:** `mv::PluginsTreeModel`

class PluginsTreeModel : public mv::[AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")
:   Plugins tree model class.

    Tree model for loaded plugins

    **Author**
    :   Thomas Kroes

    Public Functions

    PluginsTreeModel(PopulationMode populationMode = PopulationMode::Automatic, QObject \*parent = nullptr)
    :   Construct with `populationMode` and pointer to `parent` object.

        Parameters:
        :   - **populationMode** – Population mode
            - **parent** – Pointer to parent object

    virtual plugin::Plugins getPlugins() const override
    :   Get plugins.

        Returns:
        :   Vector of plugins

    virtual plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*getPlugin(const QModelIndex &modelIndex) const override
    :   Get plugin for `modelIndex`.

        Parameters:
        :   **modelIndex** – Index to retrieve

        Returns:
        :   Pointer to plugin (maybe nullptr)

    virtual void setPlugins(const plugin::Plugins &plugins) override
    :   Set the `plugins` from which can be picked (mode is set to StorageMode::Manual)

        Parameters:
        :   **plugins** – Vector of plugins

    virtual void populateFromPluginManager() override
    :   Synchronize the plugins with the core.

    virtual void addPlugin([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_tree_model.html#_CPPv4N2mv16PluginsTreeModel9addPluginEPN6plugin6PluginE "mv::PluginsTreeModel::addPlugin::plugin")::Plugin \*plugin) override
    :   Add `plugin` to the model.

        Parameters:
        :   **plugin** – Pointer to plugin

    virtual void removePlugin([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_tree_model.html#_CPPv4N2mv16PluginsTreeModel12removePluginEPN6plugin6PluginE "mv::PluginsTreeModel::removePlugin::plugin")::Plugin \*plugin) override
    :   Remove `plugin` from the model.

        Parameters:
        :   **plugin** – Pointer to plugin
