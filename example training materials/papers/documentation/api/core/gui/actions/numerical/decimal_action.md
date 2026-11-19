# DecimalAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html

**Documentation path:** `api/core/gui/actions/numerical/decimal_action.html`

---

# DecimalAction

**Qualified name:** `mv::gui::DecimalAction`

class DecimalAction : public mv::gui::[NumericalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction")<float>
:   Decimal action class.

    Stores a float value and creates widgets to interact with it

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit Q\_INVOKABLE DecimalAction(QObject \*parent, const QString &title, float minimum = [INIT\_MIN](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalAction8INIT_MINE "mv::gui::DecimalAction::INIT_MIN"), float maximum = [INIT\_MAX](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalAction8INIT_MAXE "mv::gui::DecimalAction::INIT_MAX"), float value = [INIT\_VALUE](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalAction10INIT_VALUEE "mv::gui::DecimalAction::INIT_VALUE"), std::uint32\_t numberOfDecimals = INIT\_NUMBER\_OF\_DECIMALS, bool logarithmic = [INIT\_LOGARITHMIC](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalAction16INIT_LOGARITHMICE "mv::gui::DecimalAction::INIT_LOGARITHMIC"), float logarithmicGamma = [INIT\_LOGARITHMIC\_GAMMA](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalAction22INIT_LOGARITHMIC_GAMMAE "mv::gui::DecimalAction::INIT_LOGARITHMIC_GAMMA"))
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **minimum** – Minimum value
            - **maximum** – Maximum value
            - **value** – Value
            - **numberOfDecimals** – Number of decimals
            - **logarithmic** – When true, the slider position is mapped to the value through a power curve so the low end of the range gets more slider travel (the value itself is unchanged)
            - **logarithmicGamma** – Skew exponent for the logarithmic mapping; > 1 expands the low end of the range

    void initialize(float minimum, float maximum, float value, std::uint32\_t numberOfDecimals = INIT\_NUMBER\_OF\_DECIMALS)
    :   Initialize the decimal action.

        Parameters:
        :   - **minimum** – Minimum value
            - **maximum** – Maximum value
            - **value** – Value
            - **numberOfDecimals** – Number of decimals

    float getSingleStep() const
    :   Gets the single step.

    void setSingleStep(float singleStep)
    :   Sets the single step.

        Parameters:
        :   **singleStep** – Single step

    bool isLogarithmic() const
    :   Gets whether the slider uses a logarithmic (power-curve) position mapping.

    void setLogarithmic(bool logarithmic)
    :   Sets whether the slider uses a logarithmic (power-curve) position mapping.

        Parameters:
        :   **logarithmic** – Whether to use the logarithmic mapping

    float getLogarithmicGamma() const
    :   Gets the logarithmic skew exponent (gamma)

    void setLogarithmicGamma(float logarithmicGamma)
    :   Sets the logarithmic skew exponent (gamma); > 1 expands the low end of the range.

        Parameters:
        :   **logarithmicGamma** – Skew exponent

    double valueToSliderPosition(double normalizedValue) const
    :   Maps a normalized value in [0, 1] to a normalized slider position in [0, 1].

        Identity when the scale is linear.

        Parameters:
        :   **normalizedValue** – Normalized value

        Returns:
        :   Normalized slider position

    double sliderPositionToValue(double normalizedSliderPosition) const
    :   Maps a normalized slider position in [0, 1] to a normalized value in [0, 1].

        Identity when the scale is linear.

        Parameters:
        :   **normalizedSliderPosition** – Normalized slider position

        Returns:
        :   Normalized value

    virtual [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getPublicCopy() const override
    :   Get public copy of the action (other compatible actions can connect to it)

        Returns:
        :   Pointer to public copy of the action

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void valueChanged(float value)
    :   Signals that the current value changed.

        Parameters:
        :   **value** – Current value that changed

    void minimumChanged(float minimum)
    :   Signals that the minimum value changed.

        Parameters:
        :   **minimum** – New minimum

    void maximumChanged(float maximum)
    :   Signals that the maximum value changed.

        Parameters:
        :   **maximum** – New maximum

    void prefixChanged(const QString &prefix)
    :   Signals that the prefix changed.

        Parameters:
        :   **prefix** – New prefix

    void suffixChanged(const QString &suffix)
    :   Signals that the suffix changed.

        Parameters:
        :   **suffix** – New suffix

    void numberOfDecimalsChanged(std::uint32\_t numberOfDecimals)
    :   Signals that the number of decimals changed to `numberOfDecimals`.

        Parameters:
        :   **numberOfDecimals** – Number of decimals

    void singleStepChanged(float singleStep)
    :   Signals that the single step changed.

        Parameters:
        :   **singleStep** – Single step

    void logarithmicScaleChanged()
    :   Signals that the logarithmic scale (enabled state or gamma) changed.

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the decimal action.

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

    Protected Attributes

    bool \_logarithmic
    :   Single step size for spin box.

    float \_logarithmicGamma
    :   Whether the slider maps its position through a power curve.

    Protected Static Attributes

    static constexpr float INIT\_MIN = 0.0f
    :   Skew exponent for the logarithmic mapping.

    static constexpr float INIT\_MAX = 100.0f
    :   Initialization minimum value.

    static constexpr float INIT\_VALUE = 0.0
    :   Initialization maximum value.

    static constexpr int INIT\_DECIMALS = 1
    :   Initialization value.

    static constexpr bool INIT\_LOGARITHMIC = false
    :   Initialization number of decimals.

    static constexpr float INIT\_LOGARITHMIC\_GAMMA = 3.0f
    :   Linear slider mapping by default.

    Friends

    *friend class* AbstractActionsManager

    class LineEditWidget : public QLineEdit
    :   Line edit widget class for decimal action.

        Protected Functions

        LineEditWidget(QWidget \*parent, [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction") \*decimalAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **decimalAction** – Pointer to decimal action

    class SliderWidget : public QSlider
    :   Slider widget class for decimal action.

        Protected Functions

        SliderWidget(QWidget \*parent, [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction") \*decimalAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **decimalAction** – Pointer to decimal action

    class SpinBoxWidget : public QDoubleSpinBox
    :   Spinbox widget class for decimal action.

        Protected Functions

        SpinBoxWidget(QWidget \*parent, [DecimalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_action.html#_CPPv4N2mv3gui13DecimalActionE "mv::gui::DecimalAction") \*decimalAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **decimalAction** – Pointer to decimal action
