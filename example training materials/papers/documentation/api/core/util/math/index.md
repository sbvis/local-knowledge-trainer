# Math

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/math/index.html

**Documentation path:** `api/core/util/math/index.html`

---

# Math

This section documents utility functions for common mathematical operations and comparisons, including interpolation and approximate equality checks for numeric and geometric values.

## Functions

float mv::util::lerp(float v0, float v1, float t)
:   Linearly interpolates between two values v0 and v1 by t.

    Parameters:
    :   - **v0** – Start value
        - **v1** – End value
        - **t** – Interpolation factor in the range [0, 1]

    Returns:
    :   Interpolated value

template<typename T> bool mv::util::almostEqual([T](https://manivault.readthedocs.io/en/latest/api/core/util/math/index.html#_CPPv4I0EN2mv4util11almostEqualEb1T1T1T1T "mv::util::almostEqual::T") a, [T](https://manivault.readthedocs.io/en/latest/api/core/util/math/index.html#_CPPv4I0EN2mv4util11almostEqualEb1T1T1T1T "mv::util::almostEqual::T") b, [T](https://manivault.readthedocs.io/en/latest/api/core/util/math/index.html#_CPPv4I0EN2mv4util11almostEqualEb1T1T1T1T "mv::util::almostEqual::T") relativeTolerance = [T](https://manivault.readthedocs.io/en/latest/api/core/util/math/index.html#_CPPv4I0EN2mv4util11almostEqualEb1T1T1T1T "mv::util::almostEqual::T")(1e-6), [T](https://manivault.readthedocs.io/en/latest/api/core/util/math/index.html#_CPPv4I0EN2mv4util11almostEqualEb1T1T1T1T "mv::util::almostEqual::T") absoluteTolerance = [T](https://manivault.readthedocs.io/en/latest/api/core/util/math/index.html#_CPPv4I0EN2mv4util11almostEqualEb1T1T1T1T "mv::util::almostEqual::T")(1e-12))
:   Checks whether two numerical values are almost equal.

    Parameters:
    :   - **a** – Numerical value to compare
        - **b** – Numerical value to compare with
        - **relativeTolerance** – Relative tolerance
        - **absoluteTolerance** – Absolute tolerance

    Returns:
    :   Boolean determining whether the numerical values are almost equal

inline bool mv::util::arePointsEqual(const QPointF &point1, const QPointF &point2, qreal epsilon = 1e-5)
:   Checks whether two points are almost equal.

    Parameters:
    :   - **point1** – Point to compare
        - **point2** – Point to compare with
        - **epsilon** – Tolerance

    Returns:
    :   Boolean determining whether the two points are almost equal

inline bool mv::util::areSizesEqual(const QSizeF &size1, const QSizeF &size2, qreal epsilon = 1e-5)
:   Checks whether two sizes are almost equal.

    Parameters:
    :   - **size1** – Size to compare
        - **size2** – Size to compare with
        - **epsilon** – Tolerance

    Returns:
    :   Boolean determining whether the two sizes are almost equal

inline bool mv::util::areRectanglesEqual(const QRectF &rect1, const QRectF &rect2, qreal epsilon = 1e-5)
:   Checks whether two rectangles are almost equal.

    Parameters:
    :   - **rect1** – Rectangle to compare
        - **rect2** – Rectangle to compare with
        - **epsilon** – Tolerance

    Returns:
    :   Boolean determining whether the two rectangles are almost equal
