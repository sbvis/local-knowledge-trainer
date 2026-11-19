# Version

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html

**Documentation path:** `api/core/util/internal/version.html`

---

# Version

**Qualified name:** `mv::util::Version`

class Version : public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) class.

    Based on semantic versioning (major, minor and patch version number)

    It alo has optional suffix

    Public Functions

    Version(std::int32\_t major = -1, std::int32\_t minor = -1, std::int32\_t patch = -1, const std::string &suffix = "")
    :   Construct version with `major`, `minor` and `patch` version number and possibly `suffix`.

        Parameters:
        :   - **major** – Major version number
            - **minor** – Minor version number
            - **patch** – Patch version number
            - **suffix** – Suffix e.g. alpha, beta

    Version(const QString &version)
    :   Construct version with `version` string.

        Parameters:
        :   **version** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) string

    void initialize(std::int32\_t major, std::int32\_t minor, std::int32\_t patch, const std::string &suffix = "")
    :   Initialize from `major`, `minor` and `patch` version number and possibly `suffix`.

        Parameters:
        :   - **major** – Major version number
            - **minor** – Minor version number
            - **patch** – Patch version number
            - **suffix** – Suffix e.g. alpha, beta

    void initialize(const QString &version)
    :   Initialize from version string.

        Parameters:
        :   **version** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) string

    bool isValid() const
    :   Get whether the version is valid.

        Returns:
        :   Boolean determining whether the version is valid

    std::string getContext() const
    :   Get context.

        Returns:
        :   [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) context

    void setContext(const std::string &context)
    :   Set version context to `context`.

        Parameters:
        :   **context** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) context

    std::int32\_t getVersionNumber() const
    :   Get expanded version number, e.g.

        40316 for 4.3.16

        Returns:
        :   Expanded version number

    std::string getVersionString() const
    :   Get full version as string, including suffix: Major.Minor.PatchSuffix.

        Returns:
        :   version string

    std::string getShortVersionString() const
    :   Get short version as string: Major.Minor.

        Returns:
        :   version string

    std::int32\_t getMajor() const
    :   Get major version number.

        Returns:
        :   Major version number

    void setMajor(std::int32\_t major)
    :   Set major version number to `major`.

        Parameters:
        :   **major** – Major version number

    std::int32\_t getMinor() const
    :   Get minor version number.

        Returns:
        :   Minor version number

    void setMinor(std::int32\_t minor)
    :   Set minor version number to `minor`.

        Parameters:
        :   **minor** – Minor version number

    std::int32\_t getPatch() const
    :   Get patch version number.

        Returns:
        :   Patch version number

    void setPatch(std::int32\_t patch)
    :   Set patch version number to `minor`.

        Parameters:
        :   **patch** – Patch version number

    std::string getSuffix() const
    :   Get minor version number.

        Returns:
        :   Minor version number

    void setSuffix(const std::string &suffix)
    :   Set minor version number to `minor`.

        Parameters:
        :   **minor** – Minor version number

    inline bool operator>(const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &rhs) const
    :   Determines whether this version is larger than `rhs`.

        Parameters:
        :   **rhs** – Right-hand-side version to compare with

        Returns:
        :   Boolean determining whether this version is larger than `rhs`

    inline bool operator<(const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &rhs) const
    :   Determines whether this version is smaller than `rhs`.

        Parameters:
        :   **rhs** – Right-hand-side version to compare with

        Returns:
        :   Boolean determining whether this version is smaller than `rhs`

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load version from variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the version

    virtual QVariantMap toVariantMap() const override
    :   Save version to variant map.

        Returns:
        :   Variant map representation of the version
