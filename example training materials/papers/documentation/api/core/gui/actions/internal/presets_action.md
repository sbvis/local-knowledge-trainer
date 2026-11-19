# PresetsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/presets_action.html

**Documentation path:** `api/core/gui/actions/internal/presets_action.html`

---

# PresetsAction

**Qualified name:** `mv::gui::PresetsAction`

class PresetsAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Presets action class.

    Action class for interacting with widget action presets.

    This action allows you to manage the presets for a particular widget action. More precisely it allows to:

    - Save the widget action state to application settings
    - Load the widget action state from application settings
    - Save widget action default preset to application settings
    - Load widget action default preset from application settings
    - Export widget action state to preset file
    - Import widget action state from preset file
    - Manage presets for the widget action (remove presets etc.)

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Name

        enumerator DateTime
        :   Name of the preset.

            Date and time when the preset was created

    Public Functions

    Q\_INVOKABLE PresetsAction(QObject \*parent, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*sourceAction, const QString &settingsKey = "", const QString &presetType = "", const util::[StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") &icon = util::[StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon")())
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **sourceAction** – Non-owning pointer to widget action of which to save presets
            - **settingsKey** – Settings key where the presets are stored
            - **presetType** – Type of preset
            - **icon** – Icon in menu

    QString getSettingsKey() const
    :   Get settings key.

        Returns:
        :   Settings key where the recent file paths will be stored

    QString getPresetType() const
    :   Get preset type.

        Returns:
        :   Preset file type

    QStandardItemModel &getModel()
    :   Get model.

        Returns:
        :   Reference to model

    const [FilterModel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/presets_action.html#_CPPv4N2mv3gui13PresetsAction11FilterModelE "mv::gui::PresetsAction::FilterModel") &getFilterModel() const
    :   Get filter model.

        Returns:
        :   Reference to filter model

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") &getEditAction()
    :   Get edit action.

        Returns:
        :   Action which triggers a dialog in which the recent file paths can be edited

    const QVariantMap &getPresets() const
    :   Get presets.

        Returns:
        :   Variant map containing the presets

    void loadPresetsFromApplicationSettings()
    :   Load presets variant map from application settings.

    void savePresetsToApplicationSettings() const
    :   Save presets variant map to application settings.

    QMenu \*getMenu(QWidget \*parent = nullptr)
    :   Get recent file paths menu.

        Returns:
        :   Pointer to menu

    void loadPreset(const QString &name)
    :   Load preset from settings with `name`.

        Parameters:
        :   **name** – Name of the preset

    void savePreset(const QString &name)
    :   Save preset to settings with `name` and update application settings.

        Parameters:
        :   **name** – Name of the preset

    void removePreset(const QString &name)
    :   Remove preset with `name` and update application settings.

        Parameters:
        :   **name** – Name of the preset to remove

    void removePresets(const QStringList &names)
    :   Remove presets with `names` and update application settings.

        Parameters:
        :   **names** – Names of the preset to remove

    void loadDefaultPreset()
    :   Load default preset from settings.

    void saveDefaultPreset()
    :   Save default preset to settings.

    void importPreset()
    :   Import preset from file.

    void exportPreset()
    :   Export preset to file.

    void presetAboutToBeLoaded(const QString &name)
    :   Signals that preset with `name` is about to be loaded.

        Parameters:
        :   **name** – Name of the preset that is about to be loaded

    void presetLoaded(const QString &name)
    :   Signals that preset with `name` is loaded.

        Parameters:
        :   **name** – Name of the preset that was loaded

    void presetSaved(const QString &name)
    :   Signals that preset with `name` is saved.

        Parameters:
        :   **name** – Name of the preset that was saved

    void presetAboutToBeRemoved(const QString &name)
    :   Signals that preset with `name` is about to be removed.

        Parameters:
        :   **name** – Name of the preset that is about to be removed

    void presetRemoved(const QString &name)
    :   Signals that preset with `name` is removed.

        Parameters:
        :   **name** – Name of the preset that was removed

    void presetImported(const QString &filePath)
    :   Signals that preset with `filePath` is imported.

        Parameters:
        :   **filePath** – File path of the preset that was imported

    void presetExported(const QString &filePath)
    :   Signals that preset with `filePath` is exported.

        Parameters:
        :   **filePath** – File path of the preset that was exported

    Public Static Attributes

    static QMap<[Column](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/presets_action.html#_CPPv4N2mv3gui13PresetsAction6ColumnE "mv::gui::PresetsAction::Column"), QPair<QString, QString>> columnInfo
    :   Column name and tooltip.

    class ChoosePresetNameDialog : public QDialog
    :   Dialog for choosing a preset name.

        Protected Functions

        ChoosePresetNameDialog([PresetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/presets_action.html#_CPPv4N2mv3gui13PresetsActionE "mv::gui::PresetsAction") \*presetsAction, QWidget \*parent = nullptr)
        :   Construct a dialog with `parent`.

            Parameters:
            :   - **presetsAction** – Pointer to presets action
                - **parent** – Pointer to parent widget

        QSize sizeHint() const override
        :   Get preferred size.

        inline QSize minimumSizeHint() const override
        :   Get minimum size hint.

        inline [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") &getPresetNameAction()
        :   Get preset name action.

            Returns:
            :   Reference to preset name action

    class FilterModel : public QSortFilterProxyModel
    :   Filter model for presets model.

        Public Functions

        FilterModel(QObject \*parent = nullptr)
        :   Construct the filter model with `parent`.

            Parameters:
            :   **parent** – Pointer to parent object

        bool filterAcceptsRow(int row, const QModelIndex &parent) const override
        :   Returns whether `row` with `parent` is filtered out (false) or in (true)

            Parameters:
            :   - **row** – Row index
                - **parent** – Parent index

            Returns:
            :   Boolean indicating whether the item is filtered in or out

        bool lessThan(const QModelIndex &lhs, const QModelIndex &rhs) const override
        :   Compares two model indices plugin `lhs` with `rhs`.

            Parameters:
            :   - **lhs** – Left-hand model index
                - **rhs** – Right-hand model index

    class ManagePresetsDialog : public QDialog
    :   Dialog for managing presets.

        Protected Functions

        ManagePresetsDialog([PresetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/presets_action.html#_CPPv4N2mv3gui13PresetsActionE "mv::gui::PresetsAction") \*presetsAction)
        :   Construct a dialog with owning `presetsAction`.

            Parameters:
            :   **presetsAction** – Pointer to presets action

        QSize sizeHint() const override
        :   Get preferred size.

        inline QSize minimumSizeHint() const override
        :   Get minimum size hint.
