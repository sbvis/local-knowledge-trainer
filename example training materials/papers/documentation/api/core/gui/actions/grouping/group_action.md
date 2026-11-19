# GroupAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html

**Documentation path:** `api/core/gui/actions/grouping/group_action.html`

---

# GroupAction

**Qualified name:** `mv::gui::GroupAction`

class GroupAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Group action class.

    Contains zero or more child actions and either displays them horizontally or vertically.

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::NumericalPointAction< float, DecimalAction >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#classmv_1_1gui_1_1NumericalPointAction), [mv::gui::NumericalPointAction< std::int32\_t, IntegralAction >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#classmv_1_1gui_1_1NumericalPointAction), [mv::gui::NumericalRangeAction< float, DecimalAction >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#classmv_1_1gui_1_1NumericalRangeAction), [mv::gui::NumericalRangeAction< std::int32\_t, IntegralAction >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#classmv_1_1gui_1_1NumericalRangeAction), [mv::gui::RectangleAction< DecimalRangeAction >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#classmv_1_1gui_1_1RectangleAction), [mv::gui::RectangleAction< IntegralRangeAction >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#classmv_1_1gui_1_1RectangleAction), [InfoAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/info_action.html#classInfoAction), [InfoAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/info_action.html#classInfoAction), [InfoAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/info_action.html#classInfoAction), [InfoAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/info_action.html#classInfoAction), StatisticsAction, UnhideAction, [mv::gui::GlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/global_settings_group_action.html#classmv_1_1gui_1_1GlobalSettingsGroupAction), [mv::gui::HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#classmv_1_1gui_1_1HorizontalGroupAction), [mv::gui::LockingAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/locking_action.html#classmv_1_1gui_1_1LockingAction), [mv::gui::NumericalPointAction< NumericalType, NumericalActionType >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#classmv_1_1gui_1_1NumericalPointAction), [mv::gui::NumericalRangeAction< NumericalType, NumericalActionType >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#classmv_1_1gui_1_1NumericalRangeAction), [mv::gui::PixelSelectionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/pixel_selection_action.html#classmv_1_1gui_1_1PixelSelectionAction), [mv::gui::RectangleAction< NumericalRangeActionType >](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#classmv_1_1gui_1_1RectangleAction), [mv::gui::TaskAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/task_action.html#classmv_1_1gui_1_1TaskAction), [mv::gui::TasksListAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/tasks_list_action.html#classmv_1_1gui_1_1TasksListAction), mv::gui::TasksTreeAction, [mv::gui::VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#classmv_1_1gui_1_1VerticalGroupAction), [mv::gui::WindowLevelAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/window_level_action.html#classmv_1_1gui_1_1WindowLevelAction)

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator Horizontal

        enumerator Vertical
        :   Actions are arranged horizontally in the group.

        enumerator NoMargins
        :   Actions are arranged vertically in the group.

        enumerator WithMargins
        :   Do not apply margins to widget layout.

        enumerator Default
        :   Apply standard margins to widget layout.

    enum class LabelSizingType
    :   Label sizing types (in case of vertical group)

        *Values:*

        enumerator Auto

        enumerator Percentage
        :   The widest label in the group action determines the width for the other labels.

        enumerator Fixed
        :   The label width is a percentage of the available width.

            The label width is fixed width in pixels

    Public Functions

    Q\_INVOKABLE GroupAction(QObject \*parent, const QString &title, const bool &expanded = false, const Qt::AlignmentFlag &alignment = Qt::AlignmentFlag::AlignLeft)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Group title
            - **expanded** – Whether the group is initially expanded/collapsed
            - **alignment** – Item alignment

    Qt::AlignmentFlag getAlignment() const
    :   Get item alignment.

        Returns:
        :   Item alignment

    void setExpanded(const bool &expanded)
    :   Set expanded/collapsed.

    void expand()
    :   Expand the group.

    void collapse()
    :   Collapse the group.

    void toggle()
    :   Toggle the group.

    bool isExpanded() const
    :   Get whether the group is expanded.

    bool isCollapsed() const
    :   Get whether the group is collapsed.

    bool isReadOnly() const
    :   Gets the group read-only.

    void setReadOnly(const bool &readOnly)
    :   Sets the group read-only.

        Parameters:
        :   **readOnly** – Whether the group is read-only

    bool getShowLabels() const
    :   Gets whether the group should show labels or not.

    void setShowLabels(bool showLabels)
    :   Sets whether the group should show labels or not.

        Parameters:
        :   **showLabels** – Whether the group should show labels or not

    [StretchAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/stretch_action.html#_CPPv4N2mv3gui13StretchActionE "mv::gui::StretchAction") \*addStretch(std::int32\_t stretch = 1)
    :   Add stretch action to the group (this will add a stretch to the group layout in the widget)

        Parameters:
        :   **stretch** – Layout stretch

        Returns:
        :   Pointer to created stretch action (group action is owner of the action)

    virtual void addAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, std::int32\_t widgetFlags = -1, WidgetConfigurationFunction widgetConfigurationFunction = WidgetConfigurationFunction(), bool load = true)
    :   Add `action` to the group.

        Parameters:
        :   - **action** – Pointer to action to add
            - **widgetFlags** – Action widget flags (default flags if -1)
            - **widgetConfigurationFunction** – When set, overrides the standard widget configuration function in the widget action
            - **load** –

    virtual void removeAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) final
    :   Remove `action` from the group.

        Parameters:
        :   **action** – Pointer to action to add

    virtual void removeAllActions() final
    :   Remove all actions.

    virtual void clear() final
    :   Remove all actions (alias for [GroupAction::removeAllActions()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#classmv_1_1gui_1_1GroupAction_1a77bfff0b189c85f40f7c4adf72933b8c))

    virtual WidgetActions getActions() final
    :   Get actions.

        Returns:
        :   Vector of pointers to actions

    virtual ConstWidgetActions getConstActions() final
    :   Get const actions.

        Returns:
        :   Vector of const pointers to actions

    WidgetFlagsMap getWidgetFlagsMap()
    :   Get widget flags map (maps widget action pointer to widget creation flags)

        Returns:
        :   Widget flags map

    WidgetConfigurationFunctionsMap getWidgetConfigurationFunctionsMap()
    :   Get widget configuration functions map (maps widget action pointer to widget configuration function)

        Returns:
        :   Widget configuration functions map

    [LabelSizingType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupAction15LabelSizingTypeE "mv::gui::GroupAction::LabelSizingType") getLabelSizingType() const
    :   Get the label sizing type.

        Returns:
        :   Label sizing type enum

    void setLabelSizingType(const [LabelSizingType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupAction15LabelSizingTypeE "mv::gui::GroupAction::LabelSizingType") &labelSizingType)
    :   Sets the label sizing type.

        Parameters:
        :   **labelSizingType** – Type of label sizing

    std::uint32\_t getLabelWidthPercentage() const
    :   Gets the user label width in percentages.

    void setLabelWidthPercentage(std::uint32\_t labelWidthPercentage)
    :   Sets the user label width in percentages (sets the label sizing type to [LabelSizingType::Percentage](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#classmv_1_1gui_1_1GroupAction_1a4c4645c84c864b7039dd1e25e42088b8a37be07209f53a5d636d5c904ca9ae64c))

        Parameters:
        :   **labelWidthPercentage** – User label width in percentages

    std::uint32\_t getLabelWidthFixed() const
    :   Gets the user label width in pixels.

    void setLabelWidthFixed(std::uint32\_t labelWidthFixed)
    :   Sets the user label width in pixels (sets the label sizing type to [LabelSizingType::Fixed](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#classmv_1_1gui_1_1GroupAction_1a4c4645c84c864b7039dd1e25e42088b8a4457d440870ad6d42bab9082d9bf9b61))

        Parameters:
        :   **labelWidthFixed** – User label width in pixels

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void actionsChanged(const WidgetActions &actions)
    :   Signals that the actions changed to `actions`.

        Parameters:
        :   **actions** – Update vector of pointers to actions in the group

    void expanded()
    :   Signals that the group got expanded.

    void collapsed()
    :   Signals that the group got collapsed.

    void readOnlyChanged(const bool &readOnly)
    :   Signals that the group read-only status changed to `readOnly`.

        Parameters:
        :   **readOnly** – Read-only status

    void showLabelsChanged(const bool &showLabels)
    :   Signals that the group show labels option changed to `showLabels`.

        Parameters:
        :   **showLabels** – Whether label are visible or not

    void labelSizingTypeChanged(const [LabelSizingType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupAction15LabelSizingTypeE "mv::gui::GroupAction::LabelSizingType") &labelSizingType)
    :   Signals that the label sizing type changed to `labelSizingType`.

        Parameters:
        :   **labelSizingType** – Label sizing type

    void labelWidthPercentageChanged(const std::uint32\_t &labelWidthPercentage)
    :   Signals that the label width in percentages changed to `labelWidthPercentage`.

        Parameters:
        :   **labelWidthPercentage** – Label width in percentages

    void labelWidthFixedChanged(const std::uint32\_t &labelWidthFixed)
    :   Signals that the label width in fixed pixels changed to `labelWidthFixed`.

        Parameters:
        :   **labelWidthFixed** – Label width in fixed pixels

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the group action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    class HorizontalWidget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   Widget class for arranging the groups actions horizontally.

        Protected Functions

        HorizontalWidget(QWidget \*parent, [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **groupAction** – Pointer to group action which creates the widget
                - **widgetFlags** – Widget flags for the configuration of the widget (type)

        ~HorizontalWidget() override
        :   Destructor.

        Friends

        *friend class* GroupAction

    class VerticalWidget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   Widget class for arranging the groups actions vertically.

        Protected Functions

        VerticalWidget(QWidget \*parent, [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **groupAction** – Pointer to group action which creates the widget
                - **widgetFlags** – Widget flags for the configuration of the widget (type)

        ~VerticalWidget() override
        :   Destructor.

        Protected Attributes

        QGridLayout \_layout
        :   Pointer to group action which created the widget.

        Friends

        *friend class* GroupAction
