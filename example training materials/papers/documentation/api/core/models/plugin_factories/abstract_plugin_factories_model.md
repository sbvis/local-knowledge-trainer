# AbstractPluginFactoriesModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html

**Documentation path:** `api/core/models/plugin_factories/abstract_plugin_factories_model.html`

---

# AbstractPluginFactoriesModel

**Qualified name:** `mv::AbstractPluginFactoriesModel`

class AbstractPluginFactoriesModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Plugin factories model class.

    Base standard item model for plugin factories

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::PluginFactoriesListModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/plugin_factories_list_model.html#classmv_1_1PluginFactoriesListModel), [mv::PluginFactoriesTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/plugin_factories_tree_model.html#classmv_1_1PluginFactoriesTreeModel)

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Name

        enumerator Version
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#classmv_1_1AbstractPluginFactoriesModel_1_1Item) name.

        enumerator NumberOfInstances
        :   Plugin version.

        enumerator Count
        :   Number of current instances.

    Public Functions

    AbstractPluginFactoriesModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    class Item : public QStandardItem
    :   Base standard model item class for plugin factory item.

        Subclassed by [mv::AbstractPluginFactoriesModel::NameItem](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#classmv_1_1AbstractPluginFactoriesModel_1_1NameItem), [mv::AbstractPluginFactoriesModel::NumberOfInstancesItem](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#classmv_1_1AbstractPluginFactoriesModel_1_1NumberOfInstancesItem), [mv::AbstractPluginFactoriesModel::VersionItem](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#classmv_1_1AbstractPluginFactoriesModel_1_1VersionItem)

        Public Functions

        Item(const QString &type, plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory)
        :   Construct with `type` and pointer to `pluginFactory`.

            Parameters:
            :   - **type** – View type
                - **pluginFactory** – Pointer to plugin factory

        QString getType() const
        :   Get type return Plugin type string.

        plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*getPluginFactory() const
        :   Get plugin factory return Pointer to plugin factory.

    class NameItem : public mv::[AbstractPluginFactoriesModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#_CPPv4N2mv28AbstractPluginFactoriesModelE "mv::AbstractPluginFactoriesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#_CPPv4N2mv28AbstractPluginFactoriesModel4ItemE "mv::AbstractPluginFactoriesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#classmv_1_1AbstractPluginFactoriesModel_1_1Item) class for displaying the plugin factory kind.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const QString &type, plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class NumberOfInstancesItem : public mv::[AbstractPluginFactoriesModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#_CPPv4N2mv28AbstractPluginFactoriesModelE "mv::AbstractPluginFactoriesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#_CPPv4N2mv28AbstractPluginFactoriesModel4ItemE "mv::AbstractPluginFactoriesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#classmv_1_1AbstractPluginFactoriesModel_1_1Item) class for displaying the number of current plugin instances.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const QString &type, plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory)
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

        inline Row(const QString &type, plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory)
        :   Construct with `type` and pointer to `pluginFactory`.

            Parameters:
            :   - **type** – View type
                - **pluginFactory** – Pointer to plugin factory

        inline Row(const QString &type)
        :   Construct with `type`.

            Parameters:
            :   **type** – View type

        inline Row(plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory)
        :   Construct with pointer to `pluginFactory`.

            Parameters:
            :   **pluginFactory** – Pointer to plugin factory

    class VersionItem : public mv::[AbstractPluginFactoriesModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#_CPPv4N2mv28AbstractPluginFactoriesModelE "mv::AbstractPluginFactoriesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#_CPPv4N2mv28AbstractPluginFactoriesModel4ItemE "mv::AbstractPluginFactoriesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#classmv_1_1AbstractPluginFactoriesModel_1_1Item) class for displaying the plugin factory version.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const QString &type, plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
