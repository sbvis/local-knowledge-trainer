# ColorAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_action.html

**Documentation path:** `api/core/gui/actions/color/color_action.html`

---

# ColorAction

**Qualified name:** `mv::gui::ColorAction`

class ColorAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Color widget action class.

    Stores a color and creates widgets to interact with it

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator Picker

        enumerator ResetPushButton
        :   The widget includes a color picker.

        enumerator Basic
        :   The widget includes a reset push button.

        enumerator All

    Public Functions

    Q\_INVOKABLE ColorAction(QObject \*parent, const QString &title, const QColor &color = [DEFAULT\_COLOR](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_action.html#_CPPv4N2mv3gui11ColorAction13DEFAULT_COLORE "mv::gui::ColorAction::DEFAULT_COLOR"))
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **color** – Initial color

    QColor getColor() const
    :   Gets the current color.

    void setColor(const QColor &color)
    :   Sets the current color.

        Parameters:
        :   **color** – Current color

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void colorChanged(const QColor &color)
    :   Signals that the current color changed.

        Parameters:
        :   **color** – Current color that changed

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the color action.

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

    static const QColor DEFAULT\_COLOR
    :   Current color.

        Default default color

    class PushButtonWidget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   Color picker push button class for color action.

        Protected Functions

        PushButtonWidget(QWidget \*parent, [ColorAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_action.html#_CPPv4N2mv3gui11ColorActionE "mv::gui::ColorAction") \*colorAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **colorAction** – Pointer to color action

        Protected Attributes

        [ColorPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_picker_action.html#_CPPv4N2mv3gui17ColorPickerActionE "mv::gui::ColorPickerAction") \_colorPickerAction
        :   Widget layout.

        [ToolButton](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_action.html#_CPPv4N2mv3gui11ColorAction16PushButtonWidget10ToolButtonE "mv::gui::ColorAction::PushButtonWidget::ToolButton") \_toolButton
        :   Color picker action.

        Friends

        *friend class* ColorAction

        class ToolButton : public QToolButton
        :   Extended tool button widget class with display of current color.

            Public Functions

            ToolButton(QWidget \*parent, [ColorPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/color/color_picker_action.html#_CPPv4N2mv3gui17ColorPickerActionE "mv::gui::ColorPickerAction") &colorPickerAction)
            :   Constructor.

                Parameters:
                :   - **parent** – Parent widget
                    - **colorPickerAction** – Reference to color picker action

            void paintEvent(QPaintEvent \*paintEvent) override
            :   Paint event to override default paint.

                Parameters:
                :   **paintEvent** – Pointer to paint event
