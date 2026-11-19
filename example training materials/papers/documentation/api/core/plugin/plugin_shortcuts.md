# PluginShortcuts

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_shortcuts.html

**Documentation path:** `api/core/plugin/plugin_shortcuts.html`

---

# PluginShortcuts

This class is for documenting plugin shortcuts (used to display a shortcut map in the UI).

Note

This is merely for *documenting* shortcuts, it assumes the plugin developer has already established the shortcut handling in their own code.

For binding and documenting the same sequence, choosing shortcut scope, grouping entries, and handling shared factory state, see [Documenting plugin shortcuts](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/shortcuts.html).

**Qualified name:** `mv::PluginShortcuts`

class PluginShortcuts : public QObject
:   Plugin shortcuts class.

    This class is a facade of [mv::util::ShortcutMap](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#classmv_1_1util_1_1ShortcutMap)

    Public Functions

    PluginShortcuts([plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_shortcuts.html#_CPPv4N2mv15PluginShortcuts15PluginShortcutsEPN6plugin6PluginE "mv::PluginShortcuts::PluginShortcuts::plugin")::Plugin \*plugin)
    :   Construct with pointer to `plugin` and `parent` object.

        Parameters:
        :   **plugin** – Pointer to plugin

    util::[ShortcutMap](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMapE "mv::util::ShortcutMap") &getMap()
    :   Get the shortcut map.

        Returns:
        :   Shortcut map

    const util::[ShortcutMap](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMapE "mv::util::ShortcutMap") &getMap() const
    :   Get the shortcut map.

        Returns:
        :   Shortcut map

    void add(const util::[ShortcutMap](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMapE "mv::util::ShortcutMap")::[Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMap8ShortcutE "mv::util::ShortcutMap::Shortcut") &shortcut)
    :   Add `shortcut` to the map.

        Parameters:
        :   **shortcut** – Shortcut to add

    void remove(const util::[ShortcutMap](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMapE "mv::util::ShortcutMap")::[Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMap8ShortcutE "mv::util::ShortcutMap::Shortcut") &shortcut)
    :   Remove `shortcut` from the map.

        Parameters:
        :   **shortcut** – Shortcut to remove

    util::[ShortcutMap](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMapE "mv::util::ShortcutMap")::Shortcuts getShortcuts(const QStringList &categories = QStringList()) const
    :   Get shortcuts for `categories`.

        Parameters:
        :   **categories** – Categories to retrieve shortcuts for (all shortcuts if empty)

        Returns:
        :   Vector of shortcuts

    bool hasShortcuts(const QStringList &categories = QStringList()) const
    :   Establish whether any shortcut exists for `categories`.

        Parameters:
        :   **categories** – Categories to check (all categories if empty)

        Returns:
        :   Boolean determining whether any shortcut exists

    void view()
    :   View shortcut map.

    Protected Attributes

    gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_viewAction
    :   Pointer to parent plugin.
