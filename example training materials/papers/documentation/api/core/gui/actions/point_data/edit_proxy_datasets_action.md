# EditProxyDatasetsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/edit_proxy_datasets_action.html

**Documentation path:** `api/core/gui/actions/point_data/edit_proxy_datasets_action.html`

---

# EditProxyDatasetsAction

**Qualified name:** `EditProxyDatasetsAction`

class EditProxyDatasetsAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Edit proxy datasets action class.

    Action class for editing proxy datasets

    **Author**
    :   Thomas Kroes

    Public Functions

    EditProxyDatasetsAction(QObject \*parent, const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &points)
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
    :   Get widget representation of the edit proxy datasets action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/edit_proxy_datasets_action.html#classEditProxyDatasetsAction_1_1Widget) flags for the configuration of the widget (type)

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/edit_proxy_datasets_action.html#classEditProxyDatasetsAction_1_1Widget) class for edit proxy datasets action.

        Public Functions

        Widget(QWidget \*parent, [EditProxyDatasetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/edit_proxy_datasets_action.html#_CPPv423EditProxyDatasetsAction "EditProxyDatasetsAction") \*editProxyDatasetsAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **editProxyDatasetsAction** – Pointer to edit proxy datasets action
