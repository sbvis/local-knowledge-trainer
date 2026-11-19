# NumberOfSelectedPointsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/number_of_selected_points_action.html

**Documentation path:** `api/core/gui/actions/point_data/number_of_selected_points_action.html`

---

# NumberOfSelectedPointsAction

**Qualified name:** `NumberOfSelectedPointsAction`

class NumberOfSelectedPointsAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Number of selected points action class.

    Action class for viewing the number of selected points

    **Author**
    :   Thomas Kroes

    Public Functions

    NumberOfSelectedPointsAction(QObject \*parent, const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &points)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **points** – Smart pointer to points dataset

    mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &getPoints()
    :   Get points.

        Returns:
        :   Smart pointer to points dataset

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the number of selected points action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/number_of_selected_points_action.html#classNumberOfSelectedPointsAction_1_1Widget) flags for the configuration of the widget (type)

    Protected Attributes

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_numberOfSelectedPointsAction
    :   Points dataset reference.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/number_of_selected_points_action.html#classNumberOfSelectedPointsAction_1_1Widget) class for number of selected points action.

        Public Functions

        Widget(QWidget \*parent, [NumberOfSelectedPointsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/number_of_selected_points_action.html#_CPPv428NumberOfSelectedPointsAction "NumberOfSelectedPointsAction") \*numberOfSelectedPointsAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **numberOfSelectedPointsAction** – Pointer to number of selected points action
