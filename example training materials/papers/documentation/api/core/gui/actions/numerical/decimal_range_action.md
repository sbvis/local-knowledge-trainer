# DecimalRangeAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html

**Documentation path:** `api/core/gui/actions/numerical/decimal_range_action.html`

---

# DecimalRangeAction

**Qualified name:** `mv::gui::DecimalRangeAction`

class DecimalRangeAction : public mv::gui::[NumericalRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction")<float, [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction")>
:   Decimal range action class.

    Stores a decimal range and creates widgets to interact with it

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE DecimalRangeAction(QObject \*parent, const QString &title, const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<float> &limits = util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<float>(INIT\_LIMIT\_MIN, [INIT\_LIMIT\_MAX](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeAction14INIT_LIMIT_MAXE "mv::gui::DecimalRangeAction::INIT_LIMIT_MAX")), const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<float> &range = util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<float>([INIT\_RANGE\_MIN](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeAction14INIT_RANGE_MINE "mv::gui::DecimalRangeAction::INIT_RANGE_MIN"), [INIT\_RANGE\_MAX](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeAction14INIT_RANGE_MAXE "mv::gui::DecimalRangeAction::INIT_RANGE_MAX")), std::int32\_t numberOfDecimals = [INIT\_NUMBER\_OF\_DECIMALS](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeAction23INIT_NUMBER_OF_DECIMALSE "mv::gui::DecimalRangeAction::INIT_NUMBER_OF_DECIMALS"))
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **limitMin** – Range lower limit
            - **limitMax** – Range upper limit
            - **rangeMin** – Range minimum
            - **rangeMax** – Range maximum

    void limitsChanged(const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<float> &limits)
    :   Signals that the limits changed to `limits`.

        Parameters:
        :   **limits** – Limits

    void rangeChanged(const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<float> &range)
    :   Signals that the range changed to `range`.

        Parameters:
        :   **range** – Range

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the decimal range action.

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

    Protected Static Attributes

    static constexpr float INIT\_LIMIT\_MAX = 100.0f
    :   Default minimum limit.

    static constexpr float INIT\_RANGE\_MIN = 0.0f
    :   Default maximum limit.

    static constexpr float INIT\_RANGE\_MAX = 100.0f
    :   Default minimum range.

    static constexpr float INIT\_NUMBER\_OF\_DECIMALS = 2
    :   Default maximum range.

    Friends

    *friend class* AbstractActionsManager

    class DecimalRangeWidget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   Widget class for decimal range action.

        Protected Functions

        DecimalRangeWidget(QWidget \*parent, [DecimalRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeActionE "mv::gui::DecimalRangeAction") \*decimalRangeAction, const std::int32\_t &widgetFlags = 0)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **decimalRangeAction** – Pointer to decimal range action
                - **widgetFlags** – Widget flags for the configuration of the widget (type)
