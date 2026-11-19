# ManiVault exception

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html

**Documentation path:** `api/core/util/exception/mani_vault_exception.html`

---

# ManiVault exception

`ManiVaultException` extends `std::runtime_error` with structured application diagnostic context.

class ManiVaultException : public std::runtime\_error
:   Exception type carrying ManiVault diagnostic context.

    [ManiVaultException](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#classmv_1_1ManiVaultException) extends std::runtime\_error with severity, user-facing message text, technical cause, source/context location, structured details, a diagnostic identifier, and captured debug stack trace metadata. It is used when errors need to be shown to users and reported with enough context for diagnostics.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Subclassed by [mv::AbstractProjectManager::ProjectDownloadException](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#classmv_1_1AbstractProjectManager_1_1ProjectDownloadException)

    Public Functions

    ManiVaultException(util::[SeverityLevel](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv4util13SeverityLevelE "mv::util::SeverityLevel") severity, QString message, QString what, QString where = {}, QVariantMap details = {}, std::source\_location location = std::source\_location::current())
    :   Constructs a ManiVault exception.

        The constructor stores source-location metadata, creates a diagnostic id, and appends the current debug stack trace to the details map.

        Parameters:
        :   - **severity** – Severity associated with the exception.
            - **message** – User-facing exception message.
            - **what** – Technical cause or short diagnostic description.
            - **where** – Optional source or workflow context where the error occurred.
            - **details** – Optional structured diagnostic details.
            - **location** – C++ source location captured at the throw site.

    [ManiVaultException](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv18ManiVaultExceptionE "mv::ManiVaultException") withAddedDetails(const QVariantMap &additionalDetails) const
    :   Returns a copy of this exception with additional details.

        Additional detail keys overwrite existing keys with the same name.

        Parameters:
        :   **additionalDetails** – Details to merge into the copied exception.

        Returns:
        :   New exception containing the merged details.

    util::[SeverityLevel](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv4util13SeverityLevelE "mv::util::SeverityLevel") getSeverity() const
    :   Returns the exception severity.

        Returns:
        :   Severity level.

    QString getMessage() const
    :   Returns the user-facing exception message.

        Returns:
        :   Exception message.

    QString getWhat() const
    :   Returns the technical exception cause.

        Returns:
        :   Technical exception text.

    QString getWhere() const
    :   Returns the source or context where the exception occurred.

        Returns:
        :   Context location string.

    QVariantMap getDetails() const
    :   Returns structured diagnostic details.

        Returns:
        :   Diagnostic details map.

    QUuid getDiagnosticId() const
    :   Returns the unique diagnostic identifier.

        Returns:
        :   Diagnostic id.

    util::StackTrace getStackTrace() const
    :   Returns the captured debug stack trace.

        Returns:
        :   Stack trace frames.

enum class mv::util::SeverityLevel
:   Severity level.

    Enum for representing the severity level of an event

    *Values:*

    enumerator Info

    enumerator Warning

    enumerator Error

    enumerator Fatal
