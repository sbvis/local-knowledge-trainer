# ToggleAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html

**Documentation path:** `api/core/gui/actions/toggle/toggle_action.html`

---

# ToggleAction

**Qualified name:** `mv::gui::ToggleAction`

class ToggleAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Toggle action class.

    Toggle action with check/setEnabled button UI

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator Icon
        :   Push button options.

        enumerator Text
        :   Enable push button icon.

        enumerator CheckBox
        :   Enable push button text.

        enumerator PushButton
        :   The widget includes a checkbox.

        enumerator ToggleImage
        :   The widget includes a setEnabled push button with text.

        enumerator ToggleImageText
        :   Widget uses an image that changes based on toggle state.

        enumerator PushButtonIcon
        :   Widget uses an image that changes based on toggle state and also includes a title label.

            Push button configurations

        enumerator PushButtonText
        :   Push button with icon only.

        enumerator PushButtonIconText
        :   Push button with text only.

        enumerator Default
        :   Push button with icon and text.

    Public Functions

    Q\_INVOKABLE ToggleAction(QObject \*parent, const QString &title, bool toggled = false)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **toggled** – Toggled

    void setChecked(bool checked)
    :   Overrides the base class [setChecked()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#classmv_1_1gui_1_1ToggleAction_1a8e43a865c30c008cbdb98fe3c47d04cd)

        Parameters:
        :   **checked** – Checked status

    bool getIndeterminate() const
    :   Get indeterminate state.

        Returns:
        :   Whether the toggle action is in an indeterminate state

    void setIndeterminate(bool indeterminate)
    :   Set indeterminate state.

        Parameters:
        :   **indeterminate** – Whether the toggle action is in an indeterminate state

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void indeterminateChanged(bool indeterminate)
    :   Signals that the indeterminate value changed.

        Parameters:
        :   **indeterminate** – Whether the toggle action is in an indeterminate state

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the setEnabled action.

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

    Friends

    *friend class* AbstractActionsManager

    class CheckBoxWidget : public QCheckBox
    :   Check box widget class for toggle action.

        Protected Functions

        CheckBoxWidget(QWidget \*parent, [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \*toggleAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **toggleAction** – Pointer to toggle action

        bool eventFilter(QObject \*target, QEvent \*event) override
        :   Respond to `target` `event`.

            Parameters:
            :   - **target** – Object of which an event occurred
                - **event** – The event that took place

        Friends

        *friend class* ToggleAction

    class PushButtonWidget : public QPushButton
    :   Push button widget class for toggle action.

        Protected Functions

        PushButtonWidget(QWidget \*parent, [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \*toggleAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **toggleAction** – Pointer to toggle action
                - **widgetFlags** – Widget flags

        void resizeEvent(QResizeEvent \*event) override
        :   Override this event to make the push button square (in case only an icon is used)

            Parameters:
            :   **event** – Pointer to resize event

        Protected Attributes

        std::int32\_t \_widgetFlags
        :   Pointer to toggle action.

        Friends

        *friend class* ToggleAction

    class ToggleImageLabelWidget : public QWidget
    :   Toggle image widget class for toggle action.

        Protected Functions

        ToggleImageLabelWidget(QWidget \*parent, [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \*toggleAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **toggleAction** – Pointer to toggle action
                - **widgetFlags** – Widget flags

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event that occurred

        Friends

        *friend class* ToggleAction
