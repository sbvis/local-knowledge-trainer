# ActionsWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/actions_widget.html

**Documentation path:** `api/core/gui/widgets/internal/actions_widget.html`

---

# ActionsWidget

**Qualified name:** `mv::gui::ActionsWidget`

class ActionsWidget : public QWidget
:   Actions widget class.

    Widget class for viewing the contents of an actions model (e.g. list or hierarchy)

    **Author**
    :   Thomas Kroes

    Public Functions

    ActionsWidget(QWidget \*parent, [AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel") &actionsModel, const QString &itemTypeName = "Parameter")
    :   Constructor.

        Parameters:
        :   - **parent** – Parent widget
            - **actionsModel** – Reference to actions input model
            - **itemTypeName** – Name of the action in the hierarchy widget

    [ActionsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_filter_model.html#_CPPv4N2mv18ActionsFilterModelE "mv::ActionsFilterModel") &getFilterModel()
    :   Get filter model.

        Returns:
        :   Reference to actions filter model

    [HierarchyWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/hierarchy_widget.html#_CPPv4N2mv3gui15HierarchyWidgetE "mv::gui::HierarchyWidget") &getHierarchyWidget()
    :   Get hierarchy widget.

        Returns:
        :   Reference to hierarchy widget

    void setRequestContextMenuCallback(RequestContextMenuFN requestContextMenu)
    :   Sets the callback function which is called when the widget asks for a context menu.

        Parameters:
        :   **requestContextMenu** – Callback function which is called when the widget asks for a context menu
