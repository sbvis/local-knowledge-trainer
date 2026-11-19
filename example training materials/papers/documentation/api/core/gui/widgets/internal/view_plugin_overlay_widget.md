# ViewPluginOverlayWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_overlay_widget.html

**Documentation path:** `api/core/gui/widgets/internal/view_plugin_overlay_widget.html`

---

# ViewPluginOverlayWidget

**Qualified name:** `mv::gui::ViewPluginOverlayWidget`

class ViewPluginOverlayWidget : public mv::gui::[OverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/overlay_widget.html#_CPPv4N2mv3gui13OverlayWidgetE "mv::gui::OverlayWidget")
:   View plugin widget class.

    Overlays the view plugin widget with an overlay widget

    **Author**
    :   Thomas Kroes

    Public Functions

    ViewPluginOverlayWidget(plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin)
    :   Construct with pointer to source `view` plugin.

        Parameters:
        :   **viewPlugin** – Pointer to source view plugin

    QVBoxLayout &getMainLayout()
    :   Get main layout.

        Returns:
        :   Reference to main layout
