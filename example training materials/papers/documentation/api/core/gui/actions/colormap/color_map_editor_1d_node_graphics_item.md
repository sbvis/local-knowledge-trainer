# ColorMapEditor1DNodeGraphicsItem

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node_graphics_item.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_editor_1d_node_graphics_item.html`

---

# ColorMapEditor1DNodeGraphicsItem

**Qualified name:** `mv::gui::ColorMapEditor1DNodeGraphicsItem`

class ColorMapEditor1DNodeGraphicsItem : public QObject, public QGraphicsItem
:   Color map editor one-dimensional node graphics item class.

    Graphics item for drawing a node in a graphics view

    **Author**
    :   Thomas Kroes and Mitchell M. de Boer

    Public Functions

    ColorMapEditor1DNodeGraphicsItem([ColorMapEditor1DWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_widget.html#_CPPv4N2mv3gui22ColorMapEditor1DWidgetE "mv::gui::ColorMapEditor1DWidget") &colorMapEditor1DWidget, [ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") &node)
    :   Constructor.

        Parameters:
        :   - **colorMapEditor1DWidget** – Reference to owning one-dimensional color map editor widget
            - **node** – Reference to source node

    [ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") &getNode()
    :   Get associated node.

        Returns:
        :   Reference to node

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Respond to target object events.

        Parameters:
        :   - **target** – Object of which an event occurred
            - **event** – The event that took place

    QRectF boundingRect() const override
    :   Get the node bounding rectangle.

        Returns:
        :   Bounding rectangle

    QPainterPath shape() const override
    :   Get node shape.

        Returns:
        :   Shape as a painter path

    void paint(QPainter \*painter, const QStyleOptionGraphicsItem \*option, QWidget \*widget) override
    :   Paint the node.

        Parameters:
        :   - **painter** – Pointer to painter
            - **option** – Pointer to graphics item style options
            - **widget** – Pointer to widget

    void pressed(QGraphicsSceneMouseEvent \*event)
    :   Invoked when the node is pressed.

        Parameters:
        :   **event** – Pointer to graphics mouse event

    [ColorMapEditor1DWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_widget.html#_CPPv4N2mv3gui22ColorMapEditor1DWidgetE "mv::gui::ColorMapEditor1DWidget") &getColorMapEditor1DWidget()
    :   Get the one-dimensional color map editor widget.

        Returns:
        :   Reference to one-dimensional color map editor widget

    void colorChanged(const QColor &color)
    :   Signals that the node color changed.

        Parameters:
        :   **color** – Node color

    void normalizedCoordinateChanged(const QPointF &normalizedCoordinate)
    :   Signals that the normalized node coordinates changed.

        Parameters:
        :   **normalizedCoordinate** – Normalized coordinate

    Protected Functions

    void mousePressEvent(QGraphicsSceneMouseEvent \*event) override
    :   Invoked when the mouse presses the node.

        Parameters:
        :   **event** – Pointer to graphics scene mouse event

    void mouseMoveEvent(QGraphicsSceneMouseEvent \*event) override
    :   Invoked when the mouse moves over the node.

        Parameters:
        :   **event** – Pointer to graphics scene mouse event

    void mouseReleaseEvent(QGraphicsSceneMouseEvent \*event) override
    :   Invoked when the mouse button releases.

        Parameters:
        :   **event** – Pointer to graphics scene mouse event

    void hoverEnterEvent(QGraphicsSceneHoverEvent \*event) override
    :   Invoked when the mouse starts to hover over the node.

        Parameters:
        :   **event** – Pointer to graphics scene hover event

    void hoverLeaveEvent(QGraphicsSceneHoverEvent \*event) override
    :   Invoked when the mouse leaves the node after hovering.

        Parameters:
        :   **event** – Pointer to graphics scene hover event
