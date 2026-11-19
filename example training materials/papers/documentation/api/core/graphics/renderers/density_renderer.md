# DensityRenderer

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/density_renderer.html

**Documentation path:** `api/core/graphics/renderers/density_renderer.html`

---

# DensityRenderer

**Qualified name:** `mv::gui::DensityRenderer`

class DensityRenderer : public mv::[Renderer2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer_2d.html#_CPPv4N2mv10Renderer2DE "mv::Renderer2D")
:   Public Functions

    virtual void resize(QSize renderSize) override
    :   Resize the renderer to `renderSize`.

        Parameters:
        :   **renderSize** – New size of the renderer

    virtual void setDataBounds(const QRectF &dataBounds) override
    :   Set data bounds to `dataBounds`.

        Parameters:
        :   **dataBounds** – Data bounds

    virtual QRectF computeWorldBounds() const override
    :   Update the world bounds.

    void setDensityComputationDataBounds(const QRectF &bounds)
    :   Set density computation data boundss.

        Parameters:
        :   **bounds** – Density computation data bounds

    void setColormap(const QImage &image)
    :   Loads a colormap from an image and loads as the current colormap for the landscape view.

        Parameters:
        :   **image** – Color map image

    virtual void render() override
    :   Render.

    virtual void destroy() override
    :   Destroy the renderer.
