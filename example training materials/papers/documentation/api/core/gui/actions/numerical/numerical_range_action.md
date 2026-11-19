# NumericalRangeAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html

**Documentation path:** `api/core/gui/actions/numerical/numerical_range_action.html`

---

# NumericalRangeAction

**Qualified name:** `mv::gui::NumericalRangeAction`

template<typename NumericalType, typename NumericalActionType> class NumericalRangeAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Numerical range action base class.

    Stores a numerical range and creates widgets to interact with it

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget settings.

        *Values:*

        enumerator MinimumSpinBox

        enumerator MinimumLineEdit
        :   Widget includes a spin box for the minimum range.

        enumerator Slider
        :   Widget includes a label for the minimum range.

        enumerator MaximumSpinBox
        :   Widget includes a slider.

        enumerator MaximumLineEdit
        :   Widget includes a spin box for the maximum range.

        enumerator Default
        :   Widget includes a label for the maximum range.

    Public Functions

    inline NumericalRangeAction(QObject \*parent, const QString &title, const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType")> &limits, const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType")> &range)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **limits** – Limits
            - **range** – Range

    inline void initialize(const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType")> &limits, const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType")> &range)
    :   Initializes the numerical range action with `limits` and `range`.

        Parameters:
        :   - **limits** – Limits
            - **range** – Range

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") getMinimum() const
    :   Get range minimum.

        Returns:
        :   Range minimum

    inline void setMinimum([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") minimum)
    :   Set range minimum to `minimum`.

        Returns:
        :   Range minimum

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") getMaximum() const
    :   Get range maximum.

        Returns:
        :   Range maximum

    inline void setMaximum([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") maximum)
    :   Set range maximum to `maximum`.

        Returns:
        :   Range maximum

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") getLength() const
    :   Get length of the range.

        Returns:
        :   Range length

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") getCenter() const
    :   Get center of the range.

        Returns:
        :   Range center

    inline util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType")> getRange() const
    :   Get the range.

    inline void setRange(const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType")> &range)
    :   Sets the range to `range`.

        Parameters:
        :   **range** – Range

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") getLimitsMinimum() const
    :   Get limits minimum.

        Returns:
        :   Limits minimum

    inline void setLimitsMinimum([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") limitsMinimum)
    :   Set limits minimum to `limitsMinimum`.

        Parameters:
        :   **limitsMinimum** – Limits minimum

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") getLimitsMaximum() const
    :   Get limits maximum.

        Returns:
        :   Limits maximum

    inline void setLimitsMaximum([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") limitsMaximum)
    :   Set limits maximum to `limitsMaximum`.

        Parameters:
        :   **limitsMaximum** – Limits maximum

    inline util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType")> getLimits() const
    :   Get the limits.

    inline void setLimits(const util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType")> &limits)
    :   Set limits to `limits`.

        Parameters:
        :   **limits** – Limits

    inline void shiftBy([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_range_action.html#_CPPv4I00EN2mv3gui20NumericalRangeActionE "mv::gui::NumericalRangeAction::NumericalType") amount)
    :   Shift range by `amount`.

        Parameters:
        :   **amount** – Amount of shift

    inline void expandBy(float factor)
    :   Expand by `factor`.

        Parameters:
        :   **factor** – Expansion factor

    inline virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load numerical range action from variant map.

        Parameters:
        :   **Variant** – map representation of the numerical range action

    inline virtual QVariantMap toVariantMap() const override
    :   Save numerical range action to variant map.

        Returns:
        :   Variant map representation of the numerical range action

    Protected Functions

    inline void blockLimitsChangedCallBack()
    :   Prevent RangeAction::\_limitsChanged from being called.

    inline void unblockLimitsChangedCallBack()
    :   Allow RangeAction::\_limitsChanged to be called.

    inline void blockRangeChangedCallBack()
    :   Prevent RangeAction::\_rangeChanged from being called.

    inline void unblockRangeChangedCallBack()
    :   Allow RangeAction::\_rangeChanged to be called.

    inline bool isLimitsChangedCallBackBlocked() const
    :   Get whether RangeAction::\_limitsChanged callbacks are blocked.

        Returns:
        :   Boolean determining whether RangeAction::\_limitsChanged calls are blocked

    inline bool isRangeChangedCallBackBlocked() const
    :   Get whether RangeAction::\_rangeChanged callbacks are blocked.

        Returns:
        :   Boolean determining whether RangeAction::\_rangeChanged calls are blocked

    Protected Attributes

    LimitsChangedCB \_limitsChanged
    :   Whether RangeAction::\_rangeChanged calls are blocked.

    RangeChangedCB \_rangeChanged
    :   Callback which is called when the limits change.
