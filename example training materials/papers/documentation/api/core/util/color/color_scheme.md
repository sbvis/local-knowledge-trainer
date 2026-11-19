# ColorScheme

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html

**Documentation path:** `api/core/util/color/color_scheme.html`

---

# ColorScheme

**Qualified name:** `mv::util::ColorScheme`

class ColorScheme
:   Color scheme class.

    Contains color scheme information

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Mode
    :   Color scheme modes.

        *Values:*

        enumerator BuiltIn

        enumerator UserAdded
        :   Built-in color scheme.

            Color scheme added by the user

    using Modes = std::vector<[Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode")>
    :   Vector of color scheme modes.

    Public Functions

    explicit ColorScheme(const [Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode") &mode = [Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode")::[BuiltIn](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4Mode7BuiltInE "mv::util::ColorScheme::Mode::BuiltIn"), const QString &name = "", const QString &description = "", const QPalette &palette = QPalette())
    :   Construct color scheme with `mode`, `name`, `description` and `palette`.

        Parameters:
        :   - **mode** – Color scheme mode
            - **name** – Color scheme name
            - **description** – Color scheme description
            - **palette** – Color scheme palette

    [Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode") getMode() const
    :   Get color scheme mode.

        Returns:
        :   Color scheme mode

    void setMode(const [Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode") &mode)
    :   Set color scheme mode to `mode`.

        Parameters:
        :   **mode** – Color scheme mode

    QString getName() const
    :   Get color scheme name.

        Returns:
        :   Color scheme name

    void setName(const QString &name)
    :   Set color scheme name to `name`.

        Parameters:
        :   **name** – Color scheme name

    QString getDescription() const
    :   Get color scheme description.

        Returns:
        :   Color scheme description

    void setDescription(const QString &description)
    :   Set color scheme description to `description`.

        Parameters:
        :   **description** – Color scheme description

    QPalette getPalette() const
    :   Get color scheme palette.

        Returns:
        :   Color scheme palette

    void setPalette(const QPalette &palette)
    :   Set color scheme palette to `palette`.

        Parameters:
        :   **palette** – Color scheme palette

    Public Static Attributes

    static const QMap<[Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode"), QString> modeNames
    :   Maps color scheme mode to name.
