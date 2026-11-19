# VerticalToolbarAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_toolbar_action.html

**Documentation path:** `api/core/gui/actions/grouping/vertical_toolbar_action.html`

---

# VerticalToolbarAction

**Qualified name:** `mv::gui::VerticalToolbarAction`

class VerticalToolbarAction : public mv::gui::[ToolbarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/toolbar_action.html#_CPPv4N2mv3gui13ToolbarActionE "mv::gui::ToolbarAction")
:   Vertical toolbar action class.

    [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_toolbar_action.html#classmv_1_1gui_1_1VerticalToolbarAction_1_1Widget) action for displaying actions in a vertical toolbar

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE VerticalToolbarAction(QObject \*parent, const QString &title, const Qt::AlignmentFlag &alignment = Qt::AlignmentFlag::AlignTop)
    :   Construct with `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **alignment** – Item alignment

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the vertical toolbar action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_toolbar_action.html#classmv_1_1gui_1_1VerticalToolbarAction_1_1Widget) flags for the configuration of the widget (type)

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_toolbar_action.html#classmv_1_1gui_1_1VerticalToolbarAction_1_1Widget) class for the horizontal toolbar.

        Protected Functions

        Widget(QWidget \*parent, [VerticalToolbarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_toolbar_action.html#_CPPv4N2mv3gui21VerticalToolbarActionE "mv::gui::VerticalToolbarAction") \*verticalToolbarAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **verticalToolbarAction** – Pointer to vertical toolbar action that creates the widget
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_toolbar_action.html#classmv_1_1gui_1_1VerticalToolbarAction_1_1Widget) flags for the configuration of the widget (type)

        Protected Attributes

        QVBoxLayout \*\_layout
        :   Pointer to vertical toolbar action that creates the widget.

        QVBoxLayout \*\_toolbarLayout
        :   Main layout.

        QWidget \_toolbarWidget
        :   Toolbar layout.

        Friends

        *friend class* VerticalToolbarAction
