# StatusAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/status_action.html`

---

# StatusAction

**Qualified name:** `mv::gui::StatusAction`

`StatusAction` presents a short informational message and severity through a disabled line edit. The class is marked work in progress; test severity transitions and transient-message timing before using it as persistent plugin UI.

For its role relative to notifications, workflows, logging, and plugin status-bar items, see [Status-bar content and interaction](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/content_and_interaction.html).

class StatusAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Status action class.

    Action class for reporting status

    Note: This action is a WIP

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator LineEdit

        enumerator Default
        :   Status is logged in a line edit.

    enum Status
    :   Status enumeration.

        *Values:*

        enumerator Undefined

        enumerator Info
        :   There is no status information.

        enumerator Warning
        :   Normal info.

        enumerator Error
        :   Warning.

            An error occurred

    Public Functions

    Q\_INVOKABLE StatusAction(QObject \*parent, const QString &title, const [Status](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6StatusE "mv::gui::StatusAction::Status") &status = [Status](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6StatusE "mv::gui::StatusAction::Status")::[Undefined](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6Status9UndefinedE "mv::gui::StatusAction::Status::Undefined"), const QString &message = "")
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **status** – Status type
            - **message** – Status message

    void initialize(const [Status](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6StatusE "mv::gui::StatusAction::Status") &status = [Status](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6StatusE "mv::gui::StatusAction::Status")::[Info](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6Status4InfoE "mv::gui::StatusAction::Status::Info"), const QString &message = "")
    :   Initialize the status action.

        Parameters:
        :   - **status** – Status type
            - **message** – Status message

    [Status](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6StatusE "mv::gui::StatusAction::Status") getStatus() const
    :   Get status type.

        Returns:
        :   Status type

    void setStatus(const [Status](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6StatusE "mv::gui::StatusAction::Status") &status)
    :   Set status type.

        Parameters:
        :   **status** – Status type

    QString getMessage() const
    :   Get status message.

        Returns:
        :   Status message

    void setMessage(const QString &message, bool vanish = false)
    :   Set status message.

        Parameters:
        :   - **message** – Status message
            - **vanish** – Whether to reset the message after the disappear message delay

    void statusChanged(const [Status](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusAction6StatusE "mv::gui::StatusAction::Status") &status)
    :   Signals that the status changed.

        Parameters:
        :   **status** – Status

    void messageChanged(const QString &message)
    :   Signals that the message changed.

        Parameters:
        :   **message** – Message that changed

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the status action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget

    Protected Attributes

    QString \_message
    :   Current status enum.

    Protected Static Attributes

    static constexpr std::int32\_t MESSAGE\_DISAPPEAR\_INTERVAL = 1500
    :   Status message.

    class LineEditWidget : public QLineEdit
    :   Line edit widget class for status action.

        Protected Functions

        LineEditWidget(QWidget \*parent, [StatusAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html#_CPPv4N2mv3gui12StatusActionE "mv::gui::StatusAction") \*statusAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **statusAction** – Pointer to status action
                - **widgetFlags** – Widget flags for the configuration of the widget

        Protected Attributes

        QAction \_trailingAction
        :   Pointer to status action.

        Friends

        *friend class* StatusAction
