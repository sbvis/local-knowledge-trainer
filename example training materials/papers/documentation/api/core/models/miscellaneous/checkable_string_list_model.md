# CheckableStringListModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/miscellaneous/checkable_string_list_model.html

**Documentation path:** `api/core/models/miscellaneous/checkable_string_list_model.html`

---

# CheckableStringListModel

**Qualified name:** `mv::CheckableStringListModel`

class CheckableStringListModel : public QStringListModel
:   Checkable string list model class.

    Extends the standard string list model to include ability to check items

    **Author**
    :   Thomas Kroes

    Public Types

    using CheckedIndicesSet = QSet<std::int32\_t>
    :   List of checked string indices.

    using CheckStatesList = QList<bool>
    :   Set of checked string indices.

    Public Functions

    Qt::ItemFlags flags(const QModelIndex &index) const override
    :   Get flags for model `index`.

        Parameters:
        :   **index** – Model index to get the flags for

        Returns:
        :   Item flags

    QVariant data(const QModelIndex &index, int role) const override
    :   Get data for model `index` and `role`.

        Parameters:
        :   - **index** – Model index to get the data for
            - **role** – The data role

        Returns:
        :   Data in variant form

    bool setData(const QModelIndex &index, const QVariant &value, int role) override
    :   Set data for model `index` and `role` to `value`.

        Parameters:
        :   - **index** – Model index to set the data for
            - **value** – The data value
            - **role** – The data role

        Returns:
        :   Whether setting the data was successful or not

    void setStrings(const QStringList &strings)
    :   Sets the strings in the model to `strings`.

        Parameters:
        :   **strings** – New strings

    QStringList getCheckedStrings() const
    :   Get checked strings.

        Returns:
        :   String list of checked items

    CheckedIndicesList getCheckedIndicesList() const
    :   Get checked indices list.

        Returns:
        :   List of checked indices

    [CheckedIndicesSet](https://manivault.readthedocs.io/en/latest/api/core/models/miscellaneous/checkable_string_list_model.html#_CPPv4N2mv24CheckableStringListModel17CheckedIndicesSetE "mv::CheckableStringListModel::CheckedIndicesSet") getCheckedIndicesSet() const
    :   Get checked indices set.

        Returns:
        :   Set of checked indices

    void setCheckedIndicesSet(const [CheckedIndicesSet](https://manivault.readthedocs.io/en/latest/api/core/models/miscellaneous/checkable_string_list_model.html#_CPPv4N2mv24CheckableStringListModel17CheckedIndicesSetE "mv::CheckableStringListModel::CheckedIndicesSet") &checkedIndicesSet)
    :   Set checked indices set to `checkedIndicesSet`.

        Parameters:
        :   **checkedIndicesSet** – Set of checked indices

    void setCheckedIndicesFromStrings(const QStringList &checkedStrings)
    :   Set checked indices from `checkedStrings`.

        Parameters:
        :   **checkedStrings** – List of checked strings

    void invertChecks()
    :   Invert the state of each check.
