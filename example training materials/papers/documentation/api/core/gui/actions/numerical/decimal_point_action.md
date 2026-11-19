# DecimalPointAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_point_action.html

**Documentation path:** `api/core/gui/actions/numerical/decimal_point_action.html`

---

# DecimalPointAction

**Qualified name:** `mv::gui::DecimalPointAction`

class DecimalPointAction : public mv::gui::[NumericalPointAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction")<float, [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction")>
:   Decimal action class.

    Stores a two-dimensional decimal point value.

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit Q\_INVOKABLE DecimalPointAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void valueChanged(float x, float y)
    :   Signals that the coordinate values changed to `x` and `y`.

        Parameters:
        :   - **x** – X coordinate value
            - **y** – Y coordinate value

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

    Protected Static Attributes

    static constexpr int INIT\_DECIMALS = 1
    :   Initialization value.

    Friends

    *friend class* AbstractActionsManager
