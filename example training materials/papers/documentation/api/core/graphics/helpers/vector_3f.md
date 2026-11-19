# Vector3f

**Source:** https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/vector_3f.html

**Documentation path:** `api/core/graphics/helpers/vector_3f.html`

---

# Vector3f

**Qualified name:** `mv::Vector3f`

class Vector3f
:   Public Functions

    void set(float x, float y, float z)
    :   Sets the x, y and z components of this vector to the given parameters.

        Parameters:
        :   - **x** – the x-component of the vector
            - **y** – the y-component of the vector
            - **z** – the z-component of the vector

    void add([Vector3f](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/vector_3f.html#_CPPv4N2mv8Vector3fE "mv::Vector3f") v)
    :   Adds the given vector to this vector.

        Parameters:
        :   **v** – the vector to be added

    void sub([Vector3f](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/vector_3f.html#_CPPv4N2mv8Vector3fE "mv::Vector3f") v)
    :   Subtracts the given vector from this vector.

        Parameters:
        :   **v** – the vector to be subtracted

    inline constexpr float sqrMagnitude() const
    :   Returns the squared magnitude of this vector.

        Returns:
        :   the squared magnitude of this vector

    float length()
    :   Returns the magnitude of this vector.

        Returns:
        :   the magnitude of this vector

    std::string str() const
    :   Returns a string representation of this vector.

        Returns:
        :   the string representation
