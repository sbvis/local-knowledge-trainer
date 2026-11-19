# LoggingModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html

**Documentation path:** `api/core/models/logging/logging_model.html`

---

# LoggingModel

**Qualified name:** `mv::LoggingModel`

`LoggingModel` presents the [structured message records](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html) owned by the application logger. It checks for newly captured messages when the event dispatcher wakes and adds model rows without transferring ownership of the underlying records.

Application interfaces may use this model directly or place a [LoggingFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_filter_model.html) in front of it. Plugin code normally emits Qt log messages instead of inserting model rows.

class LoggingModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Logging model.

    Model item class for log items

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Column
    :   Columns.

        *Values:*

        enumerator Number

        enumerator Type

        enumerator Message

        enumerator FileAndLine

        enumerator Function

        enumerator Category

        enumerator Count

    Public Functions

    LoggingModel(QObject \*parent = nullptr)
    :   Construct from `parent`.

        Parameters:
        :   **parent** – Pointer to parent object

    LoggingModel(const [LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModel12LoggingModelERK12LoggingModel "mv::LoggingModel::LoggingModel")&) = delete
    :   No need for copy constructor.

    ~LoggingModel() override = default
    :   No need for destructor.

    [LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &operator=(const [LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel")&) = delete
    :   No need for assignment operator.

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    class CategoryItem : public mv::[LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModel4ItemE "mv::LoggingModel::Item")
    :   Standard model item class for displaying the message category.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &loggingModel, const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &messageRecord)
        :   No need to override base constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class FileAndLineItem : public mv::[LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModel4ItemE "mv::LoggingModel::Item")
    :   Standard model item class for displaying the message file and line.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &loggingModel, const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &messageRecord)
        :   No need to override base constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class FunctionItem : public mv::[LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModel4ItemE "mv::LoggingModel::Item")
    :   Standard model item class for displaying the message function.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &loggingModel, const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &messageRecord)
        :   No need to override base constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Item : public QStandardItem, public QObject
    :   Base standard model item class for message record.

        Subclassed by [mv::LoggingModel::CategoryItem](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#classmv_1_1LoggingModel_1_1CategoryItem), [mv::LoggingModel::FileAndLineItem](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#classmv_1_1LoggingModel_1_1FileAndLineItem), [mv::LoggingModel::FunctionItem](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#classmv_1_1LoggingModel_1_1FunctionItem), [mv::LoggingModel::MessageItem](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#classmv_1_1LoggingModel_1_1MessageItem), [mv::LoggingModel::NumberItem](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#classmv_1_1LoggingModel_1_1NumberItem), [mv::LoggingModel::TypeItem](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#classmv_1_1LoggingModel_1_1TypeItem)

        Public Functions

        Item([LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &loggingModel, const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &messageRecord)
        :   Construct with `messageRecord`.

            Parameters:
            :   - **loggingModel** – Reference to owning logging model
                - **messageRecord** – Reference to message record

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        [LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &getLoggingModel()
        :   Get logging model.

            Returns:
            :   Reference to owning logging model

        const [LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &getLoggingModel() const
        :   Get logging model.

            Returns:
            :   Reference to owning logging model

        const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &getMessageRecord() const
        :   Get message record.

            Returns:
            :   Reference to message record to display item for

    class MessageItem : public mv::[LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModel4ItemE "mv::LoggingModel::Item")
    :   Standard model item class for displaying the message type.

        Public Functions

        MessageItem([LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &loggingModel, const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &messageRecord)
        :   Construct with `messageRecord`.

            Parameters:
            :   - **loggingModel** – Reference to owning logging model
                - **messageRecord** – Reference to message record

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class NumberItem : public mv::[LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModel4ItemE "mv::LoggingModel::Item")
    :   Standard model item class for interacting with the message number.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &loggingModel, const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &messageRecord)
        :   No need to override base constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining message record items in a row.

        Public Functions

        inline Row([LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &loggingModel, const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &messageRecord)
        :   Construct with reference to owning `loggingModel` and `messageRecord`.

            Parameters:
            :   - **loggingModel** – Reference to owning logging model
                - **MessageRecord** – Reference to message record

    class TypeItem : public mv::[LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModel4ItemE "mv::LoggingModel::Item")
    :   Standard model item class for displaying the message type.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item([LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#_CPPv4N2mv12LoggingModelE "mv::LoggingModel") &loggingModel, const util::[MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html#_CPPv4N2mv4util13MessageRecordE "mv::util::MessageRecord") &messageRecord)
        :   No need to override base constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
