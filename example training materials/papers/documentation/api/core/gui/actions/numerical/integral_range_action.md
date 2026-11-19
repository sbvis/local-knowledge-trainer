# IntegralRangeAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_range_action.html

**Documentation path:** `api/core/gui/actions/numerical/integral_range_action.html`

---

# IntegralRangeAction

**Qualified name:** `mv::gui::IntegralRangeAction`

class IntegralRangeAction : public mv::gui::[NumericalRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction")<std::int32\_t, [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction")>
:   Integral range action class.

    Stores an integral range and creates widgets to interact with it

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE IntegralRangeAction(QObject \*parent, const QString &title, const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<std::int32\_t> &limits = util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<std::int32\_t>(INIT\_LIMIT\_MIN, [INIT\_LIMIT\_MAX](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_range_action.html#_CPPv4N2mv3gui19IntegralRangeAction14INIT_LIMIT_MAXE "mv::gui::IntegralRangeAction::INIT_LIMIT_MAX")), const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<std::int32\_t> &range = util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<std::int32\_t>([INIT\_RANGE\_MIN](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_range_action.html#_CPPv4N2mv3gui19IntegralRangeAction14INIT_RANGE_MINE "mv::gui::IntegralRangeAction::INIT_RANGE_MIN"), [INIT\_RANGE\_MAX](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_range_action.html#_CPPv4N2mv3gui19IntegralRangeAction14INIT_RANGE_MAXE "mv::gui::IntegralRangeAction::INIT_RANGE_MAX")))
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **limitMin** – Range lower limit
            - **limitMax** – Range upper limit
            - **rangeMin** – Range minimum
            - **rangeMax** – Range maximum

    void limitsChanged(const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<std::int32\_t> &limits)
    :   Signals that the limits changed to `limits`.

        Parameters:
        :   **limits** – Limits

    void rangeChanged(const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<std::int32\_t> &range)
    :   Signals that the range changed to `range`.

        Parameters:
        :   **range** – Range

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the integral range action.

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

    static constexpr std::int32\_t INIT\_LIMIT\_MAX = 100
    :   Default minimum limit.

    static constexpr std::int32\_t INIT\_RANGE\_MIN = 0
    :   Default maximum limit.

    static constexpr std::int32\_t INIT\_RANGE\_MAX = 100
    :   Default minimum range.

    Friends

    *friend class* AbstractActionsManager

    class IntegralRangeWidget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   Widget class for integral range action.

        Protected Functions

        IntegralRangeWidget(QWidget \*parent, [IntegralRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_range_action.html#_CPPv4N2mv3gui19IntegralRangeActionE "mv::gui::IntegralRangeAction") \*integralRangeAction, const std::int32\_t &widgetFlags = 0)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **integralRangeAction** – Pointer to integral range action
                - **widgetFlags** – Widget flags for the configuration of the widget (type)
