# AbstractErrorLogger

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html

**Documentation path:** `api/core/managers/abstract_error_logger.html`

---

# AbstractErrorLogger

**Qualified name:** `mv::AbstractErrorLogger`

`AbstractErrorLogger` is the application-side base class for an optional error-reporting backend. It receives eligible handled exceptions and user feedback from [AbstractErrorManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_manager.html), and it follows the global opt-in and enablement settings exposed by that manager.

This is an application integration point, not the routine logging API for plugins. Plugin code should use Qt logging for diagnostic evidence and report user-visible failures at the boundary that owns the operation. See [Notifications, logging, errors, and diagnostics](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/index.html) for that decision model.

Concrete backends implement initialization, startup, shutdown, and DSN validation. Initialization is deliberately divided into `beginInitialization()` and `endInitialization()` so the base class can connect shared settings and track readiness around backend-specific setup.

class AbstractErrorLogger : public QObject
:   Abstract error logger class.

    Base class for logging errors.

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractErrorLogger(const QString &loggerName, QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   - **loggerName** – Name of the logger (e.g. Sentry)
            - **parent** – Pointer to parent object

    virtual void initialize() = 0
    :   Initializes the error logger and connects it to the global error-reporting settings.

    inline virtual void reportHandledException(const QString &title, const QString &exceptionType, const QString &reason, util::[SeverityLevel](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv4util13SeverityLevelE "mv::util::SeverityLevel") severity, const util::StackTrace &stackTrace, const QString &diagnosticId = {}, const QString &where = {})
    :   Reports an exception that was caught and presented to the user.

        Parameters:
        :   - **title** – User-facing title of the exception dialog.
            - **exceptionType** – Exception class or category name.
            - **reason** – Technical reason supplied by the exception.
            - **severity** – Severity assigned to the exception.
            - **stackTrace** – Structured stack trace captured for the exception.
            - **diagnosticId** – Identifier shown to the user for support correlation.
            - **where** – Optional source context in which the exception was handled.

    inline virtual bool submitUserFeedback(const QString &type, const QString &message, const QString &email)
    :   Sends standalone user feedback when the logger is available.

        Parameters:
        :   - **type** – Feedback category, such as a problem report or feature request.
            - **message** – User-provided feedback description.
            - **email** – Optional email address for follow-up.

        Returns:
        :   Boolean determining whether the feedback was accepted for transmission.

    inline QString getLoggerName() const
    :   Get the logger name.

        Returns:
        :   Logger name

    inline void requestStart()
    :   Starts the error logger when the user has opted in and reporting is enabled.

    inline void requestStop()
    :   Stops the error logger and completes its shutdown procedure.

    inline bool isInitialized() const
    :   Get whether the error logger is initialized or not.

        Returns:
        :   Boolean determining whether the error logger is initialized or not

    inline void addNotification(const QString &name, const [Notification](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html#_CPPv4N2mv19AbstractErrorLogger12NotificationE "mv::AbstractErrorLogger::Notification") &notification)
    :   Adds or replaces a delayed user notification.

        Parameters:
        :   - **name** – Name of the notification
            - **notification** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html#structmv_1_1AbstractErrorLogger_1_1Notification)

    inline virtual void beginInitialization()
    :   Begins initialization and connects common error-reporting setting notifications.

    inline virtual void endInitialization()
    :   Completes initialization and marks the logger as initialized.

    Protected Static Functions

    static inline gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getUserHasOptedAction()
    :   Get action for asking the user for consent to log errors.

    static inline gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getEnabledAction()
    :   Get action for user has opted.

    static inline gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") &getDsnAction()
    :   Get action for logging enabled.

    static inline gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getShowCrashReportDialogAction()
    :   Get action for logging data source name (DSN)

    struct Notification
    :   [Notification](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html#structmv_1_1AbstractErrorLogger_1_1Notification) struct.

        Public Members

        QString \_title
        :   Title of the notification.

        QString \_message
        :   Message of the notification.

        QIcon \_icon
        :   Icon of the notification.

        std::int32\_t \_delay = 0
        :   Delay of the notification.
