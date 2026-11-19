# DatasetsMimeData

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/datasets_mime_data.html

**Documentation path:** `api/core/data/datasets_mime_data.html`

---

# DatasetsMimeData

**Qualified name:** `mv::DatasetsMimeData`

`DatasetsMimeData` carries one or more ManiVault dataset handles through Qt drag-and-drop. Consumers can inspect the count or the handle collection before deciding which drop operations to offer.

For plugin-side validation and `DropWidget` examples, see [Dataset drag and drop](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/index.html).

class DatasetsMimeData : public QMimeData
:   Datasets mime data class.

    Class for drag-and-drop of one or more datasets

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit DatasetsMimeData(Datasets datasets)
    :   Construct with `datasets`.

        Parameters:
        :   **datasets** – Mime data datasets for dropping

    QStringList formats() const override
    :   Get supported mime types.

        Returns:
        :   List of string of supported mime types

    Datasets getDatasets() const
    :   Get stored datasets.

        Returns:
        :   Stored datasets

    const Datasets &getDatasetsRef() const
    :   Get stored datasets as a const reference.

        Returns:
        :   Stored datasets reference

    inline size\_t getDatasetsCount() const
    :   Get count of stored datasets.

        Returns:
        :   Datasets count

    Public Static Functions

    static QString format()
    :   Supported mime type.
