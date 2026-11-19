# PaletteColorAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/palette_color_action.html

**Documentation path:** `api/core/gui/actions/internal/palette_color_action.html`

---

# PaletteColorAction

**Qualified name:** `mv::gui::PaletteColorAction`

class PaletteColorAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   Palette color class.

    For editing a palette color of the application

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE PaletteColorAction(QObject \*parent, const QString &title, const QPalette::ColorGroup &colorGroup = QPalette::ColorGroup::Normal, const QPalette::ColorRole &colorRole = QPalette::ColorRole::Window)
    :   Construct a palette action with a `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **colorGroup** – Color group of the palette color
            - **colorRole** – Color role of the palette color

    void initialize(const QPalette::ColorGroup &colorGroup, const QPalette::ColorRole &colorRole)
    :   Initialize the palette color action with a `colorGroup` and `colorRole`.

        Parameters:
        :   - **colorGroup** – Color group of the palette color
            - **colorRole** – Color role of the palette color
