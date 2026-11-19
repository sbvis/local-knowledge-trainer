# ColorMapModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map_model.html

**Documentation path:** `api/core/util/color/color_map_model.html`

---

# ColorMapModel

**Qualified name:** `mv::util::ColorMapModel`

class ColorMapModel : public QAbstractListModel
:   Color map model class.

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Column
    :   Color map model columns Defines the color map model columns.

        *Values:*

        enumerator Preview

        enumerator Name
        :   Preview.

        enumerator Image
        :   Name column.

        enumerator NoDimensions
        :   Image column.

        enumerator ResourcePath
        :   Dimensionality.

        enumerator Start
        :   Resource path.

        enumerator End
        :   Column start.

    Public Functions

    int columnCount(const QModelIndex &parent) const override
    :   Returns the the number of model columns.

        Parameters:
        :   **parent** – Parent index

    int rowCount(const QModelIndex &parent) const override
    :   Returns the number of color maps in the model.

        Parameters:
        :   **parent** – Parent index

    QVariant data(const QModelIndex &index, int role) const override
    :   Returns model data for the given index.

        Parameters:
        :   - **index** – Index
            - **role** – The data role

    void setupModelData()
    :   Setups the model data (e.g.

        loads color maps from resources)

    const [ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap") \*getColorMap(const int &row) const
    :   Returns a color map given a row index.

        Parameters:
        :   **row** – Row index

    Protected Functions

    ColorMapModel(QObject \*parent = nullptr)
    :   Constructor.

        Parameters:
        :   **parent** – Parent object

    Protected Static Attributes

    static util::[ColorMapModel](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map_model.html#_CPPv4N2mv4util13ColorMapModelE "mv::util::ColorMapModel") \*globalInstance
    :   Color maps data.

        Globally available color map model instance
