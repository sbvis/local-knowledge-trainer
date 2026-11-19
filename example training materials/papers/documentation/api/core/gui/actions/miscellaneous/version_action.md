# VersionAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/version_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/version_action.html`

---

# VersionAction

**Qualified name:** `mv::gui::VersionAction`

class VersionAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   Version action class.

    For interaction with a semantic version

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE VersionAction(QObject \*parent, const QString &title)
    :   Construct with `parent` and `project`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    std::int32\_t getMajor() const
    :   Get major version number.

        Returns:
        :   Major version number

    std::int32\_t getMinor() const
    :   Get minor version number.

        Returns:
        :   Minor version number

    std::int32\_t getPatch() const
    :   Get patch version number.

        Returns:
        :   Patch version number

    QString getSuffix() const
    :   Get version suffix string.

        Returns:
        :   Version suffix string

    util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") getVersion() const
    :   Get version.

        Returns:
        :   Version

    void setVersion(const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &version)
    :   Set version to `version`.

        Parameters:
        :   **version** – Version

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load version action from variant.

        Parameters:
        :   **variantMap** – Variant representation of the project

    virtual QVariantMap toVariantMap() const override
    :   Save project to variant.

        Returns:
        :   Variant representation of the project

    void versionChanged(const util::[Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &version)
    :   Signals that the version changed to `version`.

        Parameters:
        :   **version** – Changed version
