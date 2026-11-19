# NumericalAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html

**Documentation path:** `api/core/gui/actions/numerical/numerical_action.html`

---

# NumericalAction

**Qualified name:** `mv::gui::NumericalAction`

template<typename NumericalType> class NumericalAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Numerical action class.

    Action class for manipulating a numerical value

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget settings.

        *Values:*

        enumerator SpinBox

        enumerator Slider
        :   Widget includes a spin box.

        enumerator LineEdit
        :   Widget includes a slider.

        enumerator Default
        :   Widget includes a line edit.

    Public Functions

    inline NumericalAction(QObject \*parent, const QString &title, const [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") &minimum, [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") maximum, [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") value, std::uint32\_t numberOfDecimals = [INIT\_NUMBER\_OF\_DECIMALS](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4N2mv3gui15NumericalAction23INIT_NUMBER_OF_DECIMALSE "mv::gui::NumericalAction::INIT_NUMBER_OF_DECIMALS"))
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **minimum** – Minimum value
            - **maximum** – Maximum value
            - **value** – Value
            - **numberOfDecimals** – Number of decimals

    inline virtual [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") getValue() const
    :   Gets the current value.

    inline virtual void setValue([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") value, bool silent = false)
    :   Sets the current value.

        Parameters:
        :   - **value** – Current value
            - **silent** – Prevent notification of value change

    inline virtual [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") getMinimum() const
    :   Gets the minimum value.

    inline virtual void setMinimum([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") minimum)
    :   Sets the minimum value.

        Parameters:
        :   **minimum** – Minimum value

    inline virtual [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") getMaximum() const
    :   Gets the maximum value.

    inline virtual void setMaximum([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") maximum)
    :   Sets the maximum value.

        Parameters:
        :   **maximum** – Maximum value

    inline virtual util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType")> getRange() const
    :   Gets the value range.

        Returns:
        :   Range

    inline virtual void setRange(util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType")> range)
    :   Sets the value range.

        Parameters:
        :   **range** – Range

    inline virtual void setRange([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") minimum, [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") maximum)
    :   Sets the value range.

        Parameters:
        :   - **minimum** – Minimum value
            - **maximum** – Maximum value

    inline virtual QString getPrefix() const
    :   Gets the prefix.

    inline virtual void setPrefix(const QString &prefix)
    :   Sets the prefix.

        Parameters:
        :   **prefix** – Prefix

    inline virtual QString getSuffix() const
    :   Gets the suffix.

    inline virtual void setSuffix(const QString &suffix)
    :   Sets the suffix.

        Parameters:
        :   **suffix** – Suffix

    inline virtual std::uint32\_t getNumberOfDecimals() const
    :   Gets the number of decimals.

    inline virtual void setNumberOfDecimals(std::uint32\_t numberOfDecimals)
    :   Sets the number of decimals.

        Parameters:
        :   **numberOfDecimals** – number of decimals

    inline virtual bool getUpdateDuringDrag() const
    :   Gets whether the value should update during interaction.

    inline virtual void setUpdateDuringDrag(bool updateDuringDrag)
    :   Sets whether the value should update during interaction.

        Parameters:
        :   **updateDuringDrag** – Whether the value should update during interaction

    inline virtual bool isAtMinimum() const
    :   Returns whether the current value is at its minimum.

    inline virtual bool isAtMaximum() const
    :   Returns whether the current value is at its maximum.

    inline virtual double getIntervalLength() const
    :   Returns the length of the interval defined by the minimum and maximum value.

    inline virtual double getNormalized() const
    :   Returns the normalized value.

    Protected Attributes

    [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") \_minimum
    :   Current value.

    [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction::NumericalType") \_maximum
    :   Minimum value.

    QString \_prefix
    :   Maximum value.

    QString \_suffix
    :   Prefix string.

    std::uint32\_t \_numberOfDecimals
    :   Suffix string.

    bool \_updateDuringDrag
    :   Number of decimals.

    ValueChangedCB \_valueChanged
    :   Whether the value should update during interaction.

    MinimumChangedCB \_minimumChanged
    :   Callback which is called when the value changed.

    MaximumChangedCB \_maximumChanged
    :   Callback which is called when the minimum changed.

    PrefixChangedCB \_prefixChanged
    :   Callback which is called when the maximum changed.

    SuffixChangedCB \_suffixChanged
    :   Callback which is called when the prefix changed.

    NumberOfDecimalsChangedCB \_numberOfDecimalsChanged
    :   Callback which is called when the suffix changed.

    Protected Static Attributes

    static constexpr std::uint32\_t INIT\_NUMBER\_OF\_DECIMALS = 1
    :   Callback which is called when the number of decimals changed.
