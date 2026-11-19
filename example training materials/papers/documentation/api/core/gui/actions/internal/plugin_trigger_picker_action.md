# PluginTriggerPickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_picker_action.html

**Documentation path:** `api/core/gui/actions/internal/plugin_trigger_picker_action.html`

---

# PluginTriggerPickerAction

**Qualified name:** `mv::gui::PluginTriggerPickerAction`

class PluginTriggerPickerAction : public mv::gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction")
:   Plugin trigger picker action class.

    Action class for picking (and configuring) a plugin trigger action

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    PluginTriggerPickerAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Plugin trigger picker title

    void initialize(const plugin::Type &pluginType, const Datasets &datasets)
    :   Establishes the plugin trigger actions for `pluginType` and `datasets`.

        Parameters:
        :   - **pluginType** – Type of plugin e.g. analysis, exporter
            - **datasets** – Input datasets

    void initialize(const plugin::Type &pluginType, const DataTypes &dataTypes)
    :   Establishes the plugin trigger actions for `pluginType` and `dataTypes`.

        Parameters:
        :   - **pluginType** – Type of plugin e.g. analysis, exporter
            - **dataTypes** – Vector of dataTypes

    void initialize(const QString &pluginKind, const Datasets &datasets)
    :   Establishes the plugin trigger actions for `pluginKind` and `datasets`.

        Parameters:
        :   - **pluginKind** – Kind of plugin
            - **datasets** – Input datasets

    void initialize(const QString &pluginKind, const DataTypes &dataTypes)
    :   Establishes the plugin trigger actions for `pluginKind` and `dataTypes`.

        Parameters:
        :   - **pluginKind** – Kind of plugin
            - **dataTypes** – Vector of dataTypes

    QPointer<[PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html#_CPPv4N2mv3gui19PluginTriggerActionE "mv::gui::PluginTriggerAction")> getPluginTriggerAction(const QString &sha)
    :   Get plugin trigger action by its SHA.

        Returns:
        :   sha SHA of the plugin trigger action to find

        Returns:
        :   Pointer to plugin trigger action (if found)

    PluginTriggerActions getPluginTriggerActions()
    :   Get plugin trigger actions.

        Returns:
        :   List of plugin trigger actions

    QPointer<[PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html#_CPPv4N2mv3gui19PluginTriggerActionE "mv::gui::PluginTriggerAction")> getCurrentPluginTriggerAction()
    :   Get current plugin trigger action (if any)

        Returns:
        :   Pointer to current plugin trigger action (if any)

    void setCurrentPluginTriggerAction(QPointer<[PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html#_CPPv4N2mv3gui19PluginTriggerActionE "mv::gui::PluginTriggerAction")> pluginTriggerAction)
    :   Set current plugin trigger action by `pluginTriggerAction`.

        Parameters:
        :   **pluginTriggerAction** – Pointer to plugin trigger action

    void setCurrentPluginTriggerAction(const QString &sha)
    :   Set current plugin trigger action by `sha`.

        Parameters:
        :   **sha** – Plugin trigger action sha

    [OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") &getSelectTriggerAction()
    :   Get trigger selection option action.

        Returns:
        :   Reference to trigger selection option action

    void currentPluginTriggerActionChanged(const QPointer<[PluginTriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_action.html#_CPPv4N2mv3gui19PluginTriggerActionE "mv::gui::PluginTriggerAction")> currentPluginTriggerAction)
    :   Signals that the current plugin trigger action changed.

        Parameters:
        :   **currentPluginTriggerAction** – Pointer to current plugin trigger action that changed

    void pluginTriggerActionsChanged(const PluginTriggerActions &pluginTriggerActions)
    :   Signals that the plugin trigger actions have changed.

        Parameters:
        :   **pluginTriggerActions** – List of plugin trigger actions

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the plugin trigger picker action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_picker_action.html#classmv_1_1gui_1_1PluginTriggerPickerAction_1_1Widget) flags for the configuration of the widget (type)

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_picker_action.html#classmv_1_1gui_1_1PluginTriggerPickerAction_1_1Widget) plugin trigger picker action.

        Protected Functions

        Widget(QWidget \*parent, [PluginTriggerPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_picker_action.html#_CPPv4N2mv3gui25PluginTriggerPickerActionE "mv::gui::PluginTriggerPickerAction") \*pluginTriggerPickerAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **pluginTriggerPickerAction** – Pointer to plugin trigger picker action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_trigger_picker_action.html#classmv_1_1gui_1_1PluginTriggerPickerAction_1_1Widget) flags

        Protected Attributes

        [WidgetActionCollapsedWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_collapsed_widget.html#_CPPv4N2mv3gui27WidgetActionCollapsedWidgetE "mv::gui::WidgetActionCollapsedWidget") \_configurationToolButton
        :   Pointer to plugin trigger picker action.

        Friends

        *friend class* PluginTriggerPickerAction
