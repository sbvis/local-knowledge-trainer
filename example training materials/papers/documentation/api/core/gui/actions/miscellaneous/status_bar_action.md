# StatusBarAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/status_bar_action.html`

---

# StatusBarAction

**Qualified name:** `mv::gui::StatusBarAction`

`StatusBarAction` is the application-level base for a compact inline action group with optional popup and menu content. Construction registers the action in the core’s live status-action collection; destruction removes it.

Plugin factories normally register the specialized [PluginStatusBarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_status_bar_action.html). See [Status-bar integration](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/index.html) for startup timing, positioning, ownership, and content guidance.

class StatusBarAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Status bar action class.

    Base status bar action class with popup functionality

    There are two methods to add content to the status bar popup:

    1. By setting a popup action: setPopupAction(…)
    2. By adding menu actions: addMenuAction(…)

    The index controls the location w.r.t. the other status bar items:

    - When negative, the item is inserted in between existing items(right-to-left)
    - Wen zero, the item is appended to the existing items at the right
    - Wen positive, the item is inserted in between existing items(left-to-right)

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::PluginStatusBarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_status_bar_action.html#classmv_1_1gui_1_1PluginStatusBarAction)

    Public Functions

    StatusBarAction(QObject \*parent, const QString &title, const util::[StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon") &icon = util::[StyledIcon](https://manivault.readthedocs.io/en/latest/api/core/util/icon/styled_icon.html#_CPPv4N2mv4util10StyledIconE "mv::util::StyledIcon")())
    :   Construct with `parent` object, `title` and possibly an `icon`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **icon** – Icon

    StatusBarAction(QObject \*parent, const QString &title, const QString &icon = "")
    :   Construct with `parent` object, `title` and possibly a FontAwesome `icon`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **icon** – FontAwesome icon name

    ~StatusBarAction() override
    :   Destructor for removing this action from StatusBarAction::statusBarActions.

    [HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction") &getBarGroupAction()
    :   Get bar group action.

        Returns:
        :   Reference to bar group action

    [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") &getBarIconStringAction()
    :   Get bar icon string action.

        Returns:
        :   Reference to bar icon string action

    [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getPopupAction()
    :   Get popup action.

        Returns:
        :   Pointer to popup action (maybe nullptr)

    void setPopupAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*popupAction)
    :   Set popup action to `popupAction`.

        Parameters:
        :   **popupAction** – Pointer to popup action

    void addMenuAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*menuAction)
    :   Add `menuAction`.

        Parameters:
        :   **menuAction** – Pointer to menu action

    void removeMenuAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*menuAction)
    :   Remove `menuAction`.

        Parameters:
        :   **menuAction** – Pointer to menu action to remove

    WidgetActions getMenuActions()
    :   Get menu actions.

        Returns:
        :   Pointers to menu actions

    std::int32\_t getIndex()
    :   Get index (must be called prior to main window showing, otherwise it will not have an effect)

        Returns:
        :   Position index

    void setIndex(std::int32\_t index)
    :   Set index to `index`.

        Parameters:
        :   **index** – Position index

    void popupActionChanged([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*previousPopupAction, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*popupAction)
    :   Signals that the popup action changed from `previousPopupAction` to `popupAction`.

        Parameters:
        :   - **previousPopupAction** – Pointer to previous action (maybe nullptr)
            - **popupAction** – Pointer to current action (maybe nullptr)

    void indexChanged(std::int32\_t index)
    :   Signals that the position `index` changed.

        Parameters:
        :   **index** – Position index

    void menuActionAdded([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*menuAction)
    :   Signals that `menuAction` was added.

        Parameters:
        :   **menuAction** – Pointer to menu action that was added

    void menuActionAboutToBeRemoved([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*menuAction)
    :   Signals that `menuAction` is about to be removed.

        Parameters:
        :   **menuAction** – Pointer to menu action is about to be removed

    void requirePopupShow()
    :   Signals that a popup should be displayed.

    void requirePopupHide()
    :   Signals that a popup should be hidden.

    Public Static Functions

    static WidgetActions getStatusBarActions()
    :   Get registered status bar action.

        Returns:
        :   Status bar actions

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the status bar action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html#classmv_1_1gui_1_1StatusBarAction_1_1Widget) flags for the configuration of the widget

    void showPopup()
    :   Show the popup.

    void hidePopup()
    :   Hide the popup.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html#classmv_1_1gui_1_1StatusBarAction_1_1Widget) class for display of a status bar action.

        Protected Functions

        Widget(QWidget \*parent, [StatusBarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html#_CPPv4N2mv3gui15StatusBarActionE "mv::gui::StatusBarAction") \*statusBarAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **statusBarAction** – Pointer to owning status bar action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html#classmv_1_1gui_1_1StatusBarAction_1_1Widget) flags for the configuration of the widget

        Protected Attributes

        ToolButton \_toolButton
        :   Pointer to owning status bar action.

        QWidget \*\_popupWidget
        :   Customized tool button.

        Friends

        *friend class* StatusBarAction
