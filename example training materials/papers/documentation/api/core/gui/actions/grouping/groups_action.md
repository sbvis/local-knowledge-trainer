# GroupsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html

**Documentation path:** `api/core/gui/actions/grouping/groups_action.html`

---

# GroupsAction

**Qualified name:** `mv::gui::GroupsAction`

class GroupsAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Groups action class.

    Contains a list of group actions and displays them in an accordion widget

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::ApplicationConfigurationAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/application_configuration_action.html#classmv_1_1gui_1_1ApplicationConfigurationAction)

    Public Types

    enum WidgetFlag
    :   Describes the widget configurations.

        *Values:*

        enumerator Filtering

        enumerator Expansion
        :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#classmv_1_1gui_1_1GroupsAction_1_1Widget) contains UI for filtering group actions.

        enumerator Default
        :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#classmv_1_1gui_1_1GroupsAction_1_1Widget) contains UI to expand/collapse all actions.

    Public Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the groups action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#classmv_1_1gui_1_1GroupsAction_1_1Widget) flags for the configuration of the widget (type)

    Q\_INVOKABLE GroupsAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the groups action

    void addGroupAction([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction, bool visible = true)
    :   Appends a group action.

        Parameters:
        :   - **groupAction** – Group action to add
            - **visible** – Whether the group action is visible or not

    void removeGroupAction([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Removes a group action.

        Parameters:
        :   **groupAction** – Group action to remove

    void setGroupActions(const GroupActions &groupActions)
    :   Set group actions (overwrites existing group actions)

        Parameters:
        :   **groupActions** – Vector of pointers to group actions

    void resetGroupActions()
    :   Reset group actions to default.

    const GroupActions &getGroupActions() const
    :   Get group actions.

    bool canExpandAll() const
    :   Get whether one (or more) groups can be expanded.

        Returns:
        :   Whether one (or more) groups can be expanded

    void expandAll()
    :   Expand all group actions.

    bool canCollapseAll() const
    :   Get whether one (or more) groups can be expanded.

        Returns:
        :   Whether one (or more) groups can be expanded

    void collapseAll()
    :   Collapse all group actions.

    QVector<bool> getExpansions(bool visibleOnly = true) const
    :   Get groups expansion states.

        Parameters:
        :   **visibleOnly** – Visible group actions only

        Returns:
        :   Vector of booleans, indicating whether a group is expanded or collapsed

    std::int32\_t getNumberOfExpandedGroupActions(bool visibleOnly = true) const
    :   Get number of expanded group actions.

        Parameters:
        :   **visibleOnly** – Visible group actions only

        Returns:
        :   Number of expanded group actions

    std::int32\_t getNumberOfVisibleGroupActions() const
    :   Get number of visible group actions.

        Returns:
        :   Number of visible group actions

    void setGroupActionVisibility([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction, bool visible)
    :   Hide group action.

        Parameters:
        :   - **groupAction** – Pointer to group action
            - **visible** – Whether the group action is visible

    void showGroupAction([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Show group action.

        Parameters:
        :   **groupAction** – Pointer to group action

    void showAllGroupActions()
    :   Hide all group actions.

    void hideGroupAction([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Hide group action.

        Parameters:
        :   **groupAction** – Pointer to group action

    void hideAllGroupActions()
    :   Hide all group actions.

    bool isGroupActionVisible([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction) const
    :   Get whether the group action is visible.

        Returns:
        :   Whether the group action is visible

    bool isGroupActionHidden([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction) const
    :   Get whether the group action is hidden.

        Returns:
        :   Whether the group action is hidden

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") &getUpdateTask()
    :   Get update task.

        Returns:
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) for reporting update progress

    void groupActionAdded([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Signals that a group action was added.

        Parameters:
        :   **groupAction** – Group action that was added

    void groupActionRemoved([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Signals that a group action was removed.

        Parameters:
        :   **groupAction** – Group action that was removed

    void groupActionExpanded([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Signals that a group action got expanded.

        Parameters:
        :   **groupAction** – Group action that got expanded

    void groupActionCollapsed([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Signals that a group action got collapsed.

        Parameters:
        :   **groupAction** – Group action that got collapsed

    void groupActionShown([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Signals that a group action got shown.

        Parameters:
        :   **groupAction** – Group action that got shown

    void groupActionHidden([GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \*groupAction)
    :   Signals that a group action got hidden.

        Parameters:
        :   **groupAction** – Group action that got hidden

    Protected Attributes

    QMap<[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")\*, bool> \_visibility
    :   Pointers to group actions.

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \_updateTask
    :   Group action visibility.

    class TreeWidget : public QTreeWidget
    :   Tree widget class Implemented solely to be able to update geometries by hand.

        Public Functions

        inline void updateGeometries()
        :   Update item geometries.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   Group widget class for widget action groups.

        Public Functions

        inline [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") &getFilteredActionsAction()
        :   Get action that contains filtered actions.

            Returns:
            :   Reference to filtered actions action

        Protected Functions

        Widget(QWidget \*parent, [GroupsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#_CPPv4N2mv3gui12GroupsActionE "mv::gui::GroupsAction") \*groupsAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **groupsAction** – Pointer to groups action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#classmv_1_1gui_1_1GroupsAction_1_1Widget) flags for the configuration of the widget

        void createToolbar(const std::int32\_t &widgetFlags)
        :   Create toolbar for interaction with the groups.

            Parameters:
            :   **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#classmv_1_1gui_1_1GroupsAction_1_1Widget) flags for the configuration of the widget

        void createTreeWidget(const std::int32\_t &widgetFlags)
        :   Create tree widget for display of the groups.

            Parameters:
            :   **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#classmv_1_1gui_1_1GroupsAction_1_1Widget) flags for the configuration of the widget

        void updateToolbar()
        :   Updates the state of the toolbar.

        void updateFiltering()
        :   Updates the property filtering.

        Protected Attributes

        QVBoxLayout \_layout
        :   Pointer to groups action.

        [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") \_filteredActionsAction
        :   Main layout.

        [HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction") \_toolbarAction
        :   Group action for filtered actions.

        [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_filterAction
        :   Toolbar action.

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_expandAllAction
        :   Filter action.

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_collapseAllAction
        :   Expand all datasets action.

        [TreeWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#_CPPv4N2mv3gui12GroupsAction10TreeWidgetE "mv::gui::GroupsAction::TreeWidget") \_treeWidget
        :   Collapse all datasets action.

        QMap<[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")\*, GroupSectionTreeItem\*> \_groupSectionTreeItems
        :   Tree widget for display of the groups.

        Friends

        *friend class* GroupsAction
