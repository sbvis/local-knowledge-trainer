# LoggingFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_filter_model.html

**Documentation path:** `api/core/models/logging/logging_filter_model.html`

---

# LoggingFilterModel

**Qualified name:** `mv::LoggingFilterModel`

`LoggingFilterModel` is the sorting and filtering layer for a [LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html). It supports filtering captured messages by text and Qt message type while preserving the structured column semantics needed for sorting.

class LoggingFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Logging filter model.

    Provides a sorting and filtering model for the logging model

    **Author**
    :   Thomas Kroes

    Public Functions

    LoggingFilterModel(QObject \*parent = nullptr)
    :   Constructor.

        Parameters:
        :   **parent** – Pointer to parent object

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether a give row with give parent is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index

        Returns:
        :   Boolean indicating whether the item is filtered in or out

    bool lessThan(const QModelIndex &lhs, const QModelIndex &rhs) const override
    :   Compares two cluster items.

        Parameters:
        :   - **lhs** – Left cluster
            - **rhs** – Right cluster
