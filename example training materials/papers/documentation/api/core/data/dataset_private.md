# Dataset handle state

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/dataset_private.html

**Documentation path:** `api/core/data/dataset_private.html`

---

# Dataset handle state

`DatasetPrivate` stores the identity and observed implementation behind `Dataset<T>`. It listens to core dataset events and re-emits changes as Qt signals. Plugin code normally interacts with it through `Dataset<T>` rather than constructing it directly.

class DatasetPrivate : public QObject
:   Private shared state for [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) smart references.

    [DatasetPrivate](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_private.html#classmv_1_1DatasetPrivate) stores the dataset identifier and optional [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#classmv_1_1DatasetImpl) pointer shared by [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) reference wrappers. It listens for core dataset events and re-emits them as Qt signals so [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) users can observe changes without owning the dataset implementation.

    @maintainer T. Kroes

    Subclassed by [mv::Dataset< Points >](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset), [mv::Dataset< mv::DatasetImpl >](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset), [mv::Dataset< Images >](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset), [mv::Dataset< Text >](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset), [mv::Dataset< Clusters >](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset), [mv::Dataset< DatasetType >](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset)

    Public Functions

    QString getDatasetId() const
    :   Returns the globally unique identifier of the dataset.

    void setDatasetId(const QString &datasetId)
    :   Sets the globally unique identifier of the dataset.

        Parameters:
        :   **datasetId** – Globally unique identifier of the dataset.

    [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl") \*getDataset()
    :   Returns the dataset implementation pointer.

        Returns:
        :   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) implementation pointer, or nullptr.

    const [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl") \*getDataset() const
    :   Returns the dataset implementation pointer.

        Returns:
        :   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) implementation pointer, or nullptr.

    void setDataset([DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl") \*dataset)
    :   Sets the dataset implementation pointer.

        Parameters:
        :   **dataset** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) implementation pointer, or nullptr.

    void reset(bool notify = true)
    :   Resets the dataset pointer and disconnects from dataset events.

        Parameters:
        :   **notify** – Whether to notify listeners about the reset.

    void connectNotify(const QMetaMethod &signal) override
    :   Registers event listening when a signal gains a connection.

        Parameters:
        :   **signal** – Signal that received a connection.

    void disconnectNotify(const QMetaMethod &signal) override
    :   Updates event listening when a signal loses a connection.

        Parameters:
        :   **signal** – Signal that lost a connection.

    void changed([DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl") \*dataset)
    :   Emitted when the dataset pointer changes.

        Parameters:
        :   **dataset** – Current dataset pointer, or nullptr.

    void aboutToBeRemoved()
    :   Emitted before the dataset is removed.

    void removed(const QString &datasetId)
    :   Emitted after the dataset has been removed.

        Parameters:
        :   **datasetId** – Globally unique identifier of the removed dataset.

    void dataChanged()
    :   Emitted when dataset data changes.

    void dataDimensionsChanged()
    :   Emitted when dataset dimensions change.

    void dataSelectionChanged()
    :   Emitted when dataset selection changes.

    void guiNameChanged()
    :   Emitted when the dataset GUI name changes.

    void childAdded(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &childDataset)
    :   Emitted when a child dataset is added.

        Parameters:
        :   **childDataset** – Added child dataset.

    void childRemoved(const QString &childDatasetGuid)
    :   Emitted when a child dataset is removed.

        Parameters:
        :   **childDatasetGuid** – GUID of the removed child dataset.
