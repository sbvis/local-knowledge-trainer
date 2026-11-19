# PaletteAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/palette_action.html

**Documentation path:** `api/core/gui/actions/internal/palette_action.html`

---

# PaletteAction

**Qualified name:** `mv::gui::PaletteAction`

class PaletteAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   Palette class.

    For editing the palette of the application

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Types

    using PaletteColorRoleActions = std::array<std::unique\_ptr<[PaletteColorRoleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/palette_color_role_action.html#_CPPv4N2mv3gui22PaletteColorRoleActionE "mv::gui::PaletteColorRoleAction")>, QPalette::ColorRole::NColorRoles>
    :   Palette color role actions.

    Public Functions

    Q\_INVOKABLE PaletteAction(QObject \*parent, const QString &title)
    :   Construct a palette action with a `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void initialize()
    :   Initialize the palette.

    QPalette &getPalette()
    :   Get the palette.

    void setPalette(const QPalette &palette)
    :   Set the palette to `palette`.

        Parameters:
        :   **palette** – Current palette

    void paletteChanged(const QPalette &palette)
    :   Signals that the palette changed to `palette`.

        Parameters:
        :   **palette** –

    Protected Static Attributes

    static QStringList colorRoleNames
    :   Cached palette.

    Friends

    *friend class* PaletteColorAction
