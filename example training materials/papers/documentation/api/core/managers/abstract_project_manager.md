# AbstractProjectManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html

**Documentation path:** `api/core/managers/abstract_project_manager.html`

---

# AbstractProjectManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the project manager
mv::projects().saveProject(filePath);
```

## Opening published projects

Published projects open read-only by default. When the standard Open Project dialog detects a published project, it offers **Allow edit of published project**. The choice is represented by `ProjectOpenParameters::allowEditOfPublishedProject` and is applied after opening completes successfully.

Calls that supply a file path directly do not display this dialog and retain the default value, `false`. Treat editable opening as an explicit authoring operation rather than the normal published-project experience. See [Publishing a project](https://manivault.readthedocs.io/en/latest/development/building_applications/publishing_a_project.html) for the user-facing workflow.

## Related

- Project [models](https://manivault.readthedocs.io/en/latest/api/core/models/projects/index.html)
- [Project serialization and restoration](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/index.html)

**Qualified name:** `mv::AbstractProjectManager`

class AbstractProjectManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract project manager class.

    Base abstract plugin manager class for managing projects.

    **Author**
    :   Thomas Kroes

    Public Types

    enum class State
    :   The project manager is currently.

        *Values:*

        enumerator Idle

        enumerator OpeningProject
        :   Not doing anything.

        enumerator ImportingProject
        :   Opening a project.

        enumerator SavingProject
        :   Importing a project.

        enumerator PublishingProject
        :   Saving a project.

            Publishing a project

    enum class TemporaryDirType
    :   Temporary directory in which temporary files are saved during:

        *Values:*

        enumerator Open

        enumerator Save
        :   Opening of a project.

        enumerator Publish
        :   Saving of a project.

            Publishing of a project

    enum class ProjectSerializationTaskType
    :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) for monitoring the progress of:

        *Values:*

        enumerator ProjectSerialization

        enumerator ProjectDataSerialization

        enumerator ProjectWorkspaceSerialization

    Public Functions

    inline AbstractProjectManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void newProject(const QString &workspaceFilePath = "") = 0
    :   Creates a new project, possibly also loading a workspace located at `workspaceFilePath`.

        Parameters:
        :   **workspaceFilePath** – File path of the workspace to load (will not attempt to load workspace if empty)

    virtual void newProject(const Qt::AlignmentFlag &alignment, bool logging = false) = 0
    :   Creates a new project with default system view plugins (either on the left or right, other alignments are ignored)

        Parameters:
        :   - **alignment** – Alignment of the default plugins
            - **logging** – Whether to add a logging view at the bottom

    virtual void newBlankProject() = 0
    :   Creates a new blank project (without any view plugins or data)

    virtual void openProject(QString filePath = "", bool importDataOnly = false, bool loadWorkspace = true) = 0
    :   Open project from `filePath`.

        Parameters:
        :   - **filePath** – File path of the project (choose file path when empty)
            - **importDataOnly** – Whether to only import the data from the project
            - **loadWorkspace** – Whether to load the workspace which is accompanied by the project

    virtual void openProject(QUrl url, const QString &targetDirectory = "", bool importDataOnly = false, bool loadWorkspace = true) = 0
    :   Download project from `url`, store it in `targetDir` and open it.

        Parameters:
        :   - **url** – URL of the project
            - **targetDirectory** – Directory where the project is stored (temporary directory when empty)
            - **importDataOnly** – Whether to only import the data from the project
            - **loadWorkspace** – Whether to load the workspace which is accompanied by the project

    virtual void openProject(util::ProjectsModelProjectSharedPtr project, const QString &targetDirectory = "", bool importDataOnly = false, bool loadWorkspace = true) = 0
    :   Download project from `project` model, store it in `targetDir` and open it.

        Parameters:
        :   - **project** – Shared pointer to the project model project
            - **targetDirectory** – Directory where the project is stored (temporary directory when empty)
            - **importDataOnly** – Whether to only import the data from the project
            - **loadWorkspace** – Whether to load the workspace which is accompanied by the project

    virtual void importProject(QString filePath = "") = 0
    :   Import project from `filePath` (only import the data)

        Parameters:
        :   **filePath** – File path of the project (choose file path when empty)

    virtual void saveProject(QString filePath) = 0
    :   Save a project to `filePath`.

        Parameters:
        :   **filePath** – File path of the project (choose file path when empty)

    virtual void saveProjectAs() = 0
    :   Save project to different file (user is prompted to choose the file location)

    virtual void publishProject(QString filePath = "") = 0
    :   Publish project to `filePath`.

        Parameters:
        :   **filePath** – File path of the published project

    virtual bool hasProject() const = 0
    :   Get whether a project exists.

        Returns:
        :   Boolean determining whether a project exists

    virtual const [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") \*getCurrentProject() const = 0
    :   Get current project.

        Returns:
        :   Pointer to current project (nullptr if no project is loaded)

    virtual [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") \*getCurrentProject() = 0
    :   Get current project.

        Returns:
        :   Pointer to current project (nullptr if no project is loaded)

    virtual const [ProjectsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_list_model.html#_CPPv4N2mv17ProjectsListModelE "mv::ProjectsListModel") &getProjectsListModel() const = 0
    :   Get projects list model.

        Returns:
        :   Reference to the projects list model

    virtual const [ProjectsTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_tree_model.html#_CPPv4N2mv17ProjectsTreeModelE "mv::ProjectsTreeModel") &getProjectsTreeModel() const = 0
    :   Get projects tree model.

        Returns:
        :   Reference to the projects tree model

    virtual QFuture<QString> downloadProjectAsync(QUrl url, const QString &targetDirectory = "", [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task = nullptr) = 0
    :   Download project from `url` and store it in the default downloaded projects directory.

        Parameters:
        :   - **url** – URL of the project to download
            - **targetDirectory** – Directory where the project is stored (default is empty, which means the default downloaded projects directory)
            - **task** – Optional task to associate with the download operation (must live in the main/GUI thread)

        Returns:
        :   Future containing the path to the downloaded project file

    virtual QFuture<bool> isDownloadedProjectStaleAsync(QUrl url) const = 0
    :   Establish asynchronously whether the project at `url` is updated with respect to the last downloaded version.

        Returns:
        :   Future containing a boolean determining whether the project is stale (true) or not (false)

    virtual QDir getDownloadedProjectsDir() const = 0
    :   Get the directory where downloaded projects are stored.

        Returns:
        :   Directory where downloaded projects are stored

    inline QString getTemporaryDirPath(const [TemporaryDirType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager16TemporaryDirTypeE "mv::AbstractProjectManager::TemporaryDirType") &temporaryDirType) const
    :   Get path to the temporary directory of `temporaryDirType` Throws an exception if not found and returns the path to the application temporary directory as a fall-back.

        Parameters:
        :   **temporaryDirType** – Type of temporary directory, see [AbstractProjectManager::TemporaryDirType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#classmv_1_1AbstractProjectManager_1a94c2e5ffafa5ac11a67d62d12c0ddec4)

        Returns:
        :   Path of the temporary directory

    virtual QString extractFileFromManiVaultProject(const QString &maniVaultFilePath, const QTemporaryDir &temporaryDir, const QString &filePath) = 0
    :   Extract `filePath` from compressed ManiVault project in `maniVaultFilePath`.

        Parameters:
        :   - **maniVaultFilePath** – File path of the compressed ManiVault file
            - **temporaryDir** – Temporary directory where the extracted file resides
            - **filePath** – Relative file path of the file that needs to be extracted

        Returns:
        :   File path of the extracted file, empty string if extraction failed

    virtual QImage getWorkspacePreview(const QString &projectFilePath, const QSize &targetSize = QSize(500, 500)) const = 0
    :   Get preview image of the project workspace.

        Parameters:
        :   **projectFilePath** – Path of the project file

        Returns:
        :   Preview image

    virtual QMenu &getNewProjectMenu() = 0
    :   Get new project menu.

        Returns:
        :   Pointer to new project menu

    virtual QMenu &getImportDataMenu() = 0
    :   Get import data menu.

        Returns:
        :   Pointer to import data menu

    inline [State](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager5StateE "mv::AbstractProjectManager::State") getState() const
    :   Get the state of the project manager.

        Returns:
        :   State of the project manager

    inline void setState(const [State](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager5StateE "mv::AbstractProjectManager::State") &state)
    :   Set the state of the serializable object to `state`.

        Parameters:
        :   **state** – State of the serializable object

    inline bool isOpeningProject() const
    :   Get whether the project manager is opening a project.

        Returns:
        :   Boolean determining whether the project manager is opening a project

    inline bool isImportingProject() const
    :   Get whether the project manager is importing a project.

        Returns:
        :   Boolean determining whether the project manager is importing a project

    inline bool isSavingProject() const
    :   Get whether the project manager is saving a project.

        Returns:
        :   Boolean determining whether the project manager is saving a project

    inline bool isPublishingProject() const
    :   Get whether the project manager is publishing a project.

        Returns:
        :   Boolean determining whether the project manager is publishing a project

    virtual [ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#_CPPv4N2mv17ProjectMetaActionE "mv::ProjectMetaAction") \*getProjectMetaAction(const QString &projectFilePath) = 0
    :   Get project meta action for the project with `projectFilePath`.

        Parameters:
        :   **projectFilePath** – File path of the project for which to get the meta action

        Returns:
        :   Pointer to the project meta action, or nullptr if no action is found

    inline const [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") &getProjectDownloadTask() const
    :   Get the task for project download.

        Returns:
        :   Reference to the project download task

    void projectAboutToBeCreated()
    :   Signals that a new project is about to be created.

    void projectCreated(const mv::[Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") &project)
    :   Signals that `project` is created.

        Parameters:
        :   **project** – Reference to the created project

    void projectDestroyed(const QString &projectId)
    :   Signals that project with `projectId` is destroyed.

        Parameters:
        :   **projectId** – Globally unique identifier of the project that is destroyed

    void projectAboutToBeOpened(const mv::[Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") &project)
    :   Signals that `project` is about to be opened.

        Parameters:
        :   **project** – Reference to the project that is about to be opened

    void projectOpened(const mv::[Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") &project)
    :   Signals that `project` is opened.

        Parameters:
        :   **project** – Reference to the project that is opened

    void projectAboutToBeImported(const QString &filePath)
    :   Signals that a project is about to be imported from `filePath`.

        Parameters:
        :   **filePath** – Path of the project file which is about to be imported

    void projectImported(const QString &filePath)
    :   Signals that a project is imported from `filePath`.

        Parameters:
        :   **filePath** – Path of the project file which is imported

    void projectAboutToBeSaved(const mv::[Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") &project)
    :   Signals that `project` is about to be saved.

        Parameters:
        :   **project** – Reference to the project that is about to be saved

    void projectSaved(const mv::[Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") &project)
    :   Signals that `project` is saved.

        Parameters:
        :   **project** – Reference to the saved project

    void projectAboutToBePublished(const mv::[Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") &project)
    :   Signals that `project` is about to be published.

        Parameters:
        :   **project** – Reference to the project that is about to be published

    void projectPublished(const mv::[Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") &project)
    :   Signals that `project` is published.

        Parameters:
        :   **project** – Reference to the published project

    void projectAboutToBeDestroyed(const mv::[Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#_CPPv4N2mv7ProjectE "mv::Project") &project)
    :   Signals that `project` is about to be destroyed.

        Parameters:
        :   **project** – Reference to the project that is about to be destroyed

    void stateChanged(const [State](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager5StateE "mv::AbstractProjectManager::State") &state)
    :   Signals that the state of the project manager changed to `state`.

        Parameters:
        :   **state** – State of the project manager

    Public Static Functions

    static inline QString getTemporaryDirTypeName(const [TemporaryDirType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager16TemporaryDirTypeE "mv::AbstractProjectManager::TemporaryDirType") &temporaryDirType)
    :   Get temporary dir type name.

        Parameters:
        :   **temporaryDirType** – Temporary directory type

        Returns:
        :   Temporary directory type name for `temporaryDirType`

    Protected Functions

    inline void setTemporaryDirPath(const [TemporaryDirType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager16TemporaryDirTypeE "mv::AbstractProjectManager::TemporaryDirType") &temporaryDirType, const QString &temporaryDirPath)
    :   Set path to the temporary directory of `temporaryDirType` to `temporaryDirPath`.

        Parameters:
        :   - **temporaryDirType** – Type of temporary directory, see [AbstractProjectManager::TemporaryDirType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#classmv_1_1AbstractProjectManager_1a94c2e5ffafa5ac11a67d62d12c0ddec4)
            - **temporaryDirPath** – Path of the temporary directory

    inline void unsetTemporaryDirPath(const [TemporaryDirType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager16TemporaryDirTypeE "mv::AbstractProjectManager::TemporaryDirType") &temporaryDirType)
    :   Unset path to the temporary directory of `temporaryDirType`.

        Parameters:
        :   **temporaryDirType** – Type of temporary directory, see [AbstractProjectManager::TemporaryDirType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#classmv_1_1AbstractProjectManager_1a94c2e5ffafa5ac11a67d62d12c0ddec4)

    virtual [ProjectOpenParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager21ProjectOpenParametersE "mv::AbstractProjectManager::ProjectOpenParameters") getProjectOpenParameters(const QString &filePath) const = 0
    :   Get parameters for opening a project (parameters will be obtained from a file dialog if necessary)

        Parameters:
        :   **filePath** – File path of the project for which to get the parameters

        Returns:
        :   Parameters for opening a project

    virtual [ProjectImportParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager23ProjectImportParametersE "mv::AbstractProjectManager::ProjectImportParameters") getProjectImportParameters(const QString &filePath) const = 0
    :   Get parameters for importing a project (parameters will be obtained from a file dialog if necessary)

        Parameters:
        :   **filePath** – File path of the project for which to get the parameters

        Returns:
        :   Parameters for importing a project

    virtual [ProjectSaveParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager21ProjectSaveParametersE "mv::AbstractProjectManager::ProjectSaveParameters") getProjectSaveParameters(const QString &filePath) const = 0
    :   Get parameters for saving a project (parameters will be obtained from a file dialog if necessary)

        Parameters:
        :   **filePath** – File path of the project for which to get the parameters

        Returns:
        :   Parameters for saving a project

    virtual [ProjectPublishParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager24ProjectPublishParametersE "mv::AbstractProjectManager::ProjectPublishParameters") getProjectPublishParameters(const QString &filePath) const = 0
    :   Get parameters for publishing a project (parameters will be obtained from a file dialog if necessary)

        Parameters:
        :   **filePath** – File path of the project for which to get the parameters

        Returns:
        :   Parameters for publishing a project

    inline [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") &getProjectDownloadTask()
    :   Get the task for project download.

        Returns:
        :   Reference to the project download task

    class ProjectDownloadException : public mv::[ManiVaultException](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv18ManiVaultExceptionE "mv::ManiVaultException")
    :   Exception class for file project download issue.

    struct ProjectImportParameters : public mv::[AbstractProjectManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManagerE "mv::AbstractProjectManager")::[ProjectOperationParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager26ProjectOperationParametersE "mv::AbstractProjectManager::ProjectOperationParameters")
    :   Parameters for importing a project.

        Public Functions

        inline bool isValid() const
        :   File path of the project to import (choose file path when empty)

            Determine whether the parameters are valid

            Returns:
            :   Boolean determining whether the parameters are valid (currently only checks whether the file path is not empty, but can be extended in the future if necessary)

    struct ProjectOpenParameters : public mv::[AbstractProjectManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManagerE "mv::AbstractProjectManager")::[ProjectOperationParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager26ProjectOperationParametersE "mv::AbstractProjectManager::ProjectOperationParameters")
    :   Parameters for opening a project.

        Public Functions

        inline bool isValid() const
        :   Whether to disable read-only mode after opening a published project.

            Determine whether the parameters are valid

            Returns:
            :   Boolean determining whether the parameters are valid (currently only checks whether the file path is not empty, but can be extended in the future if necessary)

        Public Members

        bool allowEditOfPublishedProject = false
        :   File path of the project to open (choose file path when empty)

    struct ProjectOperationParameters
    :   Parameters for project operations (opening, importing, saving, publishing)

        Subclassed by [mv::AbstractProjectManager::ProjectImportParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#structmv_1_1AbstractProjectManager_1_1ProjectImportParameters), [mv::AbstractProjectManager::ProjectOpenParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#structmv_1_1AbstractProjectManager_1_1ProjectOpenParameters), [mv::AbstractProjectManager::ProjectPublishParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#structmv_1_1AbstractProjectManager_1_1ProjectPublishParameters), [mv::AbstractProjectManager::ProjectSaveParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#structmv_1_1AbstractProjectManager_1_1ProjectSaveParameters)

        Public Members

        std::uint32\_t maxParallelThreads
        :   Whether to parallelize the operation (currently only used for opening a project, but can be extended in the future if necessary)

        std::uint32\_t maxLoggingDepth = 8
        :   Maximum number of threads to use when parallelizing the operation (currently only used for opening a project, but can be extended in the future if necessary)

    struct ProjectPublishParameters : public mv::[AbstractProjectManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManagerE "mv::AbstractProjectManager")::[ProjectOperationParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager26ProjectOperationParametersE "mv::AbstractProjectManager::ProjectOperationParameters")
    :   Parameters for publishing a project.

        Public Functions

        inline bool isValid() const
        :   File path of the project to publish (choose file path when empty)

            Determine whether the parameters are valid

            Returns:
            :   Boolean determining whether the parameters are valid (currently only checks whether the file path is not empty, but can be extended in the future if necessary)

    struct ProjectSaveParameters : public mv::[AbstractProjectManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManagerE "mv::AbstractProjectManager")::[ProjectOperationParameters](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html#_CPPv4N2mv22AbstractProjectManager26ProjectOperationParametersE "mv::AbstractProjectManager::ProjectOperationParameters")
    :   Parameters for downloading a project.

        Public Functions

        inline bool isValid() const
        :   File path of the project to save (choose file path when empty)

            Determine whether the parameters are valid

            Returns:
            :   Boolean determining whether the parameters are valid (currently only checks whether the file path is not empty, but can be extended in the future if necessary)
