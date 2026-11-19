# Plugins

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/plugins/index.html

**Documentation path:** `api/core/models/plugins/index.html`

---

# Plugins

**ManiVault** manages the lifetime of all plugins through the [`mv::AbstractPluginManager`](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html#_CPPv4N2mv21AbstractPluginManagerE "mv::AbstractPluginManager"). Plugins are tracked in dedicated **list** and **tree** models, which are primarily used by the UI to present plugin state and structure (for example in the plugin browser). The model classes below are for storing and filtering plugins.

Note

This API is **stable** and intended for use by **core developers**. Plugin developers typically do not need to interact with it directly, as it is fully wrapped by the plugins manager.

- [AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html)
- [PluginsTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_tree_model.html)
- [PluginsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_list_model.html)
- [PluginsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_filter_model.html)
