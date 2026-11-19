# WidgetActionCollapsedWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_collapsed_widget.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_collapsed_widget.html`

---

# WidgetActionCollapsedWidget

**Qualified name:** `mv::gui::WidgetActionCollapsedWidget`

class WidgetActionCollapsedWidget : public mv::gui::[WidgetActionViewWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_view_widget.html#_CPPv4N2mv3gui22WidgetActionViewWidgetE "mv::gui::WidgetActionViewWidget")
:   Widget action collapsed widget class.

    Displays a tool button that shows the widget in a popup

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetActionCollapsedWidget(QWidget \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Construct with pointer to \parent widget and pointer to owning `action`.

        Parameters:
        :   - **parent** – Parent widget
            - **action** – Pointer to the widget action that will be displayed in a popup

    WidgetActionCollapsedWidget(QWidget \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, WidgetConfigurationFunction widgetConfigurationFunction)
    :   Construct with pointer to \parent widget, pointer to owning `action` and `widgetConfigurationFunction`.

        Parameters:
        :   - **parent** – Parent widget
            - **action** – Pointer to the widget action that will be displayed in a popup
            - **widgetConfigurationFunction** – This function is called right after the popup action widget is created

    virtual void setAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) override
    :   Set the action to `action`.

        Parameters:
        :   **widgetAction** – Pointer to action

    inline [WidgetActionToolButton](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_tool_button.html#_CPPv4N2mv3gui22WidgetActionToolButtonE "mv::gui::WidgetActionToolButton") &getToolButton()
    :   Get tool button.

        Returns:
        :   Get reference to the tool button
