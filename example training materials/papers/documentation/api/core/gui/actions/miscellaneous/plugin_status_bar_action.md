# PluginStatusBarAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_status_bar_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/plugin_status_bar_action.html`

---

# PluginStatusBarAction

**Qualified name:** `mv::gui::PluginStatusBarAction`

`PluginStatusBarAction` associates one factory-owned status-bar item with a loaded plugin kind and can condition its visibility on that factory having active instances.

Begin with [Status-bar integration](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/index.html) for the registration pattern, multi-instance semantics, and current runtime limitations.

class PluginStatusBarAction : public mv::gui::[StatusBarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html#_CPPv4N2mv3gui15StatusBarActionE "mv::gui::StatusBarAction")
:   Plugin status bar action class.

    Extends the status bar action class with plugin specific features

    **Author**
    :   Thomas Kroes

    Public Functions

    PluginStatusBarAction(QObject \*parent, const QString &title, const QString &pluginKind = "")
    :   Construct with `parent` object, `title` and possibly a FontAwesome `icon`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **pluginKind** – Plugin kind to use (icon will be retrieved from the plugin factory when the plugin kind is valid)
