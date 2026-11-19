# Renderer2D

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer_2d.html

**Documentation path:** `api/core/graphics/renderers/renderer_2d.html`

---

# Renderer2D

**Qualified name:** `mv::Renderer2D`

class Renderer2D : public mv::[Renderer](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer.html#_CPPv4N2mv8RendererE "mv::Renderer")
:   [Renderer](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer.html#classmv_1_1Renderer) 2D class.

    Supports two-dimensional rendering:

    - Orchestrates panning and zooming using [Navigator2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#classmv_1_1Navigator2D)
    - Sets up the matrix transformations
    - Renders 2D data

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::DensityRenderer](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/density_renderer.html#classmv_1_1gui_1_1DensityRenderer), [mv::gui::PointRenderer](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/point_renderer.html#classmv_1_1gui_1_1PointRenderer)

    Public Functions

    explicit Renderer2D(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void resize(QSize renderSize) override
    :   Resize the renderer to `renderSize`.

        Parameters:
        :   **renderSize** – New size of the renderer

    virtual QSize getRenderSize() const override
    :   Get the render size.

        Returns:
        :   Render size

    [Navigator2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#_CPPv4N2mv11Navigator2DE "mv::Navigator2D") &getNavigator()
    :   Get the 2D navigator.

        Returns:
        :   Reference to the 2D navigator

    const [Navigator2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#_CPPv4N2mv11Navigator2DE "mv::Navigator2D") &getNavigator() const
    :   Get the 2D navigator.

        Returns:
        :   Reference to the 2D navigator

    void setSourceWidget(QWidget \*sourceWidget)
    :   Initializes the source widget used for setting the renderer view.

        Parameters:
        :   **sourceWidget** – Pointer to the renderer widget

    QPointer<[Navigator2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#_CPPv4N2mv11Navigator2DE "mv::Navigator2D")> getCustomNavigator() const
    :   Get custom navigator.

        Returns:
        :   Pointer to custom navigator

    void setCustomNavigator(const QPointer<[Navigator2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html#_CPPv4N2mv11Navigator2DE "mv::Navigator2D")> &customNavigator)
    :   Set custom navigator to `customNavigator`.

        Parameters:
        :   **customNavigator** – Pointer to custom navigator

    QVector3D getScreenPointToWorldPosition(const QMatrix4x4 &modelViewMatrix, const QPoint &screenPoint) const
    :   Convert `screenPoint` to point in world coordinates using `modelViewMatrix`.

        Parameters:
        :   - **modelViewMatrix** – Model-view matrix
            - **screenPoint** – Point in screen coordinates [0..width, 0..height]

        Returns:
        :   Position in world coordinates

    QVector2D getWorldPositionToNormalizedScreenPoint(const QVector3D &position) const
    :   Convert `position` in world coordinates to point in normalized screen coordinates.

        Parameters:
        :   **position** – Position in world coordinates

        Returns:
        :   Point in normalized screen coordinates [-1..1, -1..1]

    QPoint getWorldPositionToScreenPoint(const QVector3D &position) const
    :   Convert `position` in world coordinates to point in screen coordinates.

        Parameters:
        :   **position** – Position in world coordinates

        Returns:
        :   Point in screen coordinates [0..width, 0..height]

    QVector2D getScreenPointToNormalizedScreenPoint(const QVector2D &screenPoint) const
    :   Convert `screenPoint` to point in normalized screen coordinates.

        Parameters:
        :   **screenPoint** – Point in screen coordinates [0..width, 0..height]

        Returns:
        :   Point in normalized screen coordinates [-1..1, -1..1]

    QMatrix4x4 getScreenToNormalizedScreenMatrix() const
    :   Returns the matrix that converts screen coordinates [0..width, 0..height] to normalized screen coordinates [-1..1, -1..1].

    QMatrix4x4 getNormalizedScreenToScreenMatrix() const
    :   Returns the matrix that converts normalized screen coordinates [-1..1, -1..1] to screen coordinates [0..width, 0..height].

    QMatrix4x4 getProjectionMatrix() const
    :   Returns the projection matrix.

    QRect getScreenRectangleFromWorldRectangle(const QRectF &worldBoundingRectangle) const
    :   Get screen bounding rectangle from world bounding rectangle.

        Parameters:
        :   **worldBoundingRectangle** – World bounding rectangle

    QMatrix4x4 getModelMatrix() const
    :   Get model matrix.

        Returns:
        :   Model matrix

    void setModelMatrix(const QMatrix4x4 &modelMatrix)
    :   Set model matrix to `modelMatrix`.

        Parameters:
        :   **modelMatrix** – Model matrix

    QMatrix4x4 getModelViewProjectionMatrix() const
    :   Get model-view-projection matrix.

        Returns:
        :   Model-view-projection matrix

    QRectF getDataBounds() const
    :   Get data bounds.

        Returns:
        :   Data bounds

    virtual void setDataBounds(const QRectF &dataBounds)
    :   Set data bounds to `dataBounds`.

        Parameters:
        :   **dataBounds** – Data bounds

    QRectF getWorldBounds() const
    :   Get world bounds.

        Returns:
        :   World bounds

    virtual void setWorldBounds(const QRectF &worldBounds)
    :   Set world bounds to `worldBounds`.

        Parameters:
        :   **worldBounds** – World bounds

    void dataBoundsChanged(const QRectF &previousDataBounds, const QRectF &currentDataBounds)
    :   Signals that the data bounds have changed from `previousDataBounds` to `currentDataBounds`.

        Parameters:
        :   - **previousDataBounds** – Previous data bounds
            - **currentDataBounds** – Current data bounds

    void worldBoundsChanged(const QRectF &previousWorldBounds, const QRectF &currentWorldBounds)
    :   Signals that the world bounds have changed from `previousWorldBounds` to `currentWorldBounds`.

        Parameters:
        :   - **previousWorldBounds** – Previous world bounds
            - **currentWorldBounds** – Current world bounds

    Protected Functions

    virtual void beginRender() override
    :   Begin rendering (sets up the OpenGL viewport and computes the model-view-projection matrix)

    virtual void endRender() override
    :   End rendering.

    virtual QRectF computeWorldBounds() const = 0
    :   Compute the world bounds.
