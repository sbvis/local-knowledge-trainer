# StringAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html

**Documentation path:** `api/core/gui/actions/textual/string_action.html`

---

# StringAction

**Qualified name:** `mv::gui::StringAction`

class StringAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   String widget action class.

    Stores a string creates widgets to interact with it

    **Author**
    :   Thomas Kroes

    Subclassed by mv::gui::NumberOfRowsAction

    Public Types

    enum WidgetFlag
    :   Describes the widget configurations.

        *Values:*

        enumerator Label

        enumerator LineEdit
        :   Widget includes a label.

        enumerator TextEdit
        :   Widget includes a line edit.

        enumerator Default
        :   Widget includes a text edit.

    Public Functions

    explicit Q\_INVOKABLE StringAction(QObject \*parent, const QString &title, const QString &string = "")
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **string** – String

    QString getString() const
    :   Gets the current string.

    void setString(const QString &string)
    :   Sets the current string.

        Parameters:
        :   **string** – Current string

    QString getPlaceholderString() const
    :   Get placeholder text.

    void setPlaceHolderString(const QString &placeholderString)
    :   Set placeholder text.

        Parameters:
        :   **placeholderString** – Placeholder text

    QAction &getLeadingAction()
    :   Get action at leading position.

        Returns:
        :   Reference to action at leading position

    QAction &getTrailingAction()
    :   Get action at trailing position.

        Returns:
        :   Reference to action at trailing position

    QCompleter \*getCompleter() const
    :   Get completer.

        Returns:
        :   Pointer to completer

    void setCompleter(QCompleter \*completer)
    :   Set completer.

        Parameters:
        :   **completer** – Pointer to completer

    bool getSearchMode() const
    :   Get search mode (if on, there will be a leading action with a search icon and a trailing action to clear the string)

        Returns:
        :   Search mode

    void setSearchMode(bool searchMode)
    :   Set search mode (if on, there will be a leading action with a search icon and a trailing action to clear the string)

        Parameters:
        :   **searchMode** – Whether search mode is on/off

    bool isClearable() const
    :   Get whether the string can be cleared by clicking the trailing action.

        Returns:
        :   Boolean indicating whether the string can be cleared

    void setClearable(bool clearable)
    :   Set whether the string can be cleared by clicking the trailing action.

        Parameters:
        :   **clearable** – Boolean indicating whether the string can be cleared

    Qt::TextElideMode getTextElideMode() const
    :   Get text elide mode.

        Returns:
        :   Text elide mode

    void setTextElideMode(const Qt::TextElideMode &textElideMode)
    :   Set text elide mode.

        Parameters:
        :   **textElideMode** – Text elide mode

    QRegularExpressionValidator &getValidator()
    :   Get validator.

        Returns:
        :   Reference to regular expression validator

    QValidator::State isValid() const
    :   Get whether the string is QValidator::State::Acceptable, QValidator::State::Intermediate or QValidator::State::Invalid.

        Returns:
        :   Validator state

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant.

        Parameters:
        :   **variantMap** – Variant representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant.

        Returns:
        :   Variant representation of the widget action

    void stringChanged(const QString &string)
    :   Signals that the current string changed to `string`.

        Parameters:
        :   **string** – Current string that changed

    void placeholderStringChanged(const QString &placeholderString)
    :   Signals that the placeholder string changed to `placeholderString`.

        Parameters:
        :   **placeholderString** – Placeholder string that changed

    void completerChanged(QCompleter \*completer)
    :   Signals that the completer changed to `completer`.

        Parameters:
        :   **completer** – Pointer to completer

    void textElideModeChanged(const Qt::TextElideMode &textElideMode)
    :   Signals that the text elide mode changed to `textElideMode`.

        Parameters:
        :   **textElideMode** – Text elide mode

    void validatorChanged(const Qt::TextElideMode &textElideMode)
    :   Signals that the text elide mode changed to `textElideMode`.

        Parameters:
        :   **textElideMode** – Text elide mode

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the string action.

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

    QString \_placeholderString
    :   Current string.

    QAction \_leadingAction
    :   Place holder string.

    QAction \_trailingAction
    :   Action at the leading position.

    QCompleter \*\_completer
    :   Action at the trailing position.

    bool \_searchMode
    :   Pointer to completer.

    bool \_clearable
    :   Whether the string action is in search mode.

    Qt::TextElideMode \_textElideMode
    :   Whether the string can be cleared by clicking the trailing action.

    QRegularExpressionValidator \_validator
    :   Text elide mode.

    Friends

    *friend class* AbstractActionsManager

    class InlineAction : public QWidgetAction
    :   Actions shown at leading and/or trailing position.

        Public Functions

        InlineAction(QWidget \*parent = nullptr)
        :   Construct with pointer to parent widget.

            Parameters:
            :   **parent** – Pointer to parent widget

        QWidget \*createWidget(QWidget \*parent) override
        :   Create widget.

            Returns:
            :   Pointer to created widget

        void setIconByName(const QString &iconName)
        :   Set icon by name.

            Parameters:
            :   **iconName** – Name of the icon

    class LabelWidget : public QLabel
    :   Label widget class for string action.

        Protected Functions

        LabelWidget(QWidget \*parent, [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \*stringAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **stringAction** – Pointer to string action

        bool eventFilter(QObject \*target, QEvent \*event) override
        :   Respond to `target` events.

            Parameters:
            :   - **target** – Object of which an event occurred
                - **event** – The event that took place

    class LineEditWidget : public QLineEdit
    :   Line edit widget class for string action.

        Protected Functions

        LineEditWidget(QWidget \*parent, [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \*stringAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **stringAction** – Pointer to string action

    class TextEditWidget : public QTextEdit
    :   Text edit widget class for multi-line strings.

        Protected Functions

        TextEditWidget(QWidget \*parent, [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \*stringAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **stringAction** – Pointer to string action
