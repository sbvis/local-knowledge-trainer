# IntegralRectangleAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_rectangle_action.html

**Documentation path:** `api/core/gui/actions/numerical/integral_rectangle_action.html`

---

# IntegralRectangleAction

**Qualified name:** `mv::gui::IntegralRectangleAction`

class IntegralRectangleAction : public mv::gui::[RectangleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#_CPPv4I0EN2mv3gui15RectangleActionE "mv::gui::RectangleAction")<[IntegralRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_range_action.html#_CPPv4N2mv3gui19IntegralRangeActionE "mv::gui::IntegralRangeAction")>
:   Integral rectangle action class.

    Stores an integral rectangle and creates interfaces to interact with it

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE IntegralRectangleAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    inline void setRectangle(const QRect &rectangle)
    :   Set rectangle to `rectangle`.

        Parameters:
        :   **rectangle** – Rectangle

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void rectangleChanged(std::int32\_t left, std::int32\_t right, std::int32\_t bottom, std::int32\_t top)
    :   Signals that the rectangle changed.

        Parameters:
        :   - **left** – Rectangle left
            - **right** – Rectangle right
            - **bottom** – Rectangle bottom
            - **top** – Rectangle top

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
