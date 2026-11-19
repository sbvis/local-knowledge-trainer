# Project

**Source:** https://manivault.readthedocs.io/en/latest/api/core/application/project.html

**Documentation path:** `api/core/application/project.html`

---

# Project

`Project` represents the active analysis session and its project metadata. Its workflow-based serialization coordinates state from the relevant Core managers, including the data hierarchy, plugins, actions, and events.

Use [AbstractProjectManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html) for creating, opening, importing, saving, and publishing projects. The manager owns the current project; callers should not delete it or retain its pointer across project replacement.

Plugins normally participate through their own serialization contract. They should not invoke `Project::fromVariantMapWorkflow()` or `Project::toVariantMapWorkflow()` directly.

**Qualified name:** `mv::Project`

## Related

- [Project persistence](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/index.html)
- [Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html)

class Project : public QObject, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) class.

    Serializable class which encapsulates the entire ManiVault project.

    **Author**
    :   Thomas Kroes

    Public Functions

    Project(QObject \*parent = nullptr)
    :   Construct project with `parent`.

        Parameters:
        :   **parent** – Pointer to parent object

    Project(const QString &filePath, QObject \*parent = nullptr)
    :   Construct project from project JSON `filePath` and `parent`.

        Parameters:
        :   - **filePath** – Path of the project file
            - **parent** – Pointer to parent object

    QString getFilePath() const
    :   Get project file path.

        Returns:
        :   Location on disk where the project resides

    void setFilePath(const QString &filePath)
    :   Set project file path.

        Parameters:
        :   **filePath** – Location on disk where the project resides

    bool isStartupProject() const
    :   Get whether this is a startup project.

        Returns:
        :   Boolean determining whether this project is loaded at startup of ManiVault

    util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") getVersion() const
    :   Get version of the application (major and minor version number) with which the project is created.

        Returns:
        :   Pair of integers representing major and minor version number respectively

    void updateContributors()
    :   Update the contributors (adds current user if not already added)

    void setStudioMode(bool studioMode)
    :   Set studio mode to `studioMode`.

        Parameters:
        :   **studioMode** – Studio mode

    virtual workflow::UniqueWorkflowPlan fromVariantMapWorkflow(QVariantMap variantMap) override
    :   Create a workflow that restores this object’s state from a variant map.

        See Serializable::fromVariantMapWorkflow() for the full contract, execution semantics, and implementation requirements.

        Parameters:
        :   **variantMap** – Serialized object state.

        Returns:
        :   Workflow plan that restores the object state when executed.

    virtual workflow::UniqueWorkflowPlan toVariantMapWorkflow() const override
    :   Create a workflow that serializes this object’s state to a variant map.

        See Serializable::toVariantMapWorkflow() for the full contract, execution semantics, and implementation requirements.

        Returns:
        :   Workflow plan that serializes the object state when executed.

    [ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#_CPPv4N2mv17ProjectMetaActionE "mv::ProjectMetaAction") &getProjectMetaAction()
    :   Get project meta action.

        Returns:
        :   Reference to project meta action

    void filePathChanged(const QString &filePath)
    :   Signals that the project file path changed.

        Parameters:
        :   **filePath** – Location on disk where the project resides

    Public Static Functions

    static QSharedPointer<[ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#_CPPv4N2mv17ProjectMetaActionE "mv::ProjectMetaAction")> getProjectMetaActionFromProjectFilePath(const QString &projectFilePath)
    :   Get shared pointer to project meta action from the compressed `projectFilePath`.

        Returns:
        :   Shared pointer to project meta action (nullptr if not found)
