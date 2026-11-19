# TableAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/table_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/table_action.html`

---

# TableAction

**Qualified name:** `mv::gui::TableAction`

class TableAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   Table action class.

    Action class for interacting with a model in a table view

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE TableAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void initialize(QAbstractItemModel \*model, QSortFilterProxyModel \*filterModel, const QString &itemTypeName)
    :   Initializes the table action with a pointer to a `model`, possibly a `filterModel` and `itemTypeName`.

        Parameters:
        :   - **model** – Pointer to model
            - **filterModel** – Pointer to filter model (maybe nullptr)
            - **itemTypeName** – Item type name string

    inline QAbstractItemModel \*getModel()
    :   Get model.

        Returns:
        :   Pointer to model (maybe nullptr)

    inline QSortFilterProxyModel \*getFilterModel()
    :   Get filter model.

        Returns:
        :   Pointer to filter model (maybe nullptr)

    inline QItemSelectionModel &getSelectionModel()
    :   Get selection model.

        Returns:
        :   Reference to selection model

    inline QString getItemTypeName()
    :   Get item type name.

        Returns:
        :   Item type name string

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the tree action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/table_action.html#classmv_1_1gui_1_1TableAction_1_1Widget) flags for the configuration of the widget (type)

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/table_action.html#classmv_1_1gui_1_1TableAction_1_1Widget) class for table action.

        Protected Functions

        Widget(QWidget \*parent, [TableAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/table_action.html#_CPPv4N2mv3gui11TableActionE "mv::gui::TableAction") \*tableAction, const std::int32\_t &widgetFlags)
        :   Construct with pointer to `parent` widget, `treeAction` and `widgetFlags`.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **tableAction** – Pointer to owning table action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/table_action.html#classmv_1_1gui_1_1TableAction_1_1Widget) flags

        Protected Attributes

        QTableView \_tableView
        :   Pointer to owning table action.

        [InfoOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/info_overlay_widget.html#_CPPv4N2mv3gui17InfoOverlayWidgetE "mv::gui::InfoOverlayWidget") \_infoOverlayWidget
        :   Table view for showing the data.

        QString \_noItemsDescription
        :   Overlay widget that show information when there are no items in the model.

        [HorizontalHeaderAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/horizontal_header_action.html#_CPPv4N2mv3gui22HorizontalHeaderActionE "mv::gui::HorizontalHeaderAction") \_horizontalHeaderAction
        :   Overlay widget description when no items are loaded.

        Friends

        *friend class* TableAction
