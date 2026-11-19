# OptionsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/options_action.html

**Documentation path:** `api/core/gui/actions/option/options_action.html`

---

# OptionsAction

**Qualified name:** `mv::gui::OptionsAction`

class OptionsAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Options widget action class.

    Action for selecting multiple options at once

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator ComboBox

        enumerator ListView
        :   The widget includes a combobox widget.

        enumerator Selection
        :   The widget includes a list view widget.

        enumerator File
        :   The widget includes a selection control.

        enumerator Tags
        :   The widget includes a file control.

        enumerator Default
        :   The widget includes a flow layout with tags.

    Public Functions

    explicit Q\_INVOKABLE OptionsAction(QObject \*parent, const QString &title, const QStringList &options = QStringList(), const QStringList &selectedOptions = QStringList())
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **options** – Options to select from
            - **selectedOptions** – Initial selected options

    void initialize(const QStringList &options = QStringList(), const QStringList &selectedOptions = QStringList())
    :   Initialize the option action.

        Parameters:
        :   - **options** – Options to select from
            - **selectedOptions** – Initial selected options

    QStringList getOptions() const
    :   Get available options.

        Returns:
        :   Available options

    const [CheckableStringListModel](https://manivault.readthedocs.io/en/latest/api/core/models/miscellaneous/checkable_string_list_model.html#_CPPv4N2mv24CheckableStringListModelE "mv::CheckableStringListModel") &getOptionsModel() const
    :   Get options model.

        Returns:
        :   Checkable string list model

    std::uint32\_t getNumberOfOptions() const
    :   Get the number of options.

        Returns:
        :   Number of options

    bool hasOption(const QString &option) const
    :   Get whether a specific option exists.

        Parameters:
        :   **option** – Name of the option to check for

        Returns:
        :   Boolean indicating whether a specific option exists

    bool hasOptions() const
    :   Get whether there are any options.

        Returns:
        :   Boolean indicating whether there are any options

    void setOptions(const QStringList &options, bool clearSelection = false)
    :   Set the available options.

        Parameters:
        :   - **options** – Available Options
            - **clearSelection** – Whether to clear the current selection

    QStringList getSelectedOptions() const
    :   Get selected options.

        Returns:
        :   Selected options

    QList<std::int32\_t> getSelectedOptionIndices() const
    :   Get selected option indices.

        Returns:
        :   Selected options indices

    bool isOptionSelected(const QString &option) const
    :   Get whether a specific option is selected.

        Parameters:
        :   **option** – Name of the option to check for

        Returns:
        :   Boolean indicating whether the option is selected or not

    bool hasSelectedOptions() const
    :   Get whether one or more options are selected.

        Returns:
        :   Boolean indicating whether one or more options are selected

    void selectOption(const QString &option, bool unselect = false)
    :   Select option.

        Parameters:
        :   - **option** – Option to select
            - **unselect** – Whether to select or unselect the option

    void toggleOption(const QString &option)
    :   Toggle `option`.

        Parameters:
        :   **option** – Option to toggle

    void setSelectedOptions(const QStringList &selectedOptions)
    :   Set the selected options.

        Parameters:
        :   **selectedOptions** – Selected options

    void setSelectedOptions(const [CheckableStringListModel](https://manivault.readthedocs.io/en/latest/api/core/models/miscellaneous/checkable_string_list_model.html#_CPPv4N2mv24CheckableStringListModelE "mv::CheckableStringListModel")::[CheckedIndicesSet](https://manivault.readthedocs.io/en/latest/api/core/models/miscellaneous/checkable_string_list_model.html#_CPPv4N2mv24CheckableStringListModel17CheckedIndicesSetE "mv::CheckableStringListModel::CheckedIndicesSet") &selectedOptions)
    :   Set the selected options.

        Parameters:
        :   **selectedOptions** – Selected option indices

    void selectAll()
    :   Selects all options.

    void selectNone()
    :   Clears the options selection.

    void selectInvert()
    :   Inverts the options selection.

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void setSerializeAllOptions(bool serializeAllOptions)
    :   Set whether all options should be serialized to `serializeAllOptions` By default, only the selected options are serialized Setting this option to true will additionally serialize all options.

        Parameters:
        :   **serializeAllOptions** – Boolean determining whether all options should be serialized

    bool getSerializeAllOptions() const
    :   Get whether all options should be serialized.

        Returns:
        :   Boolean determining whether all options should be serialized (by default, only the selected options are serialized)

    void optionsChanged(const QStringList &options)
    :   Signals that the options changed.

        Parameters:
        :   **options** – Options

    void selectedOptionsChanged(const QStringList &selectedOptions)
    :   Signals that the selected options changed.

        Parameters:
        :   **selectedOptions** – Selected options

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the options action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    [CheckableStringListModel](https://manivault.readthedocs.io/en/latest/api/core/models/miscellaneous/checkable_string_list_model.html#_CPPv4N2mv24CheckableStringListModelE "mv::CheckableStringListModel") &getOptionsModel()
    :   Get options model.

        Returns:
        :   Checkable string list model

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive) override
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions

    Protected Attributes

    [FileAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/options_action.html#_CPPv4N2mv3gui13OptionsAction10FileActionE "mv::gui::OptionsAction::FileAction") \_fileAction
    :   Options model.

    Friends

    *friend class* AbstractActionsManager

    class ComboBoxWidget : public QWidget
    :   Combobox widget class for options action.

        Protected Functions

        ComboBoxWidget(QWidget \*parent, [OptionsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/options_action.html#_CPPv4N2mv3gui13OptionsActionE "mv::gui::OptionsAction") \*optionsAction, const std::int32\_t &widgetFlags)
        :   Construct with pointer to `parent` widget, `optionsAction` and `completer`.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **optionsAction** – Pointer to options action
                - **widgetFlags** – Widget flags for the configuration of the widget

        bool eventFilter(QObject \*target, QEvent \*event) override
        :   Respond to `target` events.

            Parameters:
            :   - **target** – Object of which an event occurred
                - **event** – The event that took place

        void updateCurrentText() const
        :   Updates the line edit text to the joined selected strings.

        Protected Attributes

        QHBoxLayout \_layout
        :   Pointer to owning options action.

        [MultiSelectComboBox](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/multi_select_combobox.html#_CPPv4N2mv3gui19MultiSelectComboBoxE "mv::gui::MultiSelectComboBox") \_comboBox
        :   Horizontal layout.

        QCompleter \_completer
        :   Combobox for selecting options.

        bool \_preventPopupClose
        :   For inline searching.

        Friends

        *friend class* OptionsAction

    class FileAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
    :   File action class.

        Action class for loading/saving selections

        **Author**
        :   Thomas Kroes

        Public Functions

        FileAction([OptionsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/options_action.html#_CPPv4N2mv3gui13OptionsActionE "mv::gui::OptionsAction") &optionsAction)
        :   Constructor.

            Parameters:
            :   **optionsAction** – Reference to owning options action

        Protected Attributes

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_loadSelectionAction
        :   Reference to owning options action.

        [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_saveSelectionAction
        :   Load selection action.

    class ListViewWidget : public QWidget
    :   List view widget class for options action.

        Protected Functions

        ListViewWidget(QWidget \*parent, [OptionsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/options_action.html#_CPPv4N2mv3gui13OptionsActionE "mv::gui::OptionsAction") \*optionsAction, const std::int32\_t &widgetFlags)
        :   Construct with pointer to `parent` widget, `optionsAction` and `completer`.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **optionsAction** – Pointer to options action
                - **widgetFlags** – Widget flags for the configuration of the widget

        Protected Attributes

        QSortFilterProxyModel \_filterModel
        :   Pointer to owning options action.

        [TableAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/table_action.html#_CPPv4N2mv3gui11TableActionE "mv::gui::TableAction") \_tableAction
        :   For filtering the options.

        Friends

        *friend class* OptionsAction

    class TagsViewWidget : public QWidget
    :   Tags view widget class for options action.

        Protected Functions

        TagsViewWidget(QWidget \*parent, [OptionsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/options_action.html#_CPPv4N2mv3gui13OptionsActionE "mv::gui::OptionsAction") \*optionsAction, const std::int32\_t &widgetFlags)
        :   Construct with pointer to `parent` widget, `optionsAction` and `completer`.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **optionsAction** – Pointer to options action
                - **widgetFlags** – Widget flags for the configuration of the widget

        Protected Attributes

        const bool \_hasSelectionTags
        :   Pointer to owning options action.

        QSortFilterProxyModel \_filterModel
        :   Whether to show tags for selection.

        [FlowLayout](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/flow_layout.html#_CPPv4N2mv3gui10FlowLayoutE "mv::gui::FlowLayout") \_flowLayout
        :   For filtering the options.

        QMap<QString, QWidget\*> \_widgetsMap
        :   Table view for showing the data.

        Friends

        *friend class* OptionsAction
