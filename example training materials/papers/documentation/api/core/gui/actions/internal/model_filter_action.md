# ModelFilterAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/model_filter_action.html

**Documentation path:** `api/core/gui/actions/internal/model_filter_action.html`

---

# ModelFilterAction

**Qualified name:** `mv::gui::ModelFilterAction`

class ModelFilterAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   Model filter action class.

    Action class for configuring filtering parameters

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE ModelFilterAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and action `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void initialize(QAbstractItemModel \*model, QSortFilterProxyModel \*filterModel, const QString &itemTypeName)
    :   Initializes the table action with a pointer to a `model`, possibly a `filterModel` and `itemTypeName`.

        Parameters:
        :   - **model** – Pointer to model
            - **filterModel** – Pointer to filter model (maybe nullptr)
            - **itemTypeName** – Item type name string
