# File Dialog

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/file_dialog.html

**Documentation path:** `api/core/gui/widgets/file_dialog.html`

---

# File Dialog

**Qualified name:** `mv::gui::FileDialog`

class FileDialog : public QFileDialog
:   File dialog class.

    GUI class for picking files and directories for open/save (defaults with non-native dialog)

    **Author**
    :   Thomas Kroes

    Subclassed by mv::gui::DirectoryOpenDialog, mv::gui::FileOpenDialog, mv::gui::FileSaveDialog

    Public Functions

    explicit FileDialog(QWidget \*parent = nullptr, const QString &caption = QString(), const QString &directory = QString(), const QString &filter = QString())
    :   Construct with pointer to `parent` widget and additional settings.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **caption** – Dialog title
            - **directory** – Initial directory
            - **filter** – Filter

    inline QSize sizeHint() const override
    :   Get preferred size.

        Returns:
        :   Size in pixels

    inline QSize minimumSizeHint() const override
    :   Get minimum size hint.

        Returns:
        :   Size in pixels

    Public Static Functions

    static QString getOpenFileName(QWidget \*parent = nullptr, const QString &caption = QString(), const QString &directory = QString(), const QString &filter = QString(), QString \*selectedFilter = nullptr, Options options = Options())
    :   Returns an existing file selected by the user, if the user presses cancel, it returns an empty file.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **caption** – Dialog title
            - **directory** – Initial directory
            - **filter** – File filter
            - **selectedFilter** – Selected filter
            - **options** – Dialog options

        Returns:
        :   File path when accepted

    static QUrl getOpenFileUrl(QWidget \*parent = nullptr, const QString &caption = QString(), const QUrl &directoryUrl = QUrl(), const QString &filter = QString(), QString \*selectedFilter = nullptr, Options options = Options(), const QStringList &supportedSchemes = QStringList())
    :   Returns an existing file URL selected by the user, if the user presses cancel, it returns an empty file URL.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **caption** – Dialog title
            - **directoryUrl** – Initial directory
            - **filter** – File filter
            - **selectedFilter** – Selected filter
            - **options** – Dialog options
            - **supportedSchemes** – Supported schemes

        Returns:
        :   File URL when accepted

    static QString getExistingDirectory(QWidget \*parent = nullptr, const QString &caption = QString(), const QString &dir = QString(), Options options = ShowDirsOnly)
    :   Returns an existing directory selected by the user, if the user presses cancel, it returns an empty directory.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **caption** – Dialog title
            - **dir** – Initial directory
            - **options** – Dialog options

        Returns:
        :   Directory path when accepted

    static QUrl getExistingDirectoryUrl(QWidget \*parent = nullptr, const QString &caption = QString(), const QUrl &directoryUrl = QUrl(), Options options = ShowDirsOnly, const QStringList &supportedSchemes = QStringList())
    :   Returns an existing directory URL selected by the user, if the user presses cancel, it returns an empty directory URL.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **caption** – Dialog title
            - **directoryUrl** – Initial directory
            - **options** – Dialog options
            - **supportedSchemes** – Supported schemes

        Returns:
        :   Directory URL when accepted
