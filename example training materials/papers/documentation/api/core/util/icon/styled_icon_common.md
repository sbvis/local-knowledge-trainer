# StyledIconCommon

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_common.html

**Documentation path:** `api/core/util/icon/styled_icon_common.html`

---

# StyledIconCommon

enum class mv::util::StyledIconMode
:   Styled icon modes.

    *Values:*

    enumerator ThemeAware

    enumerator FixedColor
    :   Icon is colored by current theme with QPalette::ColorGroup and QPalette::ColorRole the (default)

        Icon is colored by a fixed color

struct StyledIconSettings
:   Public Functions

    QPalette::ColorGroup getColorGroupForCurrentTheme() const
    :   Get color group for current theme.

        Returns:
        :   Color group for current theme

    QPalette::ColorRole getColorRoleForCurrentTheme() const
    :   Get color role for current theme.

        Returns:
        :   Color role for current theme

    Public Members

    QString \_modifierSha
    :   Icon key.

    [StyledIconMode](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_common.html#_CPPv4N2mv4util14StyledIconModeE "mv::util::StyledIconMode") \_mode
    :   Modifier icon key.

    QPalette::ColorGroup \_colorGroupLightTheme
    :   Styled icon coloring mode.

    QPalette::ColorGroup \_colorGroupDarkTheme
    :   Color group for light theme.

    QPalette::ColorRole \_colorRoleLightTheme
    :   Color group for dark theme.

    QPalette::ColorRole \_colorRoleDarkTheme
    :   Color role for light theme.

    QColor \_fixedColor
    :   Color role for dark theme.

    [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5BadgeE "mv::util::Badge")::[Parameters](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5Badge10ParametersE "mv::util::Badge::Parameters") \_badgeParameters
    :   Fixed color.
