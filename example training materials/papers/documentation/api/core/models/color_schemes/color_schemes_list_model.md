# ColorSchemesListModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/color_schemes_list_model.html

**Documentation path:** `api/core/models/color_schemes/color_schemes_list_model.html`

---

# ColorSchemesListModel

**Qualified name:** `mv::ColorSchemesListModel`

class ColorSchemesListModel : public mv::[AbstractColorSchemesModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModelE "mv::AbstractColorSchemesModel")
:   Color schemes list model class.

    List model for color schemes

    **Author**
    :   Thomas Kroes

    Public Functions

    ColorSchemesListModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    void addColorScheme(util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") colorScheme)
    :   Add `colorScheme` to the model.

        Parameters:
        :   **colorScheme** – Color scheme

    void removeColorScheme(const QString &colorSchemeName)
    :   Remove color scheme with `colorSchemeName` from the model.

        Parameters:
        :   **colorSchemeName** – Color scheme name

    Protected Functions

    void addBuiltInColorSchemes()
    :   Add built-in color schemes.
