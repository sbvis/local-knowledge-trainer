# ActionOverlayWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/action_overlay_widget.html

**Documentation path:** `api/core/gui/widgets/internal/action_overlay_widget.html`

---

# ActionOverlayWidget

**Qualified name:** `mv::gui::ActionOverlayWidget`

class ActionOverlayWidget : public mv::gui::[OverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/overlay_widget.html#_CPPv4N2mv3gui13OverlayWidgetE "mv::gui::OverlayWidget")
:   Action overlay widget class.

    Overlays the target widget with the action widget in a chosen location (alignment).

    Note: This action is developed for internal use only and is in a WIP state

    **Author**
    :   Thomas Kroes

    Public Functions

    ActionOverlayWidget(QWidget \*target, const QPointer<[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> &action, const Qt::Alignment &alignment = Qt::AlignTop | Qt::AlignLeft)
    :   Construct with pointer to `target` widget and initial opacity.

        Parameters:
        :   - **target** – Pointer to target widget (used to synchronize the geometry with, may not be nullptr)
            - **action** – Pointer to action (may not be nullptr)
            - **alignment** – Alignment of the overlay action in the target widget

    void setTargetWidget(QWidget \*targetWidget)
    :   Set target widget for overlay action to `targetWidget`.

        Parameters:
        :   **targetWidget** – Pointer to target widget (may not be nullptr)
