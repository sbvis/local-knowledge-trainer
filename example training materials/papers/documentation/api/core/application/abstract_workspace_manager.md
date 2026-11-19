# AbstractWorkspaceManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/application/abstract_workspace_manager.html

**Documentation path:** `api/core/application/abstract_workspace_manager.html`

---

# AbstractWorkspaceManager

`AbstractWorkspaceManager` is the Core-managed interface for workspace lifecycle and view layout. It creates, loads, saves, and enumerates workspaces; manages docking and isolation of view plugins; produces workspace previews; and reports lifecycle changes through Qt signals.

Plugin code accesses the active implementation through `mv::workspaces()`. Subclassing this interface is application/Core integration work rather than a normal plugin extension point.

`loadWorkspaceWorkflowPlan()` constructs a workflow plan without executing it. This allows framework code to compose workspace restoration into a larger project or application workflow while retaining progress, cancellation, and reporting behavior.

**Qualified name:** `mv::AbstractWorkspaceManager`

## Related

- [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html)
- [WorkspaceLocation](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html)
- [Parallel execution guide](https://manivault.readthedocs.io/en/latest/development/parallel_execution/index.html)

class AbstractWorkspaceManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract workspace manager class.

    Base abstract workspace manager class for managing workspaces and layout.

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractWorkspaceManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void addViewPlugin(plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*dockToViewPlugin = nullptr, gui::DockAreaFlag dockArea = gui::DockAreaFlag::Right) = 0
    :   Add a view plugin to the `dockArea` of `dockViewPlugin`.

        Parameters:
        :   - **viewPlugin** – Pointer to view plugin to add to layout
            - **dockToViewPlugin** – Pointer to view plugin to which new view plugins are docked (new view plugins be docked top-level if nullptr)
            - **dockArea** – Dock area in which `dockToViewPlugin` will be docked

    virtual void addViewPluginFloated(plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin) = 0
    :   Add a `viewPlugin` on top of the main window.

        Parameters:
        :   **viewPlugin** – Pointer to view plugin to add

    virtual void isolateViewPlugin(plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, bool isolate) = 0
    :   Set whether `viewPlugin` is isolated or not (closes all other view plugins when isolated)

        Parameters:
        :   - **viewPlugin** – Pointer to view plugin to add to layout
            - **isolate** – Whether to isolate `viewPlugin` or to reset the view layout prior to isolation

    virtual QWidget \*getWidget() = 0
    :   Get workspace widget.

        Returns:
        :   Pointer to workspace widget

    virtual QMenu \*getMenu(QWidget \*parent = nullptr) = 0
    :   Get workspace menu.

        Parameters:
        :   **parent** – Pointer to parent menu

        Returns:
        :   Pointer to created menu

    inline QString getWorkspaceFilePath() const
    :   Get the file path of the loaded workspace.

        Returns:
        :   File path of the loaded workspace

    inline void setWorkspaceFilePath(const QString &filePath)
    :   Set the file path of the loaded workspace.

        Parameters:
        :   **filePath** – File path of the loaded workspace

    inline void beginLoadWorkspace()
    :   Begin the workspace loading process.

    inline void endLoadWorkspace()
    :   End the workspace loading process.

    inline void beginSaveWorkspace()
    :   Begin the workspace saving process.

    inline void endSaveWorkspace()
    :   End the workspace saving process.

    virtual bool hasWarmedUpNativeWidgets() const = 0
    :   Applies the CSS stylesheet to the dock managers virtual void applyStyleSheet() final { QFile styleSheetFile(“:/styles/ads\_light.css”);.

        styleSheetFile.open(QIODevice::ReadOnly);

        QTextStream styleSheetStream(&styleSheetFile); auto stylesheet = styleSheetStream.readAll();

        styleSheetFile.close();

        \_mainDockManager->setStyleSheet(stylesheet); auto dockManagers = findChildren<CDockManager\*>();

        for (auto dockManager : dockManagers) dockManager->setStyleSheet(stylesheet); } Get whether the native widgets have been warmed up already, to prevent multiple warmups

        Returns:
        :   Boolean indicating whether the native widgets have been warmed up already

    virtual void setViewPluginDockWidgetPermissionsGlobally(const util::DockWidgetPermissions &dockWidgetPermissions = util::DockWidgetPermission::All, bool set = true) = 0
    :   Set `dockWidgetPermissions` for all view plugin dock widgets.

        Parameters:
        :   - **dockWidgetPermissions** – Global dock widget permission flags
            - **set** – Whether to set or unset the dock widget permission flags

    virtual void newWorkspace() = 0
    :   Creates a new workspace.

    virtual void loadWorkspace(QString filePath = "", bool addToRecentWorkspaces = true) = 0
    :   Load a workspace from disk.

        This function loads the workspace state from the specified file and restores the associated workspace configuration.

        If the file path is empty, implementations may prompt the user to select a workspace file.

        The loaded workspace may optionally be added to the recent workspace list.

        Parameters:
        :   - **filePath** – Path of the workspace file to load. When empty, implementations may present a file selection dialog.
            - **addToRecentWorkspaces** – Whether the loaded workspace should be added to the recent workspace list.

    virtual workflow::UniqueWorkflowPlan loadWorkspaceWorkflowPlan(QString filePath = "", bool addToRecentWorkspaces = true) = 0
    :   Create a workflow plan that loads a workspace from disk.

        This function constructs and returns a workflow plan but does not execute it.

        When executed, the workflow loads the workspace state from the specified file and restores the associated workspace configuration.

        Implementations may use sequential, parallel, nested, or batched workflow stages and may publish progress, warnings, messages, and outputs as appropriate.

        If the file path is empty, implementations may prompt the user to select a workspace file.

        Framework code may compose the returned workflow directly, for example as a nested workflow within a larger project or application loading workflow.

        Parameters:
        :   - **filePath** – Path of the workspace file to load. When empty, implementations may present a file selection dialog.
            - **addToRecentWorkspaces** – Whether the loaded workspace should be added to the recent workspace list.

        Returns:
        :   Workflow plan that loads the workspace when executed.

    virtual void importWorkspaceFromProjectFile(QString filePath = "", bool addToRecentWorkspaces = true) = 0
    :   Import a workspace from a project file.

        Parameters:
        :   - **filePath** – File path of the project (choose file path with dialog when empty)
            - **addToRecentWorkspaces** – Whether to add the workspace file path to the recent workspace file paths

    virtual void saveWorkspace(QString filePath = "", bool addToRecentWorkspaces = true) = 0
    :   Save a workspace to disk.

        Parameters:
        :   - **filePath** – File path of the workspace (choose file path with dialog when empty)
            - **addToRecentWorkspaces** – Whether to add the workspace file path to the recent workspace file paths

    virtual void saveWorkspaceAs() = 0
    :   Save a workspace to disk on a different location.

    virtual bool hasWorkspace() const = 0
    :   Get whether a workspace exists.

        Returns:
        :   Boolean determining whether a workspace exists

    virtual const [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html#_CPPv4N2mv9WorkspaceE "mv::Workspace") \*getCurrentWorkspace() const = 0
    :   Get current workspace.

        Returns:
        :   Pointer to current workspace (nullptr if no workspace is loaded)

    virtual [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html#_CPPv4N2mv9WorkspaceE "mv::Workspace") \*getCurrentWorkspace() = 0
    :   Get current workspace.

        Returns:
        :   Pointer to current workspace (nullptr if no workspace is loaded)

    virtual WorkspaceLocations getWorkspaceLocations(const [WorkspaceLocation](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocationE "mv::WorkspaceLocation")::Types &types = [WorkspaceLocation](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocationE "mv::WorkspaceLocation")::[Type](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4TypeE "mv::WorkspaceLocation::Type")::[All](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4Type3AllE "mv::WorkspaceLocation::Type::All")) = 0
    :   Get workspace locations for location `types`.

        Returns:
        :   List of workspace locations

    virtual QStringList getViewPluginNames(const QString &workspaceJsonFile) const = 0
    :   Get view plugin names from `workspaceJsonFile`.

        Parameters:
        :   **workspaceJsonFile** – Location of the workspace JSON file

    virtual QImage toPreviewImage() const = 0
    :   Get a preview image.

        Returns:
        :   [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html#classmv_1_1Workspace) manager preview image

    void workspaceAboutToBeCreated()
    :   Signals that a new workspace is about to be created.

    void workspaceCreated(const mv::[Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html#_CPPv4N2mv9WorkspaceE "mv::Workspace") &workspace)
    :   Signals that `workspace` is created.

        Parameters:
        :   **workspace** – Reference to the created workspace

    void workspaceAboutToBeLoaded(const QString &filePath)
    :   Signals that a workspace is about to be loaded from `filePath`.

        Parameters:
        :   **filePath** – File path of the workspace

    void workspaceLoaded(const QString &filePath)
    :   Signals that a workspace is loaded from `filePath`.

        Parameters:
        :   **filePath** – File path of the workspace

    void workspaceAboutToBeSaved(const QString &filePath)
    :   Signals that a workspace is about to be saved to `filePath`.

        Parameters:
        :   **filePath** – File path of the workspace

    void workspaceSaved(const QString &filePath)
    :   Signals that a workspace is saved to `filePath`.

        Parameters:
        :   **filePath** – File path of the workspace

    void workspaceFilePathChanged(const QString &filePath)
    :   Signals that the location of the current workspace changed to `filePath`.

        Parameters:
        :   **filePath** – File path of the workspace
