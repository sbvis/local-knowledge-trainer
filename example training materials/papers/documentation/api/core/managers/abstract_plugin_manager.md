# AbstractPluginManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html

**Documentation path:** `api/core/managers/abstract_plugin_manager.html`

---

# AbstractPluginManager

Use the plugin manager to create and destroy managed plugin instances. It applies factory creation policy and performs the surrounding initialization and ownership work. See [Requesting plugin instances](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/requesting_plugins.html) and [Plugin creation policy and instance limits](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/index.html).

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the plugins manager
mv::plugins().requestPlugin("PluginKind");
```

## Related

- Plugins [models](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/index.html)
- [Plugin communication and creation triggers](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/index.html)

**Qualified name:** `mv::AbstractPluginManager`

class AbstractPluginManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract plugin manager.

    Base abstract plugin manager class for managing plugin instances.

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractPluginManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void loadPluginFactories() = 0
    :   Loads all plugin factories from the plugin directory.

    virtual bool isPluginLoaded(const QString &kind) const = 0
    :   Determine whether a plugin of `kind` is loaded.

        Parameters:
        :   **kind** – Plugin kind

        Returns:
        :   Boolean determining whether a plugin of `kind` is loaded

    virtual plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*requestPlugin(const QString &kind, Datasets inputDatasets = Datasets(), Datasets outputDatasets = Datasets()) = 0
    :   Create a plugin of `kind` with input `datasets` If a view plugin is requested, this method will be delegated to the `requestViewPlugin` method.

        Parameters:
        :   - **kind** – Kind of plugin (name of the plugin)
            - **inputDatasets** – Zero or more datasets upon which the plugin is based (e.g. analysis plugin)
            - **outputDatasets** – Zero or more datasets that are the result of the plugin (e.g. transformation plugin)

        Returns:
        :   Pointer to created plugin, nullptr if creation failed

    template<typename PluginType> inline [PluginType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html#_CPPv4I0EN2mv21AbstractPluginManager13requestPluginEP10PluginTypeRK7QString8Datasets8Datasets "mv::AbstractPluginManager::requestPlugin::PluginType") \*requestPlugin(const QString &kind, Datasets inputDatasets = Datasets(), Datasets outputDatasets = Datasets())
    :   Create a plugin of `kind` with `inputDatasets` If a view plugin is requested, this method will be delegated to the `requestViewPlugin` method.

        Parameters:
        :   - **kind** – Kind of plugin (name of the plugin)
            - **inputDatasets** – Zero or more datasets upon which the plugin is based (e.g. analysis plugin)
            - **outputDatasets** – Zero or more datasets that are the result of the plugin (e.g. transformation plugin)

        Returns:
        :   Pointer of `PluginType` to created plugin, nullptr if creation failed

    virtual plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*requestViewPlugin(const QString &kind, plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*dockToViewPlugin = nullptr, gui::DockAreaFlag dockArea = gui::DockAreaFlag::Right, Datasets datasets = Datasets()) = 0
    :   Create a view plugin of `kind`, dock it to `dockToViewPlugin` at `dockArea` and assign the `datasets`.

        Parameters:
        :   - **kind** – Kind of plugin (name of the plugin)
            - **dockToViewPlugin** – View plugin instance to dock to
            - **dockArea** – Dock area to dock in
            - **datasets** – Datasets to assign to the view plugin

        Returns:
        :   Pointer of view plugin type to created view plugin, nullptr if creation failed

    virtual plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*requestViewPluginFloated(const QString &kind, Datasets datasets = Datasets()) = 0
    :   Create a view plugin of `kind` and float it on top of the main window.

        Parameters:
        :   - **kind** – Kind of plugin (name of the plugin)
            - **datasets** – Datasets to assign to the view plugin

        Returns:
        :   Pointer of view plugin type to created view plugin, nullptr if creation failed

    virtual void destroyPlugin([plugin](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html#_CPPv4N2mv21AbstractPluginManager13destroyPluginEPN6plugin6PluginE "mv::AbstractPluginManager::destroyPlugin::plugin")::Plugin \*plugin) = 0
    :   Destroy `plugin`.

        Parameters:
        :   **plugin** – Pointer to the plugin that is to be destroyed

    virtual void destroyPluginById(const QString &pluginId) = 0
    :   Destroy plugin by `pluginId`.

        Parameters:
        :   **pluginId** – Globally unique identifier of the plugin that is to be destroyed

    virtual plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*getPluginFactory(const QString &pluginKind) const = 0
    :   Get plugin factory from `pluginKind`.

        Parameters:
        :   **pluginKind** – Kind of plugin

        Returns:
        :   Plugin factory of `pluginKind`, nullptr if not found

    virtual std::vector<plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory")\*> getPluginFactoriesByType(const plugin::Type &pluginType) const = 0
    :   Get plugin factories for `pluginType`.

        Parameters:
        :   **pluginType** – Plugin type

        Returns:
        :   Vector of pointers to plugin factories

    virtual std::vector<plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory")\*> getPluginFactoriesByTypes(const plugin::Types &pluginTypes = plugin::Types{plugin::Type::ANALYSIS, plugin::Type::DATA, plugin::Type::LOADER, plugin::Type::WRITER, plugin::Type::TRANSFORMATION, plugin::Type::VIEW}) const = 0
    :   Get plugin factories for `pluginTypes` (by default it gets all plugins factories for all types)

        Parameters:
        :   **pluginTypes** – Plugin types

        Returns:
        :   Vector of pointers to plugin factories of `pluginTypes`

    virtual std::vector<plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")\*> getPluginsByFactory(const plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory) const = 0
    :   Get plugin instances for `pluginFactory`.

        Parameters:
        :   **pluginFactory** – Pointer to plugin factory

        Returns:
        :   Vector of pointers to plugin instances

    virtual std::vector<plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")\*> getPluginsByType(const plugin::Type &pluginType) const = 0
    :   Get plugin instances for `pluginType`.

        Parameters:
        :   **pluginType** – Plugin type

        Returns:
        :   Vector of pointers to plugin instances

    virtual std::vector<plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")\*> getPluginsByTypes(const plugin::Types &pluginTypes = plugin::Types{plugin::Type::ANALYSIS, plugin::Type::DATA, plugin::Type::LOADER, plugin::Type::WRITER, plugin::Type::TRANSFORMATION, plugin::Type::VIEW}) const = 0
    :   Get plugin instances for `pluginTypes` (by default it gets all plugins for all types)

        Parameters:
        :   **pluginTypes** – Plugin types

        Returns:
        :   Vector of pointers to plugin instances of `pluginTypes`

    virtual QStringList getPluginKindsByPluginTypes(const plugin::Types &pluginTypes = plugin::Types{plugin::Type::ANALYSIS, plugin::Type::DATA, plugin::Type::LOADER, plugin::Type::WRITER, plugin::Type::TRANSFORMATION, plugin::Type::VIEW}) const = 0
    :   Get plugin kinds by `pluginType`.

        Parameters:
        :   **pluginTypes** – Plugin type(s), all plugin types if empty

        Returns:
        :   List of plugin kinds

    virtual QStringList getLoadedPluginKinds(const plugin::Types &pluginTypes = plugin::Types{plugin::Type::ANALYSIS, plugin::Type::DATA, plugin::Type::LOADER, plugin::Type::WRITER, plugin::Type::TRANSFORMATION, plugin::Type::VIEW}) const = 0
    :   Get loaded plugin kinds by `pluginType`.

        Parameters:
        :   **pluginTypes** – Plugin type(s), all plugin types if empty

        Returns:
        :   List of loaded plugin kinds

    virtual QStringList getUsedPluginKinds(const plugin::Types &pluginTypes = plugin::Types{plugin::Type::ANALYSIS, plugin::Type::DATA, plugin::Type::LOADER, plugin::Type::WRITER, plugin::Type::TRANSFORMATION, plugin::Type::VIEW}) const = 0
    :   Get used plugin kinds by `pluginType`.

        Parameters:
        :   **pluginTypes** – Plugin type(s), all plugin types if empty

        Returns:
        :   List of used plugin kinds

    virtual gui::PluginTriggerActions getPluginTriggerActions(const plugin::Type &pluginType) const = 0
    :   Get plugin trigger actions by `pluginType`.

        Parameters:
        :   **pluginType** – Type of plugin e.g. analysis, exporter

        Returns:
        :   Vector of plugin trigger actions

    virtual gui::PluginTriggerActions getPluginTriggerActions(const plugin::Type &pluginType, const Datasets &datasets) const = 0
    :   Get plugin trigger actions by `pluginType` and `datasets`.

        Parameters:
        :   - **pluginType** – Type of plugin e.g. analysis, exporter
            - **datasets** – Vector of input datasets

        Returns:
        :   Vector of plugin trigger actions

    virtual gui::PluginTriggerActions getPluginTriggerActions(const plugin::Type &pluginType, const DataTypes &dataTypes) const = 0
    :   Get plugin trigger actions by `pluginType` and `dataTypes`.

        Parameters:
        :   - **pluginType** – Type of plugin e.g. analysis, exporter
            - **dataTypes** – Vector of input data types

        Returns:
        :   Vector of plugin trigger actions

    virtual gui::PluginTriggerActions getPluginTriggerActions(const QString &pluginKind, const Datasets &datasets) const = 0
    :   Get plugin trigger actions by `pluginKind` and `datasets`.

        Parameters:
        :   - **pluginKind** – Kind of plugin
            - **datasets** – Vector of input datasets

        Returns:
        :   Vector of plugin trigger actions

    virtual gui::PluginTriggerActions getPluginTriggerActions(const QString &pluginKind, const DataTypes &dataTypes) const = 0
    :   Get plugin trigger actions by `pluginKind` and `dataTypes`.

        Parameters:
        :   - **pluginKind** – Kind of plugin
            - **dataTypes** – Vector of input data types

        Returns:
        :   Vector of plugin trigger actions

    virtual QString getPluginGuiName(const QString &pluginKind) const = 0
    :   Get plugin GUI name from plugin kind.

        Parameters:
        :   - **pluginKind** – Kind of plugin
            - **GUI** – name of the plugin, empty if the plugin kind was not found

    virtual QIcon getPluginIcon(const QString &pluginKind) const = 0
    :   Get plugin icon from plugin kind.

        Parameters:
        :   **pluginKind** – Kind of plugin

        Returns:
        :   Plugin icon name of the plugin, null icon if the plugin kind was not found

    virtual const [PluginsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_list_model.html#_CPPv4N2mv16PluginsListModelE "mv::PluginsListModel") &getListModel() const = 0
    :   Get list model of all loaded plugins.

        Returns:
        :   Reference to plugins list model

    virtual const [PluginsTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_tree_model.html#_CPPv4N2mv16PluginsTreeModelE "mv::PluginsTreeModel") &getTreeModel() const = 0
    :   Get tree model of all loaded plugins.

        Returns:
        :   Reference to plugins tree model

    void pluginAdded([plugin](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html#_CPPv4N2mv21AbstractPluginManager11pluginAddedEPN6plugin6PluginE "mv::AbstractPluginManager::pluginAdded::plugin")::Plugin \*plugin)
    :   Signals that `plugin` instance is added to the plugin manager.

        Parameters:
        :   **plugin** – Pointer to the plugin that was added

    void pluginAboutToBeDestroyed([plugin](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html#_CPPv4N2mv21AbstractPluginManager24pluginAboutToBeDestroyedEPN6plugin6PluginE "mv::AbstractPluginManager::pluginAboutToBeDestroyed::plugin")::Plugin \*plugin)
    :   Signals that `plugin` is about to be destroyed by the plugin manager.

        Parameters:
        :   **plugin** – Pointer to the plugin that is about to be destroyed

    void pluginDestroyed(const QString &id)
    :   Signals that plugin with `id` is destroyed by the plugin manager.

        Parameters:
        :   **id** – Globally unique ID of the destroyed plugin

    void pluginFactoriesLoaded()
    :   Signals that all plugin factories have been loaded.

    Protected Functions

    virtual QStringList resolveDependencies(QDir pluginDir) const = 0
    :   Resolves plugin dependencies, returns list of resolved plugin filenames.

        Parameters:
        :   **pluginDir** – Plugin scan directory

        Returns:
        :   List of resolved plugin filenames
