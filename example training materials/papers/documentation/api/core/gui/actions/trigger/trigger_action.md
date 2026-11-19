# TriggerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html

**Documentation path:** `api/core/gui/actions/trigger/trigger_action.html`

---

# TriggerAction

**Qualified name:** `mv::gui::TriggerAction`

class TriggerAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Trigger action class.

    Action class for trigger

    **Author**
    :   Thomas Kroes

    Subclassed by ColorizeClustersAction, MergeClustersAction, PrefixClustersAction, RefreshClustersAction, RemoveClustersAction, [mv::gui::IconAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/icon_action.html#classmv_1_1gui_1_1IconAction), [mv::gui::PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html#classmv_1_1gui_1_1PluginTriggerAction), [mv::gui::PluginTriggerPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_picker_action.html#classmv_1_1gui_1_1PluginTriggerPickerAction), [mv::gui::ScriptTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/script_trigger_action.html#classmv_1_1gui_1_1ScriptTriggerAction), [mv::gui::WatchVideoAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/watch_video_action.html#classmv_1_1gui_1_1WatchVideoAction)

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator Icon
        :   Push button options.

        enumerator Text
        :   Enable push button icon.

        enumerator IconText
        :   Enable push button text.

            Push button configurations

    Public Functions

    virtual void setIconByName(const QString &iconName) override
    :   Set the icon by `iconName` and use the default icon font and version.

        Parameters:
        :   **iconName** – Name of the icon

    virtual void setIconByName(const QString &iconName, const QString &iconFontName, const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &iconFontVersion) override
    :   Set the icon by `iconName` and possibly override the default `iconFontName` and `iconFontVersion`.

        Parameters:
        :   - **iconName** – Name of the icon
            - **iconFontName** – Name of the icon font
            - **iconFontVersion** – Version of the icon font

    Q\_INVOKABLE TriggerAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the trigger action.

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

    class PushButtonWidget : public QPushButton
    :   Push button widget class for trigger action.

        Protected Functions

        PushButtonWidget(QWidget \*parent, [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \*triggerAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **triggerAction** – Pointer to trigger action
                - **widgetFlags** – Widget flags

        void resizeEvent(QResizeEvent \*event) override
        :   Override this event to make the push button square (in case only an icon is used)

            Parameters:
            :   **event** – Pointer to resize event

        void paintEvent(QPaintEvent \*event) override
        :   Override paint event to fix icon alignment issues.

            Parameters:
            :   **event** – Pointer to paint event

        Protected Attributes

        std::int32\_t \_widgetFlags
        :   Pointer to trigger action.

        Friends

        *friend class* TriggerAction
