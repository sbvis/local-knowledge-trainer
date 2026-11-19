# DatasetTaskHandler

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/handlers/dataset_task_handler.html

**Documentation path:** `api/core/task/handlers/dataset_task_handler.html`

---

# DatasetTaskHandler

**Qualified name:** `mv::DatasetTaskHandler`

class DatasetTaskHandler : public mv::[AbstractTaskHandler](https://manivault.readthedocs.io/en/latest/api/core/task/handlers/abstract_task_handler.html#_CPPv4N2mv19AbstractTaskHandlerE "mv::AbstractTaskHandler")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) task handler class.

    Interact with dataset task.

    **Author**
    :   Thomas Kroes

    Public Functions

    DatasetTaskHandler(QObject \*parent, [DatasetTask](https://manivault.readthedocs.io/en/latest/api/core/task/types/dataset_task.html#_CPPv4N2mv11DatasetTaskE "mv::DatasetTask") \*datasetTask)
    :   Construct task handler with `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **datasetTask** – Pointer to dataset task to handle
