# Exception presentation helpers

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/exception/exception_helpers.html

**Documentation path:** `api/core/util/exception/exception_helpers.html`

---

# Exception presentation helpers

The overloads below show a modal error dialog for a reason, standard exception, or `ManiVaultException`. Use them only at the GUI boundary that consumes the failure.

void mv::util::exceptionMessageBox(const QString &title, const QString &reason, QWidget \*parent = nullptr)
:   Shows a modal exception dialog with a custom reason.

    The dialog displays the supplied reason, includes technical stack-trace details when available from the active error manager, and offers a copy action for the full report.

    Parameters:
    :   - **title** – Dialog title.
        - **reason** – Human-readable explanation of the error.
        - **parent** – Optional parent widget.

void mv::util::exceptionMessageBox(const QString &title, const std::exception &exception, QWidget \*parent = nullptr)
:   Shows a modal exception dialog for a standard C++ exception.

    Parameters:
    :   - **title** – Dialog title.
        - **exception** – Exception whose what() text is shown as the error reason.
        - **parent** – Optional parent widget.

void mv::util::exceptionMessageBox(const QString &title, const [ManiVaultException](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv18ManiVaultExceptionE "mv::ManiVaultException") &exception, QWidget \*parent = nullptr)
:   Shows a modal exception dialog for a ManiVault exception.

    The dialog uses the exception message and stack trace carried by the [ManiVaultException](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#classmv_1_1ManiVaultException) instance.

    Parameters:
    :   - **title** – Dialog title.
        - **exception** – ManiVault exception to display.
        - **parent** – Optional parent widget.
