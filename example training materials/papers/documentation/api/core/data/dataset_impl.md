# Dataset implementation

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html

**Documentation path:** `api/core/data/dataset_impl.html`

---

# Dataset implementation

`DatasetImpl` is the polymorphic base for concrete dataset implementations. It defines common metadata, hierarchy, source and subset relationships, selections, locking, properties, grouping, linked data, tasks, and serialization behavior.

class DatasetImpl : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) implementation class Base dataset class from which concrete dataset classes derive.

    Subclassed by Clusters, Colors, Images, Points, Text

    Public Types

    enum class StorageType
    :   Type of storage.

        *Values:*

        enumerator Owner

        enumerator Proxy
        :   The set is the data owner (has raw data)

            The set does not have raw data, it relies on proxy datasets to obtain data

    enum LinkedDataFlag
    :   Linked data propagation flags.

        *Values:*

        enumerator Send

        enumerator Receive
        :   The set may send linked propagate linked data.

        enumerator SendReceive
        :   The set may receive linked data.

    Public Functions

    explicit DatasetImpl(const QString &rawDataName, bool mayUnderive = true, const QString &id = "")
    :   Construct with `rawDataName` and possibly initialize with `id`.

        Parameters:
        :   - **rawDataName** – Name of the raw data
            - **mayUnderive** – Whether the dataset may be un-derived, if not it should always co-exist with its source
            - **id** – Globally unique dataset identifier, if empty an new ID will be generated

    ~DatasetImpl() override
    :   Destructor.

    virtual void init()
    :   Performs startup initialization.

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> copy() const = 0
    :   Get a copy of the dataset.

        Returns:
        :   Smart pointer to copy of dataset

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> createSubsetFromSelection(const QString &guiName, const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &parentDataSet = [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>(), const bool &visible = true) const = 0
    :   Create subset from the current selection and specify where the subset will be placed in the data hierarchy.

        Parameters:
        :   - **guiName** – Name of the subset in the GUI
            - **parentDataSet** – Smart pointer to parent dataset in the data hierarchy (default is below the set)
            - **visible** – Whether the subset will be visible in the UI

        Returns:
        :   Smart pointer to the created subset

    [StorageType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImpl11StorageTypeE "mv::DatasetImpl::StorageType") getStorageType() const
    :   Get the data storage type.

        Returns:
        :   Data storage type

    void setStorageType(const [StorageType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImpl11StorageTypeE "mv::DatasetImpl::StorageType") &storageType)
    :   Set the data storage type.

        Parameters:
        :   **type** – Data storage type

    QString getGuiName() const
    :   Get the GUI name of the dataset.

    void setGuiName(const QString &guiName)
    :   Set gui name to `guiName`.

        Parameters:
        :   **guiName** – GUI name

    bool isFull() const
    :   Returns true if this set represents the full data and false if it’s a subset.

    bool isDerivedData() const
    :   Returns whether the dataset is derived.

    bool mayUnderive() const
    :   Returns whether the dataset may be un-derived, if not it should always co-exist with its source.

    [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") getDataType() const
    :   Returns the data type of the raw data associated with this dataset.

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4I0ENK2mv11DatasetImpl16getSourceDatasetE7DatasetI11DatasetTypeEv "mv::DatasetImpl::getSourceDataset::DatasetType")> getSourceDataset() const
    :   Get source dataset if the given set is derived.

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4I0ENK2mv11DatasetImpl20getNextSourceDatasetE7DatasetI11DatasetTypeEv "mv::DatasetImpl::getNextSourceDataset::DatasetType")> getNextSourceDataset() const
    :   Get source dataset if the given set is derived.

    void setSourceDataset([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
    :   Marks this dataset as derived and sets the source dataset to `dataset`.

        Parameters:
        :   **dataset** – Smart pointer to the source dataset

    void setSourceDataset(const QString &datasetId)
    :   Marks this dataset as derived and sets the source dataset globally unique identifier to `datasetId` Note: use this when the source dataset itself is not physically available but can be lazily obtained later.

        Parameters:
        :   **datasetId** – Globally unique identifier of the source dataset

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4I0ENK2mv11DatasetImpl14getFullDatasetE7DatasetI11DatasetTypeEv "mv::DatasetImpl::getFullDataset::DatasetType")> getFullDataset() const
    :   Returns the original full dataset this subset was created from.

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getSelection() const
    :   Gets the selection associated with this data set.

        If the data set is derived then the selection of the source data will be returned. Otherwise, the selection of the set’s data will be returned.

        Returns:
        :   The selection associated with this data set

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4I0ENK2mv11DatasetImpl12getSelectionE7DatasetI11DatasetTypeEv "mv::DatasetImpl::getSelection::DatasetType")> getSelection() const
    :   Gets the selection associated with this data set.

        If the data set is derived then the selection of the source data will be returned. Otherwise, the selection of the set’s data will be returned.

        Returns:
        :   The selection of dataset type associated with this data set

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &getSmartPointer()
    :   Get reference to smart pointer which is owned by the set.

        Returns:
        :   Reference to smart pointer which is owned by the set

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> toSmartPointer() const
    :   Get smart pointer to set.

        Returns:
        :   Smart pointer to the set

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4I0ENK2mv11DatasetImpl14toSmartPointerE7DatasetI11DatasetTypeEv "mv::DatasetImpl::toSmartPointer::DatasetType")> toSmartPointer() const
    :   Get smart pointer to set.

        Returns:
        :   Smart pointer to the set

    void makeSubsetOf([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> fullDataset)
    :   Makes this set a subset of a full dataset.

        Parameters:
        :   **fullDataset** – Smart pointer to full dataset

    QString getRawDataKind() const
    :   Get plugin kind of the raw data.

        Returns:
        :   Plugin kind of the raw data

    virtual std::uint64\_t getRawDataSize() const
    :   Get amount of data occupied by the raw data.

        Returns:
        :   Size of the raw data in bytes

    QString getRawDataSizeHumanReadable() const
    :   Get amount of data occupied by the raw data in human readable string format.

        Returns:
        :   Size of the raw data in bytes in human readable string format

    virtual QString getLocation(bool recompute = false) const override
    :   Get location.

        Returns:
        :   Path relative to the top-level action

    [DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") &getDataHierarchyItem()
    :   Get reference to data hierarchy item.

    const [DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") &getDataHierarchyItem() const
    :   Get reference to data hierarchy item.

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getParent() const
    :   Get parent dataset (if any)

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4I0ENK2mv11DatasetImpl9getParentE7DatasetI11DatasetTypeEv "mv::DatasetImpl::getParent::DatasetType")> getParent() const
    :   Get parent dataset (if any)

    QVector<[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>> getChildren(const QVector<[DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType")> &dataTypes = QVector<[DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType")>(), bool recursively = true) const
    :   Get child datasets (if any) of the specified type(s)

        Parameters:
        :   - **dataTypes** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) type(s) to filter out (no filtering if `dataTypes` is empty)
            - **recursively** – Whether to collect children recursively

        Returns:
        :   Child datasets of the dataset type(s)

    QVector<[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")>> getChildren(const [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") &filterDataType) const
    :   Get child datasets (if any) of the specified type.

        Parameters:
        :   **filterDataType** – Type of data to filter

        Returns:
        :   Child datasets of the dataset type

    virtual std::vector<std::uint32\_t> &getSelectionIndices() = 0
    :   Get selection indices.

        Returns:
        :   [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) indices

    virtual void setSelectionIndices(const std::vector<std::uint32\_t> &indices) = 0
    :   Select by indices.

        Parameters:
        :   **indices** – [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) indices

    std::int32\_t getSelectionSize() const
    :   Get size of the selection.

    virtual bool canSelect() const = 0
    :   Determines whether items can be selected.

    virtual bool canSelectAll() const = 0
    :   Determines whether all items can be selected.

    virtual bool canSelectNone() const = 0
    :   Determines whether there are any items which can be deselected.

    virtual bool canSelectInvert() const = 0
    :   Determines whether the item selection can be inverted (more than one)

    virtual void selectAll() = 0
    :   Select all items.

    virtual void selectNone() = 0
    :   De-select all items.

    virtual void selectInvert() = 0
    :   Invert item selection.

    void lock(bool cache = false)
    :   Lock the dataset and possibly `cache` the current lock state.

        Parameters:
        :   **cache** – Whether to cache the current lock state

    void unlock(bool cache = false)
    :   Unlock the dataset and possibly `cache` the current lock state.

        Parameters:
        :   **cache** – Whether to cache the current lock state

    bool isLocked() const
    :   Get whether the dataset is locked.

        Returns:
        :   Boolean indicating whether the dataset is locked

    void setLocked(bool locked, bool cache = false)
    :   Set whether the dataset is `locked` and possibly `cache` the current lock state.

        Parameters:
        :   - **locked** – Boolean indicating whether the dataset is locked
            - **cache** – Whether to cache the current lock state

    void restoreLockedFromCache()
    :   Restore the lock status to the cached value.

    QVariant getProperty(const QString &name, const QVariant &defaultValue = QVariant()) const
    :   Get property in variant form.

        Parameters:
        :   - **name** – Name of the property
            - **defaultValue** – Default value

        Returns:
        :   Property in variant form

    void setProperty(const QString &name, const QVariant &value)
    :   Set property.

        Parameters:
        :   - **name** – Name of the property
            - **value** – Property value

    bool hasProperty(const QString &name) const
    :   Determines whether a property with a give name exists.

        Parameters:
        :   - **name** – Name of the property
            - **value** – If property with the given name exists

    QStringList propertyNames() const
    :   Returns a list of available property names.

    void setAnalysis(plugin::[AnalysisPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html#_CPPv4N2mv6plugin14AnalysisPluginE "mv::plugin::AnalysisPlugin") \*analysis)
    :   Set analysis.

        Parameters:
        :   **analysis** – Pointer to analysis plugin

    plugin::[AnalysisPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html#_CPPv4N2mv6plugin14AnalysisPluginE "mv::plugin::AnalysisPlugin") \*getAnalysis()
    :   Get analysis.

        Returns:
        :   Pointer to analysis plugin

    virtual workflow::UniqueWorkflowPlan fromVariantMapWorkflow(QVariantMap variantMap) override
    :   Create a workflow that restores this object’s state from a variant map.

        See Serializable::fromVariantMapWorkflow() for the full contract, execution semantics, and implementation requirements.

        Parameters:
        :   **variantMap** – Serialized object state.

        Returns:
        :   Workflow plan that restores the object state when executed.

    virtual workflow::UniqueWorkflowPlan toVariantMapWorkflow() const override
    :   Create a workflow that serializes this object’s state to a variant map.

        See Serializable::toVariantMapWorkflow() for the full contract, execution semantics, and implementation requirements.

        Returns:
        :   Workflow plan that serializes the object state when executed.

    std::int32\_t getGroupIndex() const
    :   Get group index.

    void setGroupIndex(const std::int32\_t &groupIndex)
    :   Set group index.

        Parameters:
        :   **groupIndex** – group index

    Datasets getProxyMembers() const
    :   Get member datasets.

        Returns:
        :   Proxy member datasets

    virtual void setProxyMembers(const Datasets &proxyMembers)
    :   Set the proxy member datasets (automatically sets the dataset type to Type::Proxy)

        Parameters:
        :   **proxyMembers** – Proxy member datasets

    virtual bool mayProxy(const Datasets &proxyDatasets) const
    :   Establish whether a proxy dataset may be created with candidate `proxyDatasets`.

        Parameters:
        :   **proxyDatasets** – Candidate proxy datasets

        Returns:
        :   Boolean indicating whether a proxy dataset may be created with candidate `proxyDatasets`

    bool isProxy() const
    :   Establish whether the set is a proxy dataset (comprised of foreign datasets)

        Returns:
        :   Boolean indicating whether the set is a proxy dataset

    void addAction(mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") &widgetAction)
    :   Add `widgetAction` to the corresponding data hierarchy item.

        Parameters:
        :   **widgetAction** – Widget action to add

    mv::gui::WidgetActions getActions() const
    :   Get attached actions.

        Returns:
        :   List of widget actions

    virtual QMenu \*getContextMenu(QWidget \*parent = nullptr) override
    :   Get the context menu.

        Parameters:
        :   **parent** – Parent widget

        Returns:
        :   Context menu

    void populateContextMenu(QMenu \*contextMenu)
    :   Populates existing menu with actions menus.

        Parameters:
        :   **contextMenu** – Context menu to populate

    void removeAllLinkedData()
    :   Removes all mappings of global selection indices from this dataset.

    void removeLinkedDataset(const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &targetDataSet)
    :   Removes mappings of global selection indices from this dataset to a target dataset.

        Parameters:
        :   **targetDataSet** – The target dataset

    void removeLinkedDataMapping(const QString &mappingID)
    :   Removes a mapping from this dataset.

        Parameters:
        :   **mappingID** – unique identifier (as obtained with [getId()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a0ddf624829acac13a384d1bff05d8e53)) of to-be-removed mapping

    std::int32\_t getLinkedDataFlags() const
    :   Get flags for linked data.

        Returns:
        :   Flags for linked data

    void setLinkedDataFlags(std::int32\_t linkedDataFlags)
    :   Set flags for linked data.

        Parameters:
        :   **linkedDataFlags** – Flags for linked data

    void setLinkedDataFlag(std::int32\_t linkedDataFlag, bool set = true)
    :   Set linked data flag.

        Parameters:
        :   **linkedDataFlag** – Linked data

    bool hasLinkedDataFlag(std::int32\_t linkedDataFlag) const
    :   Determine whether `linkedDataFlag` is set or not.

        Parameters:
        :   **linkedDataFlag** – Linked data

        Returns:
        :   Boolean determining linkedDataFlag Linked data

    inline virtual void resolveLinkedData(bool force = false)
    :   Resolves linked data for the dataset.

        Parameters:
        :   **force** – Force update of all linked data (ignores linked data flags)

    QString getRawDataName() const
    :   Get the name of the raw data.

    [DatasetTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/dataset_task.html#_CPPv4N2mv11DatasetTaskE "mv::DatasetTask") &getTask()
    :   Get task.

        Returns:
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) for display in the data hierarchy and foreground

    void setAboutToBeRemoved(bool aboutToBeRemoved = true)
    :   Set about to be removed to `aboutToBeRemoved`.

        Parameters:
        :   **aboutToBeRemoved** – Boolean determining whether the set is in the process of being removed

    bool isAboutToBeRemoved() const
    :   Get whether the set is in the process of being removed.

        Returns:
        :   Boolean determining whether the set is in the process of being removed

    inline [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl") &operator=(const [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl") &other)
    :   Assignment operator.

        Parameters:
        :   **other** – Reference to assign from
