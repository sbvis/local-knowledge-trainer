# Texture

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/texture.html

**Documentation path:** `api/core/graphics/helpers/texture.html`

---

# Texture

**Qualified name:** `mv::Texture`

class Texture : protected QOpenGLFunctions\_3\_3\_Core
:   Base texture class.

    Contains most of the functionality, but can only be used through one of the sub-classes. The texture subclasses provide the specifics of the operations performed on the texture (such as dimensionality). It is wise to only call functions in this class when an OpenGL context is current and active, otherwise their behaviour is undefined.

    Subclassed by mv::Texture1D, mv::Texture2D

    Public Functions

    inline Texture(GLenum target)
    :   [Texture](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/texture.html#classmv_1_1Texture) constructor.

        Parameters:
        :   **target** – The GLenum specifying the target of texture operations. GL\_TEXTURE\_1D, GL\_TEXTURE\_2D and GL\_TEXTURE\_3D are accepted.

    inline void create()
    :   Initializes the use of OpenGL functions in this context and generates the raw OpenGL Id of the texture.

        This function should be called before doing any other texture operations and only when an OpenGL context is current and active.

    inline void destroy()
    :   Deletes the OpenGL texture Id and invalidates this texture until [create()](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/texture.html#classmv_1_1Texture_1ac6fe816305635c03b2c34b858495a80e) is called again.

    inline void bind(unsigned int textureUnit)
    :   Binds the texture to the given texture unit.

        Parameters:
        :   **textureUnit** – The texture unit should be a value in the range [0-16). One shouldn’t try to pass OpenGL texture units in here, as the given value gets added to GL\_TEXTURE0.

    inline void bind()
    :   Binds the texture to the active texture unit.

    inline void release()
    :   Unbinds the texture by binding the default (0) texture.

    inline bool isCreated()
    :   Return whether the texture has been allocated.

    inline GLuint getHandle()
    :   Return the raw OpenGL texture Id.
