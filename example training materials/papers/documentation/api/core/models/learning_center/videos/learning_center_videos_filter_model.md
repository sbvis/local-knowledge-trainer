# LearningCenterVideosFilterModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_filter_model.html

**Documentation path:** `api/core/models/learning_center/videos/learning_center_videos_filter_model.html`

---

# LearningCenterVideosFilterModel

**Qualified name:** `mv::LearningCenterVideosFilterModel`

class LearningCenterVideosFilterModel : public mv::[SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#_CPPv4N2mv20SortFilterProxyModelE "mv::SortFilterProxyModel")
:   Learning center videos filter model class.

    Filtering model for the learning center videos model

    **Author**
    :   Thomas Kroes

    Public Functions

    LearningCenterVideosFilterModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    bool filterAcceptsRow(int row, const QModelIndex &parent) const override
    :   Returns whether `row` with `parent` is filtered out (false) or in (true)

        Parameters:
        :   - **row** – Row index
            - **parent** – Parent index

        Returns:
        :   Boolean indicating whether the item is filtered in or out

    void setSourceModel(QAbstractItemModel \*sourceModel) override
    :   Set source model to `sourceModel`.

        Parameters:
        :   **sourceModel** – Pointer to source model

    bool lessThan(const QModelIndex &lhs, const QModelIndex &rhs) const override
    :   Compares two model indices plugin `lhs` with `rhs`.

        Parameters:
        :   - **lhs** – Left-hand model index
            - **rhs** – Right-hand model index
