# DatasetTask

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/types/dataset_task.html

**Documentation path:** `api/core/task/types/dataset_task.html`

---

# DatasetTask

**Qualified name:** `mv::DatasetTask`

`DatasetTask` associates progress with a dataset and exposes it through data-hierarchy and foreground presentation. Plugin code normally accesses the task already owned by a dataset through `dataset->getTask()`.

For dataset lifetime and progress guidance, see [Threading and integration](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/threading_and_integration.html).

class DatasetTask : public mv::[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")
:   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) task class.

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) for reporting progress related to datasets (for instance in the data hierarchy plugin).

    **Author**
    :   Thomas Kroes

    Public Functions

    DatasetTask(QObject \*parent, const QString &name, const Status &status = Status::Undefined, bool mayKill = false)
    :   Construct task with `parent` object, `name` and initial `status`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **name** – Name of the task
            - **status** – Initial status of the task
            - **mayKill** – Boolean determining whether the task may be killed or not

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getDataset()
    :   Get the dataset that the task refers to.

    void setDataset([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
    :   Set dataset to `dataset`.

        Parameters:
        :   **dataset** – The dataset that the task refers to
