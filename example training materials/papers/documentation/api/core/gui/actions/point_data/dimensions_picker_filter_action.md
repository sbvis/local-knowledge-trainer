# DimensionsPickerFilterAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_filter_action.html

**Documentation path:** `api/core/gui/actions/point_data/dimensions_picker_filter_action.html`

---

# DimensionsPickerFilterAction

**Qualified name:** `mv::gui::DimensionsPickerFilterAction`

class DimensionsPickerFilterAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Dimensions picker filter action.

    Action class for filtering dimensions

    **Author**
    :   Thomas Kroes

    Public Functions

    DimensionsPickerFilterAction([DimensionsPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#_CPPv422DimensionsPickerAction "DimensionsPickerAction") &dimensionsPickerAction)
    :   Constructor.

        Parameters:
        :   **dimensionsPickerAction** – Reference to the dimensions picker action

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the dimensions picker filter action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_filter_action.html#classmv_1_1gui_1_1DimensionsPickerFilterAction_1_1Widget) flags for the configuration of the widget

    Protected Attributes

    [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_nameFilterAction
    :   Reference to the dimensions picker action.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_filter_action.html#classmv_1_1gui_1_1DimensionsPickerFilterAction_1_1Widget) class for dimensions picker filter action.

        Protected Functions

        Widget(QWidget \*parent, [DimensionsPickerFilterAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_filter_action.html#_CPPv4N2mv3gui28DimensionsPickerFilterActionE "mv::gui::DimensionsPickerFilterAction") \*dimensionsPickerFilterAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **dimensionsPickerFilterAction** – Pointer to dimensions picker filter action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_filter_action.html#classmv_1_1gui_1_1DimensionsPickerFilterAction_1_1Widget) flags for the configuration of the widget
