# AbstractPluginsModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html

**Documentation path:** `api/core/models/plugins/abstract_plugins_model.html`

---

# AbstractPluginsModel

**Qualified name:** `mv::AbstractPluginsModel`

class AbstractPluginsModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Abstract plugin manager model class.

    Base standard item model for plugins

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::PluginsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_list_model.html#classmv_1_1PluginsListModel), [mv::PluginsTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_tree_model.html#classmv_1_1PluginsTreeModel)

    Public Types

    enum class PopulationMode
    :   Population.

        *Values:*

        enumerator Manual

        enumerator Automatic
        :   …done manually with `setPlugins()`

            …performed every time a plugin is added or removed

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Name

        enumerator Category
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1Item) name (plugin type, factory name or plugin name)

        enumerator Id
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1Item) category (type, factory or instance)

        enumerator Count
        :   Globally unique plugin instance identifier.

    Public Functions

    AbstractPluginsModel([PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationModeE "mv::AbstractPluginsModel::PopulationMode") populationMode = [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationModeE "mv::AbstractPluginsModel::PopulationMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationMode9AutomaticE "mv::AbstractPluginsModel::PopulationMode::Automatic"), QObject \*parent = nullptr)
    :   Construct plugin manager model with `parent`.

        Parameters:
        :   **parent** – Pointer to parent object

    [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationModeE "mv::AbstractPluginsModel::PopulationMode") getPopulationMode() const
    :   Get current population mode.

        Returns:
        :   Population mode

    void setPopulationMode([PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel14PopulationModeE "mv::AbstractPluginsModel::PopulationMode") populationMode)
    :   Set population mode to `populationMode`.

        Parameters:
        :   **populationMode** – Population mode

    virtual plugin::Plugins getPlugins() const = 0
    :   Get plugins.

        Returns:
        :   Vector of plugins

    virtual plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*getPlugin(const QModelIndex &modelIndex) const = 0
    :   Get plugin for `modelIndex`.

        Parameters:
        :   **modelIndex** – Index to retrieve

        Returns:
        :   Pointer to plugin (maybe nullptr)

    virtual void setPlugins(const plugin::Plugins &plugins) = 0
    :   Set the `plugins` from which can be picked (mode is set to StorageMode::Manual)

        Parameters:
        :   **plugins** – Vector of plugins

    Protected Functions

    virtual void populateFromPluginManager() = 0
    :   Synchronize the plugins with the core.

    virtual void addPlugin([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel9addPluginEPN6plugin6PluginE "mv::AbstractPluginsModel::addPlugin::plugin")::Plugin \*plugin) = 0
    :   Add `plugin` to the model.

        Parameters:
        :   **plugin** – Pointer to plugin

    virtual void removePlugin([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel12removePluginEPN6plugin6PluginE "mv::AbstractPluginsModel::removePlugin::plugin")::Plugin \*plugin) = 0
    :   Remove `plugin` from the model.

        Parameters:
        :   **plugin** – Pointer to plugin

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    class CategoryItem : public mv::[AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel4ItemE "mv::AbstractPluginsModel::Item")
    :   Standard model item class for displaying the item category.

        Public Functions

        Item([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel12CategoryItem4ItemEPN6plugin6PluginERK7QString "mv::AbstractPluginsModel::CategoryItem::Item::plugin")::Plugin \*plugin, const QString &title)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IdItem : public mv::[AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel4ItemE "mv::AbstractPluginsModel::Item"), public QObject
    :   Standard model item class for displaying the plugin Id.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel6IdItem4ItemEPN6plugin6PluginERK7QString "mv::AbstractPluginsModel::IdItem::Item::plugin")::Plugin \*plugin, const QString &title)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Item : public QStandardItem
    :   Base standard model item class for a dataset.

        Subclassed by [mv::AbstractPluginsModel::CategoryItem](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1CategoryItem), [mv::AbstractPluginsModel::IdItem](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1IdItem), [mv::AbstractPluginsModel::NameItem](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1NameItem)

        Public Functions

        Item([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel4Item4ItemEPN6plugin6PluginERK7QString "mv::AbstractPluginsModel::Item::Item::plugin")::Plugin \*plugin, const QString &title)
        :   Construct with pointer to the `plugin` and `title`.

            Parameters:
            :   - **plugin** – Pointer to plugin (maybe nullptr)
                - **title** – [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1Item) title

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*getPlugin() const
        :   Get plugin return Pointer to plugin (maybe nullptr)

    class NameItem : public mv::[AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModelE "mv::AbstractPluginsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel4ItemE "mv::AbstractPluginsModel::Item")
    :   Standard model item class for displaying the item name.

        Public Functions

        Item([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel8NameItem4ItemEPN6plugin6PluginERK7QString "mv::AbstractPluginsModel::NameItem::Item::plugin")::Plugin \*plugin, const QString &title)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining items in a row.

        Public Functions

        inline Row([plugin](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#_CPPv4N2mv20AbstractPluginsModel3Row3RowEPN6plugin6PluginERK7QStringRK7QStringRK7QStringRK5QIcon "mv::AbstractPluginsModel::Row::Row::plugin")::Plugin \*plugin, const QString &name, const QString &category, const QString &id, const QIcon &icon = QIcon())
        :   Construct with pointer to `plugin`, `name`, `category`, `id` and possibly `icon`.

            Parameters:
            :   - **plugin** – Pointer to plugin (maybe nullptr)
                - **name** – [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1Item) name
                - **category** – [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1Item) category
                - **id** – Globally unique plugin instance identifier
                - **icon** – [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel_1_1Item) icon
