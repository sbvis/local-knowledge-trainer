# HardwareSpecFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/hardware_spec_filter_model.html

**Documentation path:** `api/core/models/hardware_spec/hardware_spec_filter_model.html`

---

# HardwareSpecFilterModel

**Qualified name:** `mv::HardwareSpecFilterModel`

class HardwareSpecFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Hardware specs filter model class.

    Sorting and filtering model for the hardware specs model.

    **Author**
    :   Thomas Kroes

    Public Functions

    HardwareSpecFilterModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether `row` with `parent` is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index

        Returns:
        :   Boolean indicating whether the item is filtered in or out
