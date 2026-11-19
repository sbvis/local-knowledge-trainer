# StretchAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/stretch_action.html

**Documentation path:** `api/core/gui/actions/grouping/stretch_action.html`

---

# StretchAction

**Qualified name:** `mv::gui::StretchAction`

class StretchAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Stretch action class.

    Action class for adding layout stretch to group actions (does not have a widget)

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE StretchAction(QObject \*parent, const QString &title, std::int32\_t stretch = 1)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Group title
            - **stretch** – Layout stretch

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

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
