# Model

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/model/model.html

**Documentation path:** `api/core/util/model/model.html`

---

# Model

This section documents utility functions for querying and operating on Qt model structures, such as retrieving persistent model indexes or standard items at a specific column.

---

## Functions

QList<QPersistentModelIndex> mv::util::getAllPersistentModelIndexesAtColumn(const QAbstractItemModel \*model, std::int32\_t columnIndex)
:   Get all persistent model indexes at `columnIndex` from `model`.

    Parameters:
    :   - **model** – Pointer to the model
        - **columnIndex** – Index of the column to retrieve model indexes from

    Returns:
    :   List of persistent model indexes at the specified column index

QList<QStandardItem\*> mv::util::getAllStandardItemsAtColumn(const QStandardItemModel \*model, std::int32\_t columnIndex)
:   Get all items at `columnIndex` from `model`.

    Parameters:
    :   - **model** – Pointer to the model
        - **columnIndex** – Index of the column to retrieve items from

    Returns:
    :   List of standard items at the specified column index
