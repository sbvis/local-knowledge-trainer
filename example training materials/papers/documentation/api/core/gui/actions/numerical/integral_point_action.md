# IntegralPointAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_point_action.html

**Documentation path:** `api/core/gui/actions/numerical/integral_point_action.html`

---

# IntegralPointAction

**Qualified name:** `mv::gui::IntegralPointAction`

class IntegralPointAction : public mv::gui::[NumericalPointAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction")<std::int32\_t, [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction")>
:   Integral action class.

    Stores a two-dimensional integral point value.

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit Q\_INVOKABLE IntegralPointAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void valueChanged(std::int32\_t x, std::int32\_t y)
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
