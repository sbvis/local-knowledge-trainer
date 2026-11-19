# DimensionsPickerSelectAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_select_action.html

**Documentation path:** `api/core/gui/actions/point_data/dimensions_picker_select_action.html`

---

# DimensionsPickerSelectAction

**Qualified name:** `mv::gui::DimensionsPickerSelectAction`

class DimensionsPickerSelectAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Dimensions picker select action.

    Action class for selecting dimensions based on visibility

    **Author**
    :   Thomas Kroes

    Public Functions

    DimensionsPickerSelectAction([DimensionsPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#_CPPv422DimensionsPickerAction "DimensionsPickerAction") &dimensionsPickerAction)
    :   Constructor.

        Parameters:
        :   **dimensionsPickerAction** – Reference to the dimensions picker action

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the dimensions picker select action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_select_action.html#classmv_1_1gui_1_1DimensionsPickerSelectAction_1_1Widget) flags for the configuration of the widget

    Protected Attributes

    [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction") \_selectionThresholdAction
    :   Reference to the dimensions picker action.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_selectVisibleAction
    :   [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) threshold action.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_computeStatisticsAction
    :   Select visible dimensions action.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_selectNonVisibleAction
    :   Compute statistics action.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_loadSelectionAction
    :   Select non visible dimensions action.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_saveSelectionAction
    :   Load selection action.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_loadExclusionAction
    :   Save selection action.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_select_action.html#classmv_1_1gui_1_1DimensionsPickerSelectAction_1_1Widget) class for dimensions picker miscellaneous action.

        Protected Functions

        Widget(QWidget \*parent, [DimensionsPickerSelectAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_select_action.html#_CPPv4N2mv3gui28DimensionsPickerSelectActionE "mv::gui::DimensionsPickerSelectAction") \*dimensionsPickerSelectAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **dimensionsPickerSelectAction** – Pointer to dimensions picker select action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_select_action.html#classmv_1_1gui_1_1DimensionsPickerSelectAction_1_1Widget) flags for the configuration of the widget
