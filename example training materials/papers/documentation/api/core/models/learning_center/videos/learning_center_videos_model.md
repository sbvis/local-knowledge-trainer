# LearningCenterVideosModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html

**Documentation path:** `api/core/models/learning_center/videos/learning_center_videos_model.html`

---

# LearningCenterVideosModel

**Qualified name:** `mv::LearningCenterVideosModel`

class LearningCenterVideosModel : public QStandardItemModel
:   Learning center videos model class.

    Contains video content for the learning center

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Type

        enumerator Title

        enumerator Tags

        enumerator Date

        enumerator Summary

        enumerator Resource

        enumerator Thumbnail

        enumerator Delegate

        enumerator Count

    Public Functions

    LearningCenterVideosModel(QObject \*parent = nullptr)
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

    QSet<QString> getTagsSet() const
    :   Get tags.

        Returns:
        :   All tags

    void addVideo(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video)
    :   Add `video`.

        Parameters:
        :   **video** – Pointer to video to add

    void updateTags()
    :   Builds a set of all video tags and emits LearningCenterVideosModel::tagsChanged(…)

    void tagsChanged(const QSet<QString> &tags)
    :   Signals that the tags changed to `tags`.

        Parameters:
        :   **tags** – New tags

    Public Static Attributes

    static QMap<[Column](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel6ColumnE "mv::LearningCenterVideosModel::Column"), [ColumHeaderInfo](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel15ColumHeaderInfoE "mv::LearningCenterVideosModel::ColumHeaderInfo")> columnInfo
    :   Column name and tooltip.

    struct ColumHeaderInfo
    :   Header strings for several data roles.

        Public Members

        QString \_edit
        :   Header string for display role.

        QString \_tooltip
        :   Header string for edit role.

    class DateItem : public mv::[LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel4ItemE "mv::LearningCenterVideosModel::Item")
    :   Standard model item class for displaying the video date.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class DelegateItem : public mv::[LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel4ItemE "mv::LearningCenterVideosModel::Item")
    :   Standard model item class for displaying the video delegate.

        Public Functions

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Item : public QStandardItem
    :   Base standard model item class for video.

        Subclassed by [mv::LearningCenterVideosModel::DateItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#classmv_1_1LearningCenterVideosModel_1_1DateItem), [mv::LearningCenterVideosModel::DelegateItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#classmv_1_1LearningCenterVideosModel_1_1DelegateItem), [mv::LearningCenterVideosModel::ResourceItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#classmv_1_1LearningCenterVideosModel_1_1ResourceItem), [mv::LearningCenterVideosModel::SummaryItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#classmv_1_1LearningCenterVideosModel_1_1SummaryItem), [mv::LearningCenterVideosModel::TagsItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#classmv_1_1LearningCenterVideosModel_1_1TagsItem), [mv::LearningCenterVideosModel::ThumbnailItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#classmv_1_1LearningCenterVideosModel_1_1ThumbnailItem), [mv::LearningCenterVideosModel::TitleItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#classmv_1_1LearningCenterVideosModel_1_1TitleItem), [mv::LearningCenterVideosModel::TypeItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#classmv_1_1LearningCenterVideosModel_1_1TypeItem)

        Public Functions

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   Construct with pointer `video`.

            Parameters:
            :   - **video** – Const pointer to video object
                - **editable** – Boolean determining whether the item is editable or not

        const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*getVideo() const
        :   Get video return Pointer to the video.

    class ResourceItem : public mv::[LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel4ItemE "mv::LearningCenterVideosModel::Item")
    :   Standard model item class for displaying the video resource.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   No need for custom constructor.

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

        inline Row(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video)
        :   Construct with pointer to `video` object.

            Parameters:
            :   **video** – Pointer to video object

    class SummaryItem : public mv::[LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel4ItemE "mv::LearningCenterVideosModel::Item")
    :   Standard model item class for displaying the video summary.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class TagsItem : public mv::[LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel4ItemE "mv::LearningCenterVideosModel::Item")
    :   Standard model item class for displaying the video tags.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class ThumbnailItem : public mv::[LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel4ItemE "mv::LearningCenterVideosModel::Item")
    :   Standard model item class for displaying the video thumbnail.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class TitleItem : public mv::[LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel4ItemE "mv::LearningCenterVideosModel::Item")
    :   Standard model item class for displaying the video title.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class TypeItem : public mv::[LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModel4ItemE "mv::LearningCenterVideosModel::Item")
    :   Standard model item class for displaying the video type.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
