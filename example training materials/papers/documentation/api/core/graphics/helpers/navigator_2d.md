# Navigator2D

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html

**Documentation path:** `api/core/graphics/helpers/navigator_2d.html`

---

# Navigator2D

**Qualified name:** `mv::Navigator2D`

class Navigator2D : public QObject
:   Navigator 2D class.

    Orchestrates panning and zooming in a widget that displays 2D data using [Renderer2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer_2d.html#classmv_1_1Renderer2D)

    **Author**
    :   Thomas Kroes

    Public Types

    enum class ZoomMarginType
    :   Type of zoom margin.

        *Values:*

        enumerator AbsoluteScreen

        enumerator RelativeToData
        :   Absolute screen pixels.

            Relative to data percentage

    Public Functions

    explicit Navigator2D([Renderer2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer_2d.html#_CPPv4N2mv10Renderer2DE "mv::Renderer2D") &renderer, QObject \*parent = nullptr)
    :   Construct a new two-dimensional navigator.

        Parameters:
        :   - **renderer** – Reference to parent renderer
            - **parent** – Pointer to the parent object

    void initialize(QWidget \*sourceWidget)
    :   Initializes the two-dimensional navigator with a `sourceWidget`.

        Parameters:
        :   **sourceWidget** – Pointer to the renderer widget

    bool eventFilter(QObject \*watched, QEvent \*event) override
    :   Watch `watched` for events.

        Parameters:
        :   - **watched** – Watched object
            - **event** – Event

        Returns:
        :   True if the event was handled, false otherwise

    QMatrix4x4 getViewMatrix() const
    :   Get the view matrix.

        Returns:
        :   View matrix

    QRectF getZoomRectangleWorld() const
    :   Get the world zoom rectangle.

        Returns:
        :   Zoom rectangle in world coordinates

    void setZoomRectangleWorld(const QRectF &zoomRectangleWorld)
    :   Set the world zoom rectangle to `zoomRectangleWorld`.

        Parameters:
        :   **zoomRectangleWorld** – Zoom rectangle in world coordinates

    [ZoomMarginType](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#_CPPv4N2mv11Navigator2D14ZoomMarginTypeE "mv::Navigator2D::ZoomMarginType") getZoomMarginType() const
    :   Get the zoom rectangle margin type.

        Returns:
        :   Zoom rectangle margin type

    void setZoomMarginType([ZoomMarginType](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#_CPPv4N2mv11Navigator2D14ZoomMarginTypeE "mv::Navigator2D::ZoomMarginType") zoomMarginType)
    :   Set the zoom rectangle margin type to `zoomMarginType`.

        Parameters:
        :   **zoomMarginType** – Zoom rectangle margin type

    float getZoomMarginScreen() const
    :   Get the zoom rectangle margin.

        Returns:
        :   Zoom rectangle margin in screen coordinates

    void setZoomMarginScreen(float zoomMarginScreen)
    :   Set the zoom margin in screen coordinates to `zoomMarginScreen`.

        Parameters:
        :   **zoomMarginScreen** – Zoom margin in screen coordinates

    float getZoomMarginData() const
    :   Get the zoom rectangle margin.

        Returns:
        :   Zoom rectangle margin in data coordinates

    void setZoomMarginData(float zoomMarginData)
    :   Set the zoom margin in data coordinates to `zoomMarginData`.

        Parameters:
        :   **zoomMarginData** – Zoom margin in data coordinates

    float getZoomFactor() const
    :   Get the zoom factor.

        Returns:
        :   Zoom factor

    void setZoomFactor(float zoomFactor)
    :   Set the zoom factor to `zoomFactor`.

        Parameters:
        :   **zoomFactor** – Zoom factor

    float getZoomPercentage() const
    :   Get the zoom percentage.

        Returns:
        :   Zoom percentage

    void setZoomPercentage(float zoomPercentage)
    :   Set the zoom percentage to `zoomPercentage`.

        Parameters:
        :   **zoomPercentage** – Zoom percentage

    bool isEnabled() const
    :   Get whether the navigator is enabled.

        Returns:
        :   Boolean determining whether the navigator is enabled

    void setEnabled(bool enabled)
    :   Set enabled to `enabled`.

        Parameters:
        :   **enabled** – Boolean determining whether the navigator is enabled

    gui::[NavigationAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/navigation_action.html#_CPPv4N2mv3gui16NavigationActionE "mv::gui::NavigationAction") &getNavigationAction()
    :   Get the navigation action.

        Returns:
        :   Reference to the navigation action

    const gui::[NavigationAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/navigation_action.html#_CPPv4N2mv3gui16NavigationActionE "mv::gui::NavigationAction") &getNavigationAction() const
    :   Get the navigation action.

        Returns:
        :   Reference to the navigation action

    qreal getDevicePixelRatio() const
    :   Get the source widget device pixel ratio.

        Returns:
        :   Device pixel ratio

    void zoomAround(const QPoint &center, float factor)
    :   Zoom by `factor` around `center`.

        Parameters:
        :   - **center** – Point to zoom around
            - **factor** – Zoom factor

    void zoomToRectangle(const QRectF &zoomRectangle)
    :   Zoom to `zoomRectangle`.

        Parameters:
        :   **zoomRectangle** – Zoom to this rectangle

    void panBy(const QPointF &delta)
    :   Pan by `delta`.

        Parameters:
        :   **delta** – Pan by this amount

    void setZoomCenterWorld(const QPointF &zoomCenterWorld)
    :   Set the zoom center in world coordinates to `zoomCenterWorld`.

        Parameters:
        :   **zoomCenterWorld** – Zoom center in world coordinates

    void resetView(bool force = false)
    :   Reset the view.

        Parameters:
        :   **force** – Force reset event when the user has navigated

    bool isPanning() const
    :   Get whether the renderer is panning.

        Returns:
        :   Boolean determining whether the renderer is panning

    bool isZooming() const
    :   Get whether the renderer is zooming.

        Returns:
        :   Boolean determining whether the renderer is zooming

    bool isNavigating() const
    :   Get whether the renderer is navigating.

        Returns:
        :   Boolean determining whether the renderer is navigating

    bool hasUserNavigated() const
    :   Get whether the user has navigated.

        Returns:
        :   Boolean determining whether the user has navigated

    QRect getZoomRegionRectangle() const
    :   Get the zoom region rectangle in screen coordinates.

        Returns:
        :   Zoom region rectangle in screen coordinates

    void panningStarted()
    :   Signals that panning has started.

    void panningEnded()
    :   Signals that panning has ended.

    void isPanningChanged(bool isPanning)
    :   Signals that is panning changed to `isPanning`.

        Parameters:
        :   **isPanning** –

    void zoomingStarted()
    :   Signals that zooming has started.

    void zoomingEnded()
    :   Signals that zooming has ended.

    void isZoomingChanged(bool isZooming)
    :   Signals that is zooming changed to `isZooming`.

        Parameters:
        :   **isZooming** – Boolean determining whether the renderer is zooming

    void navigationStarted()
    :   Signals that navigation has started.

    void navigationEnded()
    :   Signals that navigation has ended.

    void isNavigatingChanged(bool isNavigating)
    :   Signals that is navigating changed to `isNavigating`.

        Parameters:
        :   **isNavigating** – Boolean determining whether the renderer is navigating

    void enabledChanged(bool enabled)
    :   Signals that enabled changed to `enabled`.

        Parameters:
        :   **enabled** – Boolean determining whether the navigator is enabled

    void zoomRectangleWorldChanged(const QRectF &previousZoomRectangleWorld, const QRectF &currentZoomRectangleWorld)
    :   Signals that the zoom rectangle in world coordinates has changed from `previousZoomRectangleWorld` to `currentZoomRectangleWorld`.

        Parameters:
        :   - **previousZoomRectangleWorld** – Previous world zoom rectangle
            - **currentZoomRectangleWorld** – Current world zoom rectangle

    void zoomCenterWorldChanged(const QPointF &previousZoomCenterWorld, const QPointF &currentZoomCenterWorld)
    :   Signals that the zoom center in world coordinates has changed from `previousZoomCenterWorld` to `currentZoomCenterWorld`.

        Parameters:
        :   - **previousZoomCenterWorld** – Previous world zoom center
            - **currentZoomCenterWorld** – Current world zoom center

    void zoomFactorChanged(float previousZoomFactor, float currentZoomFactor)
    :   Signals that the zoom factor has changed from `previousZoomFactor` to `currentZoomFactor`.

        Parameters:
        :   - **previousZoomFactor** – Previous zoom factor
            - **currentZoomFactor** – Current zoom factor

    void aboutToChangeZoomMargin()
    :   Signals that the zoom margin is about to chang.

    void zoomMarginChanged()
    :   Signals that the zoom margin has changed.

    Protected Functions

    void setIsPanning(bool isPanning)
    :   Set whether the renderer is panning to `isPanning`.

        Parameters:
        :   **isPanning** – Boolean determining whether the renderer is panning

    void setIsZooming(bool isZooming)
    :   Set whether the renderer is zooming to `isZooming`.

        Parameters:
        :   **isZooming** – Boolean determining whether the renderer is zooming

    void setIsNavigating(bool isNavigating)
    :   Set whether the renderer is navigating to `isNavigating`.

        Parameters:
        :   **isNavigating** – Boolean determining whether the renderer is navigating

    void beginPanning()
    :   Panning has begun.

    void endPanning()
    :   Panning has ended.

    void beginZooming()
    :   Zooming has begun.

    void endZooming()
    :   Zooming has ended.

    void beginNavigation()
    :   Navigation has begun.

    void endNavigation()
    :   Navigation has ended.

    void beginChangeZoomRectangleWorld()
    :   Begin changing the zoom rectangle in world coordinates.

    void endChangeZoomRectangleWorld()
    :   End changing the zoom rectangle in world coordinates.

    void beginZoomToRegion()
    :   Begin zooming to a region.

    void endZoomToRegion()
    :   End zooming to a region.

    void beginChangeZoomMargin()
    :   Begin zoom margin change.

    void endChangeZoomMargin()
    :   End zoom margin change.

    void changeCursor(const QCursor &cursor)
    :   Change the cursor to `cursor`.

        Parameters:
        :   **cursor** – Cursor

    void restoreCursor() const
    :   Restore cached cursor.

    class ZoomOverlayWidget : public mv::gui::[OverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/overlay_widget.html#_CPPv4N2mv3gui13OverlayWidgetE "mv::gui::OverlayWidget")
    :   For drawing the zoom region.

        Public Functions

        ZoomOverlayWidget([Navigator2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#_CPPv4N2mv11Navigator2DE "mv::Navigator2D") &navigator, QWidget \*targetWidget)
        :   Construct a new zoom overlay widget.

            Parameters:
            :   - **navigator** – Reference to the navigator
                - **targetWidget** – Pointer to the target widget

        void paintEvent(QPaintEvent \*event) override
        :   Override the paint event to draw the zoom regio rectangle.

            Parameters:
            :   **event** –
