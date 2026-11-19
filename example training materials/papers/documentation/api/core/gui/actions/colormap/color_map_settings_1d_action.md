# ColorMapSettings1DAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_1d_action.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_settings_1d_action.html`

---

# ColorMapSettings1DAction

**Qualified name:** `mv::gui::ColorMapSettings1DAction`

class ColorMapSettings1DAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Color map settings one-dimensional action class.

    [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_1d_action.html#classmv_1_1gui_1_1ColorMapSettings1DAction_1_1Widget) action class for one-dimensional color map settings

    **Author**
    :   Thomas Kroes

    Public Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the one-dimensional color map settings action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_1d_action.html#classmv_1_1gui_1_1ColorMapSettings1DAction_1_1Widget) flags for the configuration of the widget (type)

    Protected Functions

    Q\_INVOKABLE ColorMapSettings1DAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    Friends

    *friend class* ColorMapAction

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_1d_action.html#classmv_1_1gui_1_1ColorMapSettings1DAction_1_1Widget) class for one-dimensional color map settings action.

        Public Functions

        Widget(QWidget \*parent, [ColorMapSettings1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_1d_action.html#_CPPv4N2mv3gui24ColorMapSettings1DActionE "mv::gui::ColorMapSettings1DAction") \*colorMapSettings1DAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **colorMapSettings1DAction** – Pointer to one-dimensional color map settings action
