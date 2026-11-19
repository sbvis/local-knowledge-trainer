# StyledIcon

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html

**Documentation path:** `api/core/util/icon/styled_icon.html`

---

# StyledIcon

`StyledIcon` creates theme-aware icons from bundled icon fonts and can apply palette roles, fixed colors, modifiers, and badges. For practical selection and styling patterns, see [Using icons in plugins](https://manivault.readthedocs.io/en/latest/development/building_plugins/icons.html).

**Qualified name:** `mv::util::StyledIcon`

class StyledIcon
:   Styled icon class.

    [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#classmv_1_1util_1_1StyledIcon) class is a wrapper around QIcon that allows for easy creation of icons from icon fonts.

    - Support icon fonts (FontAwesome, Material Design Icons, etc.)
    - Supports custom icons
    - Theme-aware (due to [StyledIconEngine](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_engine.html#classmv_1_1util_1_1StyledIconEngine))

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit StyledIcon(const QString &iconName = "", const QString &iconFontName = [defaultIconFontName](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon19defaultIconFontNameE "mv::util::StyledIcon::defaultIconFontName"), const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion = [defaultIconFontVersion](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon22defaultIconFontVersionE "mv::util::StyledIcon::defaultIconFontVersion"))
    :   Construct from `iconName`, `iconFontName` and `iconFontVersion`.

        Parameters:
        :   - **iconName** – Name of the icon
            - **iconFontName** – Name of the icon font
            - **iconFontVersion** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the icon font

    explicit StyledIcon(const QIcon &other)
    :   Copy construct from `other` styled icon.

        Parameters:
        :   **icon** –

    inline operator QIcon() const
    :   Implicit conversion to QIcon.

        Returns:
        :   Icon

    inline operator QVariant() const
    :   Implicit conversion to QVariant.

        Returns:
        :   Variant

    inline [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") &operator=(const [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") &other)
    :   Assign `other` styled icon.

        Parameters:
        :   **other** – Other styled icon to assign from

        Returns:
        :   Copied result

    void set(const QString &iconName, const QString &iconFontName = [defaultIconFontName](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon19defaultIconFontNameE "mv::util::StyledIcon::defaultIconFontName"), const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion = [defaultIconFontVersion](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon22defaultIconFontVersionE "mv::util::StyledIcon::defaultIconFontVersion"))
    :   Configure the styled icon by `iconName` and possibly override the default `iconFontName` and `iconFontVersion`.

        Parameters:
        :   - **iconName** – Name of the icon
            - **iconFontName** – Name of the icon font
            - **iconFontVersion** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the icon font

    [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") &withColorGroups(const QPalette::ColorGroup &colorGroupLightTheme, const QPalette::ColorGroup &colorGroupDarkTheme)
    :   Return styled icon with changed color groups `colorGroupLightTheme` and `colorGroupDarkTheme`.

        Parameters:
        :   - **colorGroupLightTheme** – Color group for light theme
            - **colorGroupDarkTheme** – Color group for dark theme

        Returns:
        :   Reference to changed styled icon

    [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") &withColorRoles(const QPalette::ColorRole &colorRoleLightTheme, const QPalette::ColorRole &colorRoleDarkTheme)
    :   Return styled icon with changed color roles `colorRoleLightTheme` and `colorRoleDarkTheme`.

        Parameters:
        :   - **colorRoleLightTheme** – Color role for light theme
            - **colorRoleDarkTheme** – Color role for dark theme

        Returns:
        :   Reference to changed styled icon

    [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") &withBadge(const [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5BadgeE "mv::util::Badge")::[Parameters](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5Badge10ParametersE "mv::util::Badge::Parameters") &badgeParameters)
    :   Return styled icon with `badge` parameters.

        Parameters:
        :   **badgeParameters** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) parameters

        Returns:
        :   Reference to changed styled icon

    [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") &withColor(const QColor &color)
    :   Return styled icon with changed `color`.

        Parameters:
        :   **color** – Color

        Returns:
        :   Reference to changed styled icon

    [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") withMode(const [StyledIconMode](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_common.html#_CPPv4N2mv4util14StyledIconModeE "mv::util::StyledIconMode") &mode)
    :   Return styled icon with `mode`.

        Parameters:
        :   **mode** – The mode of the styled icon

        Returns:
        :   Reference to changed styled icon

    [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") withModifier(const QString &iconName, const QString &iconFontName = [defaultIconFontName](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon19defaultIconFontNameE "mv::util::StyledIcon::defaultIconFontName"), const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion = [defaultIconFontVersion](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon22defaultIconFontVersionE "mv::util::StyledIcon::defaultIconFontVersion"))
    :   Set icon modifier.

        Parameters:
        :   - **iconName** – Name of the modifier icon
            - **iconFontName** – Name of the modifier icon font
            - **iconFontVersion** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the modifier icon font

    [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5BadgeE "mv::util::Badge")::[Parameters](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5Badge10ParametersE "mv::util::Badge::Parameters") getBadge() const
    :   Get badge.

        Returns:
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge)

    void setBadgeEnabled(bool badgeEnabled)
    :   Set badge enabled to `badgeEnabled`.

        Parameters:
        :   **badgeEnabled** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) enabled

    bool isBadgeEnabled() const
    :   Get badge enabled.

        Returns:
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) enabled

    Public Static Functions

    static [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") fromFontAwesomeRegular(const QString &iconName, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &version = [defaultIconFontVersion](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon22defaultIconFontVersionE "mv::util::StyledIcon::defaultIconFontVersion"))
    :   Create icon with `iconName` from `version` of Font Awesome regular.

        Parameters:
        :   - **iconName** – Name of the icon
            - **version** – Font Awesome version

        Returns:
        :   Named icon

    static [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") fromFontAwesomeBrandsRegular(const QString &iconName, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &version = [defaultIconFontVersion](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon22defaultIconFontVersionE "mv::util::StyledIcon::defaultIconFontVersion"))
    :   Create icon with `iconName` from `version` of Font Awesome Brands.

        Parameters:
        :   - **iconName** – Name of the icon
            - **version** – Font Awesome version

        Returns:
        :   Named icon

    static [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") fromQIcon(const QIcon &icon, const [StyledIconMode](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_common.html#_CPPv4N2mv4util14StyledIconModeE "mv::util::StyledIconMode") &mode = [StyledIconMode](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_common.html#_CPPv4N2mv4util14StyledIconModeE "mv::util::StyledIconMode")::[ThemeAware](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_common.html#_CPPv4N2mv4util14StyledIconMode10ThemeAwareE "mv::util::StyledIconMode::ThemeAware"))
    :   Create a styled icon from a Qt `icon` with `mode`.

        Parameters:
        :   - **icon** – Icon to create the styled icon from
            - **mode** – The mode of the styled icon

        Returns:
        :   Styled icon

    static QFont getIconFont(std::int32\_t fontPointSize = -1, const QString &iconFontName = [defaultIconFontName](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon19defaultIconFontNameE "mv::util::StyledIcon::defaultIconFontName"), const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion = [defaultIconFontVersion](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon22defaultIconFontVersionE "mv::util::StyledIcon::defaultIconFontVersion"))
    :   Get icon font for `iconFontName` at `iconFontVersion`.

        Parameters:
        :   - **fontPointSize** – Point size of the font
            - **iconFontName** – Name of the icon font
            - **iconFontVersion** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the icon font

        Returns:
        :   Icon font

    static QString getIconCharacter(const QString &iconName, const QString &iconFontName = [defaultIconFontName](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon19defaultIconFontNameE "mv::util::StyledIcon::defaultIconFontName"), const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion = [defaultIconFontVersion](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIcon22defaultIconFontVersionE "mv::util::StyledIcon::defaultIconFontVersion"))
    :   Converts human readable `icon` name to icon character (unicode)

        Parameters:
        :   - **iconName** – Name of the icon
            - **iconFontName** – Name of the icon font
            - **iconFontVersion** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the icon font

        Returns:
        :   Unicode icon character (empty if not found)

    Protected Static Functions

    static void initializeIconFont(const QString &iconFontName, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion)
    :   Initialize `version` of `iconFontName`.

        Parameters:
        :   - **iconFontName** – Name of the icon font
            - **iconFontVersion** – Font Awesome version

    static QString getIconFontResourceName(const QString &iconFontName, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion)
    :   Get icon font resource name for `iconFontName` at `version`.

        Parameters:
        :   - **iconFontName** – Name of the icon font
            - **iconFontVersion** – Icon font version

        Returns:
        :   Icon font resource name

    static QString getIconFontResourcePath(const QString &iconFontName, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion)
    :   Get icon font resource path for `iconFontName` at `version`.

        Parameters:
        :   - **iconFontName** – Name of the icon font
            - **iconFontVersion** – Icon font version

        Returns:
        :   Icon font resource path

    static QString getIconFontMetadataResourcePath(const QString &iconFontName, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion)
    :   Get icon font metadata resource path for `iconFontName` at `version`.

        Parameters:
        :   - **iconFontName** – Name of the icon font
            - **iconFontVersion** – Icon font version

        Returns:
        :   Icon font metadata resource path

    static QPixmap createIconPixmap(const QString &iconName, const QString &iconFontName, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion, const QColor &foregroundColor = QColor(0, 0, 0, 0), const QColor &backgroundColor = Qt::transparent)
    :   Create icon pixmap from `iconName`, `iconFontName` and `iconFontVersion`.

        Parameters:
        :   - **iconName** – Icon name
            - **iconFontName** – Font name
            - **iconFontVersion** – Font version
            - **foregroundColor** – Foreground color
            - **backgroundColor** – Background color

        Returns:
        :   Icon pixmap

    static QString getIconFontVersionString(const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &version)
    :   Get icon font version string for `version`.

        Returns:
        :   Icon font version string (e.g. 2.4)

    Protected Static Attributes

    static QMap<QString, QVariantMap> fontMetadata
    :   [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the modifier icon font.

    static QMap<QString, QFont> fonts
    :   Font-specific metadata.

    static QString defaultIconFontName
    :   Icon fonts.

    static [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") defaultIconFontVersion
    :   Default icon font name.

    static QMap<QString, QPixmap> pixmaps
    :   Default icon font version.

    static QVector<QStringList> iconFontPreferenceGroups
    :   All pixmaps for icons.

    static QMap<QString, QVector<[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version")>> iconFontVersions
    :   The order in each usb-vector determines fetching precedence.

    Friends

    *friend class* StyledIconEngine
