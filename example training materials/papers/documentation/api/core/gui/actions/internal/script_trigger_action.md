# ScriptTriggerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/script_trigger_action.html

**Documentation path:** `api/core/gui/actions/internal/script_trigger_action.html`

---

# ScriptTriggerAction

**Qualified name:** `mv::gui::ScriptTriggerAction`

class ScriptTriggerAction : public mv::gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction")
:   Script trigger action class.

    Action class for triggering script execution

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE ScriptTriggerAction(QObject \*parent, const std::shared\_ptr<util::[Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6ScriptE "mv::util::Script")> &script, const QString &menuLocation, const QIcon &icon = QIcon())
    :   Request plugin callback function (invoked when the trigger action is triggered)

        Constructor

        Parameters:
        :   - **parent** – Pointer to parent object
            - **script** – Smart pointer to the script that should be executed when the trigger action is triggered
            - **title** – Title of the plugin trigger action
            - **menuLocation** – Determines where the script trigger action resides w.r.t. other script trigger actions (for instance in the data hierarchy context menu) in a path like fashion e.g. import/images
            - **icon** – Icon representing the action (as shown in the menu)

    QString getMenuLocation() const
    :   Get menu location.

        Returns:
        :   Path-separated menu location

    QIcon getLanguageIcon() const
    :   Get icon representing the scripting language.

        Returns:
        :   Icon representing the scripting language

    Friends

    *friend class* plugin::PluginFactory
