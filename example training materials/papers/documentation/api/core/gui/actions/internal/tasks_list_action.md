# TasksListAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/tasks_list_action.html

**Documentation path:** `api/core/gui/actions/internal/tasks_list_action.html`

---

# TasksListAction

**Qualified name:** `mv::gui::TasksListAction`

class TasksListAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Tasks list action class.

    Action class for managing tasks

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE TasksListAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    [AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel") \*getModel()
    :   Get tasks model.

        Returns:
        :   Pointer to the tasks model

    [TasksFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_filter_model.html#_CPPv4N2mv16TasksFilterModelE "mv::TasksFilterModel") \*getFilterModel()
    :   Get tasks filter model.

        Returns:
        :   Pointer to the tasks filter model

    void initialize([AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel") \*model, [TasksFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_filter_model.html#_CPPv4N2mv16TasksFilterModelE "mv::TasksFilterModel") \*filterModel, const QString &itemTypeName, WidgetConfigurationFunction widgetConfigurationFunction = WidgetConfigurationFunction(), bool mayLoadTasksPlugin = true)
    :   Initialize the action with pointers to tasks `model` and `filterModel`.

        Parameters:
        :   - **model** – Pointer to the tasks model
            - **filterModel** – Pointer to the tasks filter model
            - **itemTypeName** – Item type name string
            - **widgetConfigurationFunction** – Configuration function to call after the widget has been configured by the tasks action
            - **mayLoadTasksPlugin** – When set to true, adds a trigger action to the toolbar for loading the tasks plugin

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the color action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/tasks_list_action.html#classmv_1_1gui_1_1TasksListAction_1_1Widget) flags for the configuration of the widget (type)

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/tasks_list_action.html#classmv_1_1gui_1_1TasksListAction_1_1Widget) action for listing the tasks vertically.

        Protected Functions

        Widget(QWidget \*parent, [TasksListAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/tasks_list_action.html#_CPPv4N2mv3gui15TasksListActionE "mv::gui::TasksListAction") \*tasksListAction, const std::int32\_t &widgetFlags)
        :   Construct with pointer to `parent` widget, owning `tasksListAction` and `widgetFlags`.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **tasksListAction** – Pointer to owning tasks list action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/tasks_list_action.html#classmv_1_1gui_1_1TasksListAction_1_1Widget) flags for the configuration of the widget (type)

        Protected Attributes

        QGridLayout \_layout
        :   Pointer to owning tasks list action.

        WidgetsMap \_widgetsMap
        :   Tasks layout.

        Friends

        *friend class* TasksListAction
