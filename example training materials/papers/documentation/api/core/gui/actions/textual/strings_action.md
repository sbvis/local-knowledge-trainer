# StringsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/strings_action.html

**Documentation path:** `api/core/gui/actions/textual/strings_action.html`

---

# StringsAction

**Qualified name:** `mv::gui::StringsAction`

class StringsAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Strings widget action class.

    Stores a string list and creates widgets to interact with it (add/remove/rename)

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget configurations.

        *Values:*

        enumerator MayEdit

        enumerator ListView
        :   Strings may be added and removed from the user interface.

        enumerator EditableListView
        :   Widget includes a list view.

        enumerator Default
        :   Widget includes a list view with which strings may be added and removed from the user interface.

    Public Functions

    explicit Q\_INVOKABLE StringsAction(QObject \*parent, const QString &title, const QStringList &strings = QStringList())
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **strings** – Strings

    QString getCategory() const
    :   Get string category.

        Returns:
        :   String category

    void setCategory(const QString &category)
    :   Set string category.

        Parameters:
        :   **category** – Category

    QStringList getStrings() const
    :   Get strings.

        Returns:
        :   Strings as string list

    void setStrings(const QStringList &strings)
    :   Set strings.

        Parameters:
        :   **strings** – Strings

    QStringList getLockedStrings() const
    :   Get locked strings.

        Returns:
        :   Locked strings as string list

    void setLockedStrings(const QStringList &lockedStrings)
    :   Set locked strings to `lockedStrings`.

        Parameters:
        :   **lockedStrings** – Locked strings

    bool allowsDuplicates() const
    :   Check whether this action allows duplicates.

        Returns:
        :   True if duplicates are allowed, false otherwise

    void setAllowDuplicates(bool allowDuplicates)
    :   Set whether this action allows duplicates to `allowDuplicates`.

        Parameters:
        :   **allowDuplicates** – True to allow duplicates, false otherwise

    Qt::TextElideMode getTextElideMode() const
    :   Get text elide mode.

        Returns:
        :   Text elide mode

    void setTextElideMode(const Qt::TextElideMode &textElideMode)
    :   Set text elide mode to `textElideMode`.

        Parameters:
        :   **textElideMode** – Text elide mode

    bool mayAddString(const QString &string) const
    :   Check whether `string` may be added.

        Parameters:
        :   **string** – String to check

        Returns:
        :   True if the string may be added, false otherwise

    void addString(const QString &string)
    :   Add string.

        Parameters:
        :   **string** – String to add

    void addStrings(const QStringList &strings, bool allowDuplication = false)
    :   Add /p strings.

        Parameters:
        :   - **strings** – Strings to add
            - **allowDuplication** – Whether to allow duplication of strings, defaults to false

    void removeString(const QString &string)
    :   Remove string.

        Parameters:
        :   **string** – String to remove

    void removeStrings(const QStringList &strings)
    :   Remove strings.

        Parameters:
        :   **strings** – Strings to remove

    void updateString(const QString &oldString, const QString &newString)
    :   Update string `oldString` to `newString`.

        Parameters:
        :   - **oldString** – Old string
            - **newString** – New string

    inline const QStringListModel &getStringsModel() const
    :   Get model for the strings.

        Returns:
        :   Reference to the string list model containing the strings

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant.

        Parameters:
        :   **variantMap** – Variant representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant.

        Returns:
        :   Variant representation of the widget action

    void stringsChanged(const QStringList &strings)
    :   Signals that the strings changed.

        Parameters:
        :   **strings** – Updated strings

    void stringsAdded(const QStringList &strings)
    :   Signals that `strings` were added.

        Parameters:
        :   **strings** – Added strings

    void lockedStringsChanged(const QStringList &lockedStrings)
    :   Signals that locked string changed to `lockedStrings`.

        Parameters:
        :   **lockedStrings** – Locked strings

    void stringsRemoved(const QStringList &strings)
    :   Signals that `strings` were removed.

        Parameters:
        :   **strings** – Removed strings

    void allowDuplicatesChanged(bool allowDuplicates)
    :   Signals that the allow duplicates setting changed to `allowDuplicates`.

        Parameters:
        :   **allowDuplicates** – Whether duplicates are allowed

    void stringUpdated(const QString &oldString, const QString &newString)
    :   Signals that a string was updated from `oldString` to `newString`.

        Parameters:
        :   - **oldString** – Old string
            - **newString** – New string

    void textElideModeChanged(const Qt::TextElideMode &oldTextElideMode, const Qt::TextElideMode &newTextElideMode)
    :   Signals that the text elide mode changed from `oldTextElideMode` to `newTextElideMode`.

        Parameters:
        :   - **oldTextElideMode** – Old text elide mode
            - **newTextElideMode** – New text elide mode

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the strings action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    inline QStringListModel &getStringsModel()
    :   Get model for the strings.

        Returns:
        :   Reference to the string list model containing the strings

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

    QStringListModel \_stringsModel
    :   Type of string.

    QStringList \_lockedStrings
    :   Model for the strings.

    [HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction") \_toolbarAction
    :   Strings that are locked and cannot be removed or renamed.

    [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_nameAction
    :   Toolbar action.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_addAction
    :   String name action.

    [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_removeAction
    :   Add string action.

    QCompleter \*\_completer
    :   Remove string action.

    bool \_allowDuplicates
    :   Pointer to completer for auto-completion, maybe nullptr.

    Qt::TextElideMode \_textElideMode
    :   Whether to allow string duplicates.

    Friends

    *friend class* AbstractActionsManager

    class ListWidget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   Widget class for strings action.

        Protected Functions

        ListWidget(QWidget \*parent, [StringsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/strings_action.html#_CPPv4N2mv3gui13StringsActionE "mv::gui::StringsAction") \*stringsAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **stringsAction** – Pointer to strings action
                - **widgetFlags** – Widget flags for the configuration of the widget (type)
