# WidgetActionBadgeOverlayWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_badge_overlay_widget.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_badge_overlay_widget.html`

---

# WidgetActionBadgeOverlayWidget

**Qualified name:** `mv::gui::WidgetActionBadgeOverlayWidget`

class WidgetActionBadgeOverlayWidget : public mv::gui::[OverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/overlay_widget.html#_CPPv4N2mv3gui13OverlayWidgetE "mv::gui::OverlayWidget")
:   Widget action badge overlay widget class.

    Overlay widget class for showing a badge over an action widget

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetActionBadgeOverlayWidget(QWidget \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Construct with parent widget.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **action** – Pointer to widget action to highlight

    void paintEvent(QPaintEvent \*paintEvent)
    :   Paint event.

        Parameters:
        :   **paintEvent** – Pointer to paint event
