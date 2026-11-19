# Icon

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/icon/index.html

**Documentation path:** `api/core/util/icon/index.html`

---

# Icon

This section documents the classes and helper functions used to create, style, and compose icons within the user interface. It covers icon styling infrastructure as well as utility functions for generating composite icons, overlays, and badge-enhanced variants used throughout the application and its plugins.

For guidance on named icons, theme behavior, custom resources, modifiers, and badges, see [Using icons in plugins](https://manivault.readthedocs.io/en/latest/development/building_plugins/icons.html).

## Classes

- [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html)
- [StyledIconCommon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_common.html)
- [StyledIconEngine](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_engine.html)

## Functions

QIcon mv::gui::createIcon(const QPixmap &pixmap, const QList<QSize> &pixmapSizes = defaultIconPixmapSizes)
:   Convenience function to create icon from a `pixmap` and for `pixmapSizes`.

    Parameters:
    :   - **pixmap** – Source pixmap
        - **pixmapSizes** – Pixmap size in the icon

    Returns:
    :   Icon

QIcon mv::gui::createOverlayIcon(const QIcon &icon, const QPixmap &overlay)
:   Convenience function to overlay `icon` pixmap(s) with an overlay `pixmap`.

    Parameters:
    :   - **icon** – Source icon
        - **overlay** – Overlay pixmap

    Returns:
    :   Overlay icon

QIcon mv::gui::combineIcons(const QIcon &iconA, const QIcon &iconB)
:   Draws `iconB` on top of `iconA`.

    Parameters:
    :   - **iconA** – Icon A
        - **iconB** – Icon B (overlays iconA)

    Returns:
    :   Combined icon

QIcon mv::gui::createPluginIcon(const QString &characters)
:   Convenience function to create a plugin icon, which consists of maximum of four characters laid out in a grid.

    Parameters:
    :   **characters** – Characters

    Returns:
    :   Plugin icon

QIcon mv::gui::combineIconsHorizontally(const QVector<QIcon> &icons)
:   Combines two (or more) icons into a horizontal icon.

    Parameters:
    :   **icons** – Vector of input icons (need to be the same height)

    Returns:
    :   Combined icon

QPixmap mv::gui::createNumberBadgeOverlayPixmap(std::uint32\_t number, const QColor &backgroundColor, const QColor &foregroundColor)
:   Creates a pixmap with a number badge from `number`, `badgeBackgroundColor` and `foregroundColor`.

    Parameters:
    :   - **number** – Integral to display in the badge
        - **backgroundColor** – Color of the badge background
        - **foregroundColor** – Color of the badge foreground (text)

    Returns:
    :   Number badge pixmap

QPixmap mv::gui::createNumberBadgeOverlayPixmap(const util::[Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5BadgeE "mv::util::Badge") &widgetActionBadge)
:   Creates a pixmap with a number badge from `widgetActionBadge`.

    Parameters:
    :   **widgetActionBadge** – Widget action badge configuration

    Returns:
    :   Number badge pixmap

QIcon mv::gui::createIconWithNumberBadgeOverlay(const QIcon &icon, const util::[Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5BadgeE "mv::util::Badge") &widgetActionBadge, std::uint32\_t iconMargin = 0)
:   Overlays `icon` with a `number` badge in `color` and with `alignment`.

    Parameters:
    :   - **icon** – Icon to overlay
        - **widgetActionBadge** – Widget action badge configuration
        - **iconMargin** – Icon margin

    Returns:
    :   Icon with badge overlay
