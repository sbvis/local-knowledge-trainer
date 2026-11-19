# ColorMapEditor1DAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_editor_1d_action.html`

---

# ColorMapEditor1DAction

**Qualified name:** `mv::gui::ColorMapEditor1DAction`

class ColorMapEditor1DAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Color map editor 1D action class.

    Action class for manually defining a one-dimensional color map

    **Author**
    :   Thomas Kroes and Mitchell M. de Boer

    Public Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the one-dimensional color map editor action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html#classmv_1_1gui_1_1ColorMapEditor1DAction_1_1Widget) flags for the configuration of the widget

    QImage getColorMapImage() const
    :   Get color map image.

        Returns:
        :   Color map image

    QVector<[ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode")\*> &getNodes()
    :   Get nodes.

        Returns:
        :   Nodes

    [ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*addNode(const QPointF &normalizedCoordinate, const QColor &color = Qt::gray)
    :   Add node at normalized coordinate.

        Parameters:
        :   - **normalizedCoordinate** – Normalized coordinate
            - **color** – Node color
            - **radius** – Node radius

        Returns:
        :   Pointer to created node

    void removeNode([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node)
    :   Remove node.

        Parameters:
        :   **node** – Pointer to node which is to be removed

    [ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*getPreviousNode([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node) const
    :   Get previous node.

        Parameters:
        :   **node** – Pointer to node of which to obtain the previous node

        Returns:
        :   Pointer to previous node (node if it has no previous node)

    [ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*getNextNode([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node) const
    :   Get next node.

        Parameters:
        :   **node** – Pointer to node of which to obtain the next node

        Returns:
        :   Pointer to next node (node if it has no previous node)

    const Histogram &getHistogram() const
    :   Get one-dimensional histogram.

        Returns:
        :   One-dimensional histogram

    void setHistogram(const Histogram &histogram)
    :   Set background one-dimensional histogram.

        Parameters:
        :   **histogram** – One-dimensional histogram

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void nodeAdded([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node)
    :   Signals that a node is added.

        Parameters:
        :   **node** – Pointer to added node

    void nodeAboutToBeRemoved([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node)
    :   Signals that a node is about to be removed.

        Parameters:
        :   **node** – Pointer to node which is about to be removed

    void nodeRemoved(const std::uint32\_t &index)
    :   Signals that a node is removed.

        Parameters:
        :   **index** – Index of the node which is removed

    void histogramChanged(const Histogram &histogram)
    :   Signals that the histogram changed.

        Parameters:
        :   **histogram** – Histogram

    Protected Functions

    Q\_INVOKABLE ColorMapEditor1DAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void sortNodes()
    :   Sort nodes and update their index.

    void updateColorMap()
    :   Update the color map image.

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive) override
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions

    Protected Attributes

    QVector<[ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode")\*> \_nodes
    :   Reference to color map action.

    [ColorMapEditor1DNodeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node_action.html#_CPPv4N2mv3gui26ColorMapEditor1DNodeActionE "mv::gui::ColorMapEditor1DNodeAction") \_nodeAction
    :   All sorted nodes.

    QImage \_colorMapImage
    :   Node action.

    Histogram \_histogram
    :   Output color map image.

    Protected Static Attributes

    static constexpr QSize colorMapImageSize = QSize(256, 1)
    :   Histogram.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html#classmv_1_1gui_1_1ColorMapEditor1DAction_1_1Widget) class for one-dimensional color map editor action.

        Public Functions

        Widget(QWidget \*parent, [ColorMapEditor1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html#_CPPv4N2mv3gui22ColorMapEditor1DActionE "mv::gui::ColorMapEditor1DAction") \*colorMapEditor1DAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **colorMapEditor1DAction** – Pointer to one-dimensional color map editor action

        Protected Attributes

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_goToFirstNodeAction
        :   Color map editor widget.

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_goToPreviousNodeAction
        :   Go to first node action.

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_goToNextNodeAction
        :   Go to previous node action.

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_goToLastNodeAction
        :   Go to next node action.

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_removeNodeAction
        :   Go to last node action.
