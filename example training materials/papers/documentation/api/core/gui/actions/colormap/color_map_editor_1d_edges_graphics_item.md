# ColorMapEditor1DEdgesGraphicsItem

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_edges_graphics_item.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_editor_1d_edges_graphics_item.html`

---

# ColorMapEditor1DEdgesGraphicsItem

**Qualified name:** `mv::gui::ColorMapEditor1DEdgesGraphicsItem`

class ColorMapEditor1DEdgesGraphicsItem : public QObject, public QGraphicsItem
:   Color map editor 1D edges graphics item class.

    Graphics item class which visually connected nodes in a one-dimensional color map

    **Author**
    :   Thomas Kroes and Mitchell M. de Boer

    Public Functions

    ColorMapEditor1DEdgesGraphicsItem([ColorMapEditor1DWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_widget.html#_CPPv4N2mv3gui22ColorMapEditor1DWidgetE "mv::gui::ColorMapEditor1DWidget") &colorMapEditor1DWidget)
    :   Constructor.

        Parameters:
        :   **colorMapEditor1DWidget** – Reference to one-dimensional color map editor widget

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Respond to target object events.

        Parameters:
        :   - **target** – Object of which an event occurred
            - **event** – The event that took place

    Protected Functions

    QRectF boundingRect() const override
    :   Get edges bounding rectangle.

        Returns:
        :   Bounding rectangle

    void paint(QPainter \*painter, const QStyleOptionGraphicsItem \*option, QWidget \*widget) override
    :   Paint the edges.

        Parameters:
        :   - **painter** – Pointer to painter
            - **option** – Pointer to style options
            - **widget** – Pointer to widget
