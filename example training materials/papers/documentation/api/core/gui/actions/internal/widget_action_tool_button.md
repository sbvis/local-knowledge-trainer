# WidgetActionToolButton

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_tool_button.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_tool_button.html`

---

# WidgetActionToolButton

**Qualified name:** `mv::gui::WidgetActionToolButton`

class WidgetActionToolButton : public QToolButton
:   Widget action tool button.

    Specialized tool button which show an action widget as a popup

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetActionToolButton(QWidget \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Create with pointer to `parent` widget and owning `action`.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **action** – Pointer to owning action

    WidgetActionToolButton(QWidget \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, WidgetConfigurationFunction widgetConfigurationFunction)
    :   Construct with pointer to \parent widget, pointer to owning `action` and `widgetConfigurationFunction`.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **action** – Pointer to owning action
            - **widgetConfigurationFunction** – This function is called right after the popup action widget is created

    void paintEvent(QPaintEvent \*paintEvent) override
    :   Override paint event for custom painting.

        Parameters:
        :   **paintEvent** – Pointer to paint event

    [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction() const
    :   Get action.

        Returns:
        :   Pointer to action (maybe nullptr)

    void setAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Set the action to `action` (ownership is not transferred)

        Parameters:
        :   **action** – Pointer to action

    WidgetConfigurationFunction getWidgetConfigurationFunction()
    :   Get widget configuration function.

        Returns:
        :   Function that is called right after a widget action widget is created

    inline bool getShowIndicator() const
    :   Get show indicator.

        Returns:
        :   Boolean determining whether to show the indicator or not

    inline void setShowIndicator(bool showIndicator)
    :   Set show indicator to `showIndicator`.

        Parameters:
        :   **showIndicator** – Boolean determining whether to show the indicator or not

    inline Qt::Alignment getIndicatorAlignment() const
    :   Get alignment of the indicator.

        Returns:
        :   Alignment of the indicator

    inline void setIndicatorAlignment(Qt::Alignment indicatorAlignment)
    :   Set alignment of the indicator to `indicatorAlignment`.

        Parameters:
        :   **indicatorAlignment** – Alignment of the indicator

    void actionChanged([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*previousAction, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*currentAction)
    :   Signals that the current action changed from `previousAction` to `currentAction`.

        Parameters:
        :   - **previousAction** – Pointer to previous action (maybe nullptr)
            - **currentAction** – Pointer to current action (maybe nullptr)
