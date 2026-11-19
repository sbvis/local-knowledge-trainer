# Application

**Source:** https://manivault.readthedocs.io/en/latest/api/core/application/application.html

**Documentation path:** `api/core/application/application.html`

---

# Application

`Application` is ManiVault’s process-wide `QApplication` subclass. It provides startup configuration, application identity and version information, temporary directories, the application logger, workflow execution facilities, and access to the active Core implementation.

The executable creates this object. Plugins should use `mv::Application::current()` when application-level information is genuinely required and should use the typed accessors from `CoreInterface.h` for manager services.

The Core pointer exposed by the application is non-owning: `Application` connects to Core lifecycle signals and clears the pointer during teardown. Application startup metadata and actions are application integration concerns rather than ordinary plugin state.

**Qualified name:** `mv::Application`

## Related

- [CoreInterface](https://manivault.readthedocs.io/en/latest/api/core/application/core_interface.html)
- [Building applications](https://manivault.readthedocs.io/en/latest/development/building_applications/index.html)

class Application : public QApplication, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   ManiVault (Studio) application class.

    **Author**
    :   Thomas Kroes

    Public Functions

    Application(int &argc, char \*\*argv)
    :   Constructor.

        Parameters:
        :   - **argc** – Number of command line arguments
            - **argv** – Command line arguments

    ~Application() override
    :   Custom destructor for cleaning up nicely.

    [CoreInterface](https://manivault.readthedocs.io/en/latest/api/core/application/core_interface.html#_CPPv4N2mv13CoreInterfaceE "mv::CoreInterface") \*getCore() const
    :   Get pointer to the core.

    void setCore([CoreInterface](https://manivault.readthedocs.io/en/latest/api/core/application/core_interface.html#_CPPv4N2mv13CoreInterfaceE "mv::CoreInterface") \*core)
    :   Set pointer to the core.

        Parameters:
        :   **core** – Pointer to the core

    util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") getVersion() const
    :   Get application version (major and minor version number)

        Returns:
        :   Pair of integers representing major and minor version number respectively

    QUrl getStartupProjectUrl() const
    :   Get the startup project file URL.

        Returns:
        :   Startup project URL (can be empty, in which case no project is opened at startup)

    void setStartupProjectUrl(const QUrl &startupProjectUrl)
    :   Set startup project file URL to `startupProjectUrl`.

        Parameters:
        :   **startupProjectUrl** – Startup project file URL (can be empty, in which case no project is opened at startup)

    [ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#_CPPv4N2mv17ProjectMetaActionE "mv::ProjectMetaAction") \*getStartupProjectMetaAction() const
    :   Get startup project meta action.

        Returns:
        :   Pointer to project meta action (non-nullptr when ManiVault starts up with a project)

    void setStartupProjectMetaAction([ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#_CPPv4N2mv17ProjectMetaActionE "mv::ProjectMetaAction") \*projectMetaAction)
    :   Set startup project meta action to `projectMetaAction` (the application takes ownership of the pointer)

        Parameters:
        :   **projectMetaAction** – Pointer to project meta action

    [ApplicationStartupTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/application_startup_task.html#_CPPv4N2mv22ApplicationStartupTaskE "mv::ApplicationStartupTask") &getStartupTask()
    :   Get application startup task.

    bool shouldOpenProjectAtStartup() const
    :   Get whether a project should be opened after the application starts.

        Returns:
        :   Boolean determining whether a project should be opened after the application starts

    void initialize()
    :   Perform one-time startup initialization.

    bool hasSetting(const QString &path) const
    :   Get whether a setting exists.

        Parameters:
        :   **path** – Path of the setting (e.g. General/Computation/NumberOfIterations)

        Returns:
        :   Boolean determining whether a setting exists

    QVariant getSetting(const QString &path, const QVariant &defaultValue = QVariant()) const
    :   Load setting.

        Parameters:
        :   - **path** – Path of the setting (e.g. General/Computation/NumberOfIterations)
            - **defaultValue** – Value to return if the setting with `path` was not found

        Returns:
        :   Plugin setting in variant form

    void setSetting(const QString &path, const QVariant &value)
    :   Save setting.

        Parameters:
        :   - **path** – Path of the setting (e.g. General/Computation/NumberOfIterations)
            - **value** – Value in variant form

    const QTemporaryDir &getTemporaryDir() const
    :   Get temporary dir.

        Returns:
        :   Directory where application temporary files reside

    [TemporaryDirs](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#_CPPv4N2mv11Application13TemporaryDirsE "mv::Application::TemporaryDirs") &getTemporaryDirs()
    :   Get ManiVault application temporary directories.

        Returns:
        :   Reference to temporary directories

    util::[CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html#_CPPv4N2mv4util13CodecRegistryE "mv::util::CodecRegistry") &getCodecRegistry()
    :   Get codec registry.

        Returns:
        :   Reference to codec registry

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load application state from variant map.

        Parameters:
        :   **variantMap** – Variant representation of the application

    virtual QVariantMap toVariantMap() const override
    :   Save application state to variant maps.

        Returns:
        :   Variant representation of the application

    void coreAboutToBeInitialized([CoreInterface](https://manivault.readthedocs.io/en/latest/api/core/application/core_interface.html#_CPPv4N2mv13CoreInterfaceE "mv::CoreInterface") \*core)
    :   Invoked when the core is about to be initialized (re-broadcasts corresponding `core` signal)

        Parameters:
        :   **core** – Pointer to core instance

    void coreInitialized([CoreInterface](https://manivault.readthedocs.io/en/latest/api/core/application/core_interface.html#_CPPv4N2mv13CoreInterfaceE "mv::CoreInterface") \*core)
    :   Invoked when the core has been initialized (re-broadcasts corresponding `core` signal)

        Parameters:
        :   **core** – Pointer to core instance

    void coreManagersCreated([CoreInterface](https://manivault.readthedocs.io/en/latest/api/core/application/core_interface.html#_CPPv4N2mv13CoreInterfaceE "mv::CoreInterface") \*core)
    :   Invoked when the core managers have been created (re-broadcasts corresponding `core` signal)

        Parameters:
        :   **core** – Pointer to core instance

    Public Static Functions

    static [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#_CPPv4N2mv11ApplicationE "mv::Application") \*current()
    :   Returns a pointer to the current ManiVault application (if the current application derives from [mv::Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application))

    static [CoreInterface](https://manivault.readthedocs.io/en/latest/api/core/application/core_interface.html#_CPPv4N2mv13CoreInterfaceE "mv::CoreInterface") \*core()
    :   Get pointer to the core.

    static QString getBaseName()
    :   Get the application base name (omits version)

        Returns:
        :   The application name string

    static QString getFullName()
    :   Get the full application name (includes version)

        Returns:
        :   The application name string

    static QString getAbout()
    :   Get the application about string.

        Returns:
        :   The application about string

    static workflow::WorkflowGuiThreadDispatcher &workflowGuiThreadDispatcher()
    :   Get workflow GUI thread dispatcher.

        Returns:
        :   Reference to workflow GUI thread dispatcher

    static util::[Logger](https://manivault.readthedocs.io/en/latest/api/core/util/logging/logger.html#_CPPv4N2mv4util6LoggerE "mv::util::Logger") &getLogger()
    :   Get application-wide logger instance.

        Returns:
        :   Reference to logger instance

    static std::int32\_t requestOverrideCursor(Qt::CursorShape cursorShape)
    :   Request a cursor override with the specified shape.

        If the cursor shape `cursorShape` is already registered, its reference count is incremented, but the actual cursor shape does not change. If it is not registered, the current cursor shape is changed to `cursorShape`, and the override is registered. If the cursor is overridden with a different shape, the previous override is restored before applying the new one.

        Parameters:
        :   **cursorShape** – The cursor shape to override.

        Returns:
        :   The number of active overrides for `cursorShape` after this call.

    static std::int32\_t requestRemoveOverrideCursor(Qt::CursorShape cursorShape, bool all = false)
    :   Remove a previously requested cursor override.

        If the cursor shape `cursorShape` is registered, its reference count is decremented. If the count reaches zero, the override is removed and the previous cursor override (if any) or the default cursor is restored.

        Parameters:
        :   - **cursorShape** – The cursor shape to remove.
            - **all** – If true, removes all overrides for `cursorShape` regardless of the current count.

        Returns:
        :   The number of remaining overrides for `cursorShape` after this call.

    static QString getConfigurationFileName()
    :   Get the configuration file name.

        Returns:
        :   The configuration file name

    static QString getConfigurationFilePath()
    :   Get the path to the configuration file.

        Returns:
        :   The path to the configuration file

    static bool hasConfigurationFile()
    :   Check whether a configuration file exists.

        Returns:
        :   Boolean determining whether a configuration file exists

    static void initializeAttributes()
    :   Initialize attributes (called once at application startup)

    static workflow::[AbstractWorkflowPlanExecutor](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/abstract_workflow_plan_executor.html#_CPPv4N2mv8workflow28AbstractWorkflowPlanExecutorE "mv::workflow::AbstractWorkflowPlanExecutor") &getWorkflowPlanExecutor()
    :   Get workflow plan executor.

        Returns:
        :   Reference to workflow plan executor

    static void setWorkflowPlanExecutor(workflow::UniqueWorkflowPlanExecutor workflowPlanExecutor)
    :   Set workflow plan executor to `workflowPlanExecutor` (the application takes ownership of the pointer)

        Parameters:
        :   **workflowPlanExecutor** – Pointer to workflow plan executor

    Protected Attributes

    const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") \_version
    :   Pointer to the ManiVault core.

    QSettings \_settings
    :   [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application) version.

    QString \_serializationTemporaryDirectory
    :   Settings.

    util::[Logger](https://manivault.readthedocs.io/en/latest/api/core/util/logging/logger.html#_CPPv4N2mv4util6LoggerE "mv::util::Logger") \_logger
    :   Temporary directory for serialization.

    gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \*\_exitAction
    :   Logger instance.

    QUrl \_startupProjectUrl
    :   Action for exiting the application.

    [ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#_CPPv4N2mv17ProjectMetaActionE "mv::ProjectMetaAction") \*\_startupProjectMetaAction
    :   URL of the project to automatically open upon startup (if set)

    [ApplicationStartupTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/application_startup_task.html#_CPPv4N2mv22ApplicationStartupTaskE "mv::ApplicationStartupTask") \*\_startupTask
    :   Pointer to project meta action (non-nullptr case ManiVault starts up with a project)

    QTemporaryDir \_temporaryDir
    :   [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application) startup task.

    [TemporaryDirs](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#_CPPv4N2mv11Application13TemporaryDirsE "mv::Application::TemporaryDirs") \_temporaryDirs
    :   Directory where application temporary files reside.

    QLockFile \_lockFile
    :   ManiVault application temporary directories manager.

    gui::[ApplicationConfigurationAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/application_configuration_action.html#_CPPv4N2mv3gui30ApplicationConfigurationActionE "mv::gui::ApplicationConfigurationAction") \_configurationAction
    :   Lock file is used for fail-safe purging of the temporary directory.

    util::[CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html#_CPPv4N2mv4util13CodecRegistryE "mv::util::CodecRegistry") \_codecRegistry
    :   [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application) configuration action.

    workflow::WorkflowGuiThreadDispatcher \_workflowGuiThreadDispatcher
    :   Codec registry.

    workflow::UniqueWorkflowPlanExecutor \_workflowPlanExecutor
    :   Workflow GUI thread dispatcher.

    Protected Static Attributes

    static QList<[CursorShapeCount](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#_CPPv4N2mv11Application16CursorShapeCountE "mv::Application::CursorShapeCount")> cursorOverridesCount
    :   Workflow plan executor.

        Count of cursor overrides for each cursor shape

    struct CursorShapeCount

    class TemporaryDirs : public QObject
    :   Class for managing ManiVault application temporary directories.

        Public Functions

        TemporaryDirs(QObject \*parent)
        :   Construct with pointer to /p parent object.

            Parameters:
            :   **parent** – Pointer to parent object

        QStringList getStale()
        :   Get stale ManiVault temporary directories in the OS temporary directory Stale in this context means that the <os\_temp\_dir>/ManiVault.

            <app\_session\_id>.<temp\_dir\_id>/app.lock is not locked or missing and the directory can be safely removed because it is not in use by another (ManiVault) application.

            Returns:
            :   List of stale ManiVault application temporary directories

        void removeStale(const QStringList &stale = QStringList())
        :   Removes stale directories in the OS temporary directory (ManiVault.

            <app\_session\_id>.<temp\_dir\_id>) and which are not locked by the OS @stale Stale directories to remove, removes all stale when empty

        inline [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") &getTask()
        :   Get progress task.

            Returns:
            :   Reference to progress task
