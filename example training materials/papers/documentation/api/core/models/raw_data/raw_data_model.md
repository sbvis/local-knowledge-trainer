# RawDataModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/raw_data/raw_data_model.html

**Documentation path:** `api/core/models/raw_data/raw_data_model.html`

---

# RawDataModel

**Qualified name:** `mv::RawDataModel`

class RawDataModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Raw data model class.

    Standard item model for listing raw data

    **Author**
    :   Thomas Kroes

    Public Types

    enum Column
    :   Raw data columns.

        *Values:*

        enumerator Name

        enumerator Type
        :   Name of the raw data.

        enumerator Size
        :   Data type of the raw data.

        enumerator Count
        :   Size of the raw data.

    Public Functions

    explicit RawDataModel(QObject \*parent = nullptr)
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
    :   Populate the model with raw data from the data manager.

    Protected Functions

    inline Qt::DropActions supportedDragActions() const override
    :   Get supported drag actions.

    inline Qt::DropActions supportedDropActions() const override
    :   Get the supported drop actions.

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining raw data items in a row.

        Public Functions

        inline Row(const QString &rawDataName)
        :   Construct with `rawDataName`.

            Parameters:
            :   **rawDataName** – Name of the raw data
