# NumericalRange

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html

**Documentation path:** `api/core/util/numerical_range/numerical_range.html`

---

# NumericalRange

**Qualified name:** `mv::util::NumericalRange`

template<typename NumericalType> class NumericalRange : public QPair<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType"), [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")>
:   Numerical range class.

    Stores a numerical range

    **Author**
    :   Thomas Kroes

    Public Functions

    inline NumericalRange([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType") minimum = std::numeric\_limits<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")>::max(), [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType") maximum = std::numeric\_limits<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")>::lowest())
    :   Construct from /p minimum and `maximum`.

        Parameters:
        :   - **minimum** – Range minimum
            - **maximum** – Range maximum

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType") getMinimum() const
    :   Get range minimum.

    inline void setMinimum([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType") minimum)
    :   Set range minimum to `minimum`.

        Parameters:
        :   **minimum** – Range minimum

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType") getMaximum() const
    :   Get range maximum.

    inline void setMaximum([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType") maximum)
    :   Set range maximum to `maximum`.

        Parameters:
        :   **maximum** – Range maximum

    inline void shiftBy([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType") amount)
    :   Shift range by `amount`.

        Parameters:
        :   **amount** – Amount of shift

    inline [NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")> shiftedBy([NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType") amount)
    :   Get shifted range.

        Parameters:
        :   **amount** – Amount of shift

        Returns:
        :   Shifted range

    inline [NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")> &operator+=(const [NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")> &other)
    :   Addition operator.

        Parameters:
        :   **other** – Other range

        Returns:
        :   Added range

    inline [NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")> &operator+=(float value)
    :   Addition operator.

        Parameters:
        :   **value** – Value to add

        Returns:
        :   Added range

    inline bool operator==(const [NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")> &rhs) const
    :   Equality operator.

        Parameters:
        :   **rhs** – Right-hand-side operator

    inline bool operator!=(const [NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange::NumericalType")> &rhs) const
    :   Inequality operator.

        Parameters:
        :   **rhs** – Right-hand-side operator
