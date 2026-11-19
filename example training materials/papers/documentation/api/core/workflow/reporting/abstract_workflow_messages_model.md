# AbstractWorkflowMessagesModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html

**Documentation path:** `api/core/workflow/reporting/abstract_workflow_messages_model.html`

---

# AbstractWorkflowMessagesModel

**Qualified name:** `mv::AbstractWorkflowMessagesModel`

`AbstractWorkflowMessagesModel` defines the common columns and item behavior used to present [WorkflowMessage](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html) instances. Its columns expose severity, text, emitter, location, details, timestamp, message ID, and parent-context ID.

Each row creates a shared copy of its workflow message, and every item in that row refers to the same copy. The specialized [list](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_messages_list_model.html) and [tree](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_messages_tree_model.html) models decide how rows are organized.

class AbstractWorkflowMessagesModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   **Author**
    :   Thomas Kroes

    Subclassed by [mv::WorkflowMessagesListModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_messages_list_model.html#classmv_1_1WorkflowMessagesListModel), [mv::WorkflowMessagesTreeModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_messages_tree_model.html#classmv_1_1WorkflowMessagesTreeModel)

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Level

        enumerator Text

        enumerator Emitter

        enumerator Location

        enumerator Details

        enumerator TimeStamp

        enumerator ID

        enumerator ParentID

        enumerator Count

    Public Functions

    AbstractWorkflowMessagesModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    class DetailsItem : public mv::[AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModelE "mv::AbstractWorkflowMessagesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModel4ItemE "mv::AbstractWorkflowMessagesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1Item) class for displaying the workflow message details.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(workflow::SharedWorkflowMessage message)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class EmitterItem : public mv::[AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModelE "mv::AbstractWorkflowMessagesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModel4ItemE "mv::AbstractWorkflowMessagesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1Item) class for displaying the workflow message emitter.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(workflow::SharedWorkflowMessage message)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IdItem : public mv::[AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModelE "mv::AbstractWorkflowMessagesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModel4ItemE "mv::AbstractWorkflowMessagesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1Item) class for displaying the workflow message parent ID.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(workflow::SharedWorkflowMessage message)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Item : public QStandardItem
    :   Base standard model item class for script item

        Subclassed by [mv::AbstractWorkflowMessagesModel::DetailsItem](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1DetailsItem), [mv::AbstractWorkflowMessagesModel::EmitterItem](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1EmitterItem), [mv::AbstractWorkflowMessagesModel::IdItem](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1IdItem), [mv::AbstractWorkflowMessagesModel::LevelItem](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1LevelItem), [mv::AbstractWorkflowMessagesModel::LocationItem](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1LocationItem), [mv::AbstractWorkflowMessagesModel::ParentIdItem](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1ParentIdItem), [mv::AbstractWorkflowMessagesModel::TextItem](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1TextItem), [mv::AbstractWorkflowMessagesModel::TimeStampItem](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1TimeStampItem)

        Public Functions

        Item(workflow::SharedWorkflowMessage message)
        :   Construct with reference to `message`.

            Parameters:
            :   **message** – The workflow message

        workflow::SharedWorkflowMessage getWorkflowMessage() const
        :   Get workflow message.

            Returns:
            :   Shared pointer to workflow message

        QString getTooltip() const
        :   Get tooltip for item.

            Returns:
            :   Tooltip string

    class LevelItem : public mv::[AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModelE "mv::AbstractWorkflowMessagesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModel4ItemE "mv::AbstractWorkflowMessagesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1Item) class for displaying the workflow message type.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(workflow::SharedWorkflowMessage message)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class LocationItem : public mv::[AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModelE "mv::AbstractWorkflowMessagesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModel4ItemE "mv::AbstractWorkflowMessagesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1Item) class for displaying the workflow message location.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(workflow::SharedWorkflowMessage message)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class ParentIdItem : public mv::[AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModelE "mv::AbstractWorkflowMessagesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModel4ItemE "mv::AbstractWorkflowMessagesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1Item) class for displaying the workflow message parent ID.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(workflow::SharedWorkflowMessage message)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining items in a row.

        Public Functions

        inline Row(const workflow::[WorkflowMessage](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_message.html#_CPPv4N2mv8workflow15WorkflowMessageE "mv::workflow::WorkflowMessage") &message)
        :   Construct with reference to `message`.

            Parameters:
            :   **message** – Reference to the workflow message

    class TextItem : public mv::[AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModelE "mv::AbstractWorkflowMessagesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModel4ItemE "mv::AbstractWorkflowMessagesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1Item) class for displaying the workflow message text.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(workflow::SharedWorkflowMessage message)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class TimeStampItem : public mv::[AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModelE "mv::AbstractWorkflowMessagesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#_CPPv4N2mv29AbstractWorkflowMessagesModel4ItemE "mv::AbstractWorkflowMessagesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel_1_1Item) class for displaying the workflow message timestamp.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(workflow::SharedWorkflowMessage message)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
