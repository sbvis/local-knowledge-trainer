# RecentFilesListModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/recent_files_list_model.html

**Documentation path:** `api/core/models/recent_files/recent_files_list_model.html`

---

# RecentFilesListModel

**Qualified name:** `mv::RecentFilesListModel`

class RecentFilesListModel : public mv::[AbstractRecentFilesModel](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#_CPPv4N2mv24AbstractRecentFilesModelE "mv::AbstractRecentFilesModel")
:   Recent files list model class.

    Standard item model storing and manipulating recent file paths in list format.

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    RecentFilesListModel(QObject \*parent, const QString &recentFileType)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **recentFileType** – Type of recent file, e.g. “Project” or “Workspace”

    void load()
    :   Load recent file paths from settings.

    void save() const
    :   Save to settings.

    void addRecentFilePath(const QString &filePath)
    :   Add recent `filePath`.

        Parameters:
        :   **filePath** – Recent file path to add

    void removeRecentFilePath(const QString &filePath)
    :   Remove recent `filePath`.

        Parameters:
        :   **filePath** – Recent file path to remove

    QStringList getRecentFilePaths() const
    :   Get recent file paths.

        Returns:
        :   File paths as string list

    virtual util::RecentFiles getRecentFiles() const override
    :   Get recent files.

        Returns:
        :   List of recent file objects
