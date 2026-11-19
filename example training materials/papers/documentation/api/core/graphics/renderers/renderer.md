# Renderer

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer.html

**Documentation path:** `api/core/graphics/renderers/renderer.html`

---

# Renderer

**Qualified name:** `mv::Renderer`

class Renderer : public QObject, protected QOpenGLFunctions\_3\_3\_Core
:   Subclassed by [mv::Renderer2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer_2d.html#classmv_1_1Renderer2D)

    Protected Functions

    inline explicit Renderer(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual QSize getRenderSize() const = 0
    :   Get the render size.

        Returns:
        :   Render size

    virtual void beginRender() = 0
    :   Begin rendering.

    virtual void render() = 0
    :   Render.

    virtual void endRender() = 0
    :   End rendering.

    virtual void destroy() = 0
    :   Destroy the renderer.
