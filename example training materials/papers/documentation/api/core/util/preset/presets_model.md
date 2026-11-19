# PresetsModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/preset/presets_model.html

**Documentation path:** `api/core/util/preset/presets_model.html`

---

# PresetsModel

**Qualified name:** `mv::util::PresetsModel`

class PresetsModel : public QAbstractListModel
:   Presets model class.

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Column
    :   Presets model columns.

        *Values:*

        enumerator Name

        enumerator Description
        :   Name column.

            Description column

    Public Functions

    PresetsModel(QObject \*parent = nullptr)
    :   Constructor.

        Parameters:
        :   **parent** – Pointer to parent object

    int columnCount(const QModelIndex &parent) const override
    :   Returns the the number of model columns.

        Parameters:
        :   **parent** – Parent index

    int rowCount(const QModelIndex &parent) const override
    :   Returns the number of color maps in the model.

        Parameters:
        :   **parent** – Parent index

    QVariant data(const QModelIndex &index, int role) const override
    :   Returns model data for the given index.

        Parameters:
        :   - **index** – Index
            - **role** – The data role

    void setWidgetAction(mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*widgetAction)
    :   Set widget action.

        Parameters:
        :   **widgetAction** – Pointer to widget action to retrieve the presets for
