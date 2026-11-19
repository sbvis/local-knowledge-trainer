# Global plugin settings

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/index.html

**Documentation path:** `development/building_plugins/global_settings/index.html`

---

# Global plugin settings

Global plugin settings are application preferences shared by every instance of one plugin kind. Use them for installation-wide defaults and policies that should survive application restarts independently of any project.

![Global settings](https://manivault.readthedocs.io/en/latest/_images/global_settings.png)

The principal UI-backed mechanism is a factory-owned `mv::gui::PluginGlobalSettingsGroupAction`. Its child actions appear in ManiVault’s settings dialog and persist their values through the application settings store.

Important

Global does not mean project-wide. Opening, saving, or sharing a project should not change another user’s application preferences. State belonging to one plugin instance remains project state.

- [Choosing the right scope](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/choosing_a_scope.html)
  - [Global default or live policy](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/choosing_a_scope.html#global-default-or-live-policy)
  - [When not to use global settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/choosing_a_scope.html#when-not-to-use-global-settings)
- [Defining global settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/defining_settings.html)
  - [Create a typed group](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/defining_settings.html#create-a-typed-group)
  - [Register from the factory](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/defining_settings.html#register-from-the-factory)
  - [Defaults and restoration order](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/defining_settings.html#defaults-and-restoration-order)
- [Consuming and reacting to settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/consuming_settings.html)
  - [Read through the plugin facade](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/consuming_settings.html#read-through-the-plugin-facade)
  - [Read through the settings manager](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/consuming_settings.html#read-through-the-settings-manager)
  - [UI-less application preferences](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/consuming_settings.html#ui-less-application-preferences)
  - [Apply changes safely](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/consuming_settings.html#apply-changes-safely)
- [Persistence and compatibility](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/persistence_and_compatibility.html)
  - [Stable identifiers](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/persistence_and_compatibility.html#stable-identifiers)
  - [Renaming and migration](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/persistence_and_compatibility.html#renaming-and-migration)
  - [Interaction with projects](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/persistence_and_compatibility.html#interaction-with-projects)
- [Testing and pitfalls](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/testing_and_pitfalls.html)
  - [Verification checklist](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/testing_and_pitfalls.html#verification-checklist)
  - [Common pitfalls](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/testing_and_pitfalls.html#common-pitfalls)

For exact signatures, see the [PluginGlobalSettingsGroupAction API](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html), [PluginFactory API](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html), and [settings manager API](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_settings_manager.html).
