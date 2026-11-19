# DimensionsPickerMiscellaneousAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html

**Documentation path:** `api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html`

---

# DimensionsPickerMiscellaneousAction

**Qualified name:** `mv::gui::DimensionsPickerMiscellaneousAction`

class DimensionsPickerMiscellaneousAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Dimensions picker miscellaneous widget action.

    Action class for managing dimension picker miscellaneous settings

    **Author**
    :   Thomas Kroes

    Public Functions

    DimensionsPickerMiscellaneousAction([DimensionsPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#_CPPv422DimensionsPickerAction "DimensionsPickerAction") &dimensionsPickerAction)
    :   Constructor.

        Parameters:
        :   **dimensionsPickerAction** – Reference to the dimensions picker action

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the dimensions picker miscellaneous action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html#classmv_1_1gui_1_1DimensionsPickerMiscellaneousAction_1_1Widget) flags for the configuration of the widget

    Protected Attributes

    [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_showOnlySelectedDimensionsAction
    :   Reference to the dimensions picker action.

    [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_applyExclusionListAction
    :   Show only selected dimensions action.

    [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_ignoreZeroValuesAction
    :   Apply exclusion list action.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html#classmv_1_1gui_1_1DimensionsPickerMiscellaneousAction_1_1Widget) class for dimensions picker miscellaneous action.

        Protected Functions

        Widget(QWidget \*parent, [DimensionsPickerMiscellaneousAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html#_CPPv4N2mv3gui35DimensionsPickerMiscellaneousActionE "mv::gui::DimensionsPickerMiscellaneousAction") \*dimensionsPickerMiscellaneousAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **dimensionsPickerMiscellaneousAction** – Pointer to dimensions picker miscellaneous action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html#classmv_1_1gui_1_1DimensionsPickerMiscellaneousAction_1_1Widget) flags for the configuration of the widget
