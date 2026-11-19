# SelectionsModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/selections/selections_model.html

**Documentation path:** `api/core/models/selections/selections_model.html`

---

# SelectionsModel

**Qualified name:** `mv::SelectionsModel`

class SelectionsModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Selections model class.

    Standard item model for listing selections

    **Author**
    :   Thomas Kroes

    Public Types

    enum Column
    :   [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) columns.

        *Values:*

        enumerator Name

        enumerator ID
        :   Name of the selection dataset.

        enumerator RawDataName
        :   Globally unique identifier of the selection dataset.

        enumerator RawDataType
        :   Name of the raw dataset on which the selection set is based.

        enumerator Count
        :   Type of the raw dataset on which the selection set is based.

    Public Functions

    explicit SelectionsModel(QObject \*parent = nullptr)
    :   Construct with `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    void populateFromDataManager()
    :   Populate the model with selections from the data manager.

    Protected Functions

    inline Qt::DropActions supportedDragActions() const override
    :   Get supported drag actions.

    inline Qt::DropActions supportedDropActions() const override
    :   Get the supported drop actions.

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining selection items in a row.

        Public Functions

        inline Row([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> selection)
        :   Construct with `selection`.

            Parameters:
            :   **selection** – Pointer to selection dataset to display item for
