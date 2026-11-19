# ColorMapViewAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_view_action.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_view_action.html`

---

# ColorMapViewAction

**Qualified name:** `mv::gui::ColorMapViewAction`

class ColorMapViewAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Color map view action class.

    Action class for color map display in a widget

    **Author**
    :   Thomas Kroes

    Public Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the color map view action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_view_action.html#classmv_1_1gui_1_1ColorMapViewAction_1_1Widget) flags for the configuration of the widget (type)

    Protected Functions

    Q\_INVOKABLE ColorMapViewAction([ColorMapAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapActionE "mv::gui::ColorMapAction") &colorMapAction)
    :   Constructor.

        Parameters:
        :   **colorMapAction** – Reference to color map action

    Friends

    *friend class* ColorMapSettings1DAction

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_view_action.html#classmv_1_1gui_1_1ColorMapViewAction_1_1Widget) class for color map view action.

        Public Functions

        Widget(QWidget \*parent, [ColorMapViewAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_view_action.html#_CPPv4N2mv3gui18ColorMapViewActionE "mv::gui::ColorMapViewAction") \*colorMapViewAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **colorMapViewAction** – Pointer to color map view action
