# Notifications, logging, errors, and diagnostics

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/index.html

**Documentation path:** `development/building_plugins/diagnostics/index.html`

---

# Notifications, logging, errors, and diagnostics

Good diagnostics separate the user-facing outcome from the evidence needed to understand it. Choose the least intrusive channel that matches the situation, preserve structured context as an error crosses layers, and present a failure only once at the owning boundary.

- [Choosing a reporting channel](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/choosing_a_channel.html)
- [Notifications and status](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/notifications_and_status.html)
- [Logging diagnostic evidence](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/logging.html)
- [Exceptions and diagnostic context](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/exceptions.html)
- [Failures in callbacks, tasks, and workflows](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/asynchronous_failures.html)
- [Diagnostic checklist](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/troubleshooting.html)

For exact signatures, see [notifications](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/index.html), [logging](https://manivault.readthedocs.io/en/latest/api/core/util/logging/index.html), [exceptions](https://manivault.readthedocs.io/en/latest/api/core/util/exception/index.html), and the [error manager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_manager.html).
