# AbstractScriptsModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html

**Documentation path:** `api/core/models/scripts/abstract_scripts_model.html`

---

# AbstractScriptsModel

**Qualified name:** `mv::AbstractScriptsModel`

class AbstractScriptsModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Scripts model class.

    Base standard item model for scripts

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::ScriptsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/scripts_list_model.html#classmv_1_1ScriptsListModel), [mv::ScriptsTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/scripts_tree_model.html#classmv_1_1ScriptsTreeModel)

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Type

        enumerator Language
        :   Script type item.

        enumerator Location
        :   Script language item.

        enumerator Count
        :   Script location item.

    Public Functions

    AbstractScriptsModel(QObject \*parent = nullptr)
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
    :   Base standard model item class for script item

        Subclassed by [mv::AbstractScriptsModel::LanguageItem](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#classmv_1_1AbstractScriptsModel_1_1LanguageItem), [mv::AbstractScriptsModel::LocationItem](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#classmv_1_1AbstractScriptsModel_1_1LocationItem), [mv::AbstractScriptsModel::TypeItem](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#classmv_1_1AbstractScriptsModel_1_1TypeItem)

        Public Functions

        Item(const QString &type, util::[Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6ScriptE "mv::util::Script") \*script)
        :   Construct with `type` and pointer to `script`.

            Parameters:
            :   - **type** – View type
                - **script** – Pointer to script

        util::[Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6ScriptE "mv::util::Script") \*getScript() const
        :   Get script return Pointer to script.

    class LanguageItem : public mv::[AbstractScriptsModel](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#_CPPv4N2mv20AbstractScriptsModelE "mv::AbstractScriptsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#_CPPv4N2mv20AbstractScriptsModel4ItemE "mv::AbstractScriptsModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#classmv_1_1AbstractScriptsModel_1_1Item) class for displaying the script language.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const QString &type, util::[Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6ScriptE "mv::util::Script") \*script)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class LocationItem : public mv::[AbstractScriptsModel](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#_CPPv4N2mv20AbstractScriptsModelE "mv::AbstractScriptsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#_CPPv4N2mv20AbstractScriptsModel4ItemE "mv::AbstractScriptsModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#classmv_1_1AbstractScriptsModel_1_1Item) class for displaying the script location.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const QString &type, util::[Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6ScriptE "mv::util::Script") \*script)
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

        inline Row(const QString &type, util::[Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6ScriptE "mv::util::Script") \*script)
        :   Construct with `type` and pointer to `script`.

            Parameters:
            :   - **type** – View type
                - **script** – Pointer to the script

    class TypeItem : public mv::[AbstractScriptsModel](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#_CPPv4N2mv20AbstractScriptsModelE "mv::AbstractScriptsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#_CPPv4N2mv20AbstractScriptsModel4ItemE "mv::AbstractScriptsModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#classmv_1_1AbstractScriptsModel_1_1Item) class for displaying the script type.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const QString &type, util::[Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6ScriptE "mv::util::Script") \*script)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
