# ImageAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/image_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/image_action.html`

---

# ImageAction

**Qualified name:** `mv::gui::ImageAction`

class ImageAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Image widget action class (WIP)

    For image display and storage

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget configurations.

        *Values:*

        enumerator Preview

        enumerator Loader
        :   Image preview with a label widget.

    Public Functions

    Q\_INVOKABLE ImageAction(QObject \*parent, const QString &title, bool populateFilePickerCompleter = true)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **populateFilePickerCompleter** – Whether to create a QCompleter for \_filePathAction in \_filePickerAction

    const QImage getImage() const
    :   Get the current image.

    void setImage(const QImage &image)
    :   Set the current image.

        Parameters:
        :   **image** – Current image

    void loadImage(const QString &filePath)
    :   Load image from disk.

        Parameters:
        :   **filePath** – Path of the image on disk

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load image action from variant.

        Parameters:
        :   **variantMap** – Variant representation of the image action

    virtual QVariantMap toVariantMap() const override
    :   Save image action to variant.

        Returns:
        :   Variant representation of the image action

    void imageChanged(const QImage &image)
    :   Signals that the current image changed.

        Parameters:
        :   **image** – Current image that changed

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the image action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    Protected Attributes

    [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_filePathAction
    :   Current image.

    [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_fileNameAction
    :   String action which contains the last loaded file path.

    [FilePickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/file/file_picker_action.html#_CPPv4N2mv3gui16FilePickerActionE "mv::gui::FilePickerAction") \_filePickerAction
    :   String action which contains the last loaded file name.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_previewAction
    :   Action for loading the image from disk.

    class LoaderWidget : public QWidget
    :   Loader widget class for image action.

        Protected Functions

        LoaderWidget(QWidget \*parent, [ImageAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/image_action.html#_CPPv4N2mv3gui11ImageActionE "mv::gui::ImageAction") &imageAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **imageAction** – Reference to image action

        Protected Attributes

        [HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction") \_groupAction
        :   Pointer to owning image action.

        Friends

        *friend class* ImageAction

    class PreviewWidget : public QLabel
    :   Preview widget class for image action.

        Protected Functions

        PreviewWidget(QWidget \*parent, [ImageAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/image_action.html#_CPPv4N2mv3gui11ImageActionE "mv::gui::ImageAction") &imageAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **imageAction** – Reference to image action

        Friends

        *friend class* ImageAction
