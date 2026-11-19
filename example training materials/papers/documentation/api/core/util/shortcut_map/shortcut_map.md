# ShortcutMap

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html

**Documentation path:** `api/core/util/shortcut_map/shortcut_map.html`

---

# ShortcutMap

This map documents categorized shortcuts; it does not install key bindings. For implementation patterns and shared-state considerations, see [Documenting plugin shortcuts](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/shortcuts.html).

**Qualified name:** `mv::util::ShortcutMap`

class ShortcutMap : public QObject
:   [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) map class.

    Helper class for storing a map of categorized shortcuts and creating a shortcut cheatsheet overlay widget

    Note: This class is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit ShortcutMap(const QString &title = "", QObject \*parent = nullptr)
    :   Construct with `title` and pointer to `parent` object.

        Parameters:
        :   - **title** – [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) map title
            - **parent** – Pointer to parent object

    virtual ~ShortcutMap() override = default
    :   No need for custom destructor.

    QString getTitle() const
    :   Get shortcut map title.

        Returns:
        :   [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) map title

    void setTitle(const QString &title)
    :   Set shortcut map title to `title`.

        Parameters:
        :   **title** – [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) map title

    void addShortcut(const [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMap8ShortcutE "mv::util::ShortcutMap::Shortcut") &shortcut)
    :   Add `shortcut` to the map.

        Parameters:
        :   **shortcut** – [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) to add

    void removeShortcut(const [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMap8ShortcutE "mv::util::ShortcutMap::Shortcut") &shortcut)
    :   Remove `shortcut` from the map.

        Parameters:
        :   **shortcut** – [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) to remove

    Shortcuts getShortcuts(const QStringList &categories = QStringList()) const
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

    QStringList getCategories() const
    :   Get shortcut categories.

        Returns:
        :   [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) categories

    void titleChanged(const QString &title)
    :   Signals that the shortcut map `title` has changed.

        Parameters:
        :   **title** – Updated shortcut map title

    void shortcutAdded(const [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMap8ShortcutE "mv::util::ShortcutMap::Shortcut") &shortcut)
    :   Signals that `shortcut` is added.

        Parameters:
        :   **shortcut** – [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) that is added

    void shortcutAboutToBeRemoved(const [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMap8ShortcutE "mv::util::ShortcutMap::Shortcut") &shortcut)
    :   Signals that `shortcut` is about to be removed.

        Parameters:
        :   **shortcut** – [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) that is about to be removed

    void shortcutRemoved(const [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMap8ShortcutE "mv::util::ShortcutMap::Shortcut") &shortcut)
    :   Signals that `shortcut` is removed.

        Parameters:
        :   **shortcut** – [Shortcut](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#structmv_1_1util_1_1ShortcutMap_1_1Shortcut) that is removed

    struct Shortcut
