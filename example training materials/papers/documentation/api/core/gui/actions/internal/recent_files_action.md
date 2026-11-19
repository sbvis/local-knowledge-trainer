# RecentFilesAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/recent_files_action.html

**Documentation path:** `api/core/gui/actions/internal/recent_files_action.html`

---

# RecentFilesAction

**Qualified name:** `mv::gui::RecentFilesAction`

class RecentFilesAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Recent files action class.

    Action class for storing and editing recent file paths and saving them to settings.

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE RecentFilesAction(QObject \*parent, const QString &fileType, const QString &shortcutPrefix = "", const QIcon &icon = QIcon())
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **fileType** – Type of file e.g. project or workspace
            - **shortcutPrefix** – Prefix of the shortcut
            - **icon** – Icon in menu

    void initialize(const QString &fileType, const QString &shortcutPrefix)
    :   Initializes the action.

        Parameters:
        :   - **fileType** – Type of file e.g. project or workspace
            - **shortcutPrefix** – Prefix of the shortcut

    void addRecentFilePath(const QString &filePath)
    :   Add recent `filePath`.

        Parameters:
        :   **filePath** – Recent file path

    QString getFileType() const
    :   Get file type.

        Returns:
        :   Recent file type

    QString getShortcutPrefix() const
    :   Get shortcut prefix.

        Returns:
        :   Shortcut prefix (if empty, no shortcut is created)

    const [RecentFilesListModel](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/recent_files_list_model.html#_CPPv4N2mv20RecentFilesListModelE "mv::RecentFilesListModel") &getModel() const
    :   Get list model.

        Returns:
        :   Const reference to list model

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") &getEditAction()
    :   Get edit action.

        Returns:
        :   Action which triggers a dialog in which the recent file paths can be edited

    QMenu \*getMenu(QWidget \*parent)
    :   Get recent file paths menu.

        Parameters:
        :   **parent** – Parent widget for the menu

        Returns:
        :   Pointer to menu

    void updateRecentFilePaths()
    :   Grab latest recent file paths from settings and update model.

    QStringList getRecentFilePaths() const
    :   Get recent file paths.

        Returns:
        :   File paths as string list

    util::RecentFiles getRecentFiles() const
    :   Get recent files.

        Returns:
        :   List of recent file objects

    void triggered(const QString &filePath)
    :   Signals that recent `filePath` is triggered.

    Protected Functions

    [RecentFilesListModel](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/recent_files_list_model.html#_CPPv4N2mv20RecentFilesListModelE "mv::RecentFilesListModel") &getModel()
    :   Get list model.

        Returns:
        :   Reference to list model

    class Dialog : public QDialog
    :   [Dialog](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/recent_files_action.html#classmv_1_1gui_1_1RecentFilesAction_1_1Dialog) for editing recent file paths.

        Protected Functions

        Dialog([RecentFilesAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/recent_files_action.html#_CPPv4N2mv3gui17RecentFilesActionE "mv::gui::RecentFilesAction") \*recentFilesAction)
        :   Construct a dialog with owning `recentFilePathsAction`.

            Parameters:
            :   **recentFilesAction** – Pointer to recent file paths action

        inline QSize sizeHint() const override
        :   Get preferred size.

        inline QSize minimumSizeHint() const override
        :   Get minimum size hint.
