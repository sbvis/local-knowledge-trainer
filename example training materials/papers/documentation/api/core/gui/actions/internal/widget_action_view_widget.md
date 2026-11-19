# WidgetActionViewWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_view_widget.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_view_widget.html`

---

# WidgetActionViewWidget

**Qualified name:** `mv::gui::WidgetActionViewWidget`

class WidgetActionViewWidget : public QWidget
:   Widget action view widget class.

    Base class for widgets that provide a view on an action.

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::WidgetActionCollapsedWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_collapsed_widget.html#classmv_1_1gui_1_1WidgetActionCollapsedWidget), [mv::gui::WidgetActionLabel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_label.html#classmv_1_1gui_1_1WidgetActionLabel), [mv::gui::WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#classmv_1_1gui_1_1WidgetActionWidget)

    Public Types

    enum WidgetFlag
    :   Reserved widget view flags.

        *Values:*

        enumerator PopupLayout

    Public Functions

    WidgetActionViewWidget(QWidget \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, std::int32\_t widgetFlags = 0)
    :   Constructor.

        Parameters:
        :   - **parent** – Parent widget
            - **action** – Pointer to the action that will be displayed
            - **widgetFlags** – Widget flags for the configuration of the widget

    [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction() const
    :   Get the source action.

        Returns:
        :   Pointer to source action

    virtual void setAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*widgetAction)
    :   Set the source action.

        Parameters:
        :   **widgetAction** – Pointer to source action

    std::int32\_t getWidgetFlags() const
    :   Get widget flags.

        Returns:
        :   Widget flags

    bool isPopup() const
    :   Get whether the widget is in a popup state.

        Returns:
        :   Boolean determining whether the widget is in a popup state

    void mousePressEvent(QMouseEvent \*event) override
    :   Override the mouse press event to avoid click-and-close behaviour for popups.

        Parameters:
        :   **event** – Pointer to mouse event

    Protected Functions

    void dragEnterEvent(QDragEnterEvent \*dragEnterEvent) override
    :   Invoked when a `dragEnterEvent` occurs.

        Parameters:
        :   **dragEnterEvent** – Pointer to drag enter event

    void dragLeaveEvent(QDragLeaveEvent \*dragLeaveEvent) override
    :   Invoked when a `dragLeaveEvent` occurs.

        Parameters:
        :   **dragLeaveEvent** – Pointer to drag leave event

    void dropEvent(QDropEvent \*dropEvent) override
    :   Invoked when a `dropEvent` occurs.

        Parameters:
        :   **dropEvent** – Pointer to drop event
