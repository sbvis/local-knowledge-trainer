# ProjectsModelProject

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_model_project.html

**Documentation path:** `api/core/models/projects/projects_model_project.html`

---

# ProjectsModelProject

**Qualified name:** `mv::util::ProjectsModelProject`

class ProjectsModelProject : public QObject
:   Projects model project class.

    Contains project information which is used in the project models

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit ProjectsModelProject(const QVariantMap &variantMap)
    :   Construct project from `variantMap`.

        Parameters:
        :   **variantMap** – Variant map containing the project properties

    explicit ProjectsModelProject(const QString &groupTitle)
    :   Construct project group from `groupTitle`.

        Parameters:
        :   **groupTitle** – [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) group title

    QString getTitle() const
    :   Get title.

        Returns:
        :   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) title

    QString getUUID() const
    :   Get UUID.

        Returns:
        :   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) UUID

    bool getVisible() const
    :   Get visible.

        Returns:
        :   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) visible state

    void setVisible(bool visible)
    :   Set visible to `visible`.

        Parameters:
        :   **visible** – [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) visible state

    QString getTooltip() const
    :   Get tooltip.

        Returns:
        :   Tooltip containing the title and summary

    QDateTime getServerLastModified() const
    :   Get server last modified date.

        Returns:
        :   Server last modified date

    std::int64\_t getServerDownloadSize() const
    :   Get server download size.

        Returns:
        :   Server download size of the project in bytes

    std::int64\_t getUserSpecifiedDownloadSize() const
    :   Get user-specified download size (as specified in the JSON file)

        Returns:
        :   User-specified download size of the project in bytes

    std::int64\_t getDownloadSize() const
    :   Get download size (returns user-specified download size if available and server download size otherwise)

        Returns:
        :   Download size of the project in bytes

    QString getDownloadSizeHumanReadable() const
    :   Get human-readable download size.

        Returns:
        :   Human-readable download size of the project in bytes

    bool isDownloaded() const
    :   Get whether project has been downloaded before.

        Returns:
        :   Boolean determining whether project has been downloaded before

    bool isDownloadedProjectStale() const
    :   Get whether the downloaded project is stale (if there is any)

        Returns:
        :   Boolean determining whether the downloaded project is stale

    bool requiresDownload() const
    :   Get whether the project requires download.

        Returns:
        :   Boolean determining whether the project requires download

    void setDownloaded()
    :   Flag the project as downloaded.

    bool isGroup() const
    :   Get whether this is a group.

        Returns:
        :   Boolean determining whether this is a group or a project

    QString getGroup() const
    :   Get group.

        Returns:
        :   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) group

    QStringList getTags() const
    :   Get tags.

        Returns:
        :   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) tags

    QString getDate() const
    :   Get date.

        Returns:
        :   Issue date

    QString getIconName() const
    :   Get icon name.

        Returns:
        :   Font Awesome icon name

    QString getSummary() const
    :   Get summary.

        Returns:
        :   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) summary (brief description)

    QUrl getUrl() const
    :   Get URL.

        Returns:
        :   ManiVault website project URL

    [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") getMinimumCoreVersion() const
    :   Get minimum supported ManiVault Studio core version.

        Returns:
        :   Minimum supported ManiVault Studio core version

    QStringList getRequiredPlugins() const
    :   Get required plugins.

        Returns:
        :   Required plugins

    QStringList getMissingPlugins() const
    :   Get missing plugins.

        Returns:
        :   Missing plugins

    [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") getMinimumHardwareSpec() const
    :   Get minimum hardware specification.

        Returns:
        :   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) minimum hardware specification

    [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") getRecommendedHardwareSpec() const
    :   Get recommended hardware specification.

        Returns:
        :   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) recommended hardware specification

    bool isStartup() const
    :   Get whether this is a startup project.

        Returns:
        :   Boolean determining whether this is a startup project

    QUrl getProjectsJsonDsn() const
    :   Get url of the projects JSON file DSN.

        Returns:
        :   Data Source Name (DSN) of the projects JSON file, used for loading the project

    void setProjectsJsonDsn(const QUrl &projectsJsonDsn)
    :   Set project DSN to `projectsJsonDsn`.

        Parameters:
        :   **projectsJsonDsn** – Projects JSON Data Source Name (DSN) URL

    bool isExpanded() const
    :   Get whether the project is expanded in the model.

        Returns:
        :   Boolean determining whether the project is expanded in the model

    void setExpanded(bool expanded)
    :   Set whether the project is expanded in the model to `expanded`.

        Parameters:
        :   **expanded** – Boolean determining whether the project is expanded in the model

    void updateMetadata()
    :   Determines project metadata like last modified date and download size.

    QIcon getIcon() const
    :   Get icon for the project.

        Returns:
        :   Icon for the project

    QString getDownloadedProjectFilePath() const
    :   Get the file path where the project has been downloaded to.

        Returns:
        :   File path of the downloaded project file

    QString getDownloadFileName() const
    :   Get the download file name.

        Returns:
        :   Download file name

    inline [ProjectsModelProject](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_model_project.html#_CPPv4N2mv4util20ProjectsModelProjectE "mv::util::ProjectsModelProject") &operator=(const [ProjectsModelProject](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_model_project.html#_CPPv4N2mv4util20ProjectsModelProjectE "mv::util::ProjectsModelProject") &rhs)
    :   Overload assignment operator.

        Parameters:
        :   **rhs** – Right hand side project

        Returns:
        :   Assigned project

    inline bool operator==(const [ProjectsModelProject](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_model_project.html#_CPPv4N2mv4util20ProjectsModelProjectE "mv::util::ProjectsModelProject") &other) const
    :   Get whether the project is equal to the `other` project.

        Parameters:
        :   **other** – [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) to compare with

        Returns:
        :   Boolean determining whether the project is equal to the `other` project

    void downloadSizeDetermined(std::uint64\_t size)
    :   Signals that the download size has been determined.

        Parameters:
        :   **size** – Download size in bytes

    void lastModifiedDetermined(const QDateTime &lastModified)
    :   Signals that the last modified date has been determined.

        Parameters:
        :   **lastModified** – Last modified date in milliseconds since epoch

    void downloaded()
    :   Signals that the project has been downloaded.

    void iconChanged(const QIcon &icon)
    :   Signals that the project icon has changed.

        Parameters:
        :   **icon** – New project icon

    void tooltipChanged(const QString &tooltip)
    :   Signals that the project tooltip has changed to `tooltip`.

        Parameters:
        :   **tooltip** – New project tooltip

    void visibilityChanged(bool visible)
    :   Signals that the project visibility has changed to `visible`.

        Parameters:
        :   **visible** – New project visibility
