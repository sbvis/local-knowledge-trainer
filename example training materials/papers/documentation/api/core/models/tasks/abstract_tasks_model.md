# AbstractTasksModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html

**Documentation path:** `api/core/models/tasks/abstract_tasks_model.html`

---

# AbstractTasksModel

**Qualified name:** `mv::AbstractTasksModel`

class AbstractTasksModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Tasks model class.

    Standard item model class for tasks

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::TasksListModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_list_model.html#classmv_1_1TasksListModel), [mv::TasksTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_tree_model.html#classmv_1_1TasksTreeModel)

    Public Types

    enum class Column
    :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) columns.

        *Values:*

        enumerator Name

        enumerator Enabled
        :   Name of the task.

        enumerator Visible
        :   Whether the task is enabled, disabled tasks are not included in task aggregation.

        enumerator Progress
        :   Whether the task is visible in the user interface.

        enumerator ProgressDescription
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) progress.

        enumerator ProgressText
        :   Progress description.

        enumerator Status
        :   Progress text.

        enumerator ProgressMode
        :   Status of the task.

        enumerator ID
        :   Progress mode (manual, subtasks or aggregate)

        enumerator ParentID
        :   Globally unique identifier of the task.

        enumerator Type
        :   Globally unique identifier of the parent task (empty string if not a child task)

        enumerator GuiScopes
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) type.

        enumerator MayKill
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) GUI scopes.

        enumerator Kill
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) may kill boolean.

        enumerator Count
        :   Column for killing a task.

    Public Functions

    AbstractTasksModel(QObject \*parent = nullptr)
    :   Construct with `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    QStandardItem \*itemFromTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task) const
    :   Get item from `task`.

        Returns:
        :   Pointer to found item, nullptr otherwise

    Public Static Attributes

    static QMap<[Column](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel6ColumnE "mv::AbstractTasksModel::Column"), [ColumHeaderInfo](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel15ColumHeaderInfoE "mv::AbstractTasksModel::ColumHeaderInfo")> columnInfo
    :   Column name and tooltip.

    struct ColumHeaderInfo
    :   Header strings for several data roles.

        Public Members

        QString \_edit
        :   Header string for display role.

        QString \_tooltip
        :   Header string for edit role.

    class EnabledItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying whether the task is enabled or not.

        Public Functions

        EnabledItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class GuiScopesItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the task GUI scopes.

        Public Functions

        GuiScopesItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class HeaderItem : public QStandardItem
    :   Header standard model item class.

        Public Functions

        HeaderItem(const [ColumHeaderInfo](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel15ColumHeaderInfoE "mv::AbstractTasksModel::ColumHeaderInfo") &columHeaderInfo)
        :   Construct with `columHeaderInfo`.

            Parameters:
            :   **columHeaderInfo** – Column header info

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class IdItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the task identifier.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task, bool editable = false)
        :   Use base task item constructor.

    class Item : public QStandardItem, public QObject
    :   Base standard model item class for task.

        Subclassed by [mv::AbstractTasksModel::EnabledItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1EnabledItem), [mv::AbstractTasksModel::GuiScopesItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1GuiScopesItem), [mv::AbstractTasksModel::IdItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1IdItem), [mv::AbstractTasksModel::KillItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1KillItem), [mv::AbstractTasksModel::MayKillItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1MayKillItem), [mv::AbstractTasksModel::NameItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1NameItem), [mv::AbstractTasksModel::ParentIdItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1ParentIdItem), [mv::AbstractTasksModel::ProgressDescriptionItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1ProgressDescriptionItem), [mv::AbstractTasksModel::ProgressItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1ProgressItem), [mv::AbstractTasksModel::ProgressModeItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1ProgressModeItem), [mv::AbstractTasksModel::ProgressTextItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1ProgressTextItem), [mv::AbstractTasksModel::StatusItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1StatusItem), [mv::AbstractTasksModel::TypeItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1TypeItem), [mv::AbstractTasksModel::VisibleItem](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel_1_1VisibleItem)

        Public Functions

        Item([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task, bool editable = false)
        :   Construct with `task`.

            Parameters:
            :   - **task** – Pointer to task to display item for
                - **editable** – Whether the model item is editable or not

        [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*getTask() const
        :   Get task return Pointer to task to display item for.

    class KillItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for killing a task.

        Public Functions

        KillItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class MayKillItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying whether the task may be killed.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task, bool editable = false)
        :   Use base task item constructor.

    class NameItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the task name.

        Public Functions

        NameItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data to `value` for `role`.

        inline gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") &getStringAction()
        :   Get string action.

            Returns:
            :   String action for use in item delegates

    class ParentIdItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the parent task identifier.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task, bool editable = false)
        :   Use base task item constructor.

    class ProgressDescriptionItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the progress description.

        Public Functions

        ProgressDescriptionItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class ProgressItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the task progress.

        Public Functions

        ProgressItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        inline gui::[TaskAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/task_action.html#_CPPv4N2mv3gui10TaskActionE "mv::gui::TaskAction") &getTaskAction()
        :   Get task action.

            Returns:
            :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) action for use in item delegate (its built-in progress action)

    class ProgressModeItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the progress mode.

        Public Functions

        ProgressModeItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class ProgressTextItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the progress text.

        Public Functions

        ProgressTextItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining task items in a row.

        Public Functions

        inline Row([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct row with `task`.

            Parameters:
            :   **task** – Pointer to row task

    class StatusItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the task status.

        Public Functions

        StatusItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

    class TypeItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying the task type.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task, bool editable = false)
        :   Use base task item constructor.

    class VisibleItem : public mv::[AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModelE "mv::AbstractTasksModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#_CPPv4N2mv18AbstractTasksModel4ItemE "mv::AbstractTasksModel::Item")
    :   Standard model item class for displaying whether the task is visible or not.

        Public Functions

        VisibleItem([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
        :   Construct with `task`.

            Parameters:
            :   **task** – Pointer to task to display item for

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form
