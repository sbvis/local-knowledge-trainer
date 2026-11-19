# Event types

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html

**Documentation path:** `api/core/data/events/event_types.html`

---

# Event types

`EventType` identifies dataset lifecycle and change events. The concrete event classes carry the dataset handle or stable removal information appropriate to each phase.

For a compact payload table and casting example, see [Event types and payloads](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/events/event_types.html).

enum class mv::EventType
:   *Values:*

    enumerator DatasetAdded

    enumerator DatasetDataChanged

    enumerator DatasetDataDimensionsChanged

    enumerator DatasetAboutToBeRemoved

    enumerator DatasetRemoved

    enumerator DatasetDataSelectionChanged

    enumerator DatasetChildAdded

    enumerator DatasetChildRemoved

    enumerator DatasetLocked

    enumerator DatasetUnlocked

class ManiVaultEvent
:   Subclassed by [mv::DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetEvent), mv::DatasetGroupingEvent

class DatasetEvent : public mv::[ManiVaultEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv14ManiVaultEventE "mv::ManiVaultEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event class Event container class for datasets.

    Subclassed by [mv::DatasetAboutToBeRemovedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetAboutToBeRemovedEvent), [mv::DatasetAddedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetAddedEvent), [mv::DatasetChildAddedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetChildAddedEvent), [mv::DatasetChildRemovedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetChildRemovedEvent), [mv::DatasetDataChangedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetDataChangedEvent), [mv::DatasetDataDimensionsChangedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetDataDimensionsChangedEvent), [mv::DatasetDataSelectionChangedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetDataSelectionChangedEvent), [mv::DatasetLockedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetLockedEvent), [mv::DatasetRemovedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetRemovedEvent), [mv::DatasetUnlockedEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#classmv_1_1DatasetUnlockedEvent)

    Public Functions

    inline DatasetEvent(const [EventType](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv9EventTypeE "mv::EventType") &eventType, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Constructor.

        Parameters:
        :   - **eventType** – Type of event
            - **dataset** – Smart pointer to the dataset

    inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getDataset()
    :   Get reference to the dataset.

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4I0EN2mv12DatasetEvent10getDatasetE7DatasetI11DatasetTypeEv "mv::DatasetEvent::getDataset::DatasetType")> getDataset()
    :   Get reference to the dataset.

    inline void setDataset(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Set reference to the dataset.

        Parameters:
        :   **dataset** – Reference to the dataset

class DatasetAddedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) added event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when data is added.

    Public Functions

    inline DatasetAddedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Constructor.

        Parameters:
        :   **dataset** – Smart pointer to the dataset

    inline QString getParentDatasetName() const
    :   Get the name of the parent dataset.

    inline void setParentDatasetName(const QString &parentDatasetName)
    :   Set the name of the parent dataset.

        Parameters:
        :   **parentDatasetName** – Name of the parent dataset

    inline bool getVisible() const
    :   Get whether the dataset is visible in the data hierarchy.

    inline void setVisible(const bool &visible)
    :   Set whether the dataset is visible in the data hierarchy.

        Parameters:
        :   **visible** – Whether the dataset is visible in the data hierarchy

class DatasetDataChangedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) data changed event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when dataset data has changed.

    Public Functions

    inline DatasetDataChangedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Constructor.

        Parameters:
        :   **dataset** – Smart pointer to the dataset

class DatasetDataDimensionsChangedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) data dimensions changed event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when dataset data dimensions change.

    Public Functions

    inline DatasetDataDimensionsChangedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Constructor.

        Parameters:
        :   **dataset** – Smart pointer to the dataset

class DatasetDataSelectionChangedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) data selection changed event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when dataset data selection has changed.

    Public Functions

    inline DatasetDataSelectionChangedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Constructor.

        Parameters:
        :   **dataset** – Smart pointer to the dataset

class DatasetAboutToBeRemovedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) about to be removed event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when a dataset is about to be removed.

    Public Functions

    inline DatasetAboutToBeRemovedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Constructor.

        Parameters:
        :   **dataset** – Smart pointer to dataset

class DatasetRemovedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) removed event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when a dataset has been removed.

    Public Functions

    inline DatasetRemovedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset, const QString &datasetGuid, const [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") &dataType)
    :   Constructor.

        Parameters:
        :   - **dataset** – Smart pointer to the dataset
            - **datasetGuid** – GUID of the dataset that has been removed

    inline QString getDatasetGuid() const
    :   Get the GUID of the dataset that has been removed.

    inline [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") getDataType() const
    :   Get the data type of the dataset that has been removed.

class DatasetChildAddedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) child added event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when a child dataset is added to the dataset.

    Public Functions

    inline DatasetChildAddedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &childDataset)
    :   Constructor.

        Parameters:
        :   - **dataset** – Smart pointer to the dataset
            - **childDataset** – Smart pointer to the child dataset

    inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getChildDataset() const
    :   Get smart pointer to the child dataset.

class DatasetChildRemovedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) child removed event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when a child dataset is removed from the dataset.

    Public Functions

    inline DatasetChildRemovedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset, const QString &childDatasetGuid)
    :   Constructor.

        Parameters:
        :   - **dataset** – Smart pointer to the dataset
            - **childDatasetGuid** – GUID of the child dataset

    inline QString getChildDatasetGuid() const
    :   Get GUID of the child dataset.

class DatasetLockedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) locked event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when a dataset became locked.

    Public Functions

    inline DatasetLockedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Constructor.

        Parameters:
        :   **dataset** – Smart pointer to the dataset

class DatasetUnlockedEvent : public mv::[DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) unlocked event class [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) event which is emitted by the core when a dataset became unlocked.

    Public Functions

    inline DatasetUnlockedEvent(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset)
    :   Constructor.

        Parameters:
        :   **dataset** – Smart pointer to the dataset
