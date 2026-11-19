# ColorSchemesFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/color_schemes_filter_model.html

**Documentation path:** `api/core/models/color_schemes/color_schemes_filter_model.html`

---

# ColorSchemesFilterModel

**Qualified name:** `mv::ColorSchemesFilterModel`

class ColorSchemesFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   ColorSchemes filter model class.

    Sorting and filtering model for color schemes

    **Author**
    :   Thomas Kroes

    Public Functions

    ColorSchemesFilterModel(QObject \*parent = nullptr)
    :   Construct the filter model with `parent`.

        Parameters:
        :   **parent** – Pointer to parent object

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether a given row with give parent is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index
