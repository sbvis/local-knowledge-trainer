# InfoWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/info_widget.html

**Documentation path:** `api/core/gui/widgets/internal/info_widget.html`

---

# InfoWidget

**Qualified name:** `mv::gui::InfoWidget`

class InfoWidget : public QWidget
:   Info widget class.

    Standard widget which displays an icon, title and description (used for instance as an overlay for other widgets).

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::InfoOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/info_overlay_widget.html#classmv_1_1gui_1_1InfoOverlayWidget)

    Public Functions

    InfoWidget(QWidget \*parent)
    :   Construct info widget with no text and style with application foreground and background color roles.

        Parameters:
        :   **parent** – Pointer to parent widget

    InfoWidget(QWidget \*parent, const QIcon &icon, const QString &title, const QString &description = "")
    :   Construct info widget with text and style with foreground and background colors.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **icon** – Icon
            - **title** – Title of the overlay
            - **description** – Overlay description

    void set(const QIcon &icon, const QString &title, const QString &description = "")
    :   Set overlay parameters.

        Parameters:
        :   - **icon** – Icon
            - **title** – Title of the overlay
            - **description** – Overlay description

    QColor getForegroundColor() const
    :   Get foreground color.

        Returns:
        :   Foreground color

    void setForegroundColor(const QColor foregroundColor)
    :   Set foreground color to `foregroundColor` (resets the color roles)

        Parameters:
        :   **foregroundColor** – Foreground color

    QColor getBackgroundColor() const
    :   Get background color.

        Returns:
        :   Background color

    void setBackgroundColor(const QColor backgroundColor)
    :   Set background color to `backgroundColor` (resets the color roles)

        Parameters:
        :   **backgroundColor** – Background color

    void setColors(const QColor &foregroundColor, const QColor &backgroundColor)
    :   Set colors (resets the color roles)

        Parameters:
        :   - **foregroundColor** – Foreground color
            - **backgroundColor** – Background color

    std::int32\_t getForegroundColorRole() const
    :   Get foreground color role.

        Returns:
        :   Foreground color role (zero if not used)

    void setForegroundColorRole(const QPalette::ColorRole &foregroundColorRole)
    :   Set foreground color role to `foregroundColorRole`.

        Parameters:
        :   **foregroundColorRole** – Foreground color role

    std::int32\_t getBackgroundColorRole() const
    :   Get background color role.

        Returns:
        :   Background color role (zero if not used)

    void setBackgroundColorRole(const QPalette::ColorRole &backgroundColorRole)
    :   Set background color role to `backgroundColorRole`.

        Parameters:
        :   **backgroundColorRole** – Background color role

    void setColorRoles(const QPalette::ColorRole &foregroundColorRole, const QPalette::ColorRole &backgroundColorRole)
    :   Set color roles.

        Parameters:
        :   - **foregroundColorRole** – Foreground color role
            - **backgroundColorRole** – Background color role

    void foregroundColorChanged(const QColor &previousForegroundColor, const QColor &currentForegroundColor)
    :   Signals that the foreground color changed from `previousForegroundColor` to `currentForegroundColor`.

        Parameters:
        :   - **previousForegroundColor** – Previous foreground color
            - **currentForegroundColor** – Current foreground color

    void backgroundColorChanged(const QColor &previousBackgroundColor, const QColor &currentBackgroundColor)
    :   Signals that the background color changed from `previousBackgroundColor` to `currentBackgroundColor`.

        Parameters:
        :   - **previousBackgroundColor** – Previous background color
            - **currentBackgroundColor** – Current background color

    void foregroundColorRoleChanged(const QPalette::ColorRole &previousForegroundColorRole, const QPalette::ColorRole &currentForegroundColorRole)
    :   Signals that the foreground color role changed from `previousForegroundColorRole` to `currentForegroundColorRole`.

        Parameters:
        :   - **previousForegroundColorRole** – Previous foreground color role
            - **currentForegroundColorRole** – Current foreground color role

    void backgroundColorRoleChanged(const QPalette::ColorRole &previousBackgroundColorRole, const QPalette::ColorRole &currentBackgroundColorRole)
    :   Signals that the background color role changed from `previousBackgroundColorRole` to `currentBackgroundColorRole`.

        Parameters:
        :   - **previousBackgroundColorRole** – Previous background color role
            - **currentBackgroundColorRole** – Current background color role
