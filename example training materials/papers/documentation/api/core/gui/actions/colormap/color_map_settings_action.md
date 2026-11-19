# ColorMapSettingsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_action.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_settings_action.html`

---

# ColorMapSettingsAction

**Qualified name:** `mv::gui::ColorMapSettingsAction`

class ColorMapSettingsAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Color map settings action class.

    Group action for color map settings

    **Author**
    :   Thomas Kroes

    Public Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the color map settings action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_action.html#classmv_1_1gui_1_1ColorMapSettingsAction_1_1Widget) flags for the configuration of the widget (type)

    Protected Functions

    Q\_INVOKABLE ColorMapSettingsAction([ColorMapAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapActionE "mv::gui::ColorMapAction") &colorMapAction, const QString &title)
    :   Constructor.

        Parameters:
        :   - **colorMapAction** – Reference to color map action
            - **title** – Title of the group action

    Friends

    *friend class* ColorMapAction

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_action.html#classmv_1_1gui_1_1ColorMapSettingsAction_1_1Widget) class for color map settings action.

        Public Functions

        Widget(QWidget \*parent, [ColorMapSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_action.html#_CPPv4N2mv3gui22ColorMapSettingsActionE "mv::gui::ColorMapSettingsAction") \*colorMapSettingsAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **colorMapSettingsAction** – Pointer to clusters action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_action.html#classmv_1_1gui_1_1ColorMapSettingsAction_1_1Widget) flags for the configuration of the widget (type)
