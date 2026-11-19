# ColorMapEditor1DScene

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_scene.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_editor_1d_scene.html`

---

# ColorMapEditor1DScene

**Qualified name:** `mv::gui::ColorMapEditor1DScene`

class ColorMapEditor1DScene : public QGraphicsScene
:   Color map editor one-dimensional graphics scene class.

    Graphics scene class for drawing the one-dimensional color map editor

    **Author**
    :   Thomas Kroes and Mitchell M. de Boer

    Public Functions

    ColorMapEditor1DScene([ColorMapEditor1DWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_widget.html#_CPPv4N2mv3gui22ColorMapEditor1DWidgetE "mv::gui::ColorMapEditor1DWidget") &colorMapEditor1DWidget)
    :   Constructor.

        Parameters:
        :   **colorMapEditor1DWidget** – Reference to one-dimensional color map editor widget

    void pressed(QGraphicsSceneMouseEvent \*graphicsSceneMouseEvent)
    :   Reference to owning one-dimensional color map edit widget.

    Protected Functions

    void mousePressEvent(QGraphicsSceneMouseEvent \*graphicsSceneMouseEvent)
    :   Invoked when a mouse button is pressed.

        Parameters:
        :   **graphicsSceneMouseEvent** – Pointer to graphics scene mouse event
