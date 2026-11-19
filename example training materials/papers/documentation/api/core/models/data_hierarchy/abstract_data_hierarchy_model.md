# Abstract data hierarchy model

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html

**Documentation path:** `api/core/models/data_hierarchy/abstract_data_hierarchy_model.html`

---

# Abstract data hierarchy model

`AbstractDataHierarchyModel` provides the shared roles, columns, item access, and synchronization used by concrete hierarchy models.

class AbstractDataHierarchyModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Abstract data hierarchy model class.

    Abstract standard item model class for managing the data hierarchy

    **Author**
    :   Thomas Kroes

    Subclassed by mv::DataHierarchyListModel, [mv::DataHierarchyTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/data_hierarchy_tree_model.html#classmv_1_1DataHierarchyTreeModel)

    Public Types

    enum Column
    :   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) columns.

        *Values:*

        enumerator Name

        enumerator Location
        :   Name of the dataset.

        enumerator DatasetId
        :   Location of the dataset.

        enumerator RawDataName
        :   Globally unique dataset identifier.

        enumerator RawDataSize
        :   Name of the raw data.

        enumerator SourceDatasetId
        :   Size of the raw data.

        enumerator Progress
        :   Globally unique dataset identifier of the source dataset (if this dataset is derived)

        enumerator SelectionGroupIndex
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) progress in percentage.

        enumerator IsVisible
        :   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) selection group index.

        enumerator IsGroup
        :   Whether the dataset is visible or not.

        enumerator IsDerived
        :   Whether the dataset is composed of other datasets.

        enumerator IsSubset
        :   Whether the dataset is derived from another dataset.

        enumerator IsLocked
        :   Whether the dataset is a subset or not.

        enumerator Count
        :   Whether the dataset is locked.

    Public Functions

    explicit AbstractDataHierarchyModel(QObject \*parent = nullptr)
    :   Construct with `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    Qt::DropActions supportedDragActions() const override
    :   Get supported drag actions.

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    QMimeData \*mimeData(const QModelIndexList &indexes) const override
    :   Get MIME data for supplied `indexes`.

        Parameters:
        :   **indexes** – Index list to get the MIME data for

        Returns:
        :   Pointer to MIME data

    template<typename ItemType = [Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")> inline [ItemType](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4I0EN2mv26AbstractDataHierarchyModel7getItemEP8ItemTypeRK11QModelIndex "mv::AbstractDataHierarchyModel::getItem::ItemType") \*getItem(const QModelIndex &modelIndex)
    :   Get item of `ItemType` by `modelIndex`.

        Parameters:
        :   **modelIndex** – [Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1Item) model index

        Returns:
        :   Pointer to item

    QModelIndex getModelIndex(const QString &datasetId, [Column](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel6ColumnE "mv::AbstractDataHierarchyModel::Column") column = [Column](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel6ColumnE "mv::AbstractDataHierarchyModel::Column")::[Name](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel6Column4NameE "mv::AbstractDataHierarchyModel::Column::Name")) const
    :   Get model index for `datasetId` and `column`.

        Parameters:
        :   - **datasetId** – Globally unique identifier to search for
            - **column** – Model index column return Model index (invalid if not found)

    void hideItem(const QModelIndex &index)
    :   Hides item with `index` and its descendants.

        Parameters:
        :   **index** – Index of the item to hide (column index must be zero)

    void unhideItem(const QModelIndex &index)
    :   Un-hides item with `index`.

        Parameters:
        :   **index** – Index of the item to un-hide (column index must be zero)

    class DatasetIdItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying the dataset identifier.

        Public Functions

        DatasetIdItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IsDerivedItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying whether the dataset is derived from another dataset.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, bool editable = false)
        :   Use base item constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IsGroupItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying whether the dataset belongs to a group.

        Public Functions

        IsGroupItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IsLockedItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying whether the dataset is locked.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, bool editable = false)
        :   Use base item constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IsSubsetItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying whether the dataset is a subset of another dataset.

        Public Functions

        IsSubsetItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IsVisibleItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying whether the dataset is visible or not.

        Public Functions

        IsVisibleItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Item : public QStandardItem, public QObject
    :   Base standard model item class for dataset.

        Subclassed by [mv::AbstractDataHierarchyModel::DatasetIdItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1DatasetIdItem), [mv::AbstractDataHierarchyModel::IsDerivedItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1IsDerivedItem), [mv::AbstractDataHierarchyModel::IsGroupItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1IsGroupItem), [mv::AbstractDataHierarchyModel::IsLockedItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1IsLockedItem), [mv::AbstractDataHierarchyModel::IsSubsetItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1IsSubsetItem), [mv::AbstractDataHierarchyModel::IsVisibleItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1IsVisibleItem), [mv::AbstractDataHierarchyModel::LocationItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1LocationItem), [mv::AbstractDataHierarchyModel::NameItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1NameItem), [mv::AbstractDataHierarchyModel::ProgressItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1ProgressItem), [mv::AbstractDataHierarchyModel::RawDataNameItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1RawDataNameItem), [mv::AbstractDataHierarchyModel::RawDataSizeItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1RawDataSizeItem), [mv::AbstractDataHierarchyModel::SelectionGroupIndexItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1SelectionGroupIndexItem), [mv::AbstractDataHierarchyModel::SourceDatasetIdItem](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel_1_1SourceDatasetIdItem)

        Public Functions

        Item([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, bool editable = false)
        :   Construct with `dataset`.

            Parameters:
            :   - **dataset** – Pointer to dataset to display item for
                - **editable** – Whether the model item is editable or not

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &getDataset()
        :   Get dataset return [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) to display item for.

        const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &getDataset() const
        :   Get dataset return [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) to display item for.

        inline void refreshData()
        :   Refreshes the data display.

    class LocationItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for showing the dataset location.

        Public Functions

        LocationItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class NameItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for interacting with the dataset name.

        Public Functions

        NameItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class ProgressItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying the dataset task progress.

        Public Functions

        ProgressItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        inline [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") &getDatasetTask()
        :   Get dataset task.

            Returns:
            :   Reference to dataset task

        inline gui::[TaskAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/task_action.html#_CPPv4N2mv3gui10TaskActionE "mv::gui::TaskAction") &getTaskAction()
        :   Get task action.

            Returns:
            :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) action for use in item delegate (its built-in progress action)

        QWidget \*createDelegateEditorWidget(QWidget \*parent)
        :   Create delegate editor widget as child of `parent`.

            Parameters:
            :   **parent** – Pointer to delegate parent

            Returns:
            :   Pointer to created delegate editor widget

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class RawDataNameItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying the raw data name.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, bool editable = false)
        :   Use base item constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class RawDataSizeItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying the raw data size.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, bool editable = false)
        :   Use base item constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining dataset items in a row.

        Public Functions

        inline Row([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

    class SelectionGroupIndexItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying the selection group index.

        Public Functions

        SelectionGroupIndexItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class SourceDatasetIdItem : public mv::[AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModelE "mv::AbstractDataHierarchyModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#_CPPv4N2mv26AbstractDataHierarchyModel4ItemE "mv::AbstractDataHierarchyModel::Item")
    :   Standard model item class for displaying the source dataset identifier.

        Public Functions

        SourceDatasetIdItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
        :   Construct with `dataset`.

            Parameters:
            :   **dataset** – Pointer to dataset to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
