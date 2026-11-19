# SelectedIndicesAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/selected_indices_action.html

**Documentation path:** `api/core/gui/actions/point_data/selected_indices_action.html`

---

# SelectedIndicesAction

**Qualified name:** `SelectedIndicesAction`

class SelectedIndicesAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Selected indices action class.

    Action class for selected point indices

    **Author**
    :   Thomas Kroes

    Public Functions

    SelectedIndicesAction(QObject \*parent, const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &points)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **points** – Smart pointer to points dataset

    mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &getPoints()
    :   Get points.

        Returns:
        :   Smart pointer to points dataset

    std::vector<std::uint32\_t> getSelectedIndices() const
    :   Get selected indices.

        Returns:
        :   Selected indices

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the selected indices action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/selected_indices_action.html#classSelectedIndicesAction_1_1Widget) flags for the configuration of the widget (type)

    Protected Attributes

    mv::gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") \_updateAction
    :   Points dataset reference.

    mv::gui::[ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_manualUpdateAction
    :   Update action.

    Protected Static Attributes

    static const std::int32\_t MANUAL\_UPDATE\_THRESHOLD = 1000
    :   Manual update action.

        Above this threshold, selected indices need to be updated manually

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/selected_indices_action.html#classSelectedIndicesAction_1_1Widget) class for points info action.

        Public Functions

        Widget(QWidget \*parent, [SelectedIndicesAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/selected_indices_action.html#_CPPv421SelectedIndicesAction "SelectedIndicesAction") \*selectedIndicesAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **selectedIndicesAction** – Pointer to selected indices action

        class ListView : public QListView
        :   Inherit list view to override size hint method.

            Public Functions

            inline QSize sizeHint() const override
            :   Return smallest possible size hint to avoid layout problems.
