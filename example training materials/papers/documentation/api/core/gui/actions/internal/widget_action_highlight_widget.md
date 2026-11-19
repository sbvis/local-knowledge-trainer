# WidgetActionHighlightWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_highlight_widget.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_highlight_widget.html`

---

# WidgetActionHighlightWidget

**Qualified name:** `mv::gui::WidgetActionHighlightWidget`

class WidgetActionHighlightWidget : public mv::gui::[OverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/overlay_widget.html#_CPPv4N2mv3gui13OverlayWidgetE "mv::gui::OverlayWidget")
:   Widget action highlight class.

    Overlay widget class for highlighting a widget action

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetActionHighlightWidget(QWidget \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Construct with parent widget.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **action** – Pointer to widget action to highlight

    [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction()
    :   Get the highlight action.

        Returns:
        :   Pointer to highlight action

    void setAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Set the highlight action.

        Parameters:
        :   **action** – Pointer to highlight action
