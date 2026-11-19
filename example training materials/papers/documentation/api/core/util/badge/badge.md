# Badge

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html

**Documentation path:** `api/core/util/badge/badge.html`

---

# Badge

**Qualified name:** `mv::util::Badge`

class Badge : public QObject
:   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) class.

    Draws a circle with a number with any Qt::Alignment flag and foreground (text) and background color. Currently used by the collapsed widget only.

    Note: By default the badge is disabled, use Badge::setEnabled(…) to enable it

    **Author**
    :   Thomas Kroes

    Public Functions

    Badge(QObject \*parent = nullptr, std::uint32\_t number = 0, const QColor &backgroundColor = Qt::red, const QColor &foregroundColor = Qt::white, Qt::Alignment alignment = Qt::AlignTop | Qt::AlignRight, float scale = 0.5f)
    :   Construct with pointer to `parent` object, badge `number`, `backgroundColor`, `foregroundColor`, `alignment` and `badge` scale.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **number** – Number displayed in the badge
            - **backgroundColor** – Background color the badge
            - **foregroundColor** – Foreground color the badge
            - **alignment** – Alignment of the badge
            - **scale** – Scale of the badge w.r.t. of its container

    QPixmap getPixmap() const
    :   Get pixmap.

        Returns:
        :   Pixmap representation of the badge (100 x 100)

    [Parameters](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5Badge10ParametersE "mv::util::Badge::Parameters") getParameters() const
    :   Get parameters.

        Returns:
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) parameters

    bool getEnabled() const
    :   Get badge enabled.

        Returns:
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) enabled

    void setEnabled(bool enabled)
    :   Set badge enabled to `enabled`.

        Parameters:
        :   **enabled** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) enabled

    std::uint32\_t getNumber() const
    :   Get badge number.

        Returns:
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) number

    void setNumber(std::uint32\_t number)
    :   Set badge number to `number`.

        Parameters:
        :   **number** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) number

    QColor getBackgroundColor() const
    :   Get background color.

        Returns:
        :   Background color

    void setBackgroundColor(const QColor &backgroundColor)
    :   Set background color to `backgroundColor`.

        Parameters:
        :   **backgroundColor** – Background color

    QColor getForegroundColor() const
    :   Get foreground color.

        Returns:
        :   Foreground color

    void setForegroundColor(const QColor &foregroundColor)
    :   Set foreground color to `foregroundColor`.

        Parameters:
        :   **foregroundColor** – Foreground color

    Qt::Alignment getAlignment() const
    :   Get badge alignment.

        Returns:
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) alignment

    void setAlignment(Qt::Alignment alignment)
    :   Set badge alignment to `alignment`.

        Parameters:
        :   **alignment** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) alignment

    float getScale() const
    :   Get badge scale.

        Returns:
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) scale

    void setScale(float scale)
    :   Set badge scale to `scale`.

        Parameters:
        :   **scale** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) scale

    QPixmap getCustomPixmap() const
    :   Get custom pixmap.

        Returns:
        :   Custom pixmap

    void setCustomPixmap(const QPixmap &customPixmap)
    :   Set custom pixmap to `customPixmap`.

        Parameters:
        :   **customPixmap** – Custom pixmap

    void enabledChanged(bool enabled)
    :   Signals that enabled changed to `enabled`.

        Parameters:
        :   **enabled** – Enabled

    void numberChanged(std::uint32\_t number)
    :   Signals that the badge number changed to `number`.

        Parameters:
        :   **number** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) number

    void backgroundColorChanged(const QColor &backgroundColor)
    :   Signals that the background color changed to `backgroundColor`.

        Parameters:
        :   **backgroundColor** – Background color

    void foregroundColorChanged(const QColor &foregroundColor)
    :   Signals that the foreground color changed to `foregroundColor`.

        Parameters:
        :   **foregroundColor** – Foreground color

    void alignmentChanged(Qt::Alignment alignmen)
    :   Signals that the badge alignment changed to `alignment`.

        Parameters:
        :   **alignment** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) alignment

    void scaleChanged(float scale)
    :   Signals that the badge scale changed to `scale`.

        Parameters:
        :   **scale** – [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) scale

    void customPixmapChanged(const QPixmap &customPixmap)
    :   Signals that the custom pixmap changed to `customPixmap`.

        Parameters:
        :   **customPixmap** – Custom pixmap

    void changed()
    :   Signals that the badge configuration changed.

    struct Parameters
    :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) parameters container struct.

        Public Functions

        inline Parameters(std::uint32\_t number = 0, const QColor &backgroundColor = Qt::red, const QColor &foregroundColor = Qt::white, Qt::Alignment alignment = Qt::AlignTop | Qt::AlignRight, float scale = 0.5f)
        :   Construct with `number`, `backgroundColor`, `foregroundColor`, `alignment` and `scale`.

            Parameters:
            :   - **number** – Number displayed in the badge
                - **backgroundColor** – Background color the badge
                - **foregroundColor** – Foreground color the badge
                - **alignment** – Alignment of the badge
                - **scale** – Scale of the badge w.r.t. of its container

        Public Members

        std::uint32\_t \_number
        :   Whether the badge is enabled or not.

        QColor \_backgroundColor
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) number.

        QColor \_foregroundColor
        :   Background color.

        Qt::Alignment \_alignment
        :   Foreground (text) color.

        float \_scale
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) alignment.

        QPixmap \_customPixmap
        :   [Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#classmv_1_1util_1_1Badge) scale w.r.t.

            its container
