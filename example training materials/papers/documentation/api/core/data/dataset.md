# Dataset

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html

**Documentation path:** `api/core/data/dataset.html`

---

# Dataset

`Dataset<T>` is a typed, non-owning handle to a core-managed dataset. It tracks dataset identity, becomes invalid when the implementation is removed, and exposes dataset lifecycle and change events as Qt signals inherited from `DatasetPrivate`.

template<typename DatasetType = [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> class Dataset : public mv::[DatasetPrivate](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_private.html#_CPPv4N2mv14DatasetPrivateE "mv::DatasetPrivate")
:   Smart dataset class.

    Only dataset reference template classes have access to protected members.

    Smart pointer for datasets

    This smart pointer aims to make dataset access through pointers more secure. It internally manages a pointer throughout the lifetime of a dataset (resets the datasets to nullptr when a dataset is removed etc.). Access is through standard arrow and dereference operators. It is advised to always check for pointer validity before use of the pointer. In addition, it emits data signals when data is renamed, removed etc.

    **Author**
    :   T. Kroes

    Public Functions

    inline Dataset([DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType") \*dataset = nullptr)
    :   (Default) constructor

        Parameters:
        :   **dataset** – Pointer to dataset (if any)

    inline Dataset([DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType") &dataset)
    :   Construct from dataset reference.

        Parameters:
        :   **dataset** – Reference to dataset

    inline Dataset(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4N2mv7Dataset7DatasetERK7DatasetI11DatasetTypeE "mv::Dataset::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType")> &other)
    :   Copy constructor.

        Parameters:
        :   **other** – Smart pointer to copy from

    template<typename OtherDatasetType> inline Dataset(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7Dataset7DatasetERK7DatasetI16OtherDatasetTypeE "mv::Dataset::Dataset")<[OtherDatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7Dataset7DatasetERK7DatasetI16OtherDatasetTypeE "mv::Dataset::Dataset::OtherDatasetType")> &other)
    :   Templated copy constructor.

        Parameters:
        :   **other** – Smart pointer to copy from

    inline [DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType") &operator\*()
    :   Dereference operator.

        Returns:
        :   Reference to dataset

    inline const [DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType") &operator\*() const
    :   Const dereference operator.

        Returns:
        :   Reference to dataset

    inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType")> &operator=(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType")> &rhs)
    :   Assignment operator.

        Parameters:
        :   **rhs** – Right hand side operator

    inline [DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType") \*operator->()
    :   Overloaded arrow operator.

        Returns:
        :   Pointer to dataset (if any, maybe nullptr)

    inline const [DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType") \*operator->() const
    :   Const overloaded arrow operator.

        Returns:
        :   Const pointer to dataset (if any, maybe nullptr)

    inline [DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType") \*operator()() const
    :   Parenthesis operator.

        Returns:
        :   Pointer to dataset (if any, maybe nullptr)

    template<typename TargetSetType> inline [TargetSetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0ENK2mv7Dataset3getEP13TargetSetTypev "mv::Dataset::get::TargetSetType") \*get() const
    :   Get pointer of `TargetSetType` to dataset.

        Returns:
        :   Pointer of `TargetSetType` to dataset (if any, maybe nullptr)

    inline [DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset::DatasetType") \*get() const
    :   Get pointer to dataset.

        Returns:
        :   Pointer to dataset (if any, maybe nullptr)

    inline bool isValid() const
    :   Returns smart pointer validity.

        Returns:
        :   Boolean determining whether the dataset pointer is valid (if the dataset actually exists and not about to be removed)
