# Managers

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/index.html

**Documentation path:** `api/core/managers/index.html`

---

# Managers

Managers are central coordination components in ManiVault. They encapsulate ownership, lifecycle management, and access to related subsystems such as actions, data, projects, and application state.

Rather than exposing raw collections or global services, ManiVault uses manager classes to provide a well-defined interface for querying, modifying, and observing system-wide resources. This helps keep responsibilities clearly separated and enables plugins and applications to interact with the platform in a controlled and consistent manner.

Each manager typically focuses on a specific domain and exposes a stable API for that domain. The following sections document the available manager classes and their public interfaces.

- [AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html)
- [AbstractActionsManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_actions_manager.html)
- [AbstractDataHierarchyManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_hierarchy_manager.html)
- [AbstractDataManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html)
- [AbstractErrorManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_manager.html)
- [AbstractErrorLogger](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_logger.html)
- [AbstractEventManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_event_manager.html)
- [AbstractHelpManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_help_manager.html)
- [AbstractPluginManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html)
- [AbstractProjectManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html)
- [AbstractScriptingManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_scripting_manager.html)
- [AbstractSettingsManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_settings_manager.html)
- [AbstractTaskManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_task_manager.html)
- [AbstractThemeManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_theme_manager.html)
