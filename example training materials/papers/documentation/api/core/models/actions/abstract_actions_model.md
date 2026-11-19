# AbstractActionsModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html

**Documentation path:** `api/core/models/actions/abstract_actions_model.html`

---

# AbstractActionsModel

**Qualified name:** `mv::AbstractActionsModel`

class AbstractActionsModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Abstract actions model class.

    Abstract standard item model class for actions

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::ActionsHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_hierarchy_model.html#classmv_1_1ActionsHierarchyModel), [mv::ActionsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_list_model.html#classmv_1_1ActionsListModel), mv::PublicActionsModel

    Public Types

    enum class Column
    :   Action columns.

        *Values:*

        enumerator Name

        enumerator Location
        :   Name of the action.

        enumerator ID
        :   Where the action is located in the user interface.

        enumerator Type
        :   Globally unique identifier of the action.

        enumerator Scope
        :   Action type string.

        enumerator ForceDisabled
        :   Scope of the action (whether the action is public or private)

        enumerator ForceHidden
        :   Whether the action is force disabled or not.

        enumerator MayPublish
        :   Whether the action is force hidden or not.

        enumerator MayConnect
        :   Whether the action may be published.

        enumerator MayDisconnect
        :   Whether the action may connect to a public action.

        enumerator SortIndex
        :   Whether the action may disconnect from a public action.

        enumerator Stretch
        :   The sorting index of the action (its relative position in action groups)

        enumerator ParentActionId
        :   The stretch in action groups.

        enumerator IsConnected
        :   The identifier of the parent action (if not a top-level action)

        enumerator NumberOfConnectedActions
        :   Whether the action is connected or not.

        enumerator PublicActionID
        :   Number of connected actions (in case the action is public)

        enumerator IsRoot
        :   The identifier of the public action with which the action is connected.

        enumerator IsLeaf
        :   If the action is at the root or not.

        enumerator Count
        :   If the action is a leaf or not.

    Public Functions

    AbstractActionsModel(QObject \*parent = nullptr)
    :   Construct with `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void initialize() = 0
    :   Initializes the model from the current state of the actions manager.

    Qt::ItemFlags flags(const QModelIndex &index) const override
    :   Get flags for item with `index`.

        Returns:
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1Item) flags

    gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction(const QModelIndex &index) const
    :   Get action for model `index`.

        Parameters:
        :   **index** – Model index to retrieve the action for

        Returns:
        :   Pointer to action (nullptr if not found)

    gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction(std::int32\_t rowIndex) const
    :   Get action for model `rowIndex`.

        Parameters:
        :   **rowIndex** – [Row](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1Row) index to retrieve the action for

        Returns:
        :   Pointer to action (nullptr if not found)

    gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction(const QString &name) const
    :   Get action by `name`.

        Parameters:
        :   **name** – Name of the action

        Returns:
        :   Pointer to action (nullptr if not found)

    virtual QModelIndex getActionIndex(const gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, const [Column](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel6ColumnE "mv::AbstractActionsModel::Column") &column = [Column](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel6ColumnE "mv::AbstractActionsModel::Column")::[Name](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel6Column4NameE "mv::AbstractActionsModel::Column::Name")) const final
    :   Get model index for `action` and column.

        Parameters:
        :   - **action** – Pointer to action to retrieve the model index for
            - **column** – Column to retrieve the action index for

        Returns:
        :   Found model index

    virtual QStandardItem \*getActionItem(const gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) const final
    :   Get action item for `action`.

        Parameters:
        :   **action** – Pointer to action to retrieve the model item for

        Returns:
        :   Pointer to standard item (nullptr if not found)

    Public Static Attributes

    static QMap<[Column](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel6ColumnE "mv::AbstractActionsModel::Column"), [ColumHeaderInfo](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel15ColumHeaderInfoE "mv::AbstractActionsModel::ColumHeaderInfo")> columnInfo
    :   Column name and tooltip.

    Protected Functions

    Qt::DropActions supportedDragActions() const override
    :   Get the supported drag actions.

    Qt::DropActions supportedDropActions() const override
    :   Get the supported drop actions.

    QStringList mimeTypes() const override
    :   Get mime types.

        Returns:
        :   Supported mime types

    QMimeData \*mimeData(const QModelIndexList &indexes) const override
    :   Get mime data for model `indexes`.

        Returns:
        :   Pointer to mime data for `indexes`

    bool canDropMimeData(const QMimeData \*mimeData, Qt::DropAction dropAction, int row, int column, const QModelIndex &parent) const override
    :   Determines whether `mimeData` with `action` can be dropped on `row` and `column` with `parent` model index.

        Parameters:
        :   - **mimeData** – Pointer to dropped mime data
            - **dropAction** – Drop action
            - **row** – Drop row
            - **column** – Drop column
            - **parent** – Drop parent index

        Returns:
        :   Boolean whether the drop is permitted

    bool dropMimeData(const QMimeData \*mimeData, Qt::DropAction dropAction, int row, int column, const QModelIndex &parent) override
    :   Invoked when `mimeData` is dropped.

        Parameters:
        :   - **mimeData** – Pointer to dropped mime data
            - **dropAction** – Drop action
            - **row** – Drop row
            - **column** – Drop column
            - **parent** – Drop parent index

        Returns:
        :   Boolean determining whether the drop is performed

    inline virtual void actionAddedToManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Helper method which is invoked when `action` is added to the actions manager.

        Parameters:
        :   **action** – Pointer to action that was added

    inline virtual void actionAboutToBeRemovedFromManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Helper method which is invoked when `action` is about to be removed from the actions manager.

        Parameters:
        :   **action** – Pointer to action that was removed

    inline virtual void publicActionAddedToManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction)
    :   Helper method which is invoked when `publicAction` is added to the actions manager.

        Parameters:
        :   **publicAction** – Pointer to public action that was added

    inline virtual void publicActionAboutToBeRemovedFromManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction)
    :   Helper method which is invoked when `publicAction` is about to be removed from the actions manager.

        Parameters:
        :   **publicAction** – Pointer to public action to remove

    struct ColumHeaderInfo
    :   Header strings for several data roles.

        Public Members

        QString \_edit
        :   Header string for display role.

        QString \_tooltip
        :   Header string for edit role.

    class ConnectionPermissionItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Model item class for toggling a permission flag.

        Public Functions

        ConnectionPermissionItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, const gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")::[ConnectionPermissionFlag](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetAction24ConnectionPermissionFlagE "mv::gui::WidgetAction::ConnectionPermissionFlag") &connectionPermissionFlag)
        :   Construct with `action` and `connectionPermissionFlag`.

            Parameters:
            :   - **action** – Pointer to action to display item for
                - **connectionPermissionFlag** – Connection permission flag to display

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

    class ForceDisabledItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Model item class for toggling action force disabled.

        Public Functions

        ForceDisabledItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

    class ForceHiddenItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Model item class for toggling force hidden.

        Public Functions

        ForceHiddenItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

    class HeaderItem : public QStandardItem
    :   Header standard model item class.

        Public Functions

        HeaderItem(const [ColumHeaderInfo](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel15ColumHeaderInfoE "mv::AbstractActionsModel::ColumHeaderInfo") &columHeaderInfo)
        :   Construct with `columHeaderInfo`.

            Parameters:
            :   **columHeaderInfo** – Column header info

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class IdItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying the action identifier.

        Public Functions

        IdItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class IsConnectedItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying whether the action is connected or not.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, bool editable = false)
        :   Use base action item constructor.

    class IsLeafItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying whether the action is a leaf action.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, bool editable = false)
        :   Use base action item constructor.

    class IsRootItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying whether the action is a root action.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, bool editable = false)
        :   Use base action item constructor.

    class Item : public QStandardItem, public QObject
    :   Base standard model item class for widget action.

        Subclassed by [mv::AbstractActionsModel::ConnectionPermissionItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1ConnectionPermissionItem), [mv::AbstractActionsModel::ForceDisabledItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1ForceDisabledItem), [mv::AbstractActionsModel::ForceHiddenItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1ForceHiddenItem), [mv::AbstractActionsModel::IdItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1IdItem), [mv::AbstractActionsModel::IsConnectedItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1IsConnectedItem), [mv::AbstractActionsModel::IsLeafItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1IsLeafItem), [mv::AbstractActionsModel::IsRootItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1IsRootItem), [mv::AbstractActionsModel::LocationItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1LocationItem), [mv::AbstractActionsModel::NameItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1NameItem), [mv::AbstractActionsModel::NumberOfConnectedActionsItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1NumberOfConnectedActionsItem), [mv::AbstractActionsModel::ParentActionIdItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1ParentActionIdItem), [mv::AbstractActionsModel::PublicActionIdItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1PublicActionIdItem), [mv::AbstractActionsModel::ScopeItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1ScopeItem), [mv::AbstractActionsModel::SortIndexItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1SortIndexItem), [mv::AbstractActionsModel::StretchItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1StretchItem), [mv::AbstractActionsModel::TypeItem](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel_1_1TypeItem)

        Public Functions

        Item(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, bool editable = false)
        :   Construct with `action`.

            Parameters:
            :   - **action** – Pointer to action to display item for
                - **editable** – Whether the model item is editable or not

        QPointer<gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")> getAction() const
        :   Get action return Pointer to action to display item for.

    class LocationItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying the action location.

        Public Functions

        LocationItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class NameItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying the action name.

        Public Functions

        NameItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

    class NumberOfConnectedActionsItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying the number of connected actions.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, bool editable = false)
        :   Use base action item constructor.

    class ParentActionIdItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying the parent action identifier.

        Public Functions

        ParentActionIdItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class PublicActionIdItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying the public action identifier.

        Public Functions

        PublicActionIdItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining action items in a row.

        Public Functions

        inline Row(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct row with `action`.

            Parameters:
            :   **action** – Pointer to row action

    class ScopeItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying the action scope.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, bool editable = false)
        :   Use base action item constructor.

    class SortIndexItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Model item class for action sort index.

        Public Functions

        SortIndexItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

    class StretchItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Model item class for action stretch.

        Public Functions

        StretchItem(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
        :   Construct with `action`.

            Parameters:
            :   **action** – Pointer to action to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

    class TypeItem : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModel4ItemE "mv::AbstractActionsModel::Item")
    :   Standard model item class for displaying the action type.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action, bool editable = false)
        :   Use base action item constructor.
