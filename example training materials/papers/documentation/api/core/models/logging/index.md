# Logging

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/logging/index.html

**Documentation path:** `api/core/models/logging/index.html`

---

# Logging

These models present the structured records captured by the application [Logger](https://manivault.readthedocs.io/en/latest/api/core/util/logging/logger.html). `LoggingModel` incrementally exposes new records, while `LoggingFilterModel` supplies severity and text filtering plus sorting for user interfaces.

The models do not form the plugin logging entry point. Plugins emit Qt log messages; the global logger captures them and owns the underlying records. See [Core logging](https://manivault.readthedocs.io/en/latest/api/core/util/logging/index.html) for the complete pipeline.

- [LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html)
- [LoggingFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_filter_model.html)
