# NavigationAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/navigation_action.html

**Documentation path:** `api/core/gui/actions/internal/navigation_action.html`

---

# NavigationAction

**Qualified name:** `mv::gui::NavigationAction`

class NavigationAction : public mv::gui::[HorizontalToolbarAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_toolbar_action.html#_CPPv4N2mv3gui23HorizontalToolbarActionE "mv::gui::HorizontalToolbarAction")
:   Navigation action class.

    Provides actions for navigating in a renderer (the business logic should be handled elsewhere depending on the renderer).

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE NavigationAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void setShortcutsEnabled(bool shortcutsEnabled)
    :   Set whether shortcuts are enabled.

        Parameters:
        :   **shortcutsEnabled** – Boolean determining whether shortcuts are enabled

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load navigation action from variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the navigation action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    Protected Functions

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive) override
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions
