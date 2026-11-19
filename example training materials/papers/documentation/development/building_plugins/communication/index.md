# Plugin communication and creation triggers

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/index.html

**Documentation path:** `development/building_plugins/communication/index.html`

---

# Plugin communication and creation triggers

Plugins should communicate through stable core abstractions: datasets for data exchange, actions for shared parameters and commands, and the plugin manager plus factory triggers for creating and initializing plugin instances.

- [Choosing a communication mechanism](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/choosing_a_mechanism.html)
- [Requesting plugin instances](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/requesting_plugins.html)
- [Dataset-sensitive plugin triggers](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/dataset_triggers.html)
- [Lifetime and error handling](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/lifetime_and_errors.html)

For exact signatures, see the [plugin manager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html), [plugin factory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html), and [PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html) references.
