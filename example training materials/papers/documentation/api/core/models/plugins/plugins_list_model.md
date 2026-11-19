# PluginsListModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_list_model.html

**Documentation path:** `api/core/models/plugins/plugins_list_model.html`

---

# PluginsListModel

**Qualified name:** `mv::PluginsListModel`

class PluginsListModel : public mv::[AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")
:   Plugins list model class.

    List model for loaded plugins

    **Author**
    :   Thomas Kroes

    Public Functions

    PluginsListModel(PopulationMode populationMode = PopulationMode::Automatic, QObject \*parent = nullptr)
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

    virtual void addPlugin([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_list_model.html#_CPPv4N2mv16PluginsListModel9addPluginEPN6plugin6PluginE "mv::PluginsListModel::addPlugin::plugin")::Plugin \*plugin) override
    :   Add `plugin` to the model.

        Parameters:
        :   **plugin** – Pointer to plugin

    virtual void removePlugin([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_list_model.html#_CPPv4N2mv16PluginsListModel12removePluginEPN6plugin6PluginE "mv::PluginsListModel::removePlugin::plugin")::Plugin \*plugin) override
    :   Remove `plugin` from the model.

        Parameters:
        :   **plugin** – Pointer to plugin

    QModelIndex getIndexFromPlugin(const [plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_list_model.html#_CPPv4NK2mv16PluginsListModel18getIndexFromPluginEPKN6plugin6PluginE "mv::PluginsListModel::getIndexFromPlugin::plugin")::Plugin \*plugin) const
    :   Get index from pointer to `plugin`.

        Parameters:
        :   **plugin** – Const pointer to plugin

        Returns:
        :   Model index (invalid if not found)

    QModelIndex getIndexFromPlugin(const QString &pluginId) const
    :   Get index from `pluginId`.

        Parameters:
        :   **pluginId** – Plugin globally unique identifier to retrieve the row index for

        Returns:
        :   Model index (invalid if not found)

    QStandardItem \*getItemFromPlugin(const [plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_list_model.html#_CPPv4NK2mv16PluginsListModel17getItemFromPluginEPKN6plugin6PluginE "mv::PluginsListModel::getItemFromPlugin::plugin")::Plugin \*plugin) const
    :   Get item from pointer to `plugin`.

        Parameters:
        :   **plugin** – Const pointer to plugin

        Returns:
        :   Pointer to found item, nullptr otherwise
