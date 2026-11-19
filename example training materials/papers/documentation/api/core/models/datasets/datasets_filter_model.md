# DatasetsFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/datasets/datasets_filter_model.html

**Documentation path:** `api/core/models/datasets/datasets_filter_model.html`

---

# DatasetsFilterModel

**Qualified name:** `mv::DatasetsFilterModel`

class DatasetsFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Datasets filter class.

    Proxy model for filtering datasets

    **Author**
    :   Thomas Kroes

    Public Types

    using FilterFunction = std::function<bool([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>)>
    :   Filter function signature, the input are all datasets in the core and it returns the filtered datasets.

    Public Functions

    DatasetsFilterModel(QObject \*parent = nullptr)
    :   Construct with parent `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether `row` with `parent` is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index

        Returns:
        :   Boolean indicating whether the item is filtered in or out

    void setFilterFunction(const [FilterFunction](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/datasets_filter_model.html#_CPPv4N2mv19DatasetsFilterModel14FilterFunctionE "mv::DatasetsFilterModel::FilterFunction") &filterFunction)
    :   Set datasets filter function (mode is set to StorageMode::Automatic)

        Parameters:
        :   **datasetsFilterFunction** – Filter lambda (triggered when datasets are added and/or removed from the datasets model)
