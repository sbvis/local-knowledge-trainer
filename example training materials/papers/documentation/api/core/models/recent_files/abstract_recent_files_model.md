# AbstractRecentFilesModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html

**Documentation path:** `api/core/models/recent_files/abstract_recent_files_model.html`

---

# AbstractRecentFilesModel

**Qualified name:** `mv::AbstractRecentFilesModel`

class AbstractRecentFilesModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Abstract recent files model class.

    Standard item model storing and manipulating recent file paths.

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::RecentFilesListModel](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/recent_files_list_model.html#classmv_1_1RecentFilesListModel)

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator FilePath

        enumerator DateTime
        :   Location of the recent file.

            Date and time when the file was opened

    Public Functions

    AbstractRecentFilesModel(QObject \*parent, const QString &recentFileType)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **recentFileType** – Type of recent file, e.g. “Project” or “Workspace”

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    util::[RecentFile](https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html#_CPPv4N2mv4util10RecentFileE "mv::util::RecentFile") getRecentFileFromIndex(const QModelIndex &index) const
    :   Get recent file object from `index`.

        Parameters:
        :   **index** – Model index

        Returns:
        :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#classmv_1_1AbstractRecentFilesModel_1_1Item) at `index`

    virtual util::RecentFiles getRecentFiles() const = 0
    :   Get recent files.

        Returns:
        :   List of recent file objects

    inline QString getRecentFileType() const
    :   Get recent file type.

        Returns:
        :   Recent file type, e.g. “Project” or “Workspace”

    QString getSettingsKey() const
    :   Get settings key (Models/<serialization\_name>/<recent\_file\_type>)

        Returns:
        :   Settings key

    void populated()
    :   Signals that the model has been re-populated.

    class DateTimeItem : public mv::[AbstractRecentFilesModel](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#_CPPv4N2mv24AbstractRecentFilesModelE "mv::AbstractRecentFilesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#_CPPv4N2mv24AbstractRecentFilesModel4ItemE "mv::AbstractRecentFilesModel::Item")
    :   Standard model item class for displaying the recent file date and time.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[RecentFile](https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html#_CPPv4N2mv4util10RecentFileE "mv::util::RecentFile") &recentFile)
        :   No need for custom constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class FilePathItem : public mv::[AbstractRecentFilesModel](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#_CPPv4N2mv24AbstractRecentFilesModelE "mv::AbstractRecentFilesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#_CPPv4N2mv24AbstractRecentFilesModel4ItemE "mv::AbstractRecentFilesModel::Item")
    :   Standard model item class for displaying the recent file path.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(const util::[RecentFile](https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html#_CPPv4N2mv4util10RecentFileE "mv::util::RecentFile") &recentFile)
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
    :   Base standard model item class for recent file.

        Subclassed by [mv::AbstractRecentFilesModel::DateTimeItem](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#classmv_1_1AbstractRecentFilesModel_1_1DateTimeItem), [mv::AbstractRecentFilesModel::FilePathItem](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#classmv_1_1AbstractRecentFilesModel_1_1FilePathItem)

        Public Functions

        Item(const util::[RecentFile](https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html#_CPPv4N2mv4util10RecentFileE "mv::util::RecentFile") &recentFile)
        :   Construct with `recentFile`.

            Parameters:
            :   **recentFile** – Recent file object containing file path and date time

        inline util::[RecentFile](https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html#_CPPv4N2mv4util10RecentFileE "mv::util::RecentFile") getRecentFile() const
        :   Get recent file return Recent file object.

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining items in a row.

        Public Functions

        inline Row(const util::[RecentFile](https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html#_CPPv4N2mv4util10RecentFileE "mv::util::RecentFile") &recentFile)
        :   Construct with `recentFile` object.

            Parameters:
            :   **recentFile** – Recent file object containing file path and date time
