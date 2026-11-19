# PresetsFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/preset/presets_filter_model.html

**Documentation path:** `api/core/util/preset/presets_filter_model.html`

---

# PresetsFilterModel

**Qualified name:** `mv::util::PresetsFilterModel`

class PresetsFilterModel : public QSortFilterProxyModel
:   Presets filter model class.

    **Author**
    :   Thomas Kroes

    Public Functions

    PresetsFilterModel(QObject \*parent)
    :   Constructor.

        Parameters:
        :   **parent** – Pointer to parent object

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether a give row with give parent is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index
