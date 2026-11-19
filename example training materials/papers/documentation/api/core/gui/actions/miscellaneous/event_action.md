# EventAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/event_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/event_action.html`

---

# EventAction

**Qualified name:** `mv::gui::EventAction`

class EventAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   Event action class.

    For emitting generic events

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE EventAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void triggerEvent(const QString &eventType, const QVariant &eventData)
    :   Triggers an event of `eventType` with `eventData`.

        Parameters:
        :   - **eventType** – The type of event
            - **eventData** – Event data

    void eventTriggered(const QString &eventType, const QVariant &eventData)
    :   Signals that an event of `eventType` with `eventData` has been triggered.

        Parameters:
        :   - **eventType** – The type of event
            - **eventData** – Event data

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
