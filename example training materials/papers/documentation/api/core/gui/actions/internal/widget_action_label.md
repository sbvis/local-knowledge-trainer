# WidgetActionLabel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_label.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_label.html`

---

# WidgetActionLabel

**Qualified name:** `mv::gui::WidgetActionLabel`

class WidgetActionLabel : public mv::gui::[WidgetActionViewWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_view_widget.html#_CPPv4N2mv3gui22WidgetActionViewWidgetE "mv::gui::WidgetActionViewWidget")
:   Widget action label class.

    Provides a label view on the action

    Most important features:

    - Label of which the text, visibility and tooltip is synchronized with the action
    - Provide linking commands

      - Publish an action (create a public shared action)
      - Connect to a shared action
      - Disconnect from a shared action

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator ColonAfterName

    Public Functions

    explicit WidgetActionLabel([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, QWidget \*parent = nullptr, const std::uint32\_t &flags = [ColonAfterName](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_label.html#_CPPv4N2mv3gui17WidgetActionLabel10WidgetFlag14ColonAfterNameE "mv::gui::WidgetActionLabel::ColonAfterName"))
    :   Constructor.

        Parameters:
        :   - **action** – Pointer to widget action
            - **parent** – Pointer to parent widget
            - **windowFlags** – Window flags

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Respond to target object events.

        Parameters:
        :   - **target** – Object of which an event occurred
            - **event** – The event that took place

    bool event(QEvent \*event) override
    :   Respond to widget events.

        Parameters:
        :   **event** – The event that took place

        Returns:
        :   Boolean indicating whether the event was handled

    void resizeEvent(QResizeEvent \*resizeEvent) override
    :   Invoked when the widget is resized.

        Parameters:
        :   **resizeEvent** – Pointer to the resize event

    bool geElide() const
    :   Gets whether label elide is enabled or not.

    void setElide(bool elide)
    :   Set whether label elide is enabled or not.

        Parameters:
        :   **labelElide** – Whether label elide is enabled or not

    Protected Attributes

    QLabel \_nameLabel
    :   Configuration flags.

    bool \_elide
    :   Action name label.

    QDrag \*\_drag
    :   Whether to enable label elide (e.g.

        whether to truncate text and show an ellipsis when there is insufficient space for the text)

    QPoint \_lastMousePressPosition
    :   Pointer is set during drag and drop action connection.
