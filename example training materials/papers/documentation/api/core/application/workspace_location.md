# WorkspaceLocation

**Source:** https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html

**Documentation path:** `api/core/application/workspace_location.html`

---

# WorkspaceLocation

`WorkspaceLocation` is a small value object returned by the workspace manager when enumerating discoverable workspaces. It combines a display title, file path, and location type.

The type distinguishes built-in workspaces, workspaces found on the configured global path, and recent workspaces. `WorkspaceLocation` describes a location; it is not the active `Workspace` and does not own workspace state.

**Qualified name:** `mv::WorkspaceLocation`

## Related

- [AbstractWorkspaceManager](https://manivault.readthedocs.io/en/latest/api/core/application/abstract_workspace_manager.html)
- [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html)

class WorkspaceLocation
:   [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html#classmv_1_1Workspace) location which consists of a workspace title, file path and location type.

    Public Types

    enum Type
    :   Enum determining the type of workspace location.

        *Values:*

        enumerator BuiltIn

        enumerator Path
        :   Built-in workspaces (located in /workspaces in the application dir)

        enumerator Recent
        :   Workspaces on the global workspaces path.

        enumerator All
        :   Recent workspaces.

    Public Functions

    inline explicit WorkspaceLocation(const QString &title, const QString &filePath, const [Type](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4TypeE "mv::WorkspaceLocation::Type") &type)
    :   Construct workspace location with `filePath` and `type`.

        Parameters:
        :   - **title** – Title of the workspace
            - **filePath** – Location of the workspace on disk
            - **type** – Location type of the workspace

    inline QString getTitle() const
    :   Get file path of the workspace.

        Returns:
        :   File path of the workspace

    inline QString getFilePath() const
    :   Get file path of the workspace.

        Returns:
        :   File path of the workspace

    inline [Type](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4TypeE "mv::WorkspaceLocation::Type") getType() const
    :   Get type of workspace location.

        Returns:
        :   Type

    inline QString getTypeName() const
    :   Get type name of workspace location.

        Returns:
        :   Type name

    Public Static Functions

    static inline QString getTypeName(const [Type](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4TypeE "mv::WorkspaceLocation::Type") &type)
    :   Get name of `type`.

        Returns:
        :   Type name

    Public Static Attributes

    static QMap<[Type](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4TypeE "mv::WorkspaceLocation::Type"), QString> typeNames{{[BuiltIn](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4Type7BuiltInE "mv::WorkspaceLocation::BuiltIn"), "Built-in"}, {[Path](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4Type4PathE "mv::WorkspaceLocation::Path"), "Path"}, {[Recent](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4Type6RecentE "mv::WorkspaceLocation::Recent"), "Recent"}, {[All](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html#_CPPv4N2mv17WorkspaceLocation4Type3AllE "mv::WorkspaceLocation::All"), "All"}}
    :   Map enum type to name.
