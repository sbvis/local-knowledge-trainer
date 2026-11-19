# Plugin

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html

**Documentation path:** `api/core/plugin/plugin.html`

---

# Plugin

All ManiVault plugin instances descend from this base class. For the factory–instance model, initialization order, destruction, and state ownership, see [Plugin lifecycle](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/lifecycle.html).

The plugin facade also provides access to its factory’s UI-backed global settings and to UI-less application preferences. See [Global plugin settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/index.html) before choosing these over project-owned instance state.

**Qualified name:** `mv::plugin::Plugin`

class Plugin : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Subclassed by [mv::plugin::AnalysisPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html#classmv_1_1plugin_1_1AnalysisPlugin), [mv::plugin::LoaderPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin.html#classmv_1_1plugin_1_1LoaderPlugin), [mv::plugin::RawData](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data.html#classmv_1_1plugin_1_1RawData), [mv::plugin::TransformationPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin.html#classmv_1_1plugin_1_1TransformationPlugin), [mv::plugin::ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#classmv_1_1plugin_1_1ViewPlugin), [mv::plugin::WriterPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin.html#classmv_1_1plugin_1_1WriterPlugin)

    Public Functions

    Plugin(const [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*factory)
    :   Construct with pointer to plugin `factory`.

        Parameters:
        :   **factory** – Pointer to plugin factory

    QIcon icon() const
    :   Get icon.

        Returns:
        :   Icon

    inline virtual void init()
    :   Can be implemented to initialize the plugin to a certain state.

        This function gets called when the plugin is first instantiated.

    const [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*getFactory() const
    :   Get the plugin factory for the plugin.

        Returns:
        :   Pointer to plugin factory

    ThirdPartyLicenses getThirdPartyLicenses() const
    :   Get third-party dependency licenses (facade for the [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#classmv_1_1plugin_1_1PluginFactory) class)

        Returns:
        :   Third-party dependency licenses used by the plugin

    QString getName() const
    :   Returns the unique name of this plugin.

    QString getGuiName() const
    :   Returns the GUI name of this plugin.

    QString getKind() const
    :   Returns the kind of plugin.

        The kind is specific to the particular implementation of a plugin type.

    Type getType() const
    :   Returns the type of plugin, see all types in PluginType.

    virtual util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") getVersion() const
    :   Returns the version of the plugin.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) version

    [PluginShortcuts](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_shortcuts.html#_CPPv4N2mv15PluginShortcutsE "mv::PluginShortcuts") &getShortcuts()
    :   Get shortcuts.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) shortcuts

    const [PluginShortcuts](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_shortcuts.html#_CPPv4N2mv15PluginShortcutsE "mv::PluginShortcuts") &getShortcuts() const
    :   Get shortcuts.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) shortcuts

    QVariant getProperty(const QString &name, const QVariant &defaultValue = QVariant()) const
    :   Get property in variant form.

        Parameters:
        :   - **name** – Name of the property
            - **defaultValue** – Default value

        Returns:
        :   Property in variant form

    void setProperty(const QString &name, const QVariant &value)
    :   Set property.

        Parameters:
        :   - **name** – Name of the property
            - **value** – Property value

    bool hasProperty(const QString &name) const
    :   Determines whether a property with a give name exists.

        Parameters:
        :   - **name** – Name of the property
            - **value** – If property with the given name exists

    QStringList propertyNames() const
    :   Returns a list of available property names.

    QVariant getSetting(const QString &path, const QVariant &defaultValue = QVariant()) const
    :   Load setting.

        Parameters:
        :   - **path** – Path of the setting (e.g. General/Computation/NumberOfIterations)
            - **defaultValue** – Value to return if the setting with `path` was not found

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) setting in variant form

    void setSetting(const QString &path, const QVariant &value)
    :   Save setting.

        Parameters:
        :   - **path** – Path of the setting (e.g. General/Computation/NumberOfIterations)
            - **value** – Value in variant form

    QString getGlobalSettingsPrefix() const
    :   Get global settings prefix (facade for the [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#classmv_1_1plugin_1_1PluginFactory) class)

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) global settings prefix

    gui::[PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#_CPPv4N2mv3gui31PluginGlobalSettingsGroupActionE "mv::gui::PluginGlobalSettingsGroupAction") \*getGlobalSettingsAction() const
    :   Get global settings action (facade for the [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#classmv_1_1plugin_1_1PluginFactory) class)

        Returns:
        :   Pointer to plugin global settings action (maybe nullptr if plugin does not have global settings)

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant.

        Parameters:
        :   **Variant** – representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant.

        Returns:
        :   Variant representation of the widget action

    void destroy()
    :   Destroys the plugin and removes it from the plugin manager.

    void addNotification(const QString &description, const util::[Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification")::[DurationType](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12DurationTypeE "mv::util::Notification::DurationType") &durationType = util::[Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification")::[DurationType](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12DurationTypeE "mv::util::Notification::DurationType")::[Fixed](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12DurationType5FixedE "mv::util::Notification::DurationType::Fixed"), std::int32\_t delayMs = 0) const
    :   Add plugin notification in the main window.

        Parameters:
        :   - **description** – Message description (maybe HTML)
            - **durationType** – Duration type of the notification
            - **delayMs** – Delay in milliseconds before the notification is shown

    inline virtual gui::ScriptTriggerActions getScriptTriggerActions(const Datasets &datasets) const
    :   Get script trigger actions given `datasets`.

        Example:

        ScriptTriggerActions scriptTriggerActions; if (datasets.count() == 1 && datasets.first()->getDataType() == PointType) scriptTriggerActions << new ScriptTriggerAction(nullptr, std::make\_shared<PythonScript>(“Min”, Script::Type::Analysis, “”, datasets), “Analysis/Min”); return scriptTriggerActions;

        Parameters:
        :   **datasets** – Vector of input datasets

        Returns:
        :   Vector of script trigger actions

    Protected Attributes

    const [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*\_factory
    :   Pointer to the core interface.

    const QString \_name
    :   Pointer to plugin factory.

    QMap<QString, QVariant> \_properties
    :   Unique plugin name.

    [EventListener](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_listener.html#_CPPv4N2mv13EventListenerE "mv::EventListener") \_eventListener
    :   Properties map.

    gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_guiNameAction
    :   Listen to public events.

    gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_destroyAction
    :   Action for the GUI name.

    [PluginShortcuts](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_shortcuts.html#_CPPv4N2mv15PluginShortcutsE "mv::PluginShortcuts") \_shortcuts
    :   Action for destroying the plugin.

    gui::[PluginLearningCenterAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_learning_center_action.html#_CPPv4N2mv3gui26PluginLearningCenterActionE "mv::gui::PluginLearningCenterAction") \_learningCenterAction
    :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) shortcuts.

    Friends

    *friend class* PluginFactory
