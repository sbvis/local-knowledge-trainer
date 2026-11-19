# DirectoryPickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/file/directory_picker_action.html

**Documentation path:** `api/core/gui/actions/file/directory_picker_action.html`

---

# DirectoryPickerAction

**Qualified name:** `mv::gui::DirectoryPickerAction`

class DirectoryPickerAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Directory picker action class.

    Action class for picking a directory

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

    explicit DirectoryPickerAction(QObject \*parent, const QString &title, const QString &directory = QString())
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **directory** – Directory

    QString getDirectory() const
    :   Get the current directory.

        Returns:
        :   Current directory

    void setDirectory(const QString &directory)
    :   Set the current directory.

        Parameters:
        :   **directory** – Current directory

    QString getPlaceholderString() const
    :   Get placeholder text.

        Returns:
        :   Placeholder string

    void setPlaceHolderString(const QString &placeholderString)
    :   Set placeholder text.

        Parameters:
        :   **placeholderText** – Placeholder text

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

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void directoryChanged(const QString &directory)
    :   Signals that the directory changed.

        Parameters:
        :   **directory** – Directory that changed

    void placeholderStringChanged(const QString &placeholderString)
    :   Signals that the placeholder string changed.

        Parameters:
        :   **placeholderString** – Placeholder string that changed

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the directory picker action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget

    Protected Attributes

    QCompleter \_completer
    :   Directory model.

    [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_directoryAction
    :   Completer.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_pickAction
    :   Directory action.

    bool \_useNativeDialog
    :   Pick directory action.
