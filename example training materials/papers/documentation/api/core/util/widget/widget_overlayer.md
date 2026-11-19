# WidgetOverlayer

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/widget/widget_overlayer.html

**Documentation path:** `api/core/util/widget/widget_overlayer.html`

---

# WidgetOverlayer

**Qualified name:** `mv::util::WidgetOverlayer`

class WidgetOverlayer : public QObject
:   Widget overlayer utility class.

    Helper class for layering a widget on top of another widget and synchronizing its geometry.

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetOverlayer(QObject \*parent, QWidget \*sourceWidget, QWidget \*targetWidget, float initialOpacity = 1.0f)
    :   Construct widget overlayer with pointer to `parent` object, `sourceWidget`, `targetWidget` and `initialOpacity`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **sourceWidget** – Pointer to source widget (will be layered on top of the `targetWidget`)
            - **targetWidget** – Pointer to target widget (`sourceWidget` will be layered on top of it)
            - **initialOpacity** – Opacity of `sourceWidget` at initialization

    QWidget \*getSourceWidget() const
    :   Get source widget.

        Returns:
        :   Pointer to source widget

    QWidget \*getTargetWidget() const
    :   Get target widget.

        Returns:
        :   Pointer to target widget

    void setTargetWidget(QWidget \*targetWidget)
    :   Set target widget to `targetWidget`.

        Parameters:
        :   **targetWidget** – Pointer to target widget

    void addMouseEventReceiverWidget(const QWidget \*mouseEventReceiverWidget)
    :   Add `mouseEventReceiverWidget`.

        Parameters:
        :   **mouseEventReceiverWidget** – Const pointer to mouse event receiver widget that should be added

    void removeMouseEventReceiverWidget(const QWidget \*mouseEventReceiverWidget)
    :   Remove `mouseEventReceiverWidget`.

        Parameters:
        :   **mouseEventReceiverWidget** – Const pointer to mouse event receiver widget that should be removed

    MouseEventReceiverWidgets getMouseEventReceiverWidgets()
    :   Get mouse event receiver widgets.

        Returns:
        :   Vector of mouse event receiver widgets

    bool shouldReceiveMouseEvents() const
    :   Determine the source widget should receive mouse events or not.

        Returns:
        :   Boolean determining whether the mouse cursor is under any of the mouse event receiver widgets

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Respond to `target` events.

        Parameters:
        :   - **target** – Object of which an event occurred
            - **event** – The event that took place

    void targetWidgetChanged(QWidget \*previousTargetWidget, QWidget \*currentTargetWidget)
    :   Signals that the target widget changed from `previousTargetWidget` to `currentTargetWidget`.

        Parameters:
        :   - **previousTargetWidget** – Pointer to previous target widget
            - **currentTargetWidget** – Pointer to current target widget

    void mouseEventReceiverWidgetAdded(const QWidget \*mouseEventReceiverWidget)
    :   Signals that `mouseEventReceiverWidget` is added.

        Parameters:
        :   **mouseEventReceiverWidget** – Pointer to mouse receiver widget

    void mouseEventReceiverWidgetRemoved(const QWidget \*mouseEventReceiverWidget)
    :   Signals that `mouseEventReceiverWidget` is removed.

        Parameters:
        :   **mouseEventReceiverWidget** – Pointer to mouse receiver widget
