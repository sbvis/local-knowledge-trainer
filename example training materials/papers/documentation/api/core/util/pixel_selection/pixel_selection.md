# PixelSelection

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html

**Documentation path:** `api/core/util/pixel_selection/pixel_selection.html`

---

# PixelSelection

## Classes

- [PixelSelectionTypeModel](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection_type_model.html)

## Enums

enum class mv::util::PixelSelectionType
:   Pixel selection types enum.

    *Values:*

    enumerator Rectangle

    enumerator Line
    :   Select pixels within a rectangle.

    enumerator Brush
    :   Select pixels within a line.

    enumerator Lasso
    :   A brush is used the paint the pixel selection.

    enumerator Polygon
    :   A lasso tool is used to select pixels.

    enumerator Sample
    :   Select pixels in the interior of a polygon.

    enumerator ROI
    :   Probe one pixel at a time.

        Select all pixels in a ROI

enum class mv::util::PixelSelectionModifierType
:   [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) modifiers enum.

    *Values:*

    enumerator Replace

    enumerator Add
    :   Replace selection.

    enumerator Subtract
    :   Add to selection.

        Subtract from selection

## Global variables

static const PixelSelectionTypes mv::util::defaultPixelSelectionTypes = {[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Rectangle](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType9RectangleE "mv::util::PixelSelectionType::Rectangle"), [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Line](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType4LineE "mv::util::PixelSelectionType::Line"), [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Brush](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType5BrushE "mv::util::PixelSelectionType::Brush"), [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Polygon](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType7PolygonE "mv::util::PixelSelectionType::Polygon"), [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Lasso](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType5LassoE "mv::util::PixelSelectionType::Lasso")}
:   Default pixel selection types.

static const QMap<[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType"), QString> mv::util::pixelSelectionTypes = {{[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Rectangle](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType9RectangleE "mv::util::PixelSelectionType::Rectangle"), "Rectangle"}, {[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Line](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType4LineE "mv::util::PixelSelectionType::Line"), "Line"}, {[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Brush](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType5BrushE "mv::util::PixelSelectionType::Brush"), "Brush"}, {[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Lasso](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType5LassoE "mv::util::PixelSelectionType::Lasso"), "Lasso"}, {[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Polygon](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType7PolygonE "mv::util::PixelSelectionType::Polygon"), "Polygon"}, {[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[Sample](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType6SampleE "mv::util::PixelSelectionType::Sample"), "Sample"}, {[PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType")::[ROI](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionType3ROIE "mv::util::PixelSelectionType::ROI"), "ROI"}}
:   Maps pixel selection type enum to name.

## Functions

inline QString mv::util::getPixelSelectionTypeName(const [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType") &pixelSelectionType)
:   Get pixel selection type name from enum.

    Parameters:
    :   **pixelSelectionType** – Pixel selection type

inline [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType") mv::util::getPixelSelectionTypeEnum(const QString &pixelSelectionTypeName)
:   Get pixel selection type enum from name.

    Parameters:
    :   **pixelSelectionTypeName** – Name of the pixel selection type

inline QString mv::util::getPixelSelectionModifierTypeName(const [PixelSelectionModifierType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util26PixelSelectionModifierTypeE "mv::util::PixelSelectionModifierType") &pixelSelectionModifierType)
:   Get pixel selection modifier type name.

    Parameters:
    :   **pixelSelectionModifierType** – Pixel selection modifier type

inline [PixelSelectionModifierType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util26PixelSelectionModifierTypeE "mv::util::PixelSelectionModifierType") mv::util::getPixelSelectionModifierTypeEnum(const QString &pixelSelectionModifierTypeName)
:   Get pixel selection modifier type enum from name.

    Parameters:
    :   **pixelSelectionModifierTypeName** – Name of the pixel selection type

QIcon mv::util::getPixelSelectionTypeIcon(const [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType") &selectionType)
:   Get the icon for the specified selection type.

    Parameters:
    :   **selectionType** – The type of selection e.g. brush rectangle etc.
