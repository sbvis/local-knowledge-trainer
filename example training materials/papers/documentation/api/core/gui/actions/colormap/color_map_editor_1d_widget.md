# ColorMapEditor1DWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_widget.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_editor_1d_widget.html`

---

# ColorMapEditor1DWidget

**Qualified name:** `mv::gui::ColorMapEditor1DWidget`

class ColorMapEditor1DWidget : public QGraphicsView
:   Color map editor one-dimensional widget class.

    Widget class for drawing the one-dimensional color map editor

    **Author**
    :   Thomas Kroes and Mitchell M. de Boer

    Public Functions

    ColorMapEditor1DWidget(QWidget \*parent, [ColorMapEditor1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html#_CPPv4N2mv3gui22ColorMapEditor1DActionE "mv::gui::ColorMapEditor1DAction") &colorMapEditor1DAction)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **colorMapEditor1DAction** – Reference to one-dimensional color map editor action

    ~ColorMapEditor1DWidget()
    :   Destructor.

    void showEvent(QShowEvent \*event) override
    :   Invoked when the widget is shown.

        Parameters:
        :   **Pointer** – to show event

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Respond to target object events.

        Parameters:
        :   - **target** – Object of which an event occurred
            - **event** – The event that took place

    void addNodeAtScenePosition(const QPointF &scenePosition)
    :   Add node at a specific scene position.

        Parameters:
        :   **scenePosition** – Position in scene coordinates

    void addNodeGraphicsItem([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node)
    :   Add node graphics item to the scene.

        Parameters:
        :   **node** – Pointer to node

    void removeNodeGraphicsItem([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node)
    :   Remove node graphics item.

        Parameters:
        :   **node** – pointer to node to remove

    void drawBackground(QPainter \*painter, const QRectF &rect) override
    :   Draws the editor background elements (axes etc.)

        Parameters:
        :   - **painter** – Pointer to painter
            - **rect** – Background rectangle

    QImage getColorMap()
    :   Get the color map.

        Returns:
        :   Color map image

    void selectNode([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node)
    :   Select a single node.

        Parameters:
        :   **node** – Pointer to a node

    QVector<[ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode")\*> &getNodes()
    :   Get nodes.

        Returns:
        :   Nodes

    const QVector<[ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode")\*> &getNodes() const
    :   Get nodes.

        Returns:
        :   Nodes

    [ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*getCurrentNode()
    :   Get current node (if one is selected)

        Returns:
        :   Pointer to current node (if any)

    QRectF getGraphRectangle() const
    :   Get graph rectangle (in which the nodes reside)

        Returns:
        :   Graph rectangle

    void colorMapChanged(const QImage &colorMap)
    :   Current color map.

        Signals that the color map changed

        Parameters:
        :   **colorMap** – Reference to color map

    void currentNodeChanged([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*currentNode)
    :   Signals that the current node changed.

        Parameters:
        :   **currentNode** – Pointer to the current node
