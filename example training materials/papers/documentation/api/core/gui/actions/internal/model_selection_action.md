# ModelSelectionAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/model_selection_action.html

**Documentation path:** `api/core/gui/actions/internal/model_selection_action.html`

---

# ModelSelectionAction

**Qualified name:** `mv::gui::ModelSelectionAction`

class ModelSelectionAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   Model selection action class.

    Action for selecting items in a model

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit Q\_INVOKABLE ModelSelectionAction(QObject \*parent, const QString &title, QItemSelectionModel \*selectionModel = nullptr)
    :   Construct with pointer to `parent` object, action `title` and possibly pointer to an item `selectionModel`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **selectionModel** – Pointer to item selection model

    void initialize(QItemSelectionModel \*selectionModel)
    :   Initializes with a pointer to the `selectionModel`.

        Parameters:
        :   **selectionModel** – Pointer to item selection model
