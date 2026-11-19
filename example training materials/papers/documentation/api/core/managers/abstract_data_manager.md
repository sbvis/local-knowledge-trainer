# AbstractDataManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html

**Documentation path:** `api/core/managers/abstract_data_manager.html`

---

# AbstractDataManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the data manager
mv::data()->...
```

## Related

- [Working with data and datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/index.html)
- Core [data API](https://manivault.readthedocs.io/en/latest/api/core/data/index.html)
- Data [models](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/index.html)

**Qualified name:** `mv::AbstractDataManager`

class AbstractDataManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract data manager.

    Base abstract data manager class for managing datasets.

    **Author**
    :   Thomas Kroes and Julian Thijssen

    Public Functions

    inline explicit AbstractDataManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual QStringList getRawDataNames() const = 0
    :   Get raw data names @retun Raw data names list.

    virtual std::uint64\_t getRawDataSize(const QString &rawDataName) const = 0
    :   Get raw data size by `rawDataName`.

        Parameters:
        :   **rawDataName** – Name of the raw data

        Returns:
        :   Size of the raw data in bytes

    inline std::uint64\_t getOverallRawDataSize() const
    :   Get overall raw data size.

        Returns:
        :   Overall raw data size in bytes

    virtual QString getRawDataType(const QString &rawDataName) const = 0
    :   Get raw data type string by `rawDataName`.

        Parameters:
        :   **rawDataName** – Name of the raw data

        Returns:
        :   Raw data type string

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> createDataset(const QString &kind, const QString &guiName, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &parentDataset = [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>(), const QString &id = "", bool notify = true) = 0
    :   Creates dataset of `kind` with `guiName` to the manager and returns the created dataset.

        Parameters:
        :   - **kind** – Kind of data plugin
            - **guiName** – Name of the added dataset in the GUI
            - **parentDataset** – Smart pointer to the parent dataset in the data hierarchy (will add to the root of the data hierarchy if not valid)
            - **id** – Globally unique dataset identifier (use only for deserialization)
            - **notify** – Whether to notify the core that a dataset is added

        Returns:
        :   Smart pointer to the create dataset

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> createDatasetWithoutSelection(const QString &kind, const QString &guiName, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &parentDataset = [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>(), const QString &id = "", bool notify = true) = 0
    :   Creates dataset without selection of `kind` with `guiName` to the manager and returns the created dataset (this is only used fore serialization purposes)

        Parameters:
        :   - **kind** – Kind of data plugin
            - **guiName** – Name of the added dataset in the GUI
            - **parentDataset** – Smart pointer to the parent dataset in the data hierarchy (will add to the root of the data hierarchy if not valid)
            - **id** – Globally unique dataset identifier (use only for deserialization)
            - **notify** – Whether to notify the core that a dataset is added

        Returns:
        :   Smart pointer to the create dataset

    template<class DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html#_CPPv4I0EN2mv19AbstractDataManager13createDatasetE7DatasetI11DatasetTypeERK7QStringRK7QStringRK7DatasetI11DatasetImplERK7QStringb "mv::AbstractDataManager::createDataset::DatasetType")> createDataset(const QString &kind, const QString &dataSetGuiName, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &parentDataset = [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>(), const QString &id = "", bool notify = true)
    :   Creates dataset of `kind` with `guiName` to the manager and returns the created dataset as `DatasetType`.

        Parameters:
        :   - **kind** – Kind of data plugin
            - **guiName** – Name of the added dataset in the GUI
            - **parentDataset** – Smart pointer to the parent dataset in the data hierarchy (will add to the root of the data hierarchy if not valid)
            - **id** – Globally unique dataset identifier (use only for deserialization)
            - **notify** – Whether to notify the core that a dataset is added

        Returns:
        :   Smart pointer to the added dataset

    virtual void removeDataset([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset) = 0
    :   Remove `dataset` from the manager.

        Parameters:
        :   **dataset** – Smart pointer to dataset to remove

    virtual void removeDatasets(Datasets datasets) = 0
    :   Remove `datasets` from the manager.

        Parameters:
        :   **datasets** – Smart pointer to datasets to remove

    virtual void removeDatasets(const QString &rawDataName) = 0
    :   Remove datasets that reference `rawDataName` from the manager.

        Param :

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> createDerivedDataset(const QString &guiName, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &sourceDataset, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &parentDataset = [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>(), bool notify = true) = 0
    :   Creates derived dataset from \666p sourceDataset with `guiName` and returns the created derived dataset.

        Parameters:
        :   - **guiName** – GUI name for the new dataset from the core
            - **sourceDataset** – Smart pointer to the source dataset from which this dataset will be derived
            - **parentDataset** – Smart pointer to the parent dataset in the data hierarchy (will attach to source dataset in hierarchy if not valid)
            - **notify** – Whether to notify the core that a dataset is added

        Returns:
        :   Smart pointer to the created derived dataset

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html#_CPPv4I0EN2mv19AbstractDataManager20createDerivedDatasetE7DatasetI11DatasetTypeERK7QStringRK7DatasetI11DatasetImplERK7DatasetI11DatasetImplEb "mv::AbstractDataManager::createDerivedDataset::DatasetType")> createDerivedDataset(const QString &guiName, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &sourceDataset, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &parentDataset = [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>(), bool notify = true)
    :   Creates derived dataset from `sourceDataset` with `guiName` and returns the created derived dataset as `DatasetType`.

        Parameters:
        :   - **guiName** – GUI name for the new dataset from the core
            - **sourceDataset** – Smart pointer to the source dataset from which this dataset will be derived
            - **parentDataset** – Smart pointer to the parent dataset in the data hierarchy (will attach to source dataset in hierarchy if not valid)
            - **notify** – Whether to notify the core that a dataset is added

        Returns:
        :   Smart pointer to the created derived dataset of `DatasetType`

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> createSubsetFromSelection(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &selection, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &sourceDataset, const QString &guiName, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &parentDataset, const bool &visible = true, bool notify = true) = 0
    :   Creates a copy of `selection` with the `sourceDataset`, adds it to the manager and returns the created subset.

        Parameters:
        :   - **selection** – Smart pointer to the selection set
            - **sourceDataset** – Smart pointer to the source dataset
            - **guiName** – GUI name of the subset
            - **parentDataset** – Smart pointer to the parent dataset in the data hierarchy (will attach to source dataset in hierarchy if not valid)
            - **visible** – Whether the new dataset is visible in the data hierarchy
            - **notify** – Whether to notify the core that a dataset is added

        Returns:
        :   Smart pointer to the created subset

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html#_CPPv4I0EN2mv19AbstractDataManager25createSubsetFromSelectionE7DatasetI11DatasetTypeERK7DatasetI11DatasetImplERK7DatasetI11DatasetImplERK7QStringRK7DatasetI11DatasetImplERKbb "mv::AbstractDataManager::createSubsetFromSelection::DatasetType")> createSubsetFromSelection(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &selection, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &sourceDataset, const QString &guiName, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &parentDataset, const bool &visible = true, bool notify = true)
    :   Creates a copy of `selection` with the `sourceDataset`, adds it to the manager and returns the created subset as `DatasetType`.

        Parameters:
        :   - **selection** – Smart pointer to the selection set
            - **sourceDataset** – Smart pointer to the source dataset
            - **guiName** – GUI name of the subset
            - **parentDataset** – Smart pointer to the parent dataset in the data hierarchy (will attach to source dataset in hierarchy if not valid)
            - **visible** – Whether the new dataset is visible in the data hierarchy
            - **notify** – Whether to notify the core that a dataset is added

        Returns:
        :   Smart pointer to the created subset of `DatasetType`

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getDataset(const QString &datasetId) = 0
    :   Get dataset by `datasetId`.

        Parameters:
        :   **datasetId** – Globally unique identifier of the dataset

        Returns:
        :   Smart pointer to the dataset

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html#_CPPv4I0EN2mv19AbstractDataManager10getDatasetE7DatasetI11DatasetTypeERK7QString "mv::AbstractDataManager::getDataset::DatasetType")> getDataset(const QString &datasetId)
    :   Get dataset by `datasetId` as `DatasetType`.

        Parameters:
        :   **datasetId** – Globally unique identifier of the dataset

        Returns:
        :   Smart pointer to the dataset of `DatasetType`

    virtual Datasets getAllDatasets(const std::vector<[DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType")> &dataTypes = std::vector<[DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType")>()) const = 0
    :   Get all datasets for `dataTypes`.

        Parameters:
        :   **dataTypes** – Data types filter (if empty returns all types)

        Returns:
        :   Smart pointers to datasets

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getSelection(const QString &rawDataName) = 0
    :   Get selection dataset by `rawDataName`.

        Parameters:
        :   **rawDataName** – Name of the raw data

        Returns:
        :   Smart pointer to the selection dataset

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html#_CPPv4I0EN2mv19AbstractDataManager12getSelectionE7DatasetI11DatasetTypeERK7QString "mv::AbstractDataManager::getSelection::DatasetType")> getSelection(const QString &rawDataName)
    :   Get a selection of `DatasetType` by `rawDataName`.

        Parameters:
        :   **rawdataName** – Name of the raw data

        Returns:
        :   Smart pointer to the selection dataset

    virtual Datasets getAllSelections() = 0
    :   Get all selection datasets.

        Returns:
        :   Smart pointers to selection datasets

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> groupDatasets(const Datasets &datasets, const QString &guiName = "") = 0
    :   Groups `datasets` into one dataset and returns the group dataset.

        Parameters:
        :   - **datasets** – Two or more datasets to group
            - **guiName** – Name of the created dataset in the GUI (if empty, the user will be prompted for a name)

        Returns:
        :   Smart pointer to created group dataset

    virtual gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \*getSelectionGroupingAction() = 0
    :   Get selection grouping setEnabled action.

        Returns:
        :   Pointer to selection grouping toggle action (only valid if there is a current project)

    virtual const [DatasetsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/datasets_list_model.html#_CPPv4N2mv17DatasetsListModelE "mv::DatasetsListModel") &getDatasetsListModel() const = 0
    :   Get datasets list model.

        Returns:
        :   Reference to datasets list model

    virtual void linkFilterModelToDatasetsListModel(QSortFilterProxyModel \*filterModel) = 0
    :   Link `filterModel` to the datasets list model.

        Parameters:
        :   **filterModel** – Pointer to filter model

    void rawDataAdded(plugin::[RawData](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data.html#_CPPv4N2mv6plugin7RawDataE "mv::plugin::RawData") \*rawData)
    :   Signals that `rawData` is added to the data manager.

        Parameters:
        :   **rawData** – Pointer to raw data that was added

    void rawDataAboutToBeRemoved(plugin::[RawData](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data.html#_CPPv4N2mv6plugin7RawDataE "mv::plugin::RawData") \*rawData)
    :   Signals that `rawData` is about to be removed from the data manager.

        Parameters:
        :   **rawData** – Pointer to raw data that is about to be removed

    void rawDataRemoved(const QString &rawDataId)
    :   Signals that raw data with `rawDataId` is removed from the data manager.

        Parameters:
        :   **rawData** – Pointer to raw data that was added

    void datasetAdded([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> parentDataset, bool visible = true)
    :   Signals that `dataset` is added to the data manager.

        Parameters:
        :   - **dataset** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) that was added
            - **parentDataset** – Parent dataset (if any)
            - **visible** – Whether `dataset` should be visible or not

    void datasetAboutToBeRemoved([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
    :   Signals that `dataset` is about to be removed from the data manager.

        Parameters:
        :   **dataset** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) which is about to be removed

    void datasetRemoved(const QString &datasetId)
    :   Signals that dataset with `datasetId` is removed from the data manager.

        Parameters:
        :   **datasetId** – GUID of the removed dataset

    void selectionAdded([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> selection)
    :   Signals that `selection` dataset is added to the data manager.

        Parameters:
        :   **selection** – [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) dataset that was added

    void selectionAboutToBeRemoved([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> selection)
    :   Signals that `selection` dataset is about to be removed from the data manager.

        Parameters:
        :   **selection** – [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) dataset that is about to be removed

    void selectionRemoved(const QString &selectionId)
    :   Signals that selection dataset with `selectionId` is removed from the data manager.

        Parameters:
        :   **selectionId** – GUID of the removed selection dataset

    Protected Functions

    virtual void addRawData(plugin::[RawData](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data.html#_CPPv4N2mv6plugin7RawDataE "mv::plugin::RawData") \*rawData) = 0
    :   Add `rawData` to the manager (plugin manager remains the owner)

        Parameters:
        :   **rawData** – Pointer to the raw data to add

    virtual void removeRawData(const QString &rawDataName) = 0
    :   Remove raw data with `rawDataName` from the manager if there are no more (selection) datasets referencing it.

        Parameters:
        :   **rawDataName** – Name of the raw data to remove

    virtual plugin::[RawData](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data.html#_CPPv4N2mv6plugin7RawDataE "mv::plugin::RawData") \*getRawData(const QString &rawDataName) = 0
    :   Get raw data by `rawDataName`.

        Parameters:
        :   **rawDataName** – Name of the raw data

        Returns:
        :   Pointer to raw data if found, nullptr otherwise

    template<typename RawDataType> inline [RawDataType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html#_CPPv4I0EN2mv19AbstractDataManager10getRawDataEP11RawDataTypeRK7QString "mv::AbstractDataManager::getRawData::RawDataType") \*getRawData(const QString &rawDataName)
    :   Get raw data by `rawDataName`.

        Parameters:
        :   **rawDataName** – Name of the raw data

        Returns:
        :   Pointer of `RawDataType` to raw data if found, nullptr otherwise

    virtual void addDataset([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> parentDataset, bool notify = true) = 0
    :   Adds `dataset` to the manager.

        Parameters:
        :   - **dataset** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) to added
            - **parentDataset** – Parent dataset (if any)
            - **notify** – Whether to notify the core that a dataset is added

    virtual void addSelection(const QString &rawDataName, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> selection) = 0
    :   Add `selection` on `rawDataName` to the manager.

        Parameters:
        :   - **rawDataName** – Name of the raw data
            - **selection** – Smart pointer to selection dataset

    virtual void removeSelection(const QString &rawDataName) = 0
    :   Removes selection of which the raw data name matches `rawDataName`.

        Parameters:
        :   **rawDataName** – Name of the raw data
