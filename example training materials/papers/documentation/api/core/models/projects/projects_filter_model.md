# ProjectsFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_filter_model.html

**Documentation path:** `api/core/models/projects/projects_filter_model.html`

---

# ProjectsFilterModel

**Qualified name:** `mv::ProjectsFilterModel`

class ProjectsFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) database filter model class.

    Sorting and filtering model for the project database model

    **Author**
    :   Thomas Kroes

    Public Functions

    ProjectsFilterModel(QObject \*parent = nullptr)
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

    void setSourceModel(QAbstractItemModel \*sourceModel) override
    :   Set source model to `sourceModel`.

        Parameters:
        :   **sourceModel** – Pointer to source model

    bool lessThan(const QModelIndex &lhs, const QModelIndex &rhs) const override
    :   Compares two model indices plugin `lhs` with `rhs`.

        Parameters:
        :   - **lhs** – Left-hand model index
            - **rhs** – Right-hand model index

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load from variant map.

        Parameters:
        :   **variantMap** – Variant map

    virtual QVariantMap toVariantMap() const override
    :   Save to variant map.

        Returns:
        :   Variant map
