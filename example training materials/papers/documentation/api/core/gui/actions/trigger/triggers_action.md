# TriggersAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html

**Documentation path:** `api/core/gui/actions/trigger/triggers_action.html`

---

# TriggersAction

**Qualified name:** `mv::gui::TriggersAction`

class TriggersAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Triggers action class.

    Action class for multiple triggers

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator Horizontal

        enumerator Vertical
        :   [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#structmv_1_1gui_1_1TriggersAction_1_1Trigger) buttons are distributed in a horizontal layout.

        enumerator Default
        :   [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#structmv_1_1gui_1_1TriggersAction_1_1Trigger) buttons are distributed in a vertical layout.

    Public Functions

    TriggersAction(QObject \*parent, const QString &title, const QVector<[Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersAction7TriggerE "mv::gui::TriggersAction::Trigger")> &triggers = QVector<[Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersAction7TriggerE "mv::gui::TriggersAction::Trigger")>())
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **triggers** – Vector of triggers

    const QVector<[Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersAction7TriggerE "mv::gui::TriggersAction::Trigger")> &getTriggers() const
    :   Get triggers.

        Returns:
        :   Vector of triggers

    void setTriggers(const QVector<[Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersAction7TriggerE "mv::gui::TriggersAction::Trigger")> &triggers)
    :   Set triggers.

        Parameters:
        :   **triggers** – Vector of triggers

    void setTriggerText(std::int32\_t triggerIndex, const QString &text)
    :   Set trigger text.

        Parameters:
        :   - **triggerIndex** – Index of the trigger
            - **text** – [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#structmv_1_1gui_1_1TriggersAction_1_1Trigger) text

    void setTriggerTooltip(std::int32\_t triggerIndex, const QString &tooltip)
    :   Set trigger tooltip.

        Parameters:
        :   - **triggerIndex** – Index of the trigger
            - **tooltip** – [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#structmv_1_1gui_1_1TriggersAction_1_1Trigger) tooltip

    void setTriggerEnabled(std::int32\_t triggerIndex, const bool &enabled)
    :   Set trigger enabled.

        Parameters:
        :   - **triggerIndex** – Index of the trigger
            - **enabled** – [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#structmv_1_1gui_1_1TriggersAction_1_1Trigger) enabled

    void triggersChanged(const QVector<[Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersAction7TriggerE "mv::gui::TriggersAction::Trigger")> &triggers)
    :   Signals that the triggers changed.

        Parameters:
        :   **triggers** – Triggers

    void triggerChanged(std::int32\_t triggerIndex, const [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersAction7TriggerE "mv::gui::TriggersAction::Trigger") &trigger)
    :   Signals that a trigger changed.

        Parameters:
        :   - **triggerIndex** – Index of the trigger
            - **trigger** – [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#structmv_1_1gui_1_1TriggersAction_1_1Trigger) that changed

    void triggered(std::int32\_t triggerIndex)
    :   Signals that a trigger is executed.

        Parameters:
        :   **triggerIndex** – Index of the triggered

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the triggers action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#classmv_1_1gui_1_1TriggersAction_1_1Widget) flags for the configuration of the widget

    QPushButton \*createTriggerPushButton(const [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersAction7TriggerE "mv::gui::TriggersAction::Trigger") &trigger)
    :   Create trigger push button.

        Parameters:
        :   **trigger** – [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#structmv_1_1gui_1_1TriggersAction_1_1Trigger) for the push button

        Returns:
        :   Pointer to push button

    struct Trigger
    :   [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#structmv_1_1gui_1_1TriggersAction_1_1Trigger) for push button.

        Public Functions

        inline Trigger(const QString &text, const QString &tooltip, bool enabled = true)
        :   Constructor.

            Parameters:
            :   - **text** – Push button text
                - **tooltip** – Push button tooltip
                - **enabled** – Push button enabled

        inline bool operator==(const [Trigger](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersAction7TriggerE "mv::gui::TriggersAction::Trigger") &rhs) const
        :   Comparison operator for two triggers (compares the identifiers)

            Parameters:
            :   **rhs** – Right hand sign of the comparison

        Public Members

        bool \_enabled
        :   Unique trigger identifier.

        QString \_text
        :   Push button read-only.

        QString \_tooltip
        :   Push button text.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#classmv_1_1gui_1_1TriggersAction_1_1Widget) class for triggers action.

        Protected Functions

        Widget(QWidget \*parent, [TriggersAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#_CPPv4N2mv3gui14TriggersActionE "mv::gui::TriggersAction") \*triggersAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **triggersAction** – Pointer to triggers action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/triggers_action.html#classmv_1_1gui_1_1TriggersAction_1_1Widget) flags for the configuration of the widget

        Friends

        *friend class* TriggersAction
