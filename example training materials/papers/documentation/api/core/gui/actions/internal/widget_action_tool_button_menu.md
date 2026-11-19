# WidgetActionToolButtonMenu

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_tool_button_menu.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_tool_button_menu.html`

---

# WidgetActionToolButtonMenu

**Qualified name:** `mv::gui::WidgetActionToolButtonMenu`

class WidgetActionToolButtonMenu : public QMenu
:   Widget action tool button menu.

    Specialized tool button menu class which show an action widget as a popup

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetActionToolButtonMenu([WidgetActionToolButton](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_tool_button.html#_CPPv4N2mv3gui22WidgetActionToolButtonE "mv::gui::WidgetActionToolButton") &widgetActionToolButton)
    :   Create with reference to owning `widgetActionToolButton`.

        Parameters:
        :   **widgetActionToolButton** – Reference to owning widget action tool button

    WidgetConfigurationFunction getWidgetConfigurationFunction()
    :   Get widget configuration function.

        Returns:
        :   Function that is called right after a widget action widget is created

    inline DeferredLoadWidgetAction &getDeferredLoadWidgetAction()
    :   Get deferred load widget action.

        Returns:
        :   Reference to deferred load widget action

    bool getIgnoreCloseEvent() const
    :   Get ignore close event.

        Returns:
        :   Boolean determining whether to ignore the close event

    void setIgnoreCloseEvent(bool ignoreCloseEvent)
    :   Set ignore close event to `ignoreCloseEvent`.

        Parameters:
        :   **ignoreCloseEvent** – Boolean determining whether to ignore the close event

    void closeEvent(QCloseEvent \*event) override
    :   Invoked when the menu is required to be closed.

        Parameters:
        :   **event** – Pointer to close event
