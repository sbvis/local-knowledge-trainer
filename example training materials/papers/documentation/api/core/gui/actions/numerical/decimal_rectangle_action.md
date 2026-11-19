# DecimalRectangleAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_rectangle_action.html

**Documentation path:** `api/core/gui/actions/numerical/decimal_rectangle_action.html`

---

# DecimalRectangleAction

**Qualified name:** `mv::gui::DecimalRectangleAction`

class DecimalRectangleAction : public mv::gui::[RectangleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#_CPPv4I0EN2mv3gui15RectangleActionE "mv::gui::RectangleAction")<[DecimalRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeActionE "mv::gui::DecimalRangeAction")>
:   Decimal rectangle action class.

    Stores a decimal rectangle and creates interfaces to interact with it

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE DecimalRectangleAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    inline void setRectangle(const QRectF &rectangle)
    :   Set rectangle to `rectangle`.

        Parameters:
        :   **rectangle** – Rectangle

    QRectF toRectF() const
    :   Get rectangle as Qt rectangle.

        Returns:
        :   Qt Rectangle

    void setRectF(const QRectF &rectangle)
    :   Set rectangle from Qt `rectangle`.

        Parameters:
        :   **rectangle** – Qt Rectangle

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void rectangleChanged(float left, float right, float bottom, float top)
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
