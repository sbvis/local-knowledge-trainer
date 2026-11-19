# IntegralAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html

**Documentation path:** `api/core/gui/actions/numerical/integral_action.html`

---

# IntegralAction

**Qualified name:** `mv::gui::IntegralAction`

class IntegralAction : public mv::gui::[NumericalAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_action.html#_CPPv4I0EN2mv3gui15NumericalActionE "mv::gui::NumericalAction")<std::int32\_t>
:   Integral widget action class.

    Stores an integral value and creates widgets to interact with it

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit Q\_INVOKABLE IntegralAction(QObject \*parent, const QString &title, std::int32\_t minimum = INIT\_MIN, std::int32\_t maximum = [INIT\_MAX](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralAction8INIT_MAXE "mv::gui::IntegralAction::INIT_MAX"), std::int32\_t value = [INIT\_VALUE](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralAction10INIT_VALUEE "mv::gui::IntegralAction::INIT_VALUE"))
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **minimum** – Minimum value
            - **maximum** – Maximum value

    void initialize(std::int32\_t minimum, std::int32\_t maximum, std::int32\_t value)
    :   Initialize the integral action.

        Parameters:
        :   - **minimum** – Minimum value
            - **maximum** – Maximum value
            - **value** – Value

    virtual [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getPublicCopy() const override
    :   Get public copy of the action (other compatible actions can connect to it)

        Returns:
        :   Pointer to public copy of the action

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant.

        Parameters:
        :   **Variant** – representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void valueChanged(std::int32\_t value)
    :   Signals that the current value changed.

        Parameters:
        :   **value** – Current value that changed

    void defaultValueChanged(std::int32\_t defaultValue)
    :   Signals that the default value changed.

        Parameters:
        :   **defaultValue** – Default value that changed

    void minimumChanged(std::int32\_t minimum)
    :   Signals that the minimum value changed.

        Parameters:
        :   **minimum** – New minimum

    void maximumChanged(std::int32\_t maximum)
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

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the integral action.

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

    static constexpr std::int32\_t INIT\_MAX = 100
    :   Initialization minimum value.

    static constexpr std::int32\_t INIT\_VALUE = 0
    :   Initialization maximum value.

    Friends

    *friend class* AbstractActionsManager

    class LineEditWidget : public QLineEdit
    :   Line edit widget class for integral action.

        Protected Functions

        LineEditWidget(QWidget \*parent, [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction") \*integralAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **integralAction** – Pointer to integral action

    class SliderWidget : public QSlider
    :   Slider widget class for integral action.

        Protected Functions

        SliderWidget(QWidget \*parent, [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction") \*integralAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **integralAction** – Pointer to integral action

    class SpinBoxWidget : public QSpinBox
    :   Spinbox widget class for integral action.

        Protected Functions

        SpinBoxWidget(QWidget \*parent, [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction") \*integralAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **integralAction** – Pointer to integral action
