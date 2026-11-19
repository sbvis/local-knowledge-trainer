# OverlayWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/overlay_widget.html

**Documentation path:** `api/core/gui/widgets/internal/overlay_widget.html`

---

# OverlayWidget

**Qualified name:** `mv::gui::OverlayWidget`

class OverlayWidget : public QWidget
:   Overlay widget class.

    Overlays the target widget with an overlay widget and keeps its geometry in sync with the target widget.

    By default, the overlay widget and its children are immune to mouse events (similar to the Qt widget attribute Qt::WA\_TransparentForMouseEvents). To enable/disable child widget mouse events, call OverlayWidget::addMouseEventReceiverWidget(…) or OverlayWidget::removeMouseEventReceiverWidget(…) respectively.

    For more information, refer to the [mv::util::WidgetOverlayer](https://manivault.readthedocs.io/en/latest/api/core/util/widget/widget_overlayer.html#classmv_1_1util_1_1WidgetOverlayer) class.

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::Navigator2D::ZoomOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#classmv_1_1Navigator2D_1_1ZoomOverlayWidget), [mv::gui::ActionOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/action_overlay_widget.html#classmv_1_1gui_1_1ActionOverlayWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget), [mv::gui::ViewPluginOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_overlay_widget.html#classmv_1_1gui_1_1ViewPluginOverlayWidget), [mv::gui::WidgetActionBadgeOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_badge_overlay_widget.html#classmv_1_1gui_1_1WidgetActionBadgeOverlayWidget), [mv::gui::WidgetActionHighlightWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_highlight_widget.html#classmv_1_1gui_1_1WidgetActionHighlightWidget)

    Public Functions

    OverlayWidget(QWidget \*target, float initialOpacity = 1.0f)
    :   Construct with pointer to `target` widget and initial opacity.

        Parameters:
        :   - **target** – Pointer to target widget (used to synchronize the geometry with)
            - **initialOpacity** – Opacity at initialization

    mv::util::[WidgetOverlayer](https://manivault.readthedocs.io/en/latest/api/core/util/widget/widget_overlayer.html#_CPPv4N2mv4util15WidgetOverlayerE "mv::util::WidgetOverlayer") &getWidgetOverlayer()
    :   Get the utility class for overlaying the widget.

        Returns:
        :   Widget overlayer

    virtual void addMouseEventReceiverWidget(QWidget \*mouseEventReceiverWidget) final
    :   Add `mouseEventReceiverWidget`.

        Parameters:
        :   **mouseEventReceiverWidget** – Pointer to mouse event receiver widget that should be added

    virtual void removeMouseEventReceiverWidget(QWidget \*mouseEventReceiverWidget) final
    :   Remove `mouseEventReceiverWidget`.

        Parameters:
        :   **mouseEventReceiverWidget** – Pointer to mouse event receiver widget that should be removed

    void updateMask()
    :   Update widget mask to selectively process mouse events.

    Protected Functions

    void resizeEvent(QResizeEvent \*event) override
    :   Update the mask region when the overlay widget changes size.

        Parameters:
        :   **event** – Pointer to resize event that occurred
