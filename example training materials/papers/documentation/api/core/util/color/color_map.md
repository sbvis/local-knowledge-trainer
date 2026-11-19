# ColorMap

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html

**Documentation path:** `api/core/util/color/color_map.html`

---

# ColorMap

**Qualified name:** `mv::util::ColorMap`

class ColorMap
:   Color map class.

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Type
    :   Color map types.

        *Values:*

        enumerator OneDimensional

        enumerator TwoDimensional
        :   One-dimensional color map.

            Two-dimensional color map

    Public Functions

    ColorMap(const QString &name = "", const QString &resourcePath = "", const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") &type = [Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type")::[OneDimensional](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4Type14OneDimensionalE "mv::util::ColorMap::Type::OneDimensional"), const QImage &image = QImage())
    :   (Default) constructor

        Parameters:
        :   - **name** – Name of the color map
            - **resourcePath** – Resource path of the color map image
            - **name** – Color map type
            - **image** – Color map image

    QString getName() const
    :   Returns the color map name.

    QString getResourcePath() const
    :   Returns the resource path.

    [Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") getType() const
    :   Returns the color map type.

    QImage getImage() const
    :   Returns the color map image.

    std::uint32\_t getNoDimensions() const
    :   Returns the number of dimensions.
