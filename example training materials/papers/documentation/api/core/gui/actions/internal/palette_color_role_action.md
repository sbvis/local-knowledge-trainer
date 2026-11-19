# PaletteColorRoleAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/palette_color_role_action.html

**Documentation path:** `api/core/gui/actions/internal/palette_color_role_action.html`

---

# PaletteColorRoleAction

**Qualified name:** `mv::gui::PaletteColorRoleAction`

class PaletteColorRoleAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   Palette color role class.

    For editing a palette color role

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Types

    using PaletteColorActions = std::array<std::unique\_ptr<[PaletteColorAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/palette_color_action.html#_CPPv4N2mv3gui18PaletteColorActionE "mv::gui::PaletteColorAction")>, QPalette::ColorGroup::NColorGroups>
    :   Palette color actions.

    Public Functions

    Q\_INVOKABLE PaletteColorRoleAction(QObject \*parent, const QString &title, const QPalette::ColorRole &colorRole = QPalette::ColorRole::Window)
    :   Construct a palette color rolew action with a `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **colorRole** – Color role of the palette color

    void initialize(const QPalette::ColorRole &colorRole)
    :   Initialize with the palette `colorRole`.

        Parameters:
        :   **colorRole** – Color role of the palette color

    Protected Static Attributes

    static QStringList colorGroupNames
    :   Palette color actions for each palette color group.

    Friends

    *friend class* PaletteColorAction
