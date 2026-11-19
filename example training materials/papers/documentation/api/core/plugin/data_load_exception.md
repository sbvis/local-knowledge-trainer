# DataLoadException

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/data_load_exception.html

**Documentation path:** `api/core/plugin/data_load_exception.html`

---

# DataLoadException

**Qualified name:** `mv::plugin::DataLoadException`

`DataLoadException` represents failure to load a particular file. Its `what()` text combines the file path with the technical reason, allowing the UI boundary that owns the load operation to present or record a useful cause.

Throwing the exception does not itself notify the user. Catch or propagate it through the execution mechanism that owns the loader operation, following the [diagnostics guidance](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/index.html). Avoid duplicating the same failure in a log, notification, and dialog.

struct DataLoadException : public std::exception
