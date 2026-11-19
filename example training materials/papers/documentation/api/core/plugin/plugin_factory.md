# PluginFactory

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html

**Documentation path:** `api/core/plugin/plugin_factory.html`

---

# PluginFactory

The plugin factory describes and creates instances of one plugin kind. For an implementation skeleton and guidance on factory-owned versus instance-owned state, see [Factory and plugin instance](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/factory_and_instance.html).

Factories also advertise supported data and provide default or dataset-sensitive creation triggers. For the relationship between the broad capability declaration and exact selection rules, see [Creation triggers and inputs](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/triggers_and_inputs.html).

A factory may also own and register one settings group shared by every instance of its plugin kind. See [Global plugin settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/index.html) for the lifetime and initialization pattern.

Factories can similarly register one plugin-kind status-bar action during startup. See [Status-bar integration](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/index.html) for ownership, positioning, and multi-instance behavior.

Factories also define whether standard interfaces may offer a plugin and how many live instances may coexist. See [Plugin creation policy and instance limits](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/index.html) before using the instance counters or maximum directly.

Derive a concrete factory from the specialization matching its instance type. The [plugin API overview](https://manivault.readthedocs.io/en/latest/api/core/plugin/index.html) lists the analysis, loader, transformation, view, and writer pairs; data-storage factories are documented with the data API.

**Qualified name:** `mv::plugin::PluginFactory`

class PluginFactory : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Subclassed by [mv::plugin::AnalysisPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin_factory.html#classmv_1_1plugin_1_1AnalysisPluginFactory), [mv::plugin::LoaderPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin_factory.html#classmv_1_1plugin_1_1LoaderPluginFactory), [mv::plugin::RawDataFactory](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data_factory.html#classmv_1_1plugin_1_1RawDataFactory), [mv::plugin::TransformationPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin_factory.html#classmv_1_1plugin_1_1TransformationPluginFactory), [mv::plugin::ViewPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin_factory.html#classmv_1_1plugin_1_1ViewPluginFactory), [mv::plugin::WriterPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin_factory.html#classmv_1_1plugin_1_1WriterPluginFactory)

    Public Functions

    PluginFactory(Type type, const QString &title)
    :   Constructor.

        Parameters:
        :   - **type** – The plugin type
            - **title** – The plugin factory title

    ~PluginFactory() override = default
    :   No need for custom destructor.

    QString getKind() const
    :   Get plugin kind.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) kind

    void setKind(const QString &kind)
    :   Set plugin kind.

        Parameters:
        :   **kind** – [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) kind

    Type getType() const
    :   Get the plugin type.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) type

    virtual void initialize()
    :   Perform post-construction initialization.

    const QIcon &getCategoryIcon() const
    :   Get plugin category icon.

        Returns:
        :   Category icon

    virtual QString getGlobalSettingsPrefix() const final
    :   Get settings prefix.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) factory global settings prefix

    virtual gui::[PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#_CPPv4N2mv3gui31PluginGlobalSettingsGroupActionE "mv::gui::PluginGlobalSettingsGroupAction") \*getGlobalSettingsGroupAction() const
    :   Get global settings group action.

        Returns:
        :   Pointer to plugin global settings group action (maybe nullptr if plugin does not have global settings)

    void setGlobalSettingsGroupAction(gui::[PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#_CPPv4N2mv3gui31PluginGlobalSettingsGroupActionE "mv::gui::PluginGlobalSettingsGroupAction") \*pluginGlobalSettingsGroupAction)
    :   Set plugin global settings group action to `pluginGlobalSettingsGroupAction`.

        Parameters:
        :   **pluginGlobalSettingsGroupAction** – Pointer to plugin global settings group action (maybe a nullptr)

    gui::[PluginStatusBarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_status_bar_action.html#_CPPv4N2mv3gui21PluginStatusBarActionE "mv::gui::PluginStatusBarAction") \*getStatusBarAction() const
    :   Get plugin status bar action.

        Returns:
        :   Pointer to plugin status bar action (maybe nullptr)

    void setStatusBarAction(gui::[PluginStatusBarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_status_bar_action.html#_CPPv4N2mv3gui21PluginStatusBarActionE "mv::gui::PluginStatusBarAction") \*statusBarAction)
    :   Set plugin status bar action to `statusBarAction`.

        Parameters:
        :   **statusBarAction** – Pointer to plugin status bar action (maybe a nullptr)

    virtual bool hasHelp() const
    :   Get whether the plugin has help information or not.

        Returns:
        :   Boolean determining whether the plugin has help information or not

    virtual QUrl getReadmeMarkdownUrl() const
    :   Get the read me markdown file URL.

        Returns:
        :   URL of the read me markdown file

    virtual QUrl getRepositoryUrl() const
    :   Get the URL of the GitHub repository.

        Returns:
        :   URL of the GitHub repository (or readme markdown URL if set)

    virtual QString getDefaultBranch() const
    :   Get the name of the default branch.

        Returns:
        :   Name of the default branch

    QString getGuiName() const
    :   Get the menu name of the plugin.

    void setGuiName(const QString &guiName)
    :   Set the GUI name of the plugin.

        Parameters:
        :   **guiName** – GUI name of the plugin

    util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &getVersion()
    :   Get plugin version.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) semantic version

    const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &getVersion() const
    :   Get plugin version.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) semantic version

    void setVersion(const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &version)
    :   Set the plugin version to `version`.

        Parameters:
        :   **version** – [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) semantic version

    virtual [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin") \*produce() = 0
    :   Produces the plugin.

        Returns:
        :   Pointer to the produced plugin

    bool mayProduce() const
    :   Get whether a plugin may be produced.

        Returns:
        :   Boolean determining whether a plugin may be produced

    inline virtual mv::DataTypes supportedDataTypes() const
    :   Get the data types that the plugin supports.

        Returns:
        :   Supported data types

    virtual gui::[PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html#_CPPv4N2mv3gui19PluginTriggerActionE "mv::gui::PluginTriggerAction") &getPluginTriggerAction()
    :   Get the trigger action that produces an instance of the plugin.

        Returns:
        :   Reference to a trigger action that produces an instance of the plugin

    inline virtual gui::PluginTriggerActions getPluginTriggerActions(const Datasets &datasets) const
    :   Get plugin trigger actions given `datasets`.

        Parameters:
        :   **datasets** – Vector of input datasets

        Returns:
        :   Vector of plugin trigger actions

    inline virtual gui::PluginTriggerActions getPluginTriggerActions(const DataTypes &dataTypes) const
    :   Get plugin trigger actions given `dataTypes`.

        Parameters:
        :   **dataTypes** – Vector of input data types

        Returns:
        :   Vector of plugin trigger actions

    void setAllowPluginCreationFromStandardGui(bool allowPluginCreationFromStandardGui)
    :   Set whether the plugin may be produced from the standard GUI to `allowPluginCreationFromStandardGui`.

        Parameters:
        :   **allowPluginCreationFromStandardGui** – Boolean determining whether a plugin instance may be created from the standard GUI (e.g. main menu etc.)

    bool getAllowPluginCreationFromStandardGui() const
    :   Get whether the plugin may be produced from the standard GUI.

        Returns:
        :   Boolean determining whether a plugin instance may be created from the standard GUI (e.g. main menu etc.)

    inline virtual gui::ScriptTriggerActions getScriptTriggerActions(const Datasets &datasets) const
    :   Get script trigger actions given `datasets`.

        Example:

        ScriptTriggerActions scriptTriggerActions; if (datasets.count() == 1 && datasets.first()->getDataType() == PointType) scriptTriggerActions << new ScriptTriggerAction(nullptr, std::make\_shared<PythonScript>(“Min”, Script::Type::Analysis, “”, datasets), “Analysis/Min”); return scriptTriggerActions;

        Parameters:
        :   **datasets** – Vector of input datasets

        Returns:
        :   Vector of script trigger actions

    std::uint32\_t getNumberOfInstances() const
    :   Get number of plugin instances currently loaded.

        Returns:
        :   Number of plugin instances currently loaded

    void setNumberOfInstances(std::uint32\_t numberOfInstances)
    :   Set number of plugin instances currently loaded.

        Parameters:
        :   **numberOfInstances** – Number of plugin instances currently loaded

    std::uint32\_t getNumberOfInstancesProduced() const
    :   Get number of plugin instances produced in total.

        Returns:
        :   Number of plugin instances produced in total

    void setNumberOfInstancesProduced(std::uint32\_t numberOfInstancesProduced)
    :   Set number of plugin instances produced in total.

        Parameters:
        :   **numberOfInstancesProduced** – Number of plugin instances produced in total

    std::uint32\_t getMaximumNumberOfInstances() const
    :   Get maximum number of allowed plugin instances.

    void setMaximumNumberOfInstances(std::uint32\_t maximumNumberOfInstances)
    :   Set maximum number of allowed plugin instances.

        Parameters:
        :   **maximumNumberOfInstances** – Maximum number of allowed plugin instances

    virtual void viewShortcutMap()
    :   View the shortcut map.

    [PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadataE "mv::plugin::PluginMetadata") &getPluginMetadata()
    :   Get plugin metadata.

        Returns:
        :   Reference to plugin metadata

    const [PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadataE "mv::plugin::PluginMetadata") &getPluginMetadata() const
    :   Get plugin metadata.

        Returns:
        :   Reference to plugin metadata

    ThirdPartyLicenses getThirdPartyLicenses() const
    :   Get third-party dependency licenses (facade for the [PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#classmv_1_1plugin_1_1PluginMetadata) class)

        Returns:
        :   Third-party dependency licenses used by the plugin

    void numberOfInstancesChanged(std::uint32\_t numberOfInstances)
    :   Signals that the number of instances changed to `numberOfInstances`.

        Parameters:
        :   **numberOfInstances** – Number of plugin instances

    void numberOfInstancesProducedChanged(std::uint32\_t numberOfInstancesProduced)
    :   Signals that the number of instances produced in total changed to `numberOfInstancesProduced`.

        Parameters:
        :   **numberOfInstancesProduced** – Number of plugin instances produced in total

    void pluginGlobalSettingsGroupActionChanged(gui::[PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#_CPPv4N2mv3gui31PluginGlobalSettingsGroupActionE "mv::gui::PluginGlobalSettingsGroupAction") \*pluginGlobalSettingsGroupAction)
    :   Signals that the plugin global settings group action changed to `pluginGlobalSettingsGroupAction`.

        Parameters:
        :   **pluginGlobalSettingsGroupAction** – Pointer to plugin global settings group action (maybe a nullptr)

    void statusBarActionChanged(gui::[PluginStatusBarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_status_bar_action.html#_CPPv4N2mv3gui21PluginStatusBarActionE "mv::gui::PluginStatusBarAction") \*statusBarAction)
    :   Signals that the plugin status bar action changed to `statusBarAction`.

        Parameters:
        :   **statusBarAction** – Pointer to plugin status bar action (maybe a nullptr)

    void pluginTitleChanged(const QString &previousPluginTitle, const QString &currentPluginTitle)
    :   Signals that the plugin title changed from `previousPluginTitle` to `currentPluginTitle`.

        Parameters:
        :   - **previousPluginTitle** – Previous plugin title
            - **currentPluginTitle** – Current plugin title

    void descriptionChanged(const QString &previousDescription, const QString &currentDescription)
    :   Signals that the description changed from `previousDescription` to `currentDescription`.

        Parameters:
        :   - **previousDescription** – Previous description
            - **currentDescription** – Current description

    void summaryChanged(const QString &previousSummary, const QString &currentSummary)
    :   Signals that the summary changed from `previousSummary` to `currentSummary`.

        Parameters:
        :   - **previousSummary** – Previous summary
            - **currentSummary** – Current summary

    void authorsChanged(const QStringList previousAuthors, const QStringList &currentAuthors)
    :   Signals that the authors changed from `previousAuthors` to `currentAuthors`.

        Parameters:
        :   - **previousAuthors** – Previous authors
            - **currentAuthors** – Current authors

    void copyrightNoticeChanged(const QString &previousCopyrightNotice, const QString &currentCopyrightNotice)
    :   Signals that the copyright notice changed from `previousCopyrightNotice` to `currentCopyrightNotice`.

        Parameters:
        :   - **previousCopyrightNotice** – Previous copyright notice
            - **currentCopyrightNotice** – Current copyright notice

    void aboutMarkdownChanged(const QString &previousAboutMarkdown, const QString &currentAboutMarkdown)
    :   Signals that the about text in Markdown format changed from `previousAboutMarkdown` to `currentAboutMarkdown`.

        Parameters:
        :   - **previousAboutMarkdown** – Previous about text in Markdown format
            - **currentAboutMarkdown** – Current about text in Markdown format

    Public Static Functions

    static inline void initializePluginTriggerActions(gui::PluginTriggerActions &pluginTriggerActions)
    :   Initializes a list of plugin trigger actions.

        Parameters:
        :   **pluginTriggerActions** – List of plugin trigger actions to be initialized

    Protected Functions

    void setCategoryIconByName(const QString &category)
    :   Set category icon by name.

        Parameters:
        :   **category** – Category name

    Protected Static Functions

    static QStringList getDatasetTypesAsStringList(const Datasets &datasets)
    :   Get sequence of input datasets as a string list.

        Parameters:
        :   **datasets** – Sequence of input datasets (order in which they were selected in the data hierarchy)

        Returns:
        :   String list of input dataset types

    static bool areAllDatasetsOfTheSameType(const Datasets &datasets, const [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") &dataType)
    :   Determine whether all datasets are of the same data type.

        Parameters:
        :   - **datasets** – Sequence of input datasets (order in which they were selected in the data hierarchy)
            - **dataType** – Type of data

        Returns:
        :   Whether each dataset is of the same data type

    static std::uint16\_t getNumberOfDatasetsForType(const Datasets &datasets, const [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") &dataType)
    :   Get number of datasets for `dataType`.

        Parameters:
        :   **dataType** – Data type

        Returns:
        :   Number of datasets of `datasetType`
