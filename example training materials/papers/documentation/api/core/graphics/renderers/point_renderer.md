# PointRenderer

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/point_renderer.html

**Documentation path:** `api/core/graphics/renderers/point_renderer.html`

---

# PointRenderer

**Qualified name:** `mv::gui::PointRenderer`

## Z ordering

`PointZOrderMode` controls how overlapping points receive depth:

- `InsertionOrder` assigns equal depth to every point, so draw and insertion order determine visibility. This is the default.
- `Dimension` derives depth from a scalar supplied for each point with `setZOrderChannelScalars()`. The renderer computes the scalar range and normalizes values for depth assignment.
- `Randomized` derives a deterministic pseudo-random depth from the point index. It can reduce systematic insertion-order bias without requiring a data dimension.

Configure dimension-controlled ordering by supplying one scalar per rendered point before selecting the mode:

```cpp
renderer.setZOrderChannelScalars(zOrderValues);
renderer.setZOrderMode(mv::gui::PointZOrderMode::Dimension);
```

If dimension mode has no Z-order scalar buffer, points retain equal depth. Keep the scalar vector aligned with the position vector whenever point data changes.

`getRandomizedDepthEnabled()` and `setRandomizedDepthEnabled()` remain compatibility conveniences. Enabling randomized depth selects `Randomized`; disabling it selects `InsertionOrder`. Use `getZOrderMode()` and `setZOrderMode()` when code must distinguish all three modes.

enum class mv::gui::PointZOrderMode
:   Determines how point depth is assigned during rendering.

    *Values:*

    enumerator InsertionOrder

    enumerator Dimension
    :   All points have equal depth; draw/insertion order determines visibility.

    enumerator Randomized
    :   Point depth is derived from a scalar data channel.

        Point depth is generated deterministically from the point index

class PointRenderer : public mv::[Renderer2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer_2d.html#_CPPv4N2mv10Renderer2DE "mv::Renderer2D")
:   Public Functions

    virtual void setDataBounds(const QRectF &dataBounds) override
    :   Set data bounds to `dataBounds`.

        Parameters:
        :   **dataBounds** – Data bounds

    virtual QRectF computeWorldBounds() const override
    :   Update the world bounds.

    virtual void render() override
    :   Render.

    virtual void destroy() override
    :   Destroy the renderer.

    explicit Renderer2D(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object
