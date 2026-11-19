# PluginTriggerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html

**Documentation path:** `api/core/gui/actions/internal/plugin_trigger_action.html`

---

# PluginTriggerAction

**Qualified name:** `mv::gui::PluginTriggerAction`

This action represents a default or contextual request to create a plugin instance. For factory overrides, dataset validation, and callback lifetime, see [Dataset-sensitive plugin triggers](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/dataset_triggers.html).

Trigger availability is presentation; managed creation and instance-limit enforcement remain the plugin manager’s responsibility. See [Triggers and creation requests](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/triggers_and_requests.html).

class PluginTriggerAction : public mv::gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction")
:   Plugin trigger action class.

    Action class for triggering the creation of plugins.

    By default, a plugin is automatically created when the trigger action is triggered. Custom plugin creation is possible by setting a creation handler function, see setCreatePluginFunction()

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE PluginTriggerAction(QObject \*parent, const plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory, const QString &title, const QString &tooltip, const QIcon &icon)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **pluginFactory** – Pointer to plugin factory
            - **title** – Title and menu location of the plugin trigger action, ‘menu/entry’ will create a nested entry
            - **icon** – Icon
            - **tooltip** – Tooltip of the plugin trigger action

    Q\_INVOKABLE PluginTriggerAction(QObject \*parent, const plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*pluginFactory, const QString &title, const QString &tooltip, const QIcon &icon, RequestPluginCallback requestPluginCallback)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **pluginFactory** – Pointer to plugin factory
            - **title** – Title and menu location of the plugin trigger action, ‘menu/entry’ will create a nested entry
            - **tooltip** – Tooltip of the plugin trigger action
            - **icon** – Icon
            - **requestPluginCallback** – Callback which is invoked when the trigger action is triggered

    Q\_INVOKABLE PluginTriggerAction(const [PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html#_CPPv4N2mv3gui19PluginTriggerAction19PluginTriggerActionERK19PluginTriggerActionRK7QString "mv::gui::PluginTriggerAction::PluginTriggerAction") &pluginTriggerAction, const QString &title)
    :   Copy constructor.

        Parameters:
        :   **pluginTriggerAction** – Reference to other plugin trigger action

    const plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*getPluginFactory() const
    :   Get the plugin factory.

        Returns:
        :   Pointer to the plugin factory

    QString getMenuLocation() const
    :   Get menu location of the plugin trigger action.

        Returns:
        :   Location of the plugin trigger action in a menu

    void setMenuLocation(const QString &menuLocation)
    :   Set menu location of the plugin trigger action.

        Parameters:
        :   **menuLocation** – Location of the plugin trigger action in a menu

    QString getSha() const
    :   Get sha of plugin kind + trigger title.

        Returns:
        :   Sha

    mv::Datasets getDatasets() const
    :   Get list of datasets that the plugin can work with when triggered.

        Returns:
        :   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) list

    [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getConfigurationAction()
    :   Get configuration action.

        Returns:
        :   Action for configuring the plugin creation (if available)

    void setConfigurationAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*configurationAction)
    :   Set configuration action.

        Parameters:
        :   **configurationAction** – Pointer to action for configuring the plugin creation

    void setText(const QString &text)
    :   Override base class to also update location.

        Parameters:
        :   **text** – Action text

    void setDatasets(const mv::Datasets &datasets)
    :   Set list of datasets that the plugin can work with when triggered.

        Parameters:
        :   **datasets** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) list

    void setRequestPluginCallback(RequestPluginCallback requestPluginCallback)
    :   Set the callback function which is invoked when the trigger action is triggered.

        Parameters:
        :   **requestPluginCallback** – Request plugin callback function (invoked when the trigger action is triggered)

    Protected Functions

    virtual void initialize()
    :   Sets up the trigger action.

    Friends

    *friend class* plugin::PluginFactory
