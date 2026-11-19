# Plugin creation policy and instance limits

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/index.html

**Documentation path:** `development/building_plugins/creation_policy/index.html`

---

# Plugin creation policy and instance limits

A plugin factory controls where its plugin can be offered for creation and how many instances may coexist. Configure that policy deliberately when a plugin owns an exclusive resource, has a high resource cost, should only be created in a specific context, or should have one application-wide instance.

Start with [Choosing a creation policy](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/choosing_a_policy.html). Most plugins need only one or two factory settings; the remaining pages explain how those settings interact with triggers, programmatic requests, destruction, and project restoration.

- [Choosing a creation policy](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/choosing_a_policy.html)
- [Configuring the factory](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/configuring_the_factory.html)
- [Triggers and creation requests](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/triggers_and_requests.html)
- [Lifecycle and project restoration](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/lifecycle_and_restoration.html)
- [Testing and pitfalls](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/testing_and_pitfalls.html)

## Core rules

- Put creation policy on the factory, not on a plugin instance.
- Leave the instance limit unlimited unless the plugin has a concrete exclusivity or resource reason.
- Use contextual trigger actions to decide whether a particular dataset selection is valid.
- Request instances through the plugin manager. Never call `produce()` directly.
- Let the core maintain the live and produced instance counters.
- Include project restoration in the compatibility analysis before introducing or reducing a limit.

The relevant API entry points are [PluginFactory and its role-specific factories](https://manivault.readthedocs.io/en/latest/api/core/plugin/index.html), [PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html), and [AbstractPluginManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html).
