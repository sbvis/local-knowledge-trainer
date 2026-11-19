# ColorSchemeAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/color_scheme_action.html

**Documentation path:** `api/core/gui/actions/internal/color_scheme_action.html`

---

# ColorSchemeAction

**Qualified name:** `mv::gui::ColorSchemeAction`

class ColorSchemeAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   Color scheme action class.

    For picking and editing custom color schemes

    **Author**
    :   Thomas Kroes

    Public Functions

    ColorSchemeAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void initialize()
    :   Initialize the custom color scheme action.
