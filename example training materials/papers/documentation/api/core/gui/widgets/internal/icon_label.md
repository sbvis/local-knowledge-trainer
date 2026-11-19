# IconLabel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/icon_label.html

**Documentation path:** `api/core/gui/widgets/internal/icon_label.html`

---

# IconLabel

**Qualified name:** `mv::gui::IconLabel`

class IconLabel : public QLabel
:   Icon label class.

    Icon label with tooltip (obtained with tooltip callback function)

    **Author**
    :   Thomas Kroes

    Public Types

    using ClickedCallback = std::function<void()>
    :   Callback function that is called when a tooltip is required.

    Public Functions

    IconLabel(const QIcon &icon, QWidget \*parent = nullptr)
    :   Callback function that is called when the icon label is clicked (used by non-QObject derived classes)

        Construct from `icon` and `parent` widget

        Parameters:
        :   - **icon** – Icon
            - **parent** – Pointer to parent widget

    void setIcon(const QIcon &icon)
    :   Set the icon to `icon`.

        Parameters:
        :   **icon** – Icon to set

    TooltipCallback getTooltipCallback() const
    :   Get the tooltip callback.

        Returns:
        :   TooltipCallback that is called when the sub-action is hovered

    void setTooltipCallback(const TooltipCallback &tooltipCallback)
    :   Set the tooltip callback to `tooltipCallback`.

        Parameters:
        :   **tooltipCallback** – Callback function that is called when a tooltip is required

    [ClickedCallback](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/icon_label.html#_CPPv4N2mv3gui9IconLabel15ClickedCallbackE "mv::gui::IconLabel::ClickedCallback") getClickedCallback() const
    :   Get the clicked callback.

        Returns:
        :   ClickedCallback that is called when the sub-action is clicked

    void setClickedCallback(const [ClickedCallback](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/icon_label.html#_CPPv4N2mv3gui9IconLabel15ClickedCallbackE "mv::gui::IconLabel::ClickedCallback") &clickedCallback)
    :   Set the clicked callback to `clickedCallback`.

        Parameters:
        :   **clickedCallback** – Callback function that is called when the icon label is clicked (used by non-QObject derived classes)

    void enterEvent(QEnterEvent \*enterEvent) override
    :   Triggered on mouse hover.

        Parameters:
        :   **enterEvent** – Pointer to enter event

    void leaveEvent(QEvent \*event) override
    :   Triggered on mouse leave.

        Parameters:
        :   **event** – Pointer to event

    bool event(QEvent \*event) override
    :   Handle events.

        Parameters:
        :   **event** – Pointer to event

        Returns:
        :   True if the event was handled, false otherwise
