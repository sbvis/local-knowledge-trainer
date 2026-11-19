# AbstractProjectsModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html

**Documentation path:** `api/core/models/projects/abstract_projects_model.html`

---

# AbstractProjectsModel

**Qualified name:** `mv::AbstractProjectsModel`

class AbstractProjectsModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Abstract projects model class.

    Base standard item model for projects.

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::ProjectsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_list_model.html#classmv_1_1ProjectsListModel), [mv::ProjectsTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_tree_model.html#classmv_1_1ProjectsTreeModel)

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Title

        enumerator UUID
        :   Title of the project.

        enumerator IsVisible
        :   Title of the project.

        enumerator LastModified
        :   Whether the project is visible in the model.

        enumerator Downloaded
        :   Last modified date of the project.

        enumerator Group
        :   Whether the project has been downloaded before.

        enumerator IsGroup
        :   Group title of the project.

        enumerator Tags
        :   Whether the item is a project group.

        enumerator Date
        :   Tags of the project.

        enumerator IconName
        :   Date of the project.

        enumerator Summary
        :   Icon name of the project.

        enumerator Url
        :   Summary of the project.

        enumerator MinimumCoreVersion
        :   URL of the project.

        enumerator RequiredPlugins
        :   Minimum ManiVault application core version.

        enumerator MissingPlugins
        :   Required plugins for the project.

        enumerator DownloadSize
        :   Missing plugins for the project.

        enumerator SystemCompatibility
        :   Download size of the ManiVault project.

        enumerator IsStartup
        :   System compatibility of the project.

        enumerator ProjectsJsonDsn
        :   Whether the project can be opened at application startup.

        enumerator Count
        :   Data Source Name (DSN) of the projects JSON file, used for loading the project.

            Number of columns in the model

    Public Functions

    AbstractProjectsModel(const PopulationMode &populationMode = PopulationMode::Automatic, QObject \*parent = nullptr)
    :   Construct with population `mode` and pointer to `parent` object.

        Parameters:
        :   - **populationMode** – Population mode of the model (automatic/manual)
            - **parent** – Pointer to parent object

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    void populateFromJsonByteArray(const QByteArray &jsonByteArray, std::int32\_t dsnIndex, const QString &jsonLocation)
    :   Populate the model from the Data Source Names (DSN)

        Parameters:
        :   - **jsonByteArray** – Byte array containing the JSON data to populate from
            - **dsnIndex** – Index of the DSN to populate from
            - **jsonLocation** – Location of the JSON file

    void populateFromJsonFile(const QString &filePath)
    :   Populate the model from a JSON file at `filePath`.

        Parameters:
        :   **filePath** – Path to the JSON file containing the projects data

    void updateTags()
    :   Builds a set of all project tags and emits ProjectDatabaseModel::tagsChanged(…)

    QSet<QString> getTagsSet() const
    :   Get tags.

        Returns:
        :   All tags

    util::ProjectsModelProjectSharedPtr getProject(const QModelIndex &index) const
    :   Get the project at `index`.

        Returns:
        :   Shared pointer to project at index

    void addProject(util::ProjectsModelProjectSharedPtr project, const QModelIndex &parentIndex = QModelIndex())
    :   Add `project`.

        Parameters:
        :   - **project** – Shared pointer to project to add
            - **parentIndex** – Parent index to add the project to (defaults to root)

    void removeProject(const QModelIndex &index)
    :   Remove project with `index` from the model.

        Parameters:
        :   **index** – Index of the project to remove

    void tagsChanged(const QSet<QString> &tags)
    :   Signals that the tags changed to `tags`.

        Parameters:
        :   **tags** – New tags

    void aboutToBePopulated()
    :   Signals that the model is about to be populated.

    void populated()
    :   Signals that the model has been re-populated.

    Protected Functions

    void beginPopulate()
    :   Begin the population of the model.

    virtual void populate(util::ProjectsModelProjectSharedPtrs projects)
    :   Populate the model with the given projects.

        Parameters:
        :   **projects** – Shared pointers to projects to populate the model with

    void endPopulate()
    :   End the population of the model.

    class DateItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project date.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class DownloadedItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying whether the project has been downloaded before.

        Public Functions

        DownloadedItem(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   Construct with pointer `project`.

            Parameters:
            :   - **project** – Const pointer to project
                - **editable** – Boolean determining whether the item is editable or not

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class DownloadSizeItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the download size.

        Public Functions

        DownloadSizeItem(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   Construct with pointer `project`.

            Parameters:
            :   - **project** – Const pointer to project
                - **editable** – Boolean determining whether the item is editable or not

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class GroupItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project group title.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IconNameItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project icon name.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IsGroupItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying whether the item is a project group.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IsStartupItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying whether the project is a startup project.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class IsVisibleItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project visibility.

        Public Functions

        IsVisibleItem(util::ProjectsModelProjectSharedPtr project)
        :   Construct with pointer `project`.

            Parameters:
            :   - **project** – Const pointer to project
                - **editable** – Boolean determining whether the item is editable or not

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        void setData(const QVariant &value, int role) override
        :   Set model data for `role`.

            Parameters:
            :   - **value** – Data value
                - **role** – Data role

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Item : public QStandardItem, public QObject
    :   Base standard model item class for project.

        Subclassed by [mv::AbstractProjectsModel::DateItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1DateItem), [mv::AbstractProjectsModel::DownloadSizeItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1DownloadSizeItem), [mv::AbstractProjectsModel::DownloadedItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1DownloadedItem), [mv::AbstractProjectsModel::GroupItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1GroupItem), [mv::AbstractProjectsModel::IconNameItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1IconNameItem), [mv::AbstractProjectsModel::IsGroupItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1IsGroupItem), [mv::AbstractProjectsModel::IsStartupItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1IsStartupItem), [mv::AbstractProjectsModel::IsVisibleItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1IsVisibleItem), [mv::AbstractProjectsModel::LastModifiedItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1LastModifiedItem), [mv::AbstractProjectsModel::MinimumCoreVersionItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1MinimumCoreVersionItem), [mv::AbstractProjectsModel::MissingPluginsItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1MissingPluginsItem), [mv::AbstractProjectsModel::ProjectsJsonDsnItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1ProjectsJsonDsnItem), [mv::AbstractProjectsModel::RequiredPluginsItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1RequiredPluginsItem), [mv::AbstractProjectsModel::SummaryItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1SummaryItem), [mv::AbstractProjectsModel::SystemCompatibilityItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1SystemCompatibilityItem), [mv::AbstractProjectsModel::TagsItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1TagsItem), [mv::AbstractProjectsModel::TitleItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1TitleItem), [mv::AbstractProjectsModel::UUIDItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1UUIDItem), [mv::AbstractProjectsModel::UrlItem](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel_1_1UrlItem)

        Public Functions

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   Construct with shared pointer `project`.

            Parameters:
            :   - **project** – Shared pointer to project
                - **editable** – Boolean determining whether the item is editable or not

        util::ProjectsModelProjectSharedPtr getProject() const
        :   Get project return Shared pointer to the project.

    class LastModifiedItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the download size.

        Public Functions

        LastModifiedItem(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   Construct with pointer `project`.

            Parameters:
            :   - **project** – Const pointer to project
                - **editable** – Boolean determining whether the item is editable or not

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class MinimumCoreVersionItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project minimum application core version.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class MissingPluginsItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying missing plugins.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class ProjectsJsonDsnItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying to which projects JSON DSN a row belongs.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class RequiredPluginsItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying required plugins.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
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

        inline Row(util::ProjectsModelProjectSharedPtr project)
        :   Construct with pointer to `project` object.

            Parameters:
            :   **project** – Pointer to project object

    class SummaryItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project summary.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class SystemCompatibilityItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the system compatibility with the project.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class TagsItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project tags.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class TitleItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project title.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class UrlItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project URL.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class UUIDItem : public mv::[AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModelE "mv::AbstractProjectsModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#_CPPv4N2mv21AbstractProjectsModel4ItemE "mv::AbstractProjectsModel::Item")
    :   Standard model item class for displaying the project UUID.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::ProjectsModelProjectSharedPtr project, bool editable = false)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data
