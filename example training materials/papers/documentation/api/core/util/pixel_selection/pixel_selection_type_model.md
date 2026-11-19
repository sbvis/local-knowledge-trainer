# PixelSelectionTypeModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection_type_model.html

**Documentation path:** `api/core/util/pixel_selection/pixel_selection_type_model.html`

---

# PixelSelectionTypeModel

**Qualified name:** `mv::util::PixelSelectionTypeModel`

class PixelSelectionTypeModel : public QAbstractListModel
:   Pixel selection type model class.

    **Author**
    :   Thomas Kroes

    Public Functions

    PixelSelectionTypeModel(QObject \*parent = nullptr)
    :   Construct with `parent`.

        Parameters:
        :   **parent** – Pointer to parent object

    void setPixelSelectionTypes(const PixelSelectionTypes &pixelSelectionTypes)
    :   Set pixel selection types.

        Parameters:
        :   **pixelSelectionTypes** – Allowed pixel selection types

    int rowCount(const QModelIndex &parent = QModelIndex()) const
    :   Returns the number of pixel selection types in the model.

        Parameters:
        :   **parent** – Parent index

    int columnCount(const QModelIndex &parent = QModelIndex()) const
    :   Returns the the number of model columns.

        Parameters:
        :   **parent** – Parent index

    QVariant data(const QModelIndex &index, int role) const
    :   Returns model data for the given index.

        Parameters:
        :   - **index** – Index
            - **role** – The data role
