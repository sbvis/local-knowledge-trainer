# EditColorSchemeAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/edit_color_scheme_action.html

**Documentation path:** `api/core/gui/actions/internal/edit_color_scheme_action.html`

---

# EditColorSchemeAction

**Qualified name:** `mv::gui::EditColorSchemeAction`

class EditColorSchemeAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   Edit color scheme action class.

    For creating and editing color schemes

    **Author**
    :   Thomas Kroes

    Public Functions

    EditColorSchemeAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void initialize(bool add = false)
    :   Initialize the edit color scheme action.

        Parameters:
        :   **add** – Add flag
