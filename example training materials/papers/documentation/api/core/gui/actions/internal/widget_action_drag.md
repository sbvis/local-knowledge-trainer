# WidgetActionDrag

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_drag.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_drag.html`

---

# WidgetActionDrag

**Qualified name:** `mv::gui::WidgetActionDrag`

class WidgetActionDrag : public QObject
:   Widget action drag class.

    Implements dragging behaviour for [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#classmv_1_1gui_1_1WidgetAction) derived classes.

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetActionDrag([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*dragAction)
    :   Construct with pointer to `dragAction`.

        Parameters:
        :   **dragAction** – Pointer to drag action

    bool isDragging() const
    :   Get whether dragging is taking place.

        Returns:
        :   Boolean determining whether dragging is taking place

    void start()
    :   Start the dragging process.

    void isDraggingChanged(bool isDragging)
    :   Signals that the dragging state changed to `isDragging`.

        Parameters:
        :   **isDragging** – Boolean determining if the action is being dragged
