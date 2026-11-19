# FilePickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/file/file_picker_action.html

**Documentation path:** `api/core/gui/actions/file/file_picker_action.html`

---

# FilePickerAction

**Qualified name:** `mv::gui::FilePickerAction`

class FilePickerAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   File picker action class.

    Action class for picking a file

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget configurations.

        *Values:*

        enumerator LineEdit

        enumerator PushButton
        :   Widget includes a line edit.

        enumerator Default
        :   There is a button to pick a directory.

    Public Functions

    Q\_INVOKABLE FilePickerAction(QObject \*parent, const QString &title, const QString &filePath = QString(), bool populateCompleter = true)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **filePath** – File path
            - **populateCompleter** – Whether to create a QCompleter for \_filePathAction

    QString getFilePath() const
    :   Get the current file path.

        Returns:
        :   Current file path

    QString getApplicationRelativeFilePath() const
    :   Get the application-relative file path (if it exists)

        Returns:
        :   File path relative to the application directory when the file was picked, if the picked file path was a sub-path of the application directory

    void setFilePath(const QString &filePath)
    :   Set the file path.

        Parameters:
        :   **filePath** – Current file path

    QStringList getNameFilters() const
    :   Get the name filters.

        Returns:
        :   Name filters

    void setNameFilters(const QStringList &nameFilters)
    :   Set the name filters to `nameFilters`.

        Parameters:
        :   **nameFilters** – Name filters

    QString getDefaultSuffix() const
    :   Get the default suffix.

        Returns:
        :   Default suffix

    void setDefaultSuffix(const QString &defaultSuffix)
    :   Set the default suffix to `defaultSuffix`.

        Parameters:
        :   **defaultSuffix** – Default suffix

    QString getFileType() const
    :   Get the file type.

        Returns:
        :   File type

    void setFileType(const QString &fileType)
    :   Set file type to `fileType`.

        Parameters:
        :   **fileType** – File type

    QString getPlaceholderString() const
    :   Get placeholder text.

        Returns:
        :   Placeholder string

    void setPlaceHolderString(const QString &placeholderString)
    :   Set placeholder text.

        Parameters:
        :   **placeholderString** – Placeholder text

    QString getDirectoryName() const
    :   Get directory name.

        Returns:
        :   Directory name

    void setUseNativeFileDialog(bool useNativeDialog)
    :   Set whether to use native or Qt file dialog.

        Parameters:
        :   **useNativeDialog** – Whether to use native or Qt file dialog

    bool getUseNativeFileDialog() const
    :   Get whether to use native or Qt file dialog.

        Returns:
        :   Bool whether to use native or Qt file dialog

    bool isValid() const
    :   Get whether the directory is valid or not.

        Returns:
        :   Boolean indication whether the directory is valid or not

    QString getApplicationDirectory() const
    :   Get the application directory.

        Returns:
        :   [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application) directory

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load file picker action from variant.

        Parameters:
        :   **variantMap** – Variant representation of the file picker action

    virtual QVariantMap toVariantMap() const override
    :   Save file picker action to variant.

        Returns:
        :   Variant representation of the file picker action

    void filePathChanged(const QString &filePath)
    :   Signals that the file path changed to `filePath`.

        Parameters:
        :   **filePath** – New file path

    void placeholderStringChanged(const QString &placeholderString)
    :   Signals that the placeholder string changed.

        Parameters:
        :   **placeholderString** – Placeholder string that changed

    void fileTypeChanged(const QString &fileType)
    :   Signals that the file type has changed to `fileType`.

        Parameters:
        :   **fileType** – File type

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the file picker action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget
