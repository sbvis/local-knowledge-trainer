# LearningCenterTutorialsModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html

**Documentation path:** `api/core/models/learning_center/tutorials/learning_center_tutorials_model.html`

---

# LearningCenterTutorialsModel

**Qualified name:** `mv::LearningCenterTutorialsModel`

class LearningCenterTutorialsModel : public QStandardItemModel
:   Learning center tutorial model class.

    Contains tutorial content for the learning center

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Title

        enumerator Tags

        enumerator Date

        enumerator IconName

        enumerator Summary

        enumerator Content

        enumerator Url

        enumerator ProjectUrl

        enumerator MinimumCoreVersion

        enumerator RequiredPlugins

        enumerator MissingPlugins

        enumerator Count

    Public Functions

    LearningCenterTutorialsModel(QObject \*parent = nullptr)
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

    void addTutorial(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial)
    :   Add `tutorial`.

        Parameters:
        :   **tutorial** – Pointer to tutorial to add

    void updateTags()
    :   Builds a set of all video tags and emits LearningCenterTutorialsModel::tagsChanged(…)

    void synchronizeWithDsns()
    :   Synchronize the model with the data source names.

    void tagsChanged(const QSet<QString> &tags)
    :   Signals that the tags changed to `tags`.

        Parameters:
        :   **tags** – New tags

    Public Static Attributes

    static QMap<[Column](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel6ColumnE "mv::LearningCenterTutorialsModel::Column"), [ColumHeaderInfo](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel15ColumHeaderInfoE "mv::LearningCenterTutorialsModel::ColumHeaderInfo")> columnInfo
    :   Column name and tooltip.

    struct ColumHeaderInfo
    :   Header strings for several data roles.

        Public Members

        QString \_edit
        :   Header string for display role.

        QString \_tooltip
        :   Header string for edit role.

    class ContentItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial summary.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class DateItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial date.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IconNameItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial icon name.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
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
    :   Base standard model item class for tutorial.

        Subclassed by [mv::LearningCenterTutorialsModel::ContentItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1ContentItem), [mv::LearningCenterTutorialsModel::DateItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1DateItem), [mv::LearningCenterTutorialsModel::IconNameItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1IconNameItem), [mv::LearningCenterTutorialsModel::MinimumCoreVersionItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1MinimumCoreVersionItem), [mv::LearningCenterTutorialsModel::MissingPluginsItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1MissingPluginsItem), [mv::LearningCenterTutorialsModel::ProjectUrlItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1ProjectUrlItem), [mv::LearningCenterTutorialsModel::RequiredPluginsItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1RequiredPluginsItem), [mv::LearningCenterTutorialsModel::SummaryItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1SummaryItem), [mv::LearningCenterTutorialsModel::TagsItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1TagsItem), [mv::LearningCenterTutorialsModel::TitleItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1TitleItem), [mv::LearningCenterTutorialsModel::UrlItem](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#classmv_1_1LearningCenterTutorialsModel_1_1UrlItem)

        Public Functions

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   Construct with pointer `tutorial`.

            Parameters:
            :   - **tutorial** – Const pointer to tutorial
                - **editable** – Boolean determining whether the item is editable or not

        const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*getTutorial() const
        :   Get tutorial return Pointer to the tutorial.

    class MinimumCoreVersionItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial minimum application core version.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class MissingPluginsItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying missing plugins.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class ProjectUrlItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial project URL.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class RequiredPluginsItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying required plugins.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
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

        inline Row(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial)
        :   Construct with pointer to `tutorial` object.

            Parameters:
            :   **tutorial** – Pointer to tutorial object

    class SummaryItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial summary.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class TagsItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial tags.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class TitleItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial title.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class UrlItem : public mv::[LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModel4ItemE "mv::LearningCenterTutorialsModel::Item")
    :   Standard model item class for displaying the tutorial URL.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
