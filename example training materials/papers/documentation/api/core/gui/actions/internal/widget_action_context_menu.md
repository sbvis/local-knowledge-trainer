# WidgetActionContextMenu

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_context_menu.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_context_menu.html`

---

# WidgetActionContextMenu

**Qualified name:** `mv::gui::WidgetActionContextMenu`

class WidgetActionContextMenu : public QMenu
:   Widget action context menu class.

    Context menu for one (or more) widget actions

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit WidgetActionContextMenu(QWidget \*parent, WidgetActions actions)
    :   Construct with `parent` widget and `widgetActions`.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **actions** – Actions to create the context menu for

    class ConfirmRemovePublicActionDialog : public QDialog
    :   Dialog class for asking permission prior to removing a public action.

        Public Functions

        ConfirmRemovePublicActionDialog(QWidget \*parent, WidgetActions publicActions)
        :   Construct with `parent` widget and edit `publicAction`.

            Parameters:
            :   - **parent** – Pointer to parent widget (if any)
                - **publicAction** – Reference to public action

    class EditActionsDialog : public QDialog
    :   Dialog class for editing one ore more actions.

        Public Functions

        EditActionsDialog(QWidget \*parent, WidgetActions actions)
        :   Construct with `parent` widget and edit widget `actions`.

            Parameters:
            :   - **parent** – Pointer to parent widget (if any)
                - **action** – Widget actions to edit

        void closeEvent(QCloseEvent \*event)
        :   Invoked when the dialog is closed.

            Parameters:
            :   **event** – Pointer to the close event
