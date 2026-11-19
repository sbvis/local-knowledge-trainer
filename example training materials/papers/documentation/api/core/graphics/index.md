# Graphics

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/index.html

**Documentation path:** `api/core/graphics/index.html`

---

# Graphics

The graphics module provides low-level rendering infrastructure used throughout the application for efficient and reusable GPU-based visualization. It defines a generic renderer abstraction alongside a set of helper classes that encapsulate common rendering patterns and graphics resources.

Renderers focus on orchestrating draw calls and rendering logic, while helper classes provide thin, explicit wrappers around graphics primitives such as buffers, shaders, textures, framebuffers, and mathematical types. Together, these components form a minimal and flexible foundation for building higher-level visualizations without imposing a specific rendering strategy.

## Renderer classes

Below are renderer classes often used in **ManiVault**, for instance in the [scatterplot plugin](https://github.com/ManiVaultStudio/scatterplot).

- [Renderer](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer.html)
- [Renderer2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/renderer_2d.html)
- [PointRenderer](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/point_renderer.html)
  - [Z ordering](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/point_renderer.html#z-ordering)
- [DensityRenderer](https://manivault.readthedocs.io/en/latest/api/core/graphics/renderers/density_renderer.html)

## Helper classes

The helper classes below are used to expedite the renderer development.

- [Navigator2D](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/navigator_2d.html)
- [Bounds](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/bounds.html)
- [BufferObject](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/buffer_object.html)
- [Framebuffer](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/frame_buffer.html)
- [Matrix3f](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/matrix_3f.html)
- [OffscreenBuffer](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/off_screen_buffer.html)
- [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html)
- [ShaderProgram](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/shader.html)
- [Texture](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/texture.html)
- [Vector2f](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/vector_2f.html)
- [Vector3f](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/vector_3f.html)
