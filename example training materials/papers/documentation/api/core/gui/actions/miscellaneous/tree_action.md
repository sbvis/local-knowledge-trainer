# TreeAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/tree_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/tree_action.html`

---

# TreeAction

**Qualified name:** `mv::gui::TreeAction`

class TreeAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Tree action class.

    Action class for interacting with a tree model

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator FilterToolbar

    Public Functions

    Q\_INVOKABLE TreeAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void initialize(QAbstractItemModel \*model, QSortFilterProxyModel \*filterModel, const QString &itemTypeName)
    :   Initializes the tree action with a pointer to a `model`, possibly a `filterModel` and `itemTypeName`.

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

    inline QString getItemTypeName()
    :   Get item type name.

        Returns:
        :   Item type name string

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the tree action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/tree_action.html#classmv_1_1gui_1_1TreeAction_1_1Widget) flags for the configuration of the widget (type)

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/tree_action.html#classmv_1_1gui_1_1TreeAction_1_1Widget) class for tree action.

        Protected Functions

        Widget(QWidget \*parent, [TreeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/tree_action.html#_CPPv4N2mv3gui10TreeActionE "mv::gui::TreeAction") \*treeAction, const std::int32\_t &widgetFlags)
        :   Construct with pointer to `parent` widget, `treeAction` and `widgetFlags`.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **treeAction** – Pointer to tree action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/tree_action.html#classmv_1_1gui_1_1TreeAction_1_1Widget) flags

        Friends

        *friend class* TreeAction
