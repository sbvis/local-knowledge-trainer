# OptionAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html

**Documentation path:** `api/core/gui/actions/option/option_action.html`

---

# OptionAction

**Qualified name:** `mv::gui::OptionAction`

class OptionAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Option widget action class.

    Stores options and creates widgets to interact with these

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::DatasetPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html#classmv_1_1gui_1_1DatasetPickerAction), [mv::gui::PluginPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_picker_action.html#classmv_1_1gui_1_1PluginPickerAction)

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator ComboBox

        enumerator LineEdit
        :   The widget includes a combobox widget.

        enumerator HorizontalButtons
        :   The widget includes a searchable line edit widget.

        enumerator VerticalButtons
        :   The widget includes a push button for each option in a horizontal layout.

        enumerator Clearable
        :   The widget includes a push button for each option in a vertical layout.

        enumerator Default
        :   The widget includes a push button to clear the selection (current index is set to minus one)

    Public Functions

    explicit Q\_INVOKABLE OptionAction(QObject \*parent, const QString &title, const QStringList &options = QStringList(), const QString &currentOption = "")
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **options** – Options
            - **currentOption** – Current option

    void initialize(const QStringList &options = QStringList(), const QString &currentOption = "")
    :   Initialize the option action.

        Parameters:
        :   - **options** – Options
            - **currentOption** – Current option

    void initialize(QAbstractItemModel &customModel, const QString &currentOption = "", const QString &defaultOption = "")
    :   Initialize the option action with a custom model.

        Parameters:
        :   - **customModel** – Pointer to custom model
            - **currentOption** – Current option
            - **defaultOption** – Default option

    QStringList getOptions() const
    :   Get the options.

    std::uint32\_t getNumberOfOptions() const
    :   Get the number of options.

    bool hasOption(const QString &option) const
    :   Determines whether an option exists.

    bool hasOptions() const
    :   Determines whether there are any options.

    void setOptions(const QStringList &options)
    :   Set the options.

        Parameters:
        :   **options** – Options

    void setCustomModel(QAbstractItemModel \*itemModel)
    :   Set a custom item model for more advanced display of options.

        Parameters:
        :   **itemModel** – Pointer to custom item model

    bool hasCustomModel() const
    :   Determines whether the option action has a custom item model.

    std::int32\_t getCompletionColumn() const
    :   Get the completion column.

        Returns:
        :   Completion column (defaults to 0)

    void setCompletionColumn(const std::int32\_t &completionColumn)
    :   Set the completion column to `completionColumn`.

        Parameters:
        :   **completionColumn** – Completion column (defaults to 0)

    Qt::MatchFlag getCompletionMatchMode() const
    :   Get the completion match mode.

        Returns:
        :   Match mode for the completer (defaults to Qt::MatchExactly)

    void setCompletionMatchMode(const Qt::MatchFlag &completionMatchMode)
    :   Set the completion match mode for the completer to `completionMatchMode`.

        Parameters:
        :   **completionMatchMode** – Match mode for the completer (defaults to Qt::MatchExactly)

    std::int32\_t getCurrentIndex() const
    :   Get the current option index.

    void setCurrentIndex(const std::int32\_t &currentIndex)
    :   Set the current option index.

        Parameters:
        :   **currentIndex** – Current option index

    QString getCurrentText() const
    :   Get the current option index.

    void setCurrentText(const QString &currentText)
    :   Set the current option text.

        Parameters:
        :   **currentText** – Current option text

    QString getPlaceholderString() const
    :   Get placeholder text (shown when no option selected)

    void setPlaceHolderString(const QString &placeholderString)
    :   Set placeholder text (shown when no option selected)

        Parameters:
        :   **placeholderString** – Placeholder text

    bool hasSelection() const
    :   Determines whether an option has been selected.

    const QAbstractItemModel \*getModel() const
    :   Get the used item model.

    std::int32\_t getCompleterPopupFixedWidth() const
    :   Get the fixed width of the completer popup.

        Returns:
        :   Fixed width of the completer popup (0 means no fixed width, defaults to 0)

    void setCompleterPopupFixedWidth(const std::int32\_t &completerPopupFixedWidth)
    :   Set the fixed width of the completer popup to `completerPopupFixedWidth`.

        Parameters:
        :   **completerPopupFixedWidth** – Fixed width of the completer popup (0 means no fixed width, defaults to 0)

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void modelChanged()
    :   Signals that the model changed.

    void customModelChanged(QAbstractItemModel \*customModel)
    :   Signals that the custom model changed.

        Parameters:
        :   **customModel** – Custom model

    void currentIndexChanged(const std::int32\_t &currentIndex)
    :   Signals that the current index changed.

        Parameters:
        :   **currentIndex** – Current index

    void currentTextChanged(const QString &currentText)
    :   Signals that the current text changed.

        Parameters:
        :   **currentText** – Current text

    void placeholderStringChanged(const QString &placeholderString)
    :   Signals that the placeholder string changed.

        Parameters:
        :   **placeholderString** – Placeholder string that changed

    void completionColumnChanged(std::int32\_t previousCompletionColumn, std::int32\_t currentCompletionColumn)
    :   Signals that the completion column changed from `previousCompletionColumn` to `currentCompletionColumn`.

        Parameters:
        :   - **previousCompletionColumn** – Previous completion column
            - **currentCompletionColumn** – Current completion column

    void completionMatchModeChanged(const Qt::MatchFlag &previousMatchMode, const Qt::MatchFlag &currentMatchMode)
    :   Signals that the filter index changed from `previousMatchMode` to `currentMatchMode`.

        Parameters:
        :   - **previousMatchMode** – Previous match mode
            - **currentMatchMode** – Current match mode

    void completerPopupFixedWidthChanged(std::int32\_t previousCompleterPopupFixedWidth, std::int32\_t currentCompleterPopupFixedWidth)
    :   Signals that the completer popup fixed width changed from `previousCompleterPopupFixedWidth` to `currentCompleterPopupFixedWidth`.

        Parameters:
        :   - **previousCompleterPopupFixedWidth** – Previous completer popup fixed width
            - **currentCompleterPopupFixedWidth** – Current completer popup fixed width

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the option action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

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

    QAbstractItemModel \*\_customModel
    :   Default simple string list model.

    std::int32\_t \_currentIndex
    :   Custom item model for enriched (combobox) ui.

    QString \_placeholderString
    :   Currently selected index.

    std::int32\_t \_completionColumn
    :   Place holder string.

    Qt::MatchFlag \_completionMatchMode
    :   Filter index on the custom model (if it exists, defaults to 0)

    std::int32\_t \_completerPopupFixedWidth
    :   Match mode for the completer (defaults to Qt::MatchExactly)

    Friends

    *friend class* AbstractActionsManager

    class ButtonsWidget : public QWidget
    :   Horizontal/vertical buttons widget for option action.

        Protected Functions

        ButtonsWidget(QWidget \*parent, [OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") \*optionAction, const Qt::Orientation &orientation)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **optionAction** – Pointer to option action
                - **orientation** – Orientation of the buttons widget (horizontal/vertical)

    class ComboBoxWidget : public QComboBox
    :   Combobox widget class for option action.

        Subclassed by [mv::gui::ColorMapAction::ComboBoxWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#classmv_1_1gui_1_1ColorMapAction_1_1ComboBoxWidget)

        Protected Functions

        ComboBoxWidget(QWidget \*parent, [OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") \*optionAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **optionAction** – Pointer to option action

        void paintEvent(QPaintEvent \*paintEvent) override
        :   Paint event (overridden to show placeholder text)

            Parameters:
            :   **paintEvent** – Pointer to paint event

        Friends

        *friend class* OptionAction

    class LazyIndicesModel : public QAbstractListModel
    :   Performance oriented last model which avoids unnecessary creation and clones of huge string lists.

        Public Functions

        explicit LazyIndicesModel(QObject \*parent = nullptr)
        :   Construct with pointer to `parent` object (maybe nullptr)

            Parameters:
            :   **parent** – Pointer to parent object (maybe nullptr)

        void setSourceAndMatches(QAbstractItemModel \*sourceModel, const QVector<int> &matches)
        :   Set the source model and the matches.

            Parameters:
            :   - **sourceModel** – Pointer to source model
                - **matches** – Vector of indices in the source model that matched

        int rowCount(const QModelIndex &index = QModelIndex()) const override
        :   Reimplemented to return the number of rows for `index` in the model.

            Parameters:
            :   **index** – Index in the model to check (defaults to invalid index)

            Returns:

        QVariant data(const QModelIndex &index, int role) const override
        :   Get data at `idx` for the specified `role`.

            Parameters:
            :   - **index** – Index in the model to get data for
                - **role** – Role of the data to get (defaults to Qt::DisplayRole)

            Returns:
            :   Data for the specified index and role, or an invalid QVariant if the index is invalid or the role is not Qt::DisplayRole

        bool canFetchMore(const QModelIndex &index) const override
        :   Reimplemented to return the index for the specified `row` and `column`.

            Parameters:
            :   **index** – Parent index in the model (defaults to invalid index)

            Returns:
            :   Boolean indicating whether more data can be fetched for the specified `index`

        void fetchMore(const QModelIndex &index) override
        :   Fetch more data for the specified `index`.

            Parameters:
            :   **index** – Index in the model to fetch more data for (defaults to invalid index)

    class LineEditWidget : public QLineEdit
    :   Line edit widget (with auto-completion) class for option action.

        Protected Functions

        LineEditWidget(QWidget \*parent, [OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") \*optionAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **optionAction** – Pointer to option action

        Protected Attributes

        QCompleter \_completer
        :   Pointer to owning option action.

        [StringsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionAction18StringsFilterModelE "mv::gui::OptionAction::StringsFilterModel") \_stringsFilterModel
        :   Completer for searching and filtering.

        [LazyIndicesModel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionAction16LazyIndicesModelE "mv::gui::OptionAction::LazyIndicesModel") \_lazyIndicesModel
        :   Strings filter model for optimized filtering of the source model.

        Friends

        *friend class* OptionAction

    class StringsFilterModel : public QSortFilterProxyModel
    :   Performance oriented strings filter model class (does not use regex’s etc.)

        Public Functions

        bool filterAcceptsRow(int sourceRow, const QModelIndex &sourceParent) const override
        :   Determines whether the row at `sourceRow` in `sourceParent` should be accepted.

            Parameters:
            :   - **sourceRow** – Row in the source model to check
                - **sourceParent** – Parent index in the source model to check

            Returns:
            :   True if the row should be accepted, false otherwise

        QString getTextFilter() const
        :   Get the text filter.

            Returns:
            :   Text filter

        void setTextFilter(const QString &textFilter)
        :   Set the text filter to `textFilter`.

            Parameters:
            :   **textFilter** – Text filter to apply to the source model
