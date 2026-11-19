# AbstractDatasetsModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html

**Documentation path:** `api/core/models/datasets/abstract_datasets_model.html`

---

# AbstractDatasetsModel

**Qualified name:** `mv::AbstractDatasetsModel`

class AbstractDatasetsModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Datasets model class.

    Standard item model class for datasets

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::DatasetsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/datasets_list_model.html#classmv_1_1DatasetsListModel)

    Public Types

    enum class PopulationMode
    :   Population.

        *Values:*

        enumerator Manual

        enumerator Automatic
        :   …done manually with `setDatasets()`

            …performed every time a dataset is added or removed

    enum class Column
    :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) columns.

        *Values:*

        enumerator Name

        enumerator Location
        :   Name of the dataset.

        enumerator ID
        :   Location of the dataset.

        enumerator RawDataName
        :   Globally unique identifier of the dataset.

        enumerator SourceDatasetID
        :   Name of the associated raw data.

        enumerator Count
        :   Globally unique dataset identifier of the source dataset (if this dataset is derived)

    Public Functions

    AbstractDatasetsModel([PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationModeE "mv::AbstractDatasetsModel::PopulationMode") populationMode = [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationModeE "mv::AbstractDatasetsModel::PopulationMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationMode9AutomaticE "mv::AbstractDatasetsModel::PopulationMode::Automatic"), QObject \*parent = nullptr)
    :   Construct with `populationMode` and pointer to `parent` object.

        Parameters:
        :   - **populationMode** – Population mode
            - **parent** – Pointer to parent object

    QModelIndex getIndexFromDataset([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset) const
    :   Get index from `dataset` smart pointer.

        Parameters:
        :   **dataset** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) to retrieve the index for

        Returns:
        :   Model index (invalid if not found)

    QModelIndex getIndexFromDataset(const QString &datasetId) const
    :   Get index from `datasetId`.

        Parameters:
        :   **datasetId** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) globally unique identifier to retrieve the row index for

        Returns:
        :   Model index (invalid if not found)

    QStandardItem \*getItemFromDataset(const QString &datasetId) const
    :   Get item from `datasetId`.

        Parameters:
        :   **datasetId** – Globally unique identifier of the dataset

        Returns:
        :   Pointer to found item, nullptr otherwise

    QStandardItem \*getItemFromDataset([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset) const
    :   Get item dataset smart pointer to `dataset`.

        Parameters:
        :   **dataset** – Smart pointer to the dataset

        Returns:
        :   Pointer to found item, nullptr otherwise

    [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationModeE "mv::AbstractDatasetsModel::PopulationMode") getPopulationMode() const
    :   Get current population mode.

        Returns:
        :   Population mode

    void setPopulationMode([PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationModeE "mv::AbstractDatasetsModel::PopulationMode") populationMode)
    :   Set population mode to `populationMode`.

        Parameters:
        :   **populationMode** – Population mode

    Datasets getDatasets() const
    :   Get datasets.

        Returns:
        :   Datasets

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getDataset(std::int32\_t rowIndex) const
    :   Get dataset for `rowIndex`.

        Parameters:
        :   **rowIndex** – Index of the row to retrieve

        Returns:
        :   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset)

    void setDatasets(mv::Datasets datasets)
    :   Set the datasets from which can be picked (mode is set to StorageMode::Manual)

        Parameters:
        :   **datasets** – Datasets

    Public Static Attributes

    static QMap<[Column](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel6ColumnE "mv::AbstractDatasetsModel::Column"), [ColumHeaderInfo](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel15ColumHeaderInfoE "mv::AbstractDatasetsModel::ColumHeaderInfo")> columnInfo
    :   Column name and tooltip.

    Protected Functions

    virtual void addDataset([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
    :   Add `dataset` to the model (this method is called when a dataset is added to the manager)

        Parameters:
        :   **dataset** – Smart pointer to dataset to add

    virtual void removeDataset([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset) final
    :   Remove `dataset` from the model (this method is called when a dataset is about to be removed from the manager)

        Parameters:
        :   **dataset** – Smart pointer to dataset to remove

    struct ColumHeaderInfo
    :   Header strings for several data roles.

        Public Members

        QString \_edit
        :   Header string for display role.

        QString \_tooltip
        :   Header string for edit role.

    class HeaderItem : public QStandardItem
    :   Header standard model item class.

        Public Functions

        HeaderItem(const [ColumHeaderInfo](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel15ColumHeaderInfoE "mv::AbstractDatasetsModel::ColumHeaderInfo") &columHeaderInfo)
        :   Construct with `columHeaderInfo`.

            Parameters:
            :   **columHeaderInfo** – Column header info

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class IdItem : public mv::[AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel4ItemE "mv::AbstractDatasetsModel::Item")
    :   Standard model item class for displaying the dataset identifier.

        Public Functions

        IdItem([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel") &datasetsModel, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with reference to the owning `datasetsModel` and smart pointer to the `dataset`.

            Parameters:
            :   - **datasetsModel** – Reference to the owning datasets model
                - **dataset** – Smart pointer to the dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class Item : public QStandardItem, public QObject
    :   Base standard model item class for a dataset.

        Subclassed by [mv::AbstractDatasetsModel::IdItem](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#classmv_1_1AbstractDatasetsModel_1_1IdItem), [mv::AbstractDatasetsModel::LocationItem](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#classmv_1_1AbstractDatasetsModel_1_1LocationItem), [mv::AbstractDatasetsModel::NameItem](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#classmv_1_1AbstractDatasetsModel_1_1NameItem), [mv::AbstractDatasetsModel::RawDataNameItem](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#classmv_1_1AbstractDatasetsModel_1_1RawDataNameItem), [mv::AbstractDatasetsModel::SourceDatasetIdItem](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#classmv_1_1AbstractDatasetsModel_1_1SourceDatasetIdItem)

        Public Functions

        Item([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel") &datasetsModel, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, bool editable = false)
        :   Construct with reference to the owning `datasetsModel` and smart pointer to the `dataset`.

            Parameters:
            :   - **datasetsModel** – Reference to the datasets model
                - **dataset** – Smart pointer to the dataset to display item for
                - **editable** – Whether the model item is editable or not

        [AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel") &getDatasetsModel()
        :   Get datasets model return Reference to datasets model.

        [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &getDataset()
        :   Get dataset return Reference to smart pointer to dataset to display item for.

    class LocationItem : public mv::[AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel4ItemE "mv::AbstractDatasetsModel::Item")
    :   Standard model item class for displaying the dataset location.

        Public Functions

        LocationItem([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel") &datasetsModel, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with reference to the owning `datasetsModel` and smart pointer to the `dataset`.

            Parameters:
            :   - **datasetsModel** – Reference to the owning datasets model
                - **dataset** – Smart pointer to the dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class NameItem : public mv::[AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel4ItemE "mv::AbstractDatasetsModel::Item")
    :   Standard model item class for displaying the dataset name.

        Public Functions

        NameItem([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel") &datasetsModel, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with reference to the owning `datasetsModel` and smart pointer to the `dataset`.

            Parameters:
            :   - **datasetsModel** – Reference to the owning datasets model
                - **dataset** – Smart pointer to the dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class RawDataNameItem : public mv::[AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel4ItemE "mv::AbstractDatasetsModel::Item")
    :   Standard model item class for displaying the raw data name.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel") &datasetsModel, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, bool editable = false)
        :   No need for custom constructor.

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining dataset items in a row.

        Public Functions

        inline Row([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel") &datasetsModel, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with reference to the owning `datasetsModel` and smart pointer to the `dataset`.

            Parameters:
            :   - **datasetsModel** – Reference to the owning datasets model
                - **dataset** – Smart pointer to the dataset to display item for

    class SourceDatasetIdItem : public mv::[AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel4ItemE "mv::AbstractDatasetsModel::Item")
    :   Standard model item class for displaying the source dataset identifier name.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel") &datasetsModel, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, bool editable = false)
        :   No need for custom constructor.
