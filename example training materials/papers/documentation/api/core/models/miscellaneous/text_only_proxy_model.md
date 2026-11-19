# TextOnlyProxyModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/miscellaneous/text_only_proxy_model.html

**Documentation path:** `api/core/models/miscellaneous/text_only_proxy_model.html`

---

# TextOnlyProxyModel

**Qualified name:** `mv::TextOnlyProxyModel`

class TextOnlyProxyModel : public QIdentityProxyModel
:   Text only proxy model class.

    Forwards only the display role for the specified completion column.

    Note: This is primarily used for use cases where performance in large models is needed.

    **Author**
    :   Thomas Kroes

    Public Functions

    QVariant data(const QModelIndex &index, int role) const override
    :   Get the data for the model `index` and `role`.

        Parameters:
        :   - **index** – Index of the data to retrieve
            - **role** – Role of the data to retrieve

        Returns:
        :   Data for the model index and role

    std::int32\_t getCompletionColumn() const
    :   Get the completion column.

        Returns:
        :   Column index of the completion column

    void setCompletionColumn(std::int32\_t completionColumn)
    :   Set the completion column to `completionColumn`.

        Parameters:
        :   **completionColumn** – Column index of the completion column

    void completionColumnChanged(std::int32\_t column)
    :   Signals that the completion column changed to `column`.

        Parameters:
        :   **column** – Column index of the completion column
