# ColorPickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_picker_action.html

**Documentation path:** `api/core/gui/actions/color/color_picker_action.html`

---

# ColorPickerAction

**Qualified name:** `mv::gui::ColorPickerAction`

class ColorPickerAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Color picker action class.

    Note: for internal use by the color action only

    **Author**
    :   Thomas Kroes

    Public Functions

    QColor getColor() const
    :   Gets the current color.

    void setColor(const QColor &color)
    :   Sets the current color.

        Parameters:
        :   **color** – Current color

    void colorChanged(const QColor &color)
    :   Signals that the current color changed.

        Parameters:
        :   **color** – Current color that changed

    void defaultColorChanged(const QColor &defaultColor)
    :   Signals that the default color changed.

        Parameters:
        :   **defaultColor** – Default color that changed

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the color picker action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_picker_action.html#classmv_1_1gui_1_1ColorPickerAction_1_1Widget) flags for the configuration of the widget (type)

    Q\_INVOKABLE ColorPickerAction(QObject \*parent, const QString &title, const QColor &color = [DEFAULT\_COLOR](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_picker_action.html#_CPPv4N2mv3gui17ColorPickerAction13DEFAULT_COLORE "mv::gui::ColorPickerAction::DEFAULT_COLOR"))
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **color** – Initial color

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

    static const QColor DEFAULT\_COLOR
    :   Current color.

        Default default color

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   Color picker widget class for color picker action.

        Protected Functions

        Widget(QWidget \*parent, [ColorPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_picker_action.html#_CPPv4N2mv3gui17ColorPickerActionE "mv::gui::ColorPickerAction") \*colorPickerAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **colorPickerAction** – Pointer to color picker action

        Protected Attributes

        QColorDialog \_colorDialog
        :   Main layout.

        [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction") \_hueAction
        :   Non-visible color dialog from which the color picker control is stolen.

        [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction") \_saturationAction
        :   Hue action.

        [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction") \_lightnessAction
        :   Saturation action.

        bool \_updateColorPickerAction
        :   Lightness action.

        Friends

        *friend class* ColorPickerAction
