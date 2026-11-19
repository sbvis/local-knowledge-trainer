# ColorMapFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map_filter_model.html

**Documentation path:** `api/core/util/color/color_map_filter_model.html`

---

# ColorMapFilterModel

**Qualified name:** `mv::util::ColorMapFilterModel`

class ColorMapFilterModel : public QSortFilterProxyModel
:   Color map filter model class.

    **Author**
    :   Thomas Kroes

    Public Functions

    ColorMapFilterModel(QObject \*parent, const [ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") &type = [ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type")::[OneDimensional](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4Type14OneDimensionalE "mv::util::ColorMap::Type::OneDimensional"))
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **type** – Type of color map

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether a give row with give parent is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index

    [ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") getType() const
    :   Returns the type of color map.

    void setType(const [ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") &type)
    :   Sets the type of color map.

        Parameters:
        :   **type** – Type of color map (e.g. 1D, 2D)
