# PluginMetadata

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html

**Documentation path:** `api/core/plugin/plugin_metadata.html`

---

# PluginMetadata

This container holds the user-facing metadata supplied by a plugin factory, including its description, summary, authors and affiliations, copyright, license, and shortcut map. For its relationship to `PluginInfo.json`, Qt metadata, and CMake packaging, see [Metadata and build integration](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/metadata_and_build.html). For about, README, repository, and help integration, see [Help and metadata](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/help_and_metadata.html).

**Qualified name:** `mv::plugin::PluginMetadata`

class PluginMetadata : public QObject
:   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) metadata plugin class.

    Contains plugin properties

    **Author**
    :   T. Kroes

    Public Functions

    PluginMetadata(const [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") &pluginFactory)
    :   Construct with reference to parent `pluginFactory`.

        Parameters:
        :   **pluginFactory** – Reference to parent plugin factory

    QString getGuiName() const
    :   Get the menu name of the plugin.

    void setGuiName(const QString &guiName)
    :   Set the GUI name of the plugin.

        Parameters:
        :   **guiName** – GUI name of the plugin

    util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &getVersion()
    :   Get plugin version.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) semantic version

    const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &getVersion() const
    :   Get plugin version.

        Returns:
        :   [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) semantic version

    void setVersion(const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &version)
    :   Set the plugin version to `version`.

        Parameters:
        :   **version** – [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#classmv_1_1plugin_1_1Plugin) semantic version

    QString getDescription() const
    :   Get description.

        Returns:
        :   String that shortly describes the plugin

    void setDescription(const QString &description)
    :   Set description to `description`.

        Parameters:
        :   **description** – String that shortly describes the plugin

    bool hasDescription() const
    :   Get whether the plugin has a description or not.

        Returns:
        :   Boolean determining whether the plugin has a description or not

    QString getSummary() const
    :   Get summary.

        Returns:
        :   Elaborate description of the plugin

    void setSummary(const QString &summary)
    :   Set summary to `summary`.

        Parameters:
        :   **summary** – Elaborate description of the plugin

    bool hasSummary() const
    :   Get whether the plugin has a summary or not.

        Returns:
        :   Boolean determining whether the plugin has a summary or not

    Authors getAuthors() const
    :   Get authors.

        Returns:
        :   Authors that created and maintain the plugin

    void setAuthors(const Authors &authors)
    :   Set authors to `authors`.

        Parameters:
        :   **authors** – Authors that created and maintain the plugin

    bool hasAuthors() const
    :   Get whether the plugin has authors assigned or not.

        Returns:
        :   Boolean determining whether the plugin has authors assigned or not

    Organizations getOrganizations() const
    :   Get organizations.

        Returns:
        :   Organizations that created and maintain the plugin

    void setOrganizations(const Organizations &organizations)
    :   Set organizations to `organizations`.

        Parameters:
        :   **organizations** – Organizations that created and maintain the plugin

    bool hasOrganizations() const
    :   Get whether the plugin has organizations assigned or not.

        Returns:
        :   Boolean determining whether the plugin has organizations assigned or not

    QString getCopyrightHolder() const
    :   Get copyright holder.

        Returns:
        :   Copyright holder

    void setCopyrightHolder(const QString &copyrightHolder)
    :   Set copyright holder to `copyrightHolder`.

        Parameters:
        :   **copyrightHolder** – Copyright holder

    bool hasCopyrightHolder() const
    :   Get whether the plugin has a copyright holder or not.

        Returns:
        :   Boolean determining whether the plugin has a copyright holder or not

    QString getLicenseText() const
    :   Get license text.

        Returns:
        :   License text

    void setLicenseText(const QString &licenseText)
    :   Set license text to `licenseText`.

        Parameters:
        :   **licenseText** – License text

    bool hasLicenseText() const
    :   Get whether the plugin has a license text or not.

        Returns:
        :   Boolean determining whether the plugin has a license text or not

    ThirdPartyLicenses getThirdPartyLicenses() const
    :   Get third-party dependency licenses.

        Returns:
        :   Third-party dependency licenses used by the plugin

    void setThirdPartyLicenses(const ThirdPartyLicenses &thirdPartyLicenses)
    :   Set third-party dependency licenses.

        Parameters:
        :   **thirdPartyLicenses** – Third-party dependency licenses used by the plugin

    void addThirdPartyLicense(const ThirdPartyLicense &thirdPartyLicense)
    :   Add a third-party dependency license.

        Parameters:
        :   **thirdPartyLicense** – Third-party dependency license to add

    bool removeThirdPartyLicense(const ThirdPartyLicense &thirdPartyLicense)
    :   Remove a third-party dependency license.

        Parameters:
        :   **thirdPartyLicense** – Third-party dependency license to remove

        Returns:
        :   Whether a matching license was removed

    bool hasThirdPartyLicenses() const
    :   Get whether the plugin has third-party dependency licenses.

        Returns:
        :   Boolean determining whether third-party dependency licenses are available

    QString getAboutMarkdown() const
    :   Get about text in Markdown format.

        Returns:
        :   About text in Markdown format. When set, it overrides the standardized about Markdown generated from summary, authors and copyright notice.

    void setAboutMarkdown(const QString &aboutMarkdown)
    :   Set about text to `aboutMarkdown`.

        Parameters:
        :   **aboutMarkdown** – About text in Markdown format. When set, it overrides the standardized about Markdown generated from summary, authors and copyright notice.

    bool hasAboutMarkdown() const
    :   Get whether the plugin has about Markdown or not.

        Returns:
        :   Boolean determining whether the plugin has about Markdown or not

    util::[ShortcutMap](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMapE "mv::util::ShortcutMap") &getShortcutMap()
    :   Get shortcut map.

        Returns:
        :   Reference to the shortcut map

    const util::[ShortcutMap](https://manivault.readthedocs.io/en/latest/api/core/util/shortcut_map/shortcut_map.html#_CPPv4N2mv4util11ShortcutMapE "mv::util::ShortcutMap") &getShortcutMap() const
    :   Get shortcut map.

        Returns:
        :   Const reference to the shortcut map

    void guiNameChanged(const QString &previousGuiName, const QString &currentGuiName)
    :   Signals that the plugin GUI name changed from `previousGuiName` to `currentGuiName`.

        Parameters:
        :   - **previousGuiName** – Previous GUI name
            - **currentGuiName** – Current GUI name

    void versionChanged(const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &previousVersion, const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &currentVersion)
    :   Signals that the version changed from `previousVersion` to `currentVersion`.

        Parameters:
        :   - **previousVersion** – Previous version
            - **currentVersion** – Current version

    void descriptionChanged(const QString &previousDescription, const QString &currentDescription)
    :   Signals that the description changed from `previousDescription` to `currentDescription`.

        Parameters:
        :   - **previousDescription** – Previous description
            - **currentDescription** – Current description

    void summaryChanged(const QString &previousSummary, const QString &currentSummary)
    :   Signals that the summary changed from `previousSummary` to `currentSummary`.

        Parameters:
        :   - **previousSummary** – Previous summary
            - **currentSummary** – Current summary

    void authorsChanged(const Authors &previousAuthors, const Authors &currentAuthors)
    :   Signals that the authors changed from `previousAuthors` to `currentAuthors`.

        Parameters:
        :   - **previousAuthors** – Previous authors
            - **currentAuthors** – Current authors

    void organizationsChanged(const Organizations &previousOrganizations, const Organizations &currentOrganizations)
    :   Signals that the organizations changed from `previousOrganizations` to `currentOrganizations`.

        Parameters:
        :   - **previousOrganizations** – Previous organizations
            - **currentOrganizations** – Current organizations

    void copyrightHolderChanged(const QString &previousCopyrightHolder, const QString &currentCopyrightHolder)
    :   Signals that the copyright holder changed from `previousCopyrightHolder` to `currentCopyrightHolder`.

        Parameters:
        :   - **previousCopyrightHolder** – Previous copyright holder
            - **currentCopyrightHolder** – Current copyright holder

    void licenseTextChanged(const QString &previousLicenseText, const QString &currentLicenseText)
    :   Signals that the license text changed from `previousLicenseText` to `currentLicenseText`.

        Parameters:
        :   - **previousLicenseText** – Previous license text
            - **currentLicenseText** – Current license text

    void thirdPartyLicensesChanged(const ThirdPartyLicenses &previousThirdPartyLicenses, const ThirdPartyLicenses &currentThirdPartyLicenses)
    :   Signals that the third-party dependency licenses changed.

        Parameters:
        :   - **previousThirdPartyLicenses** – Previous third-party dependency licenses
            - **currentThirdPartyLicenses** – Current third-party dependency licenses

    void aboutMarkdownChanged(const QString &previousAboutMarkdown, const QString &currentAboutMarkdown)
    :   Signals that the about text in Markdown format changed from `previousAboutMarkdown` to `currentAboutMarkdown`.

        Parameters:
        :   - **previousAboutMarkdown** – Previous about text in Markdown format
            - **currentAboutMarkdown** – Current about text in Markdown format

    struct Author : protected mv::plugin::[PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadataE "mv::plugin::PluginMetadata")::[FormattedItem](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadata13FormattedItemE "mv::plugin::PluginMetadata::FormattedItem")
    :   [Author](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#structmv_1_1plugin_1_1PluginMetadata_1_1Author) formatted item for use in auto-generated about Markdown.

        Public Functions

        inline Author(const QString &name, const QStringList &roles = QStringList(), const QStringList &organizationNames = QStringList(), const QString &externalLink = QString())
        :   Construct with `name`, `description`, `externalLink` and `organizations`.

            Parameters:
            :   - **name** – Item name
                - **roles** – Assumed roles
                - **organizationNames** – Names of the affiliated organizations
                - **externalLink** – External link (e.g. profile website or e-mail address)

        inline QString toString(const Organizations &organizations) const
        :   Convert to string.

            Parameters:
            :   **organizations** – Organizations list

            Returns:
            :   Markdown formatted string

        inline bool operator==(const [Author](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadata6AuthorE "mv::plugin::PluginMetadata::Author") &rhs) const
        :   Equality operator.

            Parameters:
            :   **rhs** – Right-hand-side author

            Returns:
            :   Whether this author and `rhs` author are the same

        inline bool operator!=(const [Author](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadata6AuthorE "mv::plugin::PluginMetadata::Author") &rhs) const
        :   Inequality operator.

            Parameters:
            :   **rhs** – Right-hand-side author

            Returns:
            :   Whether this author and `rhs` author are not the same

        Public Members

        QStringList \_roles
        :   Affiliated organizations.

    struct FormattedItem
    :   Formatted item for use in auto-generated about Markdown.

        Subclassed by [mv::plugin::PluginMetadata::Author](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#structmv_1_1plugin_1_1PluginMetadata_1_1Author), [mv::plugin::PluginMetadata::Organization](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#structmv_1_1plugin_1_1PluginMetadata_1_1Organization)

        Public Functions

        inline FormattedItem(const QString &name, const QString &description, const QString &externalLink)
        :   Construct with `name`, `description` and `externalLink`.

            Parameters:
            :   - **name** – Item name
                - **description** – Item description
                - **externalLink** – External link

        inline QString toString() const
        :   Convert to string.

            Returns:
            :   Markdown formatted string

        inline bool operator==(const [FormattedItem](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadata13FormattedItemE "mv::plugin::PluginMetadata::FormattedItem") &rhs) const
        :   Equality operator.

            Parameters:
            :   **rhs** – Right-hand-side formatted item

            Returns:
            :   Whether this formatted item and `rhs` formatted item are the same

        inline bool operator!=(const [FormattedItem](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadata13FormattedItemE "mv::plugin::PluginMetadata::FormattedItem") &rhs) const
        :   Inequality operator.

            Parameters:
            :   **rhs** – Right-hand-side formatted item

            Returns:
            :   Whether this formatted item and `rhs` formatted item are not the same

        Public Members

        QString \_description
        :   Item name.

        QString \_externalLink
        :   Item description.

    struct Organization : public mv::plugin::[PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadataE "mv::plugin::PluginMetadata")::[FormattedItem](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadata13FormattedItemE "mv::plugin::PluginMetadata::FormattedItem")
    :   [Organization](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#structmv_1_1plugin_1_1PluginMetadata_1_1Organization) formatted item for use in auto-generated about Markdown.

        Public Functions

        inline QString toString(std::int32\_t index) const
        :   Convert to string.

            Returns:
            :   Markdown formatted string

        inline FormattedItem(const QString &name, const QString &description, const QString &externalLink)
        :   No need for custom constructor.
