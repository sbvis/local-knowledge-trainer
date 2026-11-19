# RectangleAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html

**Documentation path:** `api/core/gui/actions/numerical/rectangle_action.html`

---

# RectangleAction

**Qualified name:** `mv::gui::RectangleAction`

template<typename NumericalRangeActionType> class RectangleAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Rectangle action class.

    Base rectangle class for storing a rectangle and interfacing with it

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Axis
    :   Axis enum for distinguishing between x- and y axis range of the rectangle.

        *Values:*

        enumerator X

        enumerator Y
        :   Along x-axis.

        enumerator Count
        :   Along y-axis.

    using RectangleChangedCB = std::function<void()>
    :   Templated classes with Q\_OBJECT macro are not allowed, so use function pointers instead.

    Public Functions

    inline RectangleAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    inline QPair<util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<NumValType>, util::[NumericalRange](https://manivault.readthedocs.io/en/latest/api/core/util/numerical_range/numerical_range.html#_CPPv4I0EN2mv4util14NumericalRangeE "mv::util::NumericalRange")<NumValType>> getRectangle() const
    :   Get rectangle.

        Returns:
        :   Rectangle as a pair of numerical ranges

    inline [Bounds](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/bounds.html#_CPPv4N2mv6BoundsE "mv::Bounds") getBounds() const
    :   Get bounds.

        Returns:
        :   Rectangle as bounds

    inline void setRectangle(NumValType left, NumValType right, NumValType bottom, NumValType top)
    :   Set rectangle with `left`, `right`, `bottom` and `top` coordinates.

        Parameters:
        :   - **left** – Left of the rectangle
            - **right** – Right of the rectangle
            - **bottom** – Bottom of the rectangle
            - **top** – Top of the rectangle

    inline void setBounds(const [Bounds](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/bounds.html#_CPPv4N2mv6BoundsE "mv::Bounds") &bounds)
    :   Set rectangle from `bounds`.

        Parameters:
        :   **bounds** – Rectangle bounds

    inline NumValType getWidth() const
    :   Get rectangle width.

        Returns:
        :   Width of the rectangle

    inline NumValType getHeight() const
    :   Get rectangle height.

        Returns:
        :   Height of the rectangle

    inline QPair<NumValType, NumValType> getCenter() const
    :   Get rectangle center.

        Returns:
        :   Center of the rectangle

    inline NumValType getLeft() const
    :   Get rectangle left.

        Returns:
        :   Left of the rectangle

    inline void setLeft(typename [NumericalRangeActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#_CPPv4I0EN2mv3gui15RectangleActionE "mv::gui::RectangleAction::NumericalRangeActionType")::ValueType left)
    :   Set rectangle left to `left`.

        Parameters:
        :   **left** – Rectangle left

    inline NumValType getRight() const
    :   Get rectangle right.

        Returns:
        :   Right of the rectangle

    inline void setRight(typename [NumericalRangeActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#_CPPv4I0EN2mv3gui15RectangleActionE "mv::gui::RectangleAction::NumericalRangeActionType")::ValueType right)
    :   Set rectangle right to `right`.

        Parameters:
        :   **right** – Rectangle right

    inline NumValType getBottom() const
    :   Get rectangle bottom.

        Returns:
        :   Bottom of the rectangle

    inline void setBottom(typename [NumericalRangeActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#_CPPv4I0EN2mv3gui15RectangleActionE "mv::gui::RectangleAction::NumericalRangeActionType")::ValueType bottom)
    :   Set rectangle bottom to `bottom`.

        Parameters:
        :   **bottom** – Rectangle bottom

    inline NumValType getTop() const
    :   Get rectangle top.

        Returns:
        :   Top of the rectangle

    inline void setTop(typename [NumericalRangeActionType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#_CPPv4I0EN2mv3gui15RectangleActionE "mv::gui::RectangleAction::NumericalRangeActionType")::ValueType top)
    :   Set rectangle top to `top`.

        Parameters:
        :   **top** – Rectangle top

    inline void translateBy(QPair<NumValType, NumValType> translation)
    :   Translate by `translation`.

        Parameters:
        :   **translation** – Amount of translation

    inline void expandBy(float factor)
    :   Expand by `factor`.

        Parameters:
        :   **factor** – Expansion factor

    Protected Functions

    inline void blockRectangleChangedCallBack()
    :   Prevent [RectangleAction::\_rectangleChanged](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#classmv_1_1gui_1_1RectangleAction_1aa3412786af69fcd365b10a478e733ef2) from being called.

    inline void unblockRectangleChangedCallBack()
    :   Allow [RectangleAction::\_rectangleChanged](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#classmv_1_1gui_1_1RectangleAction_1aa3412786af69fcd365b10a478e733ef2) to be called.

    inline bool isRectangleChangedCallBackBlocked() const
    :   Get whether [RectangleAction::\_rectangleChanged](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#classmv_1_1gui_1_1RectangleAction_1aa3412786af69fcd365b10a478e733ef2) callbacks are blocked.

        Returns:
        :   Boolean determining whether [RectangleAction::\_rectangleChanged](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#classmv_1_1gui_1_1RectangleAction_1aa3412786af69fcd365b10a478e733ef2) calls are blocked

    Protected Attributes

    [RectangleChangedCB](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#_CPPv4N2mv3gui15RectangleAction18RectangleChangedCBE "mv::gui::RectangleAction::RectangleChangedCB") \_rectangleChanged
    :   Whether [RectangleAction::\_rectangleChanged](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/rectangle_action.html#classmv_1_1gui_1_1RectangleAction_1aa3412786af69fcd365b10a478e733ef2) calls are blocked.
