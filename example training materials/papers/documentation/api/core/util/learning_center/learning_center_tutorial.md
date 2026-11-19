# LearningCenterTutorial

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html

**Documentation path:** `api/core/util/learning_center/learning_center_tutorial.html`

---

# LearningCenterTutorial

For tutorial feeds, tag association, required plugins, ownership, and asynchronous availability, see [Tutorials and videos](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/tutorials_and_videos.html).

**Qualified name:** `mv::util::LearningCenterTutorial`

class LearningCenterTutorial : public QObject
:   [LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#classmv_1_1util_1_1LearningCenterTutorial) class.

    Contains tutorial information

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit LearningCenterTutorial(const QVariantMap &variantMap)
    :   Construct tutorial from `variantMap`.

        Parameters:
        :   **variantMap** – Variant map containing the tutorial properties

    const QString &getTitle() const
    :   Get title.

        Returns:
        :   Tutorial title

    const QStringList &getTags() const
    :   Get tags.

        Returns:
        :   Tutorial tags

    const QString &getDate() const
    :   Get date.

        Returns:
        :   Issue date

    const QString &getIconName() const
    :   Get icon name.

        Returns:
        :   Font Awesome icon name

    const QString &getSummary() const
    :   Get summary.

        Returns:
        :   Tutorial summary (brief description)

    const QString &getContent() const
    :   Get content.

        Returns:
        :   Full tutorial content in HTML format

    const QUrl &getUrl() const
    :   Get URL.

        Returns:
        :   ManiVault website tutorial URL

    const QUrl &getProjectUrl() const
    :   Get project URL.

        Returns:
        :   Location of the ManiVault tutorial project (if any)

    const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &getMinimumCoreVersion() const
    :   Get minimum supported ManiVault Studio core version.

        Returns:
        :   Minimum supported ManiVault Studio core version

    const QStringList &getRequiredPlugins() const
    :   Get required plugins.

        Returns:
        :   Required plugins

    const QStringList &getMissingPlugins() const
    :   Get missing plugins.

        Returns:
        :   Missing plugins

    bool hasProject() const
    :   Get whether the tutorial has a project.

        Returns:
        :   Boolean determining whether the tutorial has a project

    inline [LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") &operator=(const [LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") &rhs)
    :   Overload assignment operator.

        Parameters:
        :   **rhs** – Right hand side tutorial

        Returns:
        :   Assigned tutorial
