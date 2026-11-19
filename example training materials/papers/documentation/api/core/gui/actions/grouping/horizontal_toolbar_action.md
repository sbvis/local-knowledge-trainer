# HorizontalToolbarAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html

**Documentation path:** `api/core/gui/actions/grouping/horizontal_toolbar_action.html`

---

# HorizontalToolbarAction

**Qualified name:** `mv::gui::HorizontalToolbarAction`

class HorizontalToolbarAction : public mv::gui::[ToolbarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/toolbar_action.html#_CPPv4N2mv3gui13ToolbarActionE "mv::gui::ToolbarAction")
:   Horizontal toolbar action class.

    [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html#classmv_1_1gui_1_1HorizontalToolbarAction_1_1Widget) action for displaying actions in a horizontal toolbar

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::NavigationAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/navigation_action.html#classmv_1_1gui_1_1NavigationAction)

    Public Functions

    Q\_INVOKABLE HorizontalToolbarAction(QObject \*parent, const QString &title, const Qt::AlignmentFlag &alignment = Qt::AlignmentFlag::AlignLeft)
    :   Construct with `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **alignment** – Item alignment (Qt::AlignmentFlag::AlignLeft, Qt::AlignmentFlag::AlignCenter or Qt::AlignmentFlag::AlignRight)

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the horizontal toolbar action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html#classmv_1_1gui_1_1HorizontalToolbarAction_1_1Widget) flags for the configuration of the widget (type)

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html#classmv_1_1gui_1_1HorizontalToolbarAction_1_1Widget) class for the horizontal toolbar.

        Protected Functions

        Widget(QWidget \*parent, [HorizontalToolbarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html#_CPPv4N2mv3gui23HorizontalToolbarActionE "mv::gui::HorizontalToolbarAction") \*horizontalToolbarAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **horizontalToolbarAction** – Pointer to horizontal toolbar action that creates the widget
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html#classmv_1_1gui_1_1HorizontalToolbarAction_1_1Widget) flags for the configuration of the widget (type)

        bool eventFilter(QObject \*target, QEvent \*event) override
        :   Respond to `target` object events.

            Parameters:
            :   - **target** – Object of which an event occurred
                - **event** – The event that took place

        Protected Attributes

        QHBoxLayout \*\_layout
        :   Pointer to horizontal toolbar action that creates the widget.

        QHBoxLayout \*\_toolbarLayout
        :   Main layout.

        QWidget \_toolbarWidget
        :   Toolbar layout.

        QTimer \_timer
        :   Toolbar widget.

        Friends

        *friend class* HorizontalToolbarAction
