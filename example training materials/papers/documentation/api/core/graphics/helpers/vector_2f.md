# Vector2f

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/vector_2f.html

**Documentation path:** `api/core/graphics/helpers/vector_2f.html`

---

# Vector2f

**Qualified name:** `mv::Vector2f`

class Vector2f
:   Public Functions

    void set(float x, float y)
    :   Sets the x and y components of this vector to the given parameters.

        Parameters:
        :   - **x** – the x-component of the vector
            - **y** – the y-component of the vector

    void add([Vector2f](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/vector_2f.html#_CPPv4N2mv8Vector2fE "mv::Vector2f") v)
    :   Adds the given vector to this vector.

        Parameters:
        :   **v** – the vector to be added

    void sub([Vector2f](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/vector_2f.html#_CPPv4N2mv8Vector2fE "mv::Vector2f") v)
    :   Subtracts the given vector from this vector.

        Parameters:
        :   **v** – the vector to be subtracted

    inline constexpr float sqrMagnitude() const
    :   Returns the squared magnitude of this vector.

        Returns:
        :   the squared magnitude of this vector

    float length() const
    :   Returns the magnitude of this vector.

        Returns:
        :   the magnitude of this vector

    std::string str() const
    :   Returns a string representation of this vector.

        Returns:
        :   the string representation
