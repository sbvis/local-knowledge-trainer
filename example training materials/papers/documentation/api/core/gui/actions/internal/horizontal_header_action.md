# HorizontalHeaderAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/horizontal_header_action.html

**Documentation path:** `api/core/gui/actions/internal/horizontal_header_action.html`

---

# HorizontalHeaderAction

**Qualified name:** `mv::gui::HorizontalHeaderAction`

class HorizontalHeaderAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   Horizontal header action class.

    Action for configuring a horizontal header

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit Q\_INVOKABLE HorizontalHeaderAction(QObject \*parent, const QString &title, QHeaderView \*horizontalHeaderView = nullptr)
    :   Construct with pointer to `parent` object, action `title` and possibly pointer to an item `selectionModel`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **horizontalHeaderView** – Pointer to horizontal header view

    void initialize(QHeaderView \*horizontalHeaderView)
    :   Initializes with a pointer to the `horizontalHeaderView`.

        Parameters:
        :   **horizontalHeaderView** – Pointer to horizontal header view

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Respond to `target` object events.

        Parameters:
        :   - **target** – Object of which an event occurred
            - **event** – The event that took place
