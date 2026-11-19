# WindowLevelAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/window_level_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/window_level_action.html`

---

# WindowLevelAction

**Qualified name:** `mv::gui::WindowLevelAction`

class WindowLevelAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Window/level settings action class.

    Action class for window/level settings

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE WindowLevelAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    inline [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction") &getWindowAction()
    :   Action getters.

    void changed([WindowLevelAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/window_level_action.html#_CPPv4N2mv3gui17WindowLevelActionE "mv::gui::WindowLevelAction") &windowLevelAction)
    :   Signals the window/level changed.

    Protected Functions

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive) override
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions

    Protected Attributes

    [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction") \_levelAction
    :   Window action.

    Friends

    *friend class* AbstractActionsManager
