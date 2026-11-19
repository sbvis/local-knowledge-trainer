# Workspace

**Source:** https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html

**Documentation path:** `api/core/application/workspace.html`

---

# Workspace

`Workspace` is the serializable value associated with the current layout-oriented workspace. It stores the workspace file path and exposes actions for locking, title, description, tags, and comments.

Use [AbstractWorkspaceManager](https://manivault.readthedocs.io/en/latest/api/core/application/abstract_workspace_manager.html) to create, load, save, and query workspaces or to manipulate view-plugin layout. The manager exposes the current workspace; callers should treat that pointer as manager-owned and should not retain it across workspace replacement.

The `Workspace` object stores workspace metadata and locking state. Docking and view-plugin layout operations remain responsibilities of the workspace manager.

**Qualified name:** `mv::Workspace`

## Related

- [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html)
- [WorkspaceLocation](https://manivault.readthedocs.io/en/latest/api/core/application/workspace_location.html)

class Workspace : public QObject, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html#classmv_1_1Workspace) class.

    Container class for all view plugins in a ManiVault project.

    **Author**
    :   Thomas Kroes

    Public Functions

    Workspace(QObject \*parent = nullptr)
    :   Construct workspace with `parent`.

        Parameters:
        :   **parent** – Pointer to parent object

    Workspace(const QString &filePath, QObject \*parent = nullptr)
    :   Construct workspace with `parent` and load from `filePath`.

        Parameters:
        :   - **filePath** – Path of the workspace file
            - **parent** – Pointer to parent object

    QString getFilePath() const
    :   Get workspace file path.

        Returns:
        :   Location on disk where the workspace resides

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load workspace from variant.

        Parameters:
        :   **Variant** – representation of the workspace

    virtual QVariantMap toVariantMap() const override
    :   Save workspace to variant.

        Returns:
        :   Variant representation of the widget action

    void filePathChanged(const QString &filePath)
    :   Signals that the workspace file path changed.

        Parameters:
        :   **filePath** – Location on disk where the workspace resides

    Protected Functions

    void setFilePath(const QString &filePath)
    :   Set workspace file path.

        Parameters:
        :   **filePath** – Location on disk where the workspace resides
