# GlobalSettingsGroupAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/global_settings_group_action.html

**Documentation path:** `api/core/gui/actions/grouping/global_settings_group_action.html`

---

# GlobalSettingsGroupAction

**Qualified name:** `mv::gui::GlobalSettingsGroupAction`

`GlobalSettingsGroupAction` is the common action container for application-wide settings. When a child action belongs to its QObject hierarchy, `addAction()` assigns the child’s persistent settings prefix and loads stored state.

Plugin developers normally use the specialized [PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html) rather than deriving directly from this base. See [Global plugin settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/index.html) for ownership, scope, and compatibility guidance.

class GlobalSettingsGroupAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Global settings group action class.

    Base action class which groups settings for

    - Common global settings (e.g. tasks & parameters)
    - Plugin global settings

    This class ensures that settings are store in the correct place because it overrides the GroupAction::addAction(…) and adjusts the settings prefix of the added actions.

    Settings can be found in: ManiVault/GlobalSettings/<global\_settings\_name>/<action\_name>

    Procedure(s) for adding a common global setting: a. Add an action to an existing global settings group:

    - ApplicationSettingsAction::addAction(…)
    - MiscellaneousSettingsAction::addAction(…)
    - ParametersSettingsAction::addAction(…)
    - TasksSettingsAction::addAction(…)
    - TemporaryDirectoriesSettingsAction::addAction(…) b. Create a new settings action derived from [GlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/global_settings_group_action.html#classmv_1_1gui_1_1GlobalSettingsGroupAction), add it to the SettingsManager class and add actions to it: MySettingsAction::addAction(…)

    Procedure for adding a plugin global setting: a. If a plugin does not have global settings yet:

    1. Create a settings action (e.g. MyPluginGlobalSettingsAction) derived from [PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#classmv_1_1gui_1_1PluginGlobalSettingsGroupAction)
    2. Add actions to MyPluginGlobalSettingsAction in its constructor (MyPluginGlobalSettingsAction::addAction(…))
    3. Create an instance of MyPluginGlobalSettingsAction, and assign it to the plugin factory in the initialize() member function of the plugin factory: setGlobalSettingsGroupAction(new MyPluginGlobalSettingsAction(this, this)); b. If a plugin already has global settings:

    - Add actions to the particular settings action (derived from [PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#classmv_1_1gui_1_1PluginGlobalSettingsGroupAction))

    Procedure for retrieving global settings: Common global setting example: mv::settings().getMiscellaneousSettings().getAskConfirmationBeforeRemovingDatasetsAction() Plugin global setting example: mv::settings().getPluginGlobalSettingsGroupAction<GlobalSettingsAction>(\_exampleViewGLPlugin)->getDefaultPointSizeAction().getValue()

    **Author**
    :   Thomas Kroes

    Subclassed by mv::gui::AppearanceSettingsAction, mv::gui::ErrorLoggingSettingsAction, mv::gui::MiscellaneousSettingsAction, mv::gui::ParametersSettingsAction, [mv::gui::PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#classmv_1_1gui_1_1PluginGlobalSettingsGroupAction), mv::gui::TasksSettingsAction, mv::gui::TemporaryDirectoriesSettingsAction

    Public Functions

    GlobalSettingsGroupAction(QObject \*parent, const QString &title, bool expanded = true)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **expanded** – Boolean determining whether the group action is expanded by default

    virtual QString getSettingsPrefix() const override
    :   Get settings prefix for child actions.

    void addAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, std::int32\_t widgetFlags = -1, mv::gui::WidgetConfigurationFunction widgetConfigurationFunction = mv::gui::WidgetConfigurationFunction())
    :   Add `action` to the group (facade for [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#classmv_1_1gui_1_1GroupAction) that automatically sets the [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#classmv_1_1gui_1_1WidgetAction) settings prefix)

        Parameters:
        :   - **action** – Pointer to action to add
            - **widgetFlags** – Action widget flags (default flags if -1)
            - **widgetConfigurationFunction** – When set, overrides the standard widget configuration function in the widget action
            - **loadSettings** – Load settings
