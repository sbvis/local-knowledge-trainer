# AbstractHeadsUpDisplayModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html

**Documentation path:** `api/core/models/hud/abstract_heads_up_display_model.html`

---

# AbstractHeadsUpDisplayModel

**Qualified name:** `mv::AbstractHeadsUpDisplayModel`

class AbstractHeadsUpDisplayModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Heads-up display model class.

    Contains information that is displayed in the heads-up display

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::HeadsUpDisplayTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/heads_up_display_tree_model.html#classmv_1_1HeadsUpDisplayTreeModel)

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Title

        enumerator Value
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1Item) title.

        enumerator Description
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1Item) value.

        enumerator Id
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1Item) description.

        enumerator Count
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1Item) global unique identifier.

    Public Functions

    AbstractHeadsUpDisplayModel(QObject \*parent = nullptr)
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

    void addHeadsUpDisplayItem(util::HeadsUpDisplayItemSharedPtr headsUpDisplayItem)
    :   Add `headsUpDisplayItem` to the model.

        Parameters:
        :   **headsUpDisplayItem** – Heads-up display item to add

    void removeHeadsUpDisplayItem(const util::HeadsUpDisplayItemSharedPtr &headsUpDisplayItem)
    :   Remove `headsUpDisplayItem`.

        Parameters:
        :   **headsUpDisplayItem** – Heads-up display item to remove

    class DescriptionItem : public mv::[AbstractHeadsUpDisplayModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#_CPPv4N2mv27AbstractHeadsUpDisplayModelE "mv::AbstractHeadsUpDisplayModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#_CPPv4N2mv27AbstractHeadsUpDisplayModel4ItemE "mv::AbstractHeadsUpDisplayModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1Item) class for displaying the description.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::HeadsUpDisplayItemSharedPtr &headsUpDisplayItem)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IdItem : public mv::[AbstractHeadsUpDisplayModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#_CPPv4N2mv27AbstractHeadsUpDisplayModelE "mv::AbstractHeadsUpDisplayModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#_CPPv4N2mv27AbstractHeadsUpDisplayModel4ItemE "mv::AbstractHeadsUpDisplayModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1Item) class for displaying the item ID.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::HeadsUpDisplayItemSharedPtr &headsUpDisplayItem)
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
    :   Base standard model item class for heads-up display item

        Subclassed by [mv::AbstractHeadsUpDisplayModel::DescriptionItem](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1DescriptionItem), [mv::AbstractHeadsUpDisplayModel::IdItem](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1IdItem), [mv::AbstractHeadsUpDisplayModel::TitleItem](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1TitleItem), [mv::AbstractHeadsUpDisplayModel::ValueItem](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1ValueItem)

        Public Functions

        Item(const util::HeadsUpDisplayItemSharedPtr &headsUpDisplayItem)
        :   Construct with shared pointer to `headsUpDisplayItem`.

            Parameters:
            :   **headsUpDisplayItem** – Shared pointer to heads-up display item

        util::HeadsUpDisplayItemSharedPtr getHeadsupDisplayItem() const
        :   Get heads-up display item return Shared pointer to heads-up display item.

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining items in a row.

        Public Functions

        inline Row(const util::HeadsUpDisplayItemSharedPtr &headsUpDisplayItem)
        :   Construct with shared pointer to `headsUpDisplayItem`.

            Parameters:
            :   **headsUpDisplayItem** – Shared pointer to heads-up display item

    class TitleItem : public mv::[AbstractHeadsUpDisplayModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#_CPPv4N2mv27AbstractHeadsUpDisplayModelE "mv::AbstractHeadsUpDisplayModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#_CPPv4N2mv27AbstractHeadsUpDisplayModel4ItemE "mv::AbstractHeadsUpDisplayModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1Item) class for displaying the title.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::HeadsUpDisplayItemSharedPtr &headsUpDisplayItem)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class ValueItem : public mv::[AbstractHeadsUpDisplayModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#_CPPv4N2mv27AbstractHeadsUpDisplayModelE "mv::AbstractHeadsUpDisplayModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#_CPPv4N2mv27AbstractHeadsUpDisplayModel4ItemE "mv::AbstractHeadsUpDisplayModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel_1_1Item) class for displaying the value.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::HeadsUpDisplayItemSharedPtr &headsUpDisplayItem)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
