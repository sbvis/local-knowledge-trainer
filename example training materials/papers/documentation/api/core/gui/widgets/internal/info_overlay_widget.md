# InfoOverlayWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/info_overlay_widget.html

**Documentation path:** `api/core/gui/widgets/internal/info_overlay_widget.html`

---

# InfoOverlayWidget

**Qualified name:** `mv::gui::InfoOverlayWidget`

class InfoOverlayWidget : public mv::gui::[InfoWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/info_widget.html#_CPPv4N2mv3gui10InfoWidgetE "mv::gui::InfoWidget")
:   Info overlay widget class.

    Overlays the parent widget with an info widget (and synchronizes with its geometry) .

    **Author**
    :   Thomas Kroes

    Public Functions

    InfoOverlayWidget(QWidget \*parent)
    :   Construct with `parent`.

        Parameters:
        :   **parent** – Pointer to parent widget

    InfoOverlayWidget(QWidget \*parent, const QIcon &icon, const QString &title, const QString &description = "")
    :   Construct with \parent, `icon`, `title`, `description`, `backgroundColor` and `textColor`.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **icon** – Icon
            - **title** – Title of the overlay
            - **description** – Overlay description

    util::[WidgetFader](https://manivault.readthedocs.io/en/latest/api/core/util/widget/widget_fader.html#_CPPv4N2mv4util11WidgetFaderE "mv::util::WidgetFader") &getWidgetFader()
    :   Get widget fader.

        Returns:
        :   Reference to widget fader
