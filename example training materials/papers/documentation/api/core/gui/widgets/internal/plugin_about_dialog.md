# PluginAboutDialog

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/plugin_about_dialog.html

**Documentation path:** `api/core/gui/widgets/internal/plugin_about_dialog.html`

---

# PluginAboutDialog

**Qualified name:** `mv::gui::PluginAboutDialog`

class PluginAboutDialog : public QDialog
:   Plugin about dialog class.

    Show plugin about Markdown text

    **Author**
    :   Thomas Kroes

    Public Functions

    PluginAboutDialog(const plugin::[PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadataE "mv::plugin::PluginMetadata") &pluginMetaData, QWidget \*parent = nullptr)
    :   Construct with pointer to source `plugin` and pointer to `parent` widget.

        Parameters:
        :   - **pluginMetaData** – Plugin meta data
            - **parent** – Pointer to parent widget (maybe nullptr)

    inline QSize sizeHint() const override
    :   Get preferred size.

    inline QSize minimumSizeHint() const override
    :   Get minimum size hint.

    class LinksExternalWebEnginePage : public QWebEnginePage
    :   Ensure links open an external browser.
