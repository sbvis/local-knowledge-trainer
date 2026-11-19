# ColorMapEditor1DNode

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_editor_1d_node.html`

---

# ColorMapEditor1DNode

**Qualified name:** `mv::gui::ColorMapEditor1DNode`

class ColorMapEditor1DNode : public QObject, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   Color map editor one-dimensional node class.

    Container class for one-dimension color map editor node settings

    **Author**
    :   Thomas Kroes and Mitchell M. de Boer

    Public Functions

    ColorMapEditor1DNode([ColorMapEditor1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html#_CPPv4N2mv3gui22ColorMapEditor1DActionE "mv::gui::ColorMapEditor1DAction") &colorMapEditor1DAction, const QPointF &normalizedCoordinate, const QColor &color = Qt::gray)
    :   Constructor.

        Parameters:
        :   - **colorMapEditor1DAction** – Reference to owning one-dimensional color map editor
            - **normalizedCoordinate** – Normalized node coordinates
            - **color** – Node color

    std::uint32\_t getIndex() const
    :   Get sorted node index.

        Returns:
        :   Sorted node index

    void setIndex(const std::uint32\_t &index)
    :   Set sorted node index.

        Parameters:
        :   **index** – Sorted node index

    QColor getColor() const
    :   Get node color.

        Returns:
        :   Node color

    void setColor(const QColor &color)
    :   Set node color.

        Parameters:
        :   **color** – Node color

    float getRadius() const
    :   Get node radius.

        Returns:
        :   Node radius

    void setRadius(const float &radius)
    :   Set node radius.

        Parameters:
        :   **radius** – Node radius

    QPointF getNormalizedCoordinate() const
    :   Get normalized node coordinates.

        Returns:
        :   Normalized node coordinates

    void setNormalizedCoordinate(const QPointF &normalizedCoordinate)
    :   Set normalized node coordinates.

        Returns:
        :   Normalized node coordinate

    QRectF getLimits() const
    :   Get movement limits.

        Returns:
        :   Limits rectangle

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void colorChanged(const QColor &color)
    :   Signals that the node color changed.

        Parameters:
        :   **color** – Node color

    void normalizedCoordinateChanged(const QPointF &normalizedCoordinate)
    :   Signals that the normalized node coordinates changed.

        Parameters:
        :   **normalizedCoordinate** – Normalized coordinate
