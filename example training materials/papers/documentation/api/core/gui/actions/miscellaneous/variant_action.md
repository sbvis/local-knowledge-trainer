# VariantAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/variant_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/variant_action.html`

---

# VariantAction

**Qualified name:** `mv::gui::VariantAction`

class VariantAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Variant widget action class.

    Stores a Qt variant

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE VariantAction(QObject \*parent, const QString &title, const QVariant &variant = QVariant())
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **variant** – Initial variant value

    void initialize(const QVariant &variant = QVariant())
    :   Initialize the variant action.

        Parameters:
        :   **variant** – Initial variant value

    QVariant getVariant() const
    :   Get variant value.

        Returns:
        :   Variant value

    void setVariant(const QVariant &variant)
    :   Set the variant value.

        Parameters:
        :   **variant** – Variant value

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant.

        Parameters:
        :   **Variant** – representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant.

        Returns:
        :   Variant representation of the widget action

    void variantChanged(const QVariant &variant)
    :   Signals that the current variant changed.

        Parameters:
        :   **variant** – Updated variant value

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

    Friends

    *friend class* AbstractActionsManager
