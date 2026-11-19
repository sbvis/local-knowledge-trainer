# AbstractErrorManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_manager.html

**Documentation path:** `api/core/managers/abstract_error_manager.html`

---

# AbstractErrorManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the errors manager
mv::errors().getDebugStackTrace();
```

The error manager supplies application-level stack capture, consent and reporting configuration, handled-exception reporting, and user-feedback submission. An application may connect it to an [AbstractErrorLogger](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html) backend.

This reporting path is distinct from the local [Qt logging pipeline](https://manivault.readthedocs.io/en/latest/api/core/util/logging/index.html). Plugin failure-handling patterns are covered in [Notifications, logging, errors, and diagnostics](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/index.html).

**Qualified name:** `mv::AbstractErrorManager`

class AbstractErrorManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract error manager class.

    Base abstract error manager class

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractErrorManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void showErrorLoggingConsentDialog() = 0
    :   Shows the error-reporting consent dialog.

    inline virtual QString getFormattedDebugStackTrace() const
    :   Gets a formatted stack trace for debugging purposes.

        Returns a human-readable stack trace of the current execution point. The default implementation returns an empty string, indicating that stack trace generation is not supported or has not been implemented.

        Derived classes may override this function to provide platform- or application-specific stack trace generation using the available debugging facilities.

        Returns:
        :   A formatted stack trace, or an empty string if unavailable.

    inline virtual util::StackTrace getDebugStackTrace() const
    :   Gets a structured stack trace for debugging purposes.

        Returns stack frames describing the current execution point. The default implementation returns an empty stack trace, indicating that stack trace capture is not supported or has not been implemented by the active error manager.

        Derived classes may override this function to provide platform- or application-specific stack trace collection.

        Returns:
        :   Stack trace frames, or an empty stack trace if unavailable.

    inline virtual void reportHandledException(const QString &title, const QString &exceptionType, const QString &reason, util::[SeverityLevel](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv4util13SeverityLevelE "mv::util::SeverityLevel") severity, const util::StackTrace &stackTrace, const QString &diagnosticId = {}, const QString &where = {})
    :   Reports an eligible caught exception to the active error logger.

        Parameters:
        :   - **title** – User-facing title of the exception dialog.
            - **exceptionType** – Exception class or category name.
            - **reason** – Technical reason supplied by the exception.
            - **severity** – Severity assigned to the exception.
            - **stackTrace** – Structured stack trace captured for the exception.
            - **diagnosticId** – Identifier shown to the user for support correlation.
            - **where** – Optional source context in which the exception was handled.

    inline virtual bool submitUserFeedback(const QString &type, const QString &message, const QString &email)
    :   Sends a standalone problem report or feature request to the active error logger.

        Parameters:
        :   - **type** – Feedback category, such as a problem report or feature request.
            - **message** – User-provided feedback description.
            - **email** – Optional email address for follow-up.

        Returns:
        :   Boolean determining whether the feedback was accepted for transmission.

    inline virtual const gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getLoggingUserHasOptedAction() const
    :   Get action for asking the user for consent to log errors.

    inline virtual const gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getLoggingEnabledAction() const
    :   Get action for user has opted.

    inline virtual const gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") &getLoggingDsnAction() const
    :   Get action for logging enabled.

    inline virtual const gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getLoggingReportHandledExceptionsAction() const
    :   Get action for logging data source name (DSN)

    inline virtual const gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getLoggingShowCrashReportDialogAction() const
    :   Get action for reporting handled exceptions.

    Protected Functions

    inline [AbstractErrorLogger](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html#_CPPv4N2mv19AbstractErrorLoggerE "mv::AbstractErrorLogger") \*getErrorLogger() const
    :   Get the error logger.

        Returns:
        :   Pointer to the error logger (maybe nullptr)

    inline void setErrorLogger([AbstractErrorLogger](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html#_CPPv4N2mv19AbstractErrorLoggerE "mv::AbstractErrorLogger") \*errorLogger)
    :   Set the error logger to `errorLogger`.

        Parameters:
        :   **errorLogger** – Pointer to the error logger (maybe nullptr)

    virtual gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") &getLoggingAskConsentDialogAction() = 0
    :   Get action for showing a crash report dialog when the application fails.

    virtual gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getLoggingUserHasOptedAction() = 0
    :   Get action for asking the user for consent to log errors.

    virtual gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getLoggingEnabledAction() = 0
    :   Get action for user has opted.

    virtual gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") &getLoggingDsnAction() = 0
    :   Get action for logging enabled.

    virtual gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getLoggingReportHandledExceptionsAction() = 0
    :   Get action for logging data source name (DSN)

    virtual gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getLoggingShowCrashReportDialogAction() = 0
    :   Get action for reporting handled exceptions.
