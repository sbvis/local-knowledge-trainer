# PluginGlobalSettingsGroupAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html

**Documentation path:** `api/core/gui/actions/grouping/plugin_global_settings_group_action.html`

---

# PluginGlobalSettingsGroupAction

**Qualified name:** `mv::gui::PluginGlobalSettingsGroupAction`

`PluginGlobalSettingsGroupAction` groups application preferences belonging to one plugin kind. A plugin factory owns and registers a plugin-specific derived group; the settings dialog then presents its child actions.

Begin with [Global plugin settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/index.html) for a complete definition, registration, consumption, and migration pattern.

class PluginGlobalSettingsGroupAction : public mv::gui::[GlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/global_settings_group_action.html#_CPPv4N2mv3gui25GlobalSettingsGroupActionE "mv::gui::GlobalSettingsGroupAction")
:   Plugin global settings group action class.

    Global settings group action class for global plugin settings

    Procedure for adding a plugin global setting: a. If a plugin does not have global settings yet:

    1. Create a settings action (e.g. MyPluginGlobalSettingsAction) derived from [PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#classmv_1_1gui_1_1PluginGlobalSettingsGroupAction)
    2. Add actions to MyPluginGlobalSettingsAction in its constructor (MyPluginGlobalSettingsAction::addAction(…))
    3. Create an instance of MyPluginGlobalSettingsAction, and assign it to the plugin factory in the initialize() member function of the plugin factory: setGlobalSettingsGroupAction(new MyPluginGlobalSettingsAction(this, this)); b. If a plugin already has global settings:

    - Add actions to the particular settings action (derived from [PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#classmv_1_1gui_1_1PluginGlobalSettingsGroupAction))

    **Author**
    :   Thomas Kroes

    Public Functions

    PluginGlobalSettingsGroupAction(QObject \*parent, const plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory)
    :   Construct with pointer to `parent` object and `pluginFactory`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **pluginFactory** – Pointer to plugin factory
