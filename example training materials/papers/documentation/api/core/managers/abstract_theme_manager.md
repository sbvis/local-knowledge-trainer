# AbstractThemeManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_theme_manager.html

**Documentation path:** `api/core/managers/abstract_theme_manager.html`

---

# AbstractThemeManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the theme manager
mv::theme()->...
```

## Related

- Color schemes [models](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/index.html)

**Qualified name:** `mv::AbstractThemeManager`

class AbstractThemeManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract theme manager class.

    This class provides an interface for the theme manager

    **Author**
    :   Thomas Kroes

    Public Types

    enum class ColorSchemeMode
    :   Color scheme modes.

        *Values:*

        enumerator System

        enumerator SystemLightDark
        :   Color scheme is determined by the system color scheme.

        enumerator Custom
        :   Color scheme is determined by the light/dark system color scheme.

            Color scheme is determined by a custom color scheme

    using CustomColorSchemesMap = QMap<QString, QPalette>
    :   Maps custom color scheme name to palette.

    Public Functions

    inline AbstractThemeManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    inline virtual void initialize() override
    :   Perform event manager startup initialization.

    inline [ColorSchemeMode](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_theme_manager.html#_CPPv4N2mv20AbstractThemeManager15ColorSchemeModeE "mv::AbstractThemeManager::ColorSchemeMode") getColorSchemeMode() const
    :   Get the current color scheme.

        Returns:
        :   Color scheme mode

    inline void setColorSchemeMode(const [ColorSchemeMode](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_theme_manager.html#_CPPv4N2mv20AbstractThemeManager15ColorSchemeModeE "mv::AbstractThemeManager::ColorSchemeMode") &colorSchemeMode)
    :   Set the color scheme mode to `colorSchemeMode`.

        Parameters:
        :   **colorSchemeMode** – Color scheme mode

    virtual bool isSystemColorSchemeModeActive() const = 0
    :   Get whether the system color scheme mode is active.

        Returns:
        :   Boolean indicating whether the system color scheme mode is active

    virtual bool isSystemLightDarkColorSchemeModeActive() const = 0
    :   Get whether the system light/dark color scheme mode is active.

        Returns:
        :   Boolean indicating whether the system light/dark color scheme mode is active

    virtual bool isSystemLightColorSchemeActive() const = 0
    :   Get whether the light system color scheme is active.

        Returns:
        :   Boolean indicating whether the light system color scheme is active (also false when the system theme is not active)

    virtual bool isSystemDarkColorSchemeActive() const = 0
    :   Get whether the dark system color scheme is active.

        Returns:
        :   Boolean indicating whether the dark system color scheme is active (also false when the system theme is not active)

    virtual bool isCustomColorSchemeModeActive() const = 0
    :   Get whether a custom color scheme mode is active.

        Returns:
        :   Boolean indicating whether a custom color scheme mode is active

    virtual void activateSystemColorScheme() = 0
    :   Set color scheme mode to system.

    virtual void activateSystemColorSchemeLightDark() = 0
    :   Set color scheme mode to system light/dark.

    virtual void activateLightSystemColorScheme() = 0
    :   Set color scheme to system light (this will activate the system light/dark color scheme mode)

    virtual void activateDarkSystemColorScheme() = 0
    :   Set theme to system dark (this will activate the system light/dark color scheme mode)

    virtual void activateCustomColorScheme() = 0
    :   Activates the currently selected custom color scheme.

    virtual void activateCustomColorScheme(const QString &customColorSchemeName) = 0
    :   Activate custom color scheme with `customThemeName` (this will override the system color scheme)

        Parameters:
        :   **customColorSchemeName** – Custom color scheme name

    virtual QStringList getCustomColorSchemeNames(const util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme")::[Modes](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme5ModesE "mv::util::ColorScheme::Modes") &customColorSchemeModes = {util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme")::[Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode")::[BuiltIn](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4Mode7BuiltInE "mv::util::ColorScheme::Mode::BuiltIn"), util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme")::[Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode")::[UserAdded](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4Mode9UserAddedE "mv::util::ColorScheme::Mode::UserAdded")}) const = 0
    :   Get custom color scheme mode names for `customColorSchemeModes`.

        Returns:
        :   List of color scheme mode names for the custom color scheme modes

    virtual util::ColorSchemesMap getCustomColorSchemes(const util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme")::[Modes](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme5ModesE "mv::util::ColorScheme::Modes") &customColorSchemeModes = {util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme")::[Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode")::[BuiltIn](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4Mode7BuiltInE "mv::util::ColorScheme::Mode::BuiltIn"), util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme")::[Mode](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4ModeE "mv::util::ColorScheme::Mode")::[UserAdded](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorScheme4Mode9UserAddedE "mv::util::ColorScheme::Mode::UserAdded")}) const = 0
    :   Get custom color schemes for `customColorSchemeModes`.

        Parameters:
        :   **customColorSchemeModes** – Custom color scheme modes

        Returns:
        :   Color schemes map

    virtual void addCustomColorScheme(const util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &colorScheme) = 0
    :   Add custom `colorScheme`.

        Parameters:
        :   **colorScheme** – Color scheme

    virtual const [ColorSchemesListModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/color_schemes_list_model.html#_CPPv4N2mv21ColorSchemesListModelE "mv::ColorSchemesListModel") &getCustomColorSchemeListModel() const = 0
    :   Get custom color schemes list model.

        Returns:
        :   Reference to custom color schemes list model

    void colorSchemeChanged()
    :   Signals that the color scheme changed.

    void colorSchemeModeChanged(const [ColorSchemeMode](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_theme_manager.html#_CPPv4N2mv20AbstractThemeManager15ColorSchemeModeE "mv::AbstractThemeManager::ColorSchemeMode") &colorSchemeMode)
    :   Signals that the color scheme mode changed to `colorSchemeMode`.

        Parameters:
        :   **colorSchemeMode** – Color scheme mode

    Public Static Functions

    static inline void restyleAllWidgets()
    :   Restyles all widgets to implement a color scheme change.

    Protected Functions

    virtual [ColorSchemesListModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/color_schemes_list_model.html#_CPPv4N2mv21ColorSchemesListModelE "mv::ColorSchemesListModel") &getCustomColorSchemeListModel() = 0
    :   Get custom color schemes list model.

        Returns:
        :   Reference to custom color schemes list model
