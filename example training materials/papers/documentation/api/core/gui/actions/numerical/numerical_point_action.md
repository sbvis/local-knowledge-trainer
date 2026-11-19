# NumericalPointAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html

**Documentation path:** `api/core/gui/actions/numerical/numerical_point_action.html`

---

# NumericalPointAction

**Qualified name:** `mv::gui::NumericalPointAction`

template<typename NumericalType, typename NumericalActionType> class NumericalPointAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Numerical point action base class.

    Stores a two-dimensional point value.

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Axis
    :   Axis enum

        *Values:*

        enumerator X

        enumerator Y
        :   X axis.

        enumerator Count
        :   Y axis.

    Public Functions

    inline NumericalPointAction(QObject \*parent, const QString &title, [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType") minimum, [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType") maximum)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **minimum** – Minimum value
            - **maximum** – Maximum value

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType") getX() const
    :   Retrieves the X coordinate value.

        Returns:
        :   The X coordinate

    inline void setX(const [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType") &x)
    :   Set the X coordinate value.

        Parameters:
        :   **x** – X coordinate value

    inline void setY(const [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType") &y)
    :   Set the Y coordinate value.

        Parameters:
        :   **y** – Y coordinate value

    inline [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType") getY() const
    :   Retrieves the Y coordinate value.

        Returns:
        :   The Y coordinate

    inline void set(const [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType") &x, const [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType") &y)
    :   Set the X and Y coordinate values.

        Parameters:
        :   - **x** – X coordinate value
            - **y** – Y coordinate value

    inline QPoint getPoint() const
    :   Retrieves the X and Y coordinate values as a QPoint.

        Returns:
        :   QPoint value

    inline void set(const QPoint &point)
    :   Set the X and Y coordinate values from a QPoint.

        Parameters:
        :   **point** – QPoint value

    inline QPointF getPointF() const
    :   Retrieves the X and Y coordinate values as a QPointF.

        Returns:
        :   QPointF value

    inline void set(const QPointF &point)
    :   Set the X and Y coordinate values from a QPointF.

        Parameters:
        :   **point** – QPointF value

    inline std::pair<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType"), [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType")> get() const
    :   Retrieves the X and Y coordinate values as a std::pair.

        Returns:
        :   Pair of X and Y coordinate values

    inline void set(const std::pair<[NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType"), [NumericalType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/numerical_point_action.html#_CPPv4I00EN2mv3gui20NumericalPointActionE "mv::gui::NumericalPointAction::NumericalType")> &pair)
    :   Set the X and Y coordinate values from a std::pair.

        Parameters:
        :   **pair** – Pair of X and Y coordinate values

    inline QVector2D getVector() const
    :   Retrieves the X and Y coordinate values as a QVector2D.

        Returns:
        :   QVector2D value

    inline void set(const QVector2D &vector)
    :   Set the X and Y coordinate values from a Qt vector.

        Parameters:
        :   **vector** – QVector2D value

    inline virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load numerical point action from variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the numerical point action

    inline virtual QVariantMap toVariantMap() const override
    :   Save numerical point action to variant map.

        Returns:
        :   Variant map representation of the numerical point action
