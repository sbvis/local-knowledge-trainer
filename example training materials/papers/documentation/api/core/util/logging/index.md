# Logging

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/logging/index.html

**Documentation path:** `api/core/util/logging/index.html`

---

# Logging

ManiVault installs a global Qt message handler that turns diagnostic output into structured [MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html) entries held by [Logger](https://manivault.readthedocs.io/en/latest/api/core/util/logging/logger.html). The [logging models](https://manivault.readthedocs.io/en/latest/api/core/models/logging/index.html) expose those records to application interfaces for display, filtering, and sorting.

Plugin code normally writes through Qt’s `qDebug()`, `qInfo()`, `qWarning()`, and `qCritical()` functions. It should not append records to the global logger or manipulate the presentation models directly. See [Logging diagnostic evidence](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/logging.html) for severity selection, useful context, and privacy guidance.

## Logging and error reporting are different paths

This logger records local diagnostic messages. Optional reporting of handled exceptions or crashes is coordinated by [AbstractErrorManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_manager.html) and a consent-aware [AbstractErrorLogger](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html) backend. Writing a Qt log message does not replace user-facing error handling, and it should not be treated as an instruction to send telemetry.

- [MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html)
- [Logger](https://manivault.readthedocs.io/en/latest/api/core/util/logging/logger.html)
