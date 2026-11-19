# ToolbarAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/toolbar_action.html

**Documentation path:** `api/core/gui/actions/grouping/toolbar_action.html`

---

# ToolbarAction

**Qualified name:** `mv::gui::ToolbarAction`

class ToolbarAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Toolbar action class.

    Base toolbar action for displaying actions

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::HorizontalToolbarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html#classmv_1_1gui_1_1HorizontalToolbarAction), [mv::gui::VerticalToolbarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_toolbar_action.html#classmv_1_1gui_1_1VerticalToolbarAction)

    Public Functions

    Q\_INVOKABLE ToolbarAction(QObject \*parent, const QString &title, const Qt::AlignmentFlag &alignment = Qt::AlignmentFlag::AlignLeft)
    :   Construct with `parent` and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **alignment** – Item alignment

    virtual void addAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, const std::int32\_t &autoExpandPriority = -1, std::int32\_t widgetFlags = -1, WidgetConfigurationFunction widgetConfigurationFunction = WidgetConfigurationFunction()) final
    :   Add `action` to the group.

        Parameters:
        :   - **action** – Pointer to action to add
            - **autoExpandPriority** – Priority with which the action should be auto-expanded
            - **widgetFlags** – Action widget flags (default flags if -1)

    virtual void removeAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) final
    :   Remove `action` from the group.

        Parameters:
        :   **action** – Pointer to action to add

    virtual [StretchAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/stretch_action.html#_CPPv4N2mv3gui13StretchActionE "mv::gui::StretchAction") \*addStretch(std::int32\_t stretch = 1) final
    :   Add stretch action to the group with `stretch` factor.

        Parameters:
        :   **stretch** – Stretch factor

        Returns:
        :   Pointer to stretch action (the toolbar remains the owner)

    virtual WidgetActions getActions() final
    :   Get actions.

        Returns:
        :   Vector of pointers to actions

    virtual void setActionAutoExpandPriority(const [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, const std::int32\_t &autoExpandPriority) final
    :   Set `action` auto expand priority to `autoExpandPriority`.

        Parameters:
        :   - **action** – Pointer to action for which to set the auto expand priority
            - **autoExpandPriority** – Priority with which the action should be auto-expanded

    void actionWidgetsChanged(ActionItemsMap &actionWidgets)
    :   Signals that the action widgets changed to `actionWidgets`.

        Parameters:
        :   **actionWidgets** – New action widgets

    void layoutInvalidated()
    :   Signals that the layout has become invalid due to changes in auto expand priorities or change in widget size.

    Protected Functions

    virtual [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") &getGroupAction() final
    :   Get group action.

        Returns:
        :   Reference to group action

    virtual ActionItems &getActionItems()
    :   Get action items for the toolbar.

        Returns:
        :   Vector of action items

    Protected Static Attributes

    static constexpr std::int32\_t CONTENTS\_MARGIN = 4
    :   Maps action pointer to action item pointer.
