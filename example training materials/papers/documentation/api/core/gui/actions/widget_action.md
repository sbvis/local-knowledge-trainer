# Widget action

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html

**Documentation path:** `api/core/gui/actions/widget_action.html`

---

# Widget action

`WidgetAction` is the common state, widget-creation, parameter-sharing, settings, and serialization base for ManiVault action controls. Prefer a concrete typed action in plugin code and consult this class for behavior shared across all action types.

For practical lifecycle and persistence patterns, see the [plugin actions and settings guide](https://manivault.readthedocs.io/en/latest/development/building_plugins/actions/index.html). Member-action QObject ownership and widget-representation lifetime are covered by [Qt plugin considerations](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/index.html). For `setIconByName()`, custom icons, and action badges, see [Using icons in plugins](https://manivault.readthedocs.io/en/latest/development/building_plugins/icons.html).

class WidgetAction : public QWidgetAction, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   Widget action class.

    Base class for custom widget actions

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::NumericalAction< float >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#classmv_1_1gui_1_1NumericalAction), [mv::gui::NumericalAction< std::int32\_t >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#classmv_1_1gui_1_1NumericalAction), ClustersAction, CreateSetFromSelectionAction, [DimensionPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimension_picker_action.html#classDimensionPickerAction), [DimensionsPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#classDimensionsPickerAction), [EditProxyDatasetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/edit_proxy_datasets_action.html#classEditProxyDatasetsAction), FilterClustersAction, [NumberOfSelectedPointsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/number_of_selected_points_action.html#classNumberOfSelectedPointsAction), [ProxyDatasetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/proxy_datasets_action.html#classProxyDatasetsAction), SelectClustersAction, [SelectedIndicesAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/selected_indices_action.html#classSelectedIndicesAction), SubsetAction, [mv::DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#classmv_1_1DataHierarchyItem), [mv::DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#classmv_1_1DatasetImpl), [mv::gui::ColorAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_action.html#classmv_1_1gui_1_1ColorAction), [mv::gui::ColorMapAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#classmv_1_1gui_1_1ColorMapAction), mv::gui::ColorMapAxisAction, mv::gui::ColorMapDiscreteAction, [mv::gui::ColorMapEditor1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html#classmv_1_1gui_1_1ColorMapEditor1DAction), [mv::gui::ColorMapEditor1DNodeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node_action.html#classmv_1_1gui_1_1ColorMapEditor1DNodeAction), [mv::gui::ColorMapSettings1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_1d_action.html#classmv_1_1gui_1_1ColorMapSettings1DAction), [mv::gui::ColorMapSettings2DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_2d_action.html#classmv_1_1gui_1_1ColorMapSettings2DAction), [mv::gui::ColorMapSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_action.html#classmv_1_1gui_1_1ColorMapSettingsAction), [mv::gui::ColorMapViewAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_view_action.html#classmv_1_1gui_1_1ColorMapViewAction), [mv::gui::ColorPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_picker_action.html#classmv_1_1gui_1_1ColorPickerAction), [mv::gui::DimensionsPickerFilterAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_filter_action.html#classmv_1_1gui_1_1DimensionsPickerFilterAction), [mv::gui::DimensionsPickerMiscellaneousAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html#classmv_1_1gui_1_1DimensionsPickerMiscellaneousAction), [mv::gui::DimensionsPickerSelectAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_select_action.html#classmv_1_1gui_1_1DimensionsPickerSelectAction), [mv::gui::DirectoryPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/file/directory_picker_action.html#classmv_1_1gui_1_1DirectoryPickerAction), [mv::gui::FilePickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/file/file_picker_action.html#classmv_1_1gui_1_1FilePickerAction), [mv::gui::GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#classmv_1_1gui_1_1GroupAction), [mv::gui::GroupsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#classmv_1_1gui_1_1GroupsAction), [mv::gui::ImageAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/image_action.html#classmv_1_1gui_1_1ImageAction), [mv::gui::LabelProxyAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/label_proxy_action.html#classmv_1_1gui_1_1LabelProxyAction), [mv::gui::NumericalAction< NumericalType >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#classmv_1_1gui_1_1NumericalAction), [mv::gui::OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#classmv_1_1gui_1_1OptionAction), [mv::gui::OptionsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/options_action.html#classmv_1_1gui_1_1OptionsAction), [mv::gui::PluginLearningCenterAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_learning_center_action.html#classmv_1_1gui_1_1PluginLearningCenterAction), [mv::gui::PresetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/presets_action.html#classmv_1_1gui_1_1PresetsAction), [mv::gui::ProgressAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/progress_action.html#classmv_1_1gui_1_1ProgressAction), [mv::gui::RecentFilesAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/recent_files_action.html#classmv_1_1gui_1_1RecentFilesAction), [mv::gui::StatusAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#classmv_1_1gui_1_1StatusAction), [mv::gui::StatusBarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html#classmv_1_1gui_1_1StatusBarAction), [mv::gui::StretchAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/stretch_action.html#classmv_1_1gui_1_1StretchAction), [mv::gui::StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#classmv_1_1gui_1_1StringAction), [mv::gui::StringsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/strings_action.html#classmv_1_1gui_1_1StringsAction), [mv::gui::ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#classmv_1_1gui_1_1ToggleAction), [mv::gui::ToolbarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/toolbar_action.html#classmv_1_1gui_1_1ToolbarAction), [mv::gui::TreeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/tree_action.html#classmv_1_1gui_1_1TreeAction), [mv::gui::TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#classmv_1_1gui_1_1TriggerAction), [mv::gui::TriggersAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#classmv_1_1gui_1_1TriggersAction), [mv::gui::VariantAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/variant_action.html#classmv_1_1gui_1_1VariantAction), [mv::gui::ViewPluginHeadsUpDisplayAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_heads_up_display.html#classmv_1_1gui_1_1ViewPluginHeadsUpDisplayAction), [mv::plugin::Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin), [mv::plugin::PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#classmv_1_1plugin_1_1PluginFactory)

    Public Types

    enum class Scope
    :   Describes the widget action scope of use.

        *Values:*

        enumerator Private

        enumerator Public
        :   Action is in the private pool.

            Action is in the public pool and eligible for connections

    enum class HighlightOption
    :   Describes the highlight options.

        *Values:*

        enumerator None

        enumerator Moderate
        :   Action is not highlighted.

        enumerator Strong
        :   Action is moderately highlighted.

            Action is strongly highlighted

    enum class ConfigurationFlag
    :   Describes the configuration options.

        *Values:*

        enumerator HiddenInActionContextMenu

        enumerator NoLabelInGroup
        :   Do not show this action in the context menu of another action.

        enumerator ForceCollapsedInGroup
        :   Action will not have a label when it is displayed in a group.

        enumerator ForceExpandedInGroup
        :   Action will be collapsed in a horizontal group (or toolbar), no matter the circumstances.

        enumerator ToolButtonAutoRaise
        :   Action will be expanded in a horizontal group (or toolbar), no matter the circumstances.

        enumerator NoGroupBoxInPopupLayout
        :   Sets auto-raise to true when a widget action is collapsed and a tool button is used for the popup functionality.

        enumerator User
        :   Prevent group box in popup layout.

        enumerator Default
        :   And beyond for custom configuration flags.

    enum ConnectionContextFlag
    :   \*\* Describes the connection context options \*/

        *Values:*

        enumerator Api

        enumerator Gui
        :   In the context of the API.

        enumerator ApiAndGui
        :   In the context of the GUI.

    enum class ConnectionPermissionFlag
    :   Describes the connection permission options.

        *Values:*

        enumerator None

        enumerator PublishViaApi
        :   Widget may not published nor connect nor disconnect via API and GUI.

        enumerator PublishViaGui
        :   Widget may be published via the API.

        enumerator PublishViaApiAndGui
        :   Widget may be published via the GUI.

        enumerator ConnectViaApi
        :   Widget may be published via the API and the GUI.

        enumerator ConnectViaGui
        :   Widget may connect to a public action via the API.

        enumerator ConnectViaApiAndGui
        :   Widget may connect to a public action via the GUI.

        enumerator DisconnectViaApi
        :   Widget may connect to a public action via the API and the GUI.

        enumerator DisconnectViaGui
        :   Widget may disconnect from a public action via the API.

        enumerator DisconnectViaApiAndGui
        :   Widget may disconnect from a public action via the GUI.

        enumerator ForceNone
        :   Widget may disconnect from a public action via the API and the GUI.

        enumerator All
        :   Disables all connection options (API and GUI), regardless of other connection permission flags.

        enumerator Default

    Public Functions

    WidgetAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Widget action title and serialization name

    ~WidgetAction() override
    :   Destructor.

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline [WidgetActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4I0ENK2mv3gui12WidgetAction9getParentEP16WidgetActionTypev "mv::gui::WidgetAction::getParent::WidgetActionType") \*getParent() const
    :   Get parent action of `WidgetActionType`.

        Returns:
        :   Pointer to parent action (nullptr if not found or if dynamic cast fails)

    inline bool hasParent() const
    :   Establish whether the action has a parent.

        Returns:
        :   Boolean determining whether the action has a parent or not

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline bool hasParent() const
    :   Establish whether the action has a parent of `WidgetActionType`.

        Returns:
        :   Boolean determining whether the action has a parent of `WidgetActionType` or not

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline WidgetActionsOfType<[WidgetActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4I0ENK2mv3gui12WidgetAction12getAncestorsE19WidgetActionsOfTypeI16WidgetActionTypeEv "mv::gui::WidgetAction::getAncestors::WidgetActionType")> getAncestors() const
    :   Get ancestors of `WidgetActionType`.

        Returns:
        :   Pointers to ancestors of `WidgetActionType` (bottom-up)

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline WidgetActionsOfType<[WidgetActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4I0ENK2mv3gui12WidgetAction11getChildrenE19WidgetActionsOfTypeI16WidgetActionTypeEb "mv::gui::WidgetAction::getChildren::WidgetActionType")> getChildren(bool recursively = false) const
    :   Get child actions of `WidgetActionType`, possibly `recursively`.

        Parameters:
        :   **recursively** – Get children recursively

        Returns:
        :   Vector of pointers to child actions of `WidgetActionType`

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline WidgetActionsOfType<[WidgetActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4I0ENK2mv3gui12WidgetAction11getChildrenE19WidgetActionsOfTypeI16WidgetActionTypeENSt7int32_tE "mv::gui::WidgetAction::getChildren::WidgetActionType")> getChildren(std::int32\_t maxDepth) const
    :   Get child actions of `WidgetActionType`, up until `maxDepth`.

        Parameters:
        :   **maxDepth** – Max depth of included children (fully recursive when -1)

        Returns:
        :   Vector of pointers to child actions of `WidgetActionType`

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline std::uint32\_t getNumberOfChildren(bool recursively = false) const
    :   Get number of children of `WidgetActionType`, possibly `recursively`.

        Parameters:
        :   **recursively** – Count recursively

        Returns:
        :   Number of children

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline bool hasChildren() const
    :   Establishes whether this action has any children of `WidgetActionType`.

        Returns:
        :   Boolean determining whether the item has any children

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline std::int32\_t getDepth() const
    :   Get the depth of the action w.r.t.

        its furthest ancestor of `WidgetActionType`

        Returns:
        :   Item depth (root starts at zero)

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline [WidgetActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4I0ENK2mv3gui12WidgetAction15findChildByPathEP16WidgetActionTypeRK7QString "mv::gui::WidgetAction::findChildByPath::WidgetActionType") \*findChildByPath(const QString &path) const
    :   Find child of `WidgetActionType` by `path`.

        Returns:
        :   Pointer to child action of `WidgetActionType`, otherwise nullptr

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline bool isChildOf([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) const
    :   Determine whether this action is a descendant of `action` of `WidgetActionType`.

        Parameters:
        :   **action** – Action to check for

        Returns:
        :   Boolean determining whether `action` is a descendant or not

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline bool isChildOf(WidgetActions actions) const
    :   Determine whether this action is a descendant of `actions` of `WidgetActionType`.

        Parameters:
        :   **actions** – Actions to check for

        Returns:
        :   Boolean determining whether this action is descendant of one of `actions` or not

    virtual QString getLocation(bool recompute = false) const
    :   Get location and possibly `recompute` it.

        Parameters:
        :   **recompute** – Whether to re-compute the location

        Returns:
        :   Path relative to the top-level action

    template<typename WidgetActionType = [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> inline void printChildren(std::int32\_t maxDepth = -1) const
    :   Print the paths of children of `WidgetActionType`.

        Parameters:
        :   **maxDepth** – Maximum depth to print

    plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*findPluginAncestor() const
    :   Find the nearest plugin ancestor of the action.

        Returns:
        :   Pointer to plugin ancestor, otherwise nullptr

    bool isRoot() const
    :   Establish whether this action is positioned at the top of the hierarchy.

        Returns:
        :   Boolean determining whether this action is positioned at the top of the hierarchy

    bool isLeaf() const
    :   Establish whether this action is positioned at the bottom of the hierarchy.

        Returns:
        :   Boolean determining whether this action is positioned at the bottom of the hierarchy

    QWidget \*createWidget(QWidget \*parent) final override
    :   Create widget with pointer to `parent` widget.

        Parameters:
        :   **parent** – Parent widget

        Returns:
        :   Pointer to created widget

    QWidget \*createWidget(QWidget \*parent, const std::int32\_t &widgetFlags)
    :   Create widget with pointer to `parent` widget and `widgetFlags`.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags

        Returns:
        :   Pointer to created widget

    QWidget \*createWidget(QWidget \*parent, const std::int32\_t &widgetFlags, const WidgetConfigurationFunction &widgetConfigurationFunction)
    :   Create widget with pointer to `parent` widget, `widgetFlags` and `widgetConfigurationFunction`.

        Parameters:
        :   - **parent** – Parent widget
            - **widgetFlags** – Widget flags
            - **widgetConfigurationFunction** – Configuration function to run after the widget is created (overrides WidgetAction::\_widgetConfigurationFunction)

        Returns:
        :   Pointer to created widget

    QWidget \*createWidget(QWidget \*parent, const WidgetConfigurationFunction &widgetConfigurationFunction)
    :   Create widget with pointer to `parent` widget and `widgetConfigurationFunction`.

        Parameters:
        :   - **parent** – Parent widget
            - **widgetConfigurationFunction** – Configuration function to run after the widget is created (overrides WidgetAction::\_widgetConfigurationFunction)

        Returns:
        :   Pointer to created widget

    QWidget \*createCollapsedWidget(QWidget \*parent) const
    :   Create collapsed widget.

        Parameters:
        :   **parent** – Parent widget

        Returns:
        :   Pointer to collapsed widget

    QWidget \*createCollapsedWidget(QWidget \*parent, const WidgetConfigurationFunction &widgetConfigurationFunction) const
    :   Create collapsed widget.

        Parameters:
        :   - **parent** – Parent widget
            - **widgetConfigurationFunction** – Configuration function to run after the widget is created (overrides WidgetAction::\_widgetConfigurationFunction)

        Returns:
        :   Pointer to collapsed widget

    QWidget \*createLabelWidget(QWidget \*parent, const std::int32\_t &widgetFlags = 0x00001) const
    :   Create label widget.

        Parameters:
        :   - **parent** – Parent widget
            - **widgetFlags** – Label widget configuration flags

        Returns:
        :   Pointer to widget

    virtual QMenu \*getContextMenu(QWidget \*parent = nullptr)
    :   Get the context menu for the action.

        Parameters:
        :   **parent** – Parent widget

        Returns:
        :   Context menu

    std::int32\_t getSortIndex() const
    :   Get the sort index.

    void setSortIndex(const std::int32\_t &sortIndex)
    :   Set the sort index.

        Parameters:
        :   **sortIndex** – Sorting index

    std::int32\_t getStretch() const
    :   Get stretch.

        Returns:
        :   The stretch factor

    void setStretch(const std::int32\_t &stretch)
    :   Set stretch to `stretch`.

        Parameters:
        :   **stretch** – Stretch factor

    WidgetConfigurationFunction getWidgetConfigurationFunction()
    :   Get widget configuration function.

        Returns:
        :   Function that is called right after a widget action widget is created (useful for manual manipulation of the generated widget)

    void setWidgetConfigurationFunction(const WidgetConfigurationFunction &widgetConfigurationFunction)
    :   Set widget configuration function to `widgetConfigurationFunction`.

        Parameters:
        :   **widgetConfigurationFunction** – This function is called right after a widget action widget is created (useful for manual manipulation of the generated widget)

    bool getForceHidden() const
    :   Get force hidden.

        Returns:
        :   Boolean determining whether the widget action should be forcibly hidden (regardless of the visibility setting in the base QWidgetAction class)

    void setForceHidden(bool forceHidden)
    :   Set force hidden to `forceHidden`.

        Parameters:
        :   **forceHidden** – Boolean determining whether the widget action should be forcibly hidden (regardless of the enabled visibility in the base QWidgetAction class)

    bool isVisible() const
    :   Re-implement the [isVisible()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#classmv_1_1gui_1_1WidgetAction_1a90966ad7f034f98faefc55a37cd65e96) getter from the base QWidgetAction class to support the force hidden functionality.

        Returns:
        :   Boolean determining whether the widget action is visible or not

    bool getForceDisabled() const
    :   Get force disabled.

        Returns:
        :   Boolean determining whether the widget action should be forcibly disabled (regardless of the enabled setting in the base QWidgetAction class)

    void setForceDisabled(bool forceDisabled)
    :   Set force disabled to `forceDisabled`.

        Parameters:
        :   **forceDisabled** – Boolean determining whether the widget action should be forcibly disabled (regardless of the enabled setting in the base QWidgetAction class)

    bool isEnabled() const
    :   Re-implement the [isEnabled()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#classmv_1_1gui_1_1WidgetAction_1a63d766dbc7c9ce5020f1f068aa68b598) getter from the base QWidgetAction class to support the force disabled functionality.

        Returns:
        :   Boolean determining whether the widget action is enabled or not

    void setText(const QString &text)
    :   Re-implement the setText(…) setter from the base QWidgetAction class to support updating the location.

        Parameters:
        :   **text** – Text to set

    std::int32\_t getDefaultWidgetFlags() const
    :   Gets the default widget flags.

    void setDefaultWidgetFlags(std::int32\_t defaultWidgetFlags)
    :   Set the widget flags.

        Parameters:
        :   **defaultWidgetFlags** – Widget flags

    void setDefaultWidgetFlag(std::int32\_t defaultWidgetFlag, bool unset = false)
    :   Set a single widget flag on/off.

        Parameters:
        :   - **defaultWidgetFlag** – Widget flag to set on/off
            - **unset** – Whether to unset the default widget flag

    [HighlightOption](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction15HighlightOptionE "mv::gui::WidgetAction::HighlightOption") getHighlighting() const
    :   Get highlighting.

        Returns:
        :   Highlight option

    bool isHighlighted() const
    :   Determine whether the action is in a highlighted state or not.

        Returns:
        :   Boolean determining whether the action is in a highlighted state or not

    void setHighlighting(const [HighlightOption](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction15HighlightOptionE "mv::gui::WidgetAction::HighlightOption") &highlighting)
    :   Set highlighting to `highlighting`.

        Parameters:
        :   **highlighting** – Highlighting state

    void setHighlighted(bool highlighted)
    :   Set highlighted to `highlighted`.

        Parameters:
        :   **highlighted** – Boolean determining whether the action is in a normal highlighted state or not

    void highlight()
    :   Convenience method to highlight the action.

    void unHighlight()
    :   Convenience method to un-highlight the action.

    [Scope](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction5ScopeE "mv::gui::WidgetAction::Scope") getScope() const
    :   Get widget action scope.

        Returns:
        :   Widget action scope enum

    bool isPrivate() const
    :   Get whether this action is in the private actions pool.

        Returns:
        :   Boolean determining whether this action is in the private actions pool

    bool isPublic() const
    :   Get whether this action is in the public actions pool.

        Returns:
        :   Boolean determining whether this action is in the private public pool

    bool isPublished() const
    :   Get whether the action is published.

        Returns:
        :   Boolean indicating whether the action is published

    bool isConnected() const
    :   Get whether the action is connect to a public action.

        Returns:
        :   Boolean indicating whether the action is connect to a public action

    bool mayConnectToPublicAction(const [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction) const
    :   Get whether the action may connect to `publicAction`.

        Parameters:
        :   **publicAction** – Pointer to public action

        Returns:
        :   Boolean determining whether the action may connect to `publicAction`

    bool publish(const QString &name = "", bool allowDuplicateName = false)
    :   Publish this action so that other actions can connect to it.

        Parameters:
        :   - **name** – Name of the published widget action (if empty, a configuration dialog will popup)
            - **allowDuplicateName** – Boolean determining whether publishing will take place when a public with the same name already exists in the public actions database

        Returns:
        :   Boolean determining whether the action is successfully published or not

    [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getPublicAction()
    :   Get the public action to which the action is connected.

        Returns:
        :   Pointer to the public action (returns nullptr if not connected to a public action)

    virtual [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getPublicCopy() const
    :   Get public copy of the action (other compatible actions can connect to it)

        Returns:
        :   Pointer to public copy of the action

    const WidgetActions getConnectedActions() const
    :   Get connected actions.

        Returns:
        :   Vector of pointers to connected actions

    WidgetActions &getConnectedActions()
    :   Get connected actions.

        Returns:
        :   Vector of pointers to connected actions

    bool mayPublish([ConnectionContextFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction21ConnectionContextFlagE "mv::gui::WidgetAction::ConnectionContextFlag") connectionContextFlags) const
    :   Get whether a copy of this action may be published and shared, depending on the `connectionContextFlags`.

        Parameters:
        :   **connectionContextFlags** – The context from which the action will be published (API and/or GUI)

        Returns:
        :   Boolean determining whether a copy of this action may published and shared, depending on the `connectionContextFlags`

    bool mayConnect([ConnectionContextFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction21ConnectionContextFlagE "mv::gui::WidgetAction::ConnectionContextFlag") connectionContextFlags) const
    :   Get whether this action may connect to a public action, depending on the `connectionContextFlags`.

        Parameters:
        :   **connectionContextFlags** – The context from which the connection will be made (API and/or GUI)

        Returns:
        :   Boolean determining whether this action may connect to a public action, depending on the `connectionContextFlags`

    bool mayDisconnect([ConnectionContextFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction21ConnectionContextFlagE "mv::gui::WidgetAction::ConnectionContextFlag") connectionContextFlags) const
    :   Get whether this action may disconnect from a public action, depending on the `connectionContextFlags`.

        Parameters:
        :   **connectionContextFlags** – The context from which the disconnection will be initiated (API and/or GUI)

        Returns:
        :   Boolean determining whether this action may disconnect from a public action, depending on the `connectionContextFlags`

    std::int32\_t getConnectionPermissions() const
    :   Get connection permission flags.

        Returns:
        :   Connection permission flags

    bool isConnectionPermissionFlagSet([ConnectionPermissionFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction24ConnectionPermissionFlagE "mv::gui::WidgetAction::ConnectionPermissionFlag") connectionPermissionsFlag)
    :   Check whether `connectionPermissionsFlag` is set or not.

        Parameters:
        :   **connectionPermissionsFlag** – Connection permissions flag

        Returns:
        :   Boolean determining whether `connectionPermissionsFlag` is set or not

    void setConnectionPermissionsFlag([ConnectionPermissionFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction24ConnectionPermissionFlagE "mv::gui::WidgetAction::ConnectionPermissionFlag") connectionPermissionsFlag, bool unset = false, bool recursive = false)
    :   Set connection permissions flag.

        Parameters:
        :   - **connectionPermissionsFlag** – Connection permissions flag to set
            - **unset** – Whether to unset the connection permissions flag
            - **recursive** – Whether to recursively set child connection permissions

    void setConnectionPermissions(std::int32\_t connectionPermissions, bool recursive = false)
    :   Set connection permissions.

        Parameters:
        :   - **connectionPermissions** – Connection permissions value
            - **recursive** – Whether to recursively set child connection permissions

    void setConnectionPermissionsToNone(bool recursive = false)
    :   Reset connection permissions to none.

        Parameters:
        :   **recursive** – Whether to recursively set child connection permissions

    void setConnectionPermissionsToForceNone(bool recursive = false)
    :   Set connection permissions to force none (connections fully disabled, regardless of other connection permission flags)

        Parameters:
        :   **recursive** – Whether to recursively set child connection permissions

    void setConnectionPermissionsToAll(bool recursive = false)
    :   Set connection permissions to all.

        Parameters:
        :   **recursive** – Whether to recursively set child connection permissions

    void cacheConnectionPermissions(bool recursive = false)
    :   Cache connection permissions.

        Parameters:
        :   **recursive** – Whether to recursively cache child connection permissions

    void restoreConnectionPermissions(bool recursive = false)
    :   Restore connection permissions.

        Parameters:
        :   **recursive** – Whether to recursively restore child connection permissions

    bool isResettable() const
    :   Determines whether the action can be reset to its default.

        Returns:
        :   Whether the action can be reset to its default

    void reset()
    :   Reset to default.

    void setSettingsPrefix(const QString &settingsPrefix, const bool &load = true)
    :   Set settings prefix.

        Parameters:
        :   - **load** – Whether to restore settings after setting the prefix
            - **settingsPrefix** – Settings prefix

    void setSettingsPrefix([plugin](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction17setSettingsPrefixEPN6plugin6PluginERK7QStringRKb "mv::gui::WidgetAction::setSettingsPrefix::plugin")::Plugin \*plugin, const QString &settingsPrefix, const bool &load = true)
    :   Set settings prefix in the context of a plugin (the combined settings prefix will be: Plugins/PluginKind/SettingsPrefix)

        Parameters:
        :   - **load** – Whether to restore settings after setting the prefix
            - **plugin** – Pointer to plugin context
            - **settingsPrefix** – Settings prefix

    virtual QString getSettingsPrefix() const
    :   Get settings prefix.

        Returns:
        :   Settings prefix

    void loadFromSettings()
    :   Load from settings (if the settings prefix is set)

    void saveToSettings()
    :   Save to settings (if the settings prefix is set)

    QSize getPopupSizeHint() const
    :   Get size hint of popups (in case of collapsed actions)

        Returns:
        :   Popup size hint

    void setPopupSizeHint(const QSize &popupSizeHint)
    :   Set size hint of popups (in case of collapsed actions)

        Parameters:
        :   **popupSizeHint** – Popup size hint

    QSize getOverrideSizeHint() const
    :   Get override size hint.

        Returns:
        :   Override size hint

    void setOverrideSizeHint(const QSize &overrideSizeHint)
    :   Set override size hint.

        Parameters:
        :   **overrideSizeHint** – Override size hint

    std::int32\_t getConfiguration() const
    :   Get configuration.

        Returns:
        :   Configuration

    bool isConfigurationFlagSet([ConfigurationFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction17ConfigurationFlagE "mv::gui::WidgetAction::ConfigurationFlag") configurationFlag) const
    :   Check whether `configurationFlag` is set or not.

        Parameters:
        :   **configurationFlag** – Configuration flag

        Returns:
        :   Boolean determining whether `configurationFlag` is set or not

    void setConfigurationFlag([ConfigurationFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction17ConfigurationFlagE "mv::gui::WidgetAction::ConfigurationFlag") configurationFlag, bool unset = false, bool recursive = false)
    :   Set configuration flag.

        Parameters:
        :   - **configurationFlag** – Configuration flag to set
            - **unset** – Whether to unset the `configurationFlag` flag
            - **recursive** – Whether to recursively set child child configuration flag

    void setConfiguration(std::int32\_t configuration, bool recursive = false)
    :   Set configuration.

        Parameters:
        :   - **configuration** – Configuration value
            - **recursive** – Whether to recursively set child child configuration flag

    QString getTypeString(bool humanFriendly = false) const
    :   Get type string.

        Parameters:
        :   **humanFriendly** – Whether to return a type string where the namespace is omitted

        Returns:
        :   Widget action type in string format

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    bool hasCacheState(const QString &name) const
    :   Determine whether cache with name exists.

        Parameters:
        :   **name** – Name to use for the cached widget action state

    void cacheState(const QString &name = "cache")
    :   Cache the state of a widget action under `name` in the action itself (for global presets use the presets action)

        Parameters:
        :   **name** – Name to use for the cached widget action state

    void restoreState(const QString &name = "cache", bool remove = true)
    :   Restore the state of under `name`.

        Parameters:
        :   - **name** – Name of the cached widget action state to restore
            - **remove** – Whether to remove the cache

    void setStudioMode(bool studioMode, bool recursive = true)
    :   Set studio mode to `studioMode`.

        Parameters:
        :   - **studioMode** – Boolean determining whether studio mode is on or off
            - **recursive** – Boolean determining whether to also apply the studio mode to child actions recursively

    virtual void setIconByName(const QString &iconName)
    :   Set the icon by `iconName` and use the default icon font and version.

        Parameters:
        :   **iconName** – Name of the icon

    virtual void setIconByName(const QString &iconName, const QString &iconFontName, const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion)
    :   Set the icon by `iconName` and possibly override the default `iconFontName` and `iconFontVersion`.

        Parameters:
        :   - **iconName** – Name of the icon
            - **iconFontName** – Name of the icon font
            - **iconFontVersion** – Version of the icon font

    util::[Badge](https://manivault.readthedocs.io/en/latest/api/core/util/badge/badge.html#_CPPv4N2mv4util5BadgeE "mv::util::Badge") &getBadge()
    :   Get badge.

        Returns:
        :   Reference to the widget action badge

    [WidgetActionDrag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_drag.html#_CPPv4N2mv3gui16WidgetActionDragE "mv::gui::WidgetActionDrag") &getDrag()
    :   Get drag.

        Returns:
        :   Reference to the widget action drag

    void idChanged(const QString &id)
    :   Signals that the globally unique identifier changed (only happens upon de-serialization of a widget action)

        Parameters:
        :   **id** – Globally unique identifier that changed

    void sortIndexChanged(std::int32\_t sortIndex)
    :   Signals that the sort index changed to `sortIndex`.

        Parameters:
        :   **sortIndex** – Sort index (relative position in group items)

    void stretchChanged(std::int32\_t stretch)
    :   Signals that the stretch changed to `stretch`.

        Parameters:
        :   **stretch** – Stretch factor (in action groups)

    void forceHiddenChanged(bool forceHidden)
    :   Signals that force hidden changed to `forceHidden`.

        Parameters:
        :   **forceHidden** – Boolean determining whether the widget action should be forcibly hidden (regardless of the visibility setting in the base QWidgetAction class)

    void forceDisabledChanged(bool forceDisabled)
    :   Signals that force disabled changed to `forceDisabled`.

        Parameters:
        :   **forceDisabled** – Boolean determining whether the widget action should be forcibly disabled (regardless of the enabled setting in the base QWidgetAction class)

    void highlightingChanged(const [HighlightOption](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction15HighlightOptionE "mv::gui::WidgetAction::HighlightOption") &highlightOption)
    :   Signals that the highlighting options changed to `highlightOption`.

        Parameters:
        :   **highlightOption** – Current highlight option

    void isPublishedChanged(const bool &isPublished)
    :   Signals that the published state changed.

        Parameters:
        :   **isPublished** – Whether the action is published or not

    void isConnectedChanged(const bool &isConnected)
    :   Signals that the connected state changed.

        Parameters:
        :   **isConnected** – Whether the action is connected or not

    void actionConnected([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Signals that an action connected.

        Parameters:
        :   **action** – Action that connected

    void actionDisconnected([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Signals that an action disconnected.

        Parameters:
        :   **action** – Action that disconnected

    void connectionPermissionsChanged(std::int32\_t connectionPermissions)
    :   Signals that the connection permissions changed.

        Parameters:
        :   **connectionPermissions** – New connection permissions

    void configurationFlagToggled(const [ConfigurationFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction17ConfigurationFlagE "mv::gui::WidgetAction::ConfigurationFlag") &configurationFlag, bool set)
    :   Signals that `configurationFlag` is `set`.

        Parameters:
        :   - **configurationFlag** – Toggled configuration flag
            - **set** – Whether the flag was set or unset

    void configurationChanged(std::int32\_t configuration)
    :   Signals that the configuration changed.

        Parameters:
        :   **configuration** – New configuration

    void scopeChanged(const [Scope](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction5ScopeE "mv::gui::WidgetAction::Scope") &scope)
    :   Signals that the scope changed to `scope`.

        Parameters:
        :   **scope** – Scope of the widget action

    void textChanged(const QString &text)
    :   Signals that the text changed to `text`.

        Parameters:
        :   **text** – Action text

    void locationChanged(const QString &location)
    :   Signals that the location changed to `location`.

        Parameters:
        :   **location** – The path relative to the root in string format

    void widgetConfigurationFunctionChanged(WidgetConfigurationFunction &widgetConfigurationFunction)
    :   Signals that the widget configuration function changed to `widgetConfigurationFunction`.

        Parameters:
        :   **widgetConfigurationFunction** – New widget configuration function

    Public Static Attributes

    static QMap<[Scope](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction5ScopeE "mv::gui::WidgetAction::Scope"), QString> scopeNames
    :   Map scope enum to scope name.

    Protected Functions

    void makePublic(bool recursive = true)
    :   Make widget action public (and possibly all of its descendant widget actions)

        Parameters:
        :   **recursive** – Whether to also make all descendant widget actions public

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive)
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    void connectToPublicActionByName(const QString &publicActionName)
    :   Connect this action to a public action.

        Parameters:
        :   **publicActionName** – Pointer to public action to connect to

    virtual void disconnectFromPublicAction(bool recursive)
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags)
    :   Get widget representation of the action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    Friends

    *friend class* mv::AbstractActionsManager
