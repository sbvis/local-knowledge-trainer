# StyledIconEngine

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_engine.html

**Documentation path:** `api/core/util/icon/styled_icon_engine.html`

---

# StyledIconEngine

**Qualified name:** `mv::util::StyledIconEngine`

class StyledIconEngine : public QIconEngine
:   Styled icon engine class.

    Icon engine for creating theme-specific icons of the [StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#classmv_1_1util_1_1StyledIcon).

    **Author**
    :   Thomas Kroes

    Public Functions

    StyledIconEngine(const [StyledIconSettings](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon_common.html#_CPPv4N2mv4util18StyledIconSettingsE "mv::util::StyledIconSettings") &styledIconSettings)
    :   Construct from `styledIconSettings`.

        Parameters:
        :   **styledIconSettings** – Reference to styled icon settings

    void paint(QPainter \*painter, const QRect &rect, QIcon::Mode mode, QIcon::State state) override
    :   Paint the icon.

        Parameters:
        :   - **painter** – Pointer to painter
            - **rect** – Rectangle to paint
            - **mode** – Mode of the icon
            - **state** – State of the icon

    QPixmap pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state) override
    :   Get pixmap.

        Parameters:
        :   - **size** – Size of the pixmap
            - **mode** – Mode of the icon
            - **state** – State of the icon

        Returns:
        :   Pixmap

    QIconEngine \*clone() const override
    :   Clone the theme icon engine.

        Returns:
        :   Pointer to cloned theme icon engine
