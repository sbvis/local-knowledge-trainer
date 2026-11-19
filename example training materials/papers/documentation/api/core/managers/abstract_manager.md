# AbstractManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html

**Documentation path:** `api/core/managers/abstract_manager.html`

---

# AbstractManager

**Qualified name:** `mv::AbstractManager`

class AbstractManager : public QObject, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   Abstract manager.

    Base abstract manager class for the core.

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::AbstractActionsManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_actions_manager.html#classmv_1_1AbstractActionsManager), [mv::AbstractDataHierarchyManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_hierarchy_manager.html#classmv_1_1AbstractDataHierarchyManager), [mv::AbstractDataManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html#classmv_1_1AbstractDataManager), [mv::AbstractErrorManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_error_manager.html#classmv_1_1AbstractErrorManager), [mv::AbstractEventManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_event_manager.html#classmv_1_1AbstractEventManager), [mv::AbstractHelpManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_help_manager.html#classmv_1_1AbstractHelpManager), [mv::AbstractPluginManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_plugin_manager.html#classmv_1_1AbstractPluginManager), [mv::AbstractProjectManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#classmv_1_1AbstractProjectManager), [mv::AbstractScriptingManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_scripting_manager.html#classmv_1_1AbstractScriptingManager), [mv::AbstractSettingsManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_settings_manager.html#classmv_1_1AbstractSettingsManager), [mv::AbstractTaskManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_task_manager.html#classmv_1_1AbstractTaskManager), [mv::AbstractThemeManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_theme_manager.html#classmv_1_1AbstractThemeManager), [mv::AbstractWorkspaceManager](https://manivault.readthedocs.io/en/latest/api/core/application/abstract_workspace_manager.html#classmv_1_1AbstractWorkspaceManager)

    Public Functions

    inline AbstractManager(QObject \*parent, const QString &name = "")
    :   Construct manager with pointer to `parent` object and `name`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **name** – Manager name (serialization name)

    inline virtual void initialize()
    :   Perform manager startup initialization.

    inline void beginReset()
    :   Begin reset operation.

    inline virtual void reset()
    :   Resets the contents of the manager.

    inline void endReset()
    :   End reset operation.

    inline void beginInitialization()
    :   Begin the initialization process.

    inline void endInitialization()
    :   End the initialization process.

    inline bool isInitialized() const
    :   Get whether the manager is initialized or not.

        Returns:
        :   Boolean determining whether the manager is initialized or not

    inline bool isInitializing() const
    :   Get whether the manager is initializing or not.

        Returns:
        :   Boolean determining whether the manager is initializing or not

    inline bool isResetting() const
    :   Get whether the manager is resetting or not.

        Returns:
        :   Boolean determining whether the manager is resetting or not

    inline virtual QIcon getIcon() const
    :   Get manager icon.

        Returns:
        :   Icon

    inline QString getSettingsPrefix() const
    :   Get manager settings prefix.

        Returns:
        :   Settings manager prefix

    inline virtual bool mayLock() const
    :   Get whether the manager be locked.

        Returns:
        :   Boolean determining whether the manager be locked

    inline virtual bool mayUnlock() const
    :   Get whether the manager be unlocked.

        Returns:
        :   Boolean determining whether the manager be unlocked

    inline bool isCoreDestroyed() const
    :   Establish whether the core is destroyed.

        Returns:
        :   Boolean determining whether the core is destroyed

    void managerAboutToBeInitialized()
    :   Signals that the initialization process has begun.

    void managerInitialized()
    :   Signals that the initialization process has ended.

    void managerAboutToBeReset()
    :   Signals that the manager is about to be reset.

    void managerReset()
    :   Signals that the manager has been reset.

    Protected Functions

    inline void setCoreIsDestroyed()
    :   Mark core as destroyed.
