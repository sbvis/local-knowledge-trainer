# AbstractEventManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_event_manager.html

**Documentation path:** `api/core/managers/abstract_event_manager.html`

---

# AbstractEventManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the event manager
mv::events()->...
```

**Qualified name:** `mv::AbstractEventManager`

class AbstractEventManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract event manager.

    Base abstract event manager class for managing events.

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractEventManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void notifyDatasetAdded(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset) = 0
    :   Notify listeners that a new dataset has been added to the core.

        Parameters:
        :   **dataset** – Smart pointer to the dataset that was added

    virtual void notifyDatasetAboutToBeRemoved(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset) = 0
    :   Notify listeners that a dataset is about to be removed.

        Parameters:
        :   **dataset** – Smart pointer to the dataset which is about to be removed

    virtual void notifyDatasetRemoved(const QString &datasetGuid, const [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") &dataType) = 0
    :   Notify listeners that a dataset is removed.

        Parameters:
        :   - **datasetGuid** – GUID of the dataset that was removed
            - **dataType** – Type of the data

    virtual void notifyDatasetDataChanged(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset) = 0
    :   Notify listeners that a dataset has changed data.

        Parameters:
        :   **dataset** – Smart pointer to the dataset of which the data changed

    virtual void notifyDatasetDataDimensionsChanged(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset) = 0
    :   Notify listeners that a dataset has changed data dimensions.

        Parameters:
        :   **dataset** – Smart pointer to the dataset of which the data dimensions changed

    virtual void notifyDatasetDataSelectionChanged(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset, Datasets \*ignoreDatasets = nullptr) = 0
    :   Notify listeners that dataset data selection has changed.

        Parameters:
        :   - **dataset** – Smart pointer to the dataset of which the data selection changed
            - **ignoreDatasets** – Pointer to datasets that should be ignored during notification

    virtual void notifyDatasetLocked(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset) = 0
    :   Notify all listeners that a dataset is locked.

        Parameters:
        :   **dataset** – Smart pointer to the dataset

    virtual void notifyDatasetUnlocked(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &dataset) = 0
    :   Notify all listeners that a dataset is unlocked.

        Parameters:
        :   **dataset** – Smart pointer to the dataset

    virtual void registerEventListener([EventListener](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_listener.html#_CPPv4N2mv13EventListenerE "mv::EventListener") \*eventListener) = 0
    :   Register an event listener.

        Parameters:
        :   **eventListener** – Pointer to event listener to register

    virtual void unregisterEventListener([EventListener](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_listener.html#_CPPv4N2mv13EventListenerE "mv::EventListener") \*eventListener) = 0
    :   Unregister an event listener.

        Parameters:
        :   **eventListener** – Pointer to event listener to unregister

    Protected Functions

    inline void callListenerDataEvent([EventListener](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_listener.html#_CPPv4N2mv13EventListenerE "mv::EventListener") \*eventListener, [DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent") \*dataEvent)
    :   Calls `dataEvent` of the `eventListener`.

        Parameters:
        :   - **eventListener** – Pointer to event listener
            - **dataEvent** – Pointer to data event
