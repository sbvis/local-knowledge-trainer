# WidgetActionWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_widget.html`

---

# WidgetActionWidget

**Qualified name:** `mv::gui::WidgetActionWidget`

class WidgetActionWidget : public mv::gui::[WidgetActionViewWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_view_widget.html#_CPPv4N2mv3gui22WidgetActionViewWidgetE "mv::gui::WidgetActionViewWidget")
:   Widget action widget class.

    Base class for widgets that interact with a widget action

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Subclassed by ClustersActionWidget, ColorizeClustersAction::Widget, CreateSetFromSelectionAction::Widget, [DimensionPickerAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimension_picker_action.html#classDimensionPickerAction_1_1Widget), [DimensionsPickerAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#classDimensionsPickerAction_1_1Widget), [EditProxyDatasetsAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/edit_proxy_datasets_action.html#classEditProxyDatasetsAction_1_1Widget), FilterClustersAction::Widget, [NumberOfSelectedPointsAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/number_of_selected_points_action.html#classNumberOfSelectedPointsAction_1_1Widget), PrefixClustersAction::Widget, [ProxyDatasetsAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/proxy_datasets_action.html#classProxyDatasetsAction_1_1Widget), SelectClustersAction::Widget, [SelectedIndicesAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/selected_indices_action.html#classSelectedIndicesAction_1_1Widget), SubsetAction::Widget, [mv::gui::ColorAction::PushButtonWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_action.html#classmv_1_1gui_1_1ColorAction_1_1PushButtonWidget), mv::gui::ColorMapAxisAction::Widget, mv::gui::ColorMapDiscreteAction::Widget, [mv::gui::ColorMapEditor1DAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html#classmv_1_1gui_1_1ColorMapEditor1DAction_1_1Widget), [mv::gui::ColorMapEditor1DNodeAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node_action.html#classmv_1_1gui_1_1ColorMapEditor1DNodeAction_1_1Widget), [mv::gui::ColorMapSettings1DAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_1d_action.html#classmv_1_1gui_1_1ColorMapSettings1DAction_1_1Widget), [mv::gui::ColorMapSettings2DAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_2d_action.html#classmv_1_1gui_1_1ColorMapSettings2DAction_1_1Widget), [mv::gui::ColorMapSettingsAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_action.html#classmv_1_1gui_1_1ColorMapSettingsAction_1_1Widget), [mv::gui::ColorMapViewAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_view_action.html#classmv_1_1gui_1_1ColorMapViewAction_1_1Widget), [mv::gui::ColorPickerAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_picker_action.html#classmv_1_1gui_1_1ColorPickerAction_1_1Widget), [mv::gui::DecimalRangeAction::DecimalRangeWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#classmv_1_1gui_1_1DecimalRangeAction_1_1DecimalRangeWidget), [mv::gui::DimensionsPickerFilterAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_filter_action.html#classmv_1_1gui_1_1DimensionsPickerFilterAction_1_1Widget), [mv::gui::DimensionsPickerMiscellaneousAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html#classmv_1_1gui_1_1DimensionsPickerMiscellaneousAction_1_1Widget), [mv::gui::DimensionsPickerSelectAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_select_action.html#classmv_1_1gui_1_1DimensionsPickerSelectAction_1_1Widget), [mv::gui::GroupAction::HorizontalWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#classmv_1_1gui_1_1GroupAction_1_1HorizontalWidget), [mv::gui::GroupAction::VerticalWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#classmv_1_1gui_1_1GroupAction_1_1VerticalWidget), [mv::gui::GroupsAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#classmv_1_1gui_1_1GroupsAction_1_1Widget), [mv::gui::HorizontalToolbarAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html#classmv_1_1gui_1_1HorizontalToolbarAction_1_1Widget), [mv::gui::IntegralRangeAction::IntegralRangeWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_range_action.html#classmv_1_1gui_1_1IntegralRangeAction_1_1IntegralRangeWidget), [mv::gui::PluginTriggerPickerAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_picker_action.html#classmv_1_1gui_1_1PluginTriggerPickerAction_1_1Widget), [mv::gui::StatusBarAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html#classmv_1_1gui_1_1StatusBarAction_1_1Widget), [mv::gui::StringsAction::ListWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/strings_action.html#classmv_1_1gui_1_1StringsAction_1_1ListWidget), [mv::gui::TableAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/table_action.html#classmv_1_1gui_1_1TableAction_1_1Widget), [mv::gui::TasksListAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/tasks_list_action.html#classmv_1_1gui_1_1TasksListAction_1_1Widget), [mv::gui::TreeAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/tree_action.html#classmv_1_1gui_1_1TreeAction_1_1Widget), [mv::gui::TriggersAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#classmv_1_1gui_1_1TriggersAction_1_1Widget), [mv::gui::VerticalToolbarAction::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_toolbar_action.html#classmv_1_1gui_1_1VerticalToolbarAction_1_1Widget)

    Public Functions

    WidgetActionWidget(QWidget \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, std::int32\_t widgetFlags = 0)
    :   Constructor.

        Parameters:
        :   - **parent** – Parent widget
            - **action** – Pointer to the widget action that will be displayed
            - **widgetFlags** – Widget flags for the configuration of the widget

    QSize sizeHint() const override
    :   Override the size hint to account for popups.

        Returns:
        :   Size hint

    void setLayout(QLayout \*layout)
    :   Override to allow for popup layouts.

        Parameters:
        :   **layout** – Pointer to layout
