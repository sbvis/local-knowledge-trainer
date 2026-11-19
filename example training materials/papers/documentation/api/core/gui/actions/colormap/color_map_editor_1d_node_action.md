# ColorMapEditor1DNodeAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node_action.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_editor_1d_node_action.html`

---

# ColorMapEditor1DNodeAction

**Qualified name:** `mv::gui::ColorMapEditor1DNodeAction`

class ColorMapEditor1DNodeAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Color map editor 1D node action class.

    Action class for editing one-dimensional color map editor node parameters

    **Author**
    :   Mitchell M. de Boer and Thomas Kroes

    Public Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the color map editor action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node_action.html#classmv_1_1gui_1_1ColorMapEditor1DNodeAction_1_1Widget) flags for the configuration of the widget

    Q\_INVOKABLE ColorMapEditor1DNodeAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   **parent** – Pointer to parent object title Title of the action

    void connectToNode([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node)
    :   Connect to a node.

        Parameters:
        :   **node** – Pointer to node

    void disconnectFromNode([ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*node)
    :   Disconnect from a node.

        Parameters:
        :   **node** – Pointer to node

    void nodeChanged()
    :   Invoked when the node changes one of its parameters and updates the user interface accordingly.

    Protected Attributes

    [ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#_CPPv4N2mv3gui20ColorMapEditor1DNodeE "mv::gui::ColorMapEditor1DNode") \*\_currentNode
    :   Reference to owning one-dimensional color map action.

    [ColorAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_action.html#_CPPv4N2mv3gui11ColorActionE "mv::gui::ColorAction") \_colorAction
    :   Pointer to current node (if any)

    [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction") \_valueAction
    :   Node color action.

    [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction") \_opacityAction
    :   Value action.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node_action.html#classmv_1_1gui_1_1ColorMapEditor1DNodeAction_1_1Widget) class for one-dimensional color map editor node action.

        Public Functions

        Widget(QWidget \*parent, [ColorMapEditor1DNodeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node_action.html#_CPPv4N2mv3gui26ColorMapEditor1DNodeActionE "mv::gui::ColorMapEditor1DNodeAction") \*colorMapEditor1DNodeAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **colorMapEditor1DNodeAction** – Pointer to one-dimensional color map editor node action
