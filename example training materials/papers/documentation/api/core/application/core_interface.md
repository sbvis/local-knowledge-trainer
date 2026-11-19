# CoreInterface

**Source:** https://manivault.readthedocs.io/en/latest/api/core/application/core_interface.html

**Documentation path:** `api/core/application/core_interface.html`

---

# CoreInterface

`CoreInterface` is the abstract lifecycle and service boundary between the application and the Core managers. Plugin code usually includes `CoreInterface.h` and uses its typed convenience accessors rather than storing a `CoreInterface` pointer.

Common accessors include `mv::data()`, `mv::dataHierarchy()`, `mv::plugins()`, `mv::events()`, `mv::tasks()`, `mv::projects()`, and `mv::workspaces()`. They return Core-managed interfaces and are only valid while the application and Core are initialized.

Implementing this interface is application/Core integration work. Plugin developers should consume it, not subclass it.

**Qualified name:** `mv::CoreInterface`

## Related

- [Manager interfaces](https://manivault.readthedocs.io/en/latest/api/core/managers/index.html)
- [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html)

class CoreInterface : public QObject
:   Public Types

    enum class ManagerType
    :   Enumeration for distinguishing manager types.

        *Values:*

        enumerator Errors

        enumerator Actions
        :   Manager for errors.

        enumerator Theme
        :   Actions manager for storing actions.

        enumerator Plugins
        :   Manager for controlling the application theme.

        enumerator Events
        :   Plugin manager responsible for loading plug-ins and adding them to the core.

        enumerator Data
        :   Event manager for emitting global events.

        enumerator DataHierarchy
        :   Data manager responsible for storing data sets and data selections.

        enumerator Tasks
        :   Data hierarchy manager for providing a hierarchical dataset structure.

        enumerator Workspaces
        :   Manager for managing global tasks.

        enumerator Projects
        :   [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html#classmv_1_1Workspace) manager for controlling widgets layout.

        enumerator Settings
        :   Manager for loading/saving projects.

        enumerator Help
        :   Manager for managing global settings.

        enumerator Scripting
        :   Manager for getting help.

        enumerator Count
        :   Manager for al things scripting.

    Public Functions

    CoreInterface() = default
    :   Default constructor.

    virtual void createManagers() = 0
    :   Creates the core managers.

    virtual void setManagersCreated() = 0
    :   Flag the core managers as created and notify listeners.

    virtual void reset() = 0
    :   Resets the entire core implementation.

    virtual void initialize() = 0
    :   Initializes the core.

    virtual void setAboutToBeInitialized() = 0
    :   Notify listeners that the core is about to be initialized.

    virtual void setInitialized() = 0
    :   Flag the core as initialized and notify listeners.

    virtual bool isInitialized() const = 0
    :   Get whether the core is initialized or not.

        Returns:
        :   Boolean determining whether the core is initialized or not

    virtual bool isAboutToBeDestroyed() const = 0
    :   Get whether the core is about to be destroyed or not.

        Returns:
        :   Boolean determining whether the core is about to be destroyed or not

    void aboutToBeInitialized()
    :   Invoked when the core is about to be initialized.

    void aboutToBeDestroyed()
    :   Invoked when the core is about to be destroyed.

    void initialized()
    :   Invoked when the core has been initialized.

    void managersCreated()
    :   Invoked when the core managers have been created.
