# HeadsUpDisplayItem

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/heads_up_display_item/heads_up_display_item.html

**Documentation path:** `api/core/util/heads_up_display_item/heads_up_display_item.html`

---

# HeadsUpDisplayItem

**Qualified name:** `mv::util::HeadsUpDisplayItem`

class HeadsUpDisplayItem : public QObject
:   Heads-up display item class.

    Used in the heads-up display model classes.

    **Author**
    :   Thomas Kroes

    Public Functions

    HeadsUpDisplayItem(const QString &title, const QString &value, const QString &description, const HeadsUpDisplayItemSharedPtr &parent = nullptr)
    :   Construct with `title`, `value`, `description` and `parent`.

        Parameters:
        :   - **title** – Title
            - **value** – Value
            - **description** – Description
            - **parent** – Shared pointer to parent item (default: nullptr)

    Protected Functions

    void setIndex(const QPersistentModelIndex &index)
    :   Set persistent model `index` of the item.

        Parameters:
        :   **index** – Persistent model index of the item

    Friends

    *friend class* mv::AbstractHeadsUpDisplayModel
