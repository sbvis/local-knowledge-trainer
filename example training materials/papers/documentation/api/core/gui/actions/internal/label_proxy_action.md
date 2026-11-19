# LabelProxyAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/label_proxy_action.html

**Documentation path:** `api/core/gui/actions/internal/label_proxy_action.html`

---

# LabelProxyAction

**Qualified name:** `mv::gui::LabelProxyAction`

class LabelProxyAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Label proxy action class.

    Sole purpose is to override the label text of the source action

    Note: This action is developed for internal use only and is in a WIP state

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE LabelProxyAction(QObject \*parent, const QString &title, [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*sourceAction)
    :   Construct with pointer to `parent` object, `title` and `source` action.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **sourceAction** – Pointer to source action

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the label proxy action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    Friends

    *friend class* AbstractActionsManager
