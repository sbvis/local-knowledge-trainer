# HardwareSpec

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html

**Documentation path:** `api/core/util/hardware_spec/hardware_spec.html`

---

# HardwareSpec

**Qualified name:** `mv::util::HardwareSpec`

class HardwareSpec
:   Public Types

    enum class Type
    :   Hardware specification type.

        *Values:*

        enumerator System

        enumerator Minimum
        :   System hardware specification.

        enumerator Recommended
        :   Minimum hardware specification.

            Recommended hardware specification

    enum class SystemCompatibility
    :   Enum for system hardware spec compatibility with other specifications.

        *Values:*

        enumerator Incompatible

        enumerator Minimum
        :   Incompatible with the minimum and recommended hardware specification.

        enumerator Compatible
        :   Compatible with the minimum hardware specification only.

        enumerator Unknown
        :   Compatible with the minimum and recommended hardware specification.

            Unknown compatibility

    Public Functions

    HardwareSpec(const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpec4TypeE "mv::util::HardwareSpec::Type") &type)
    :   Construct with hardware specification `type`.

        Parameters:
        :   **type** – Hardware specification type

    void fromVariantMap(const QVariantMap &variantMap)
    :   Load the hardware spec from `variantMap`.

        Parameters:
        :   **variantMap** – Variant map containing the hardware spec properties

    void fromSystem()
    :   Initialize from system hardware specifications.

    bool isInitialized() const
    :   Get whether the hardware spec has been initialized.

        Returns:
        :   Boolean determining whether the hardware spec has been initialized

    template<class HardwareComponentSpecType> inline std::shared\_ptr<[HardwareComponentSpecType](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4I0ENK2mv4util12HardwareSpec24getHardwareComponentSpecENSt10shared_ptrI25HardwareComponentSpecTypeEERK7QString "mv::util::HardwareSpec::getHardwareComponentSpec::HardwareComponentSpecType")> getHardwareComponentSpec(const QString &name) const
    :   Get the hardware component specification by `name`.

        Parameters:
        :   **name** – Name of the hardware component specification

        Returns:
        :   Hardware component specification with the given name

    HardwareComponentSpecs getHardwareComponentSpecs(bool initializedOnly = true) const
    :   Get the hardware component specifications.

        Parameters:
        :   **initializedOnly** – Whether to only return initialized hardware component specifications

        Returns:
        :   Hardware component specifications

    inline bool operator==(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &other) const
    :   Get whether the hardware specification is equal to the `other` hardware specification.

        Parameters:
        :   **other** – Other hardware specification to compare with

        Returns:
        :   Boolean determining whether the hardware specification is equal to the `other` hardware specification

    inline bool operator!=(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &other) const
    :   Get whether the hardware specification is not equal to the `other` hardware specification.

        Parameters:
        :   **other** – Other hardware specification to compare with

        Returns:
        :   Boolean determining whether the hardware specification is not equal to the `other` hardware specification

    inline bool operator<(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &other) const
    :   Get whether the hardware specification is smaller than the `other` hardware specification.

        Returns:
        :   Boolean determining whether the hardware specification is smaller than the `other` hardware specification

    inline bool operator>(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &other) const
    :   Get whether the hardware specification is larger than the `other` hardware specification.

        Returns:
        :   Boolean determining whether the hardware specification is larger than the `other` hardware specification

    inline bool operator<=(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &other) const
    :   Get whether the hardware specification is equal to or smaller than the `other` hardware specification.

        Parameters:
        :   **other** – Other hardware specification to compare with

        Returns:
        :   Boolean determining whether the hardware specification is equal to or smaller than the `other` hardware specification

    inline bool operator>=(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &other) const
    :   Get whether the hardware specification is equal to or larger than the `other` hardware specification.

        Parameters:
        :   **other** – Other hardware specification to compare with

        Returns:
        :   Boolean determining whether the hardware specification is equal to or larger than the `other` hardware specification

    bool meets(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &required) const
    :   Get whether the hardware specification meets the `required` hardware specification.

        Parameters:
        :   **required** – Hardware spec that is required

        Returns:
        :   Boolean determining whether the hardware specification meets the `required` hardware specification

    QString getFailureString(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &required) const
    :   Get the reason why the hardware component spec does not meet the `required` hardware component spec.

        Parameters:
        :   **required** – Hardware component spec that is required

        Returns:
        :   String containing the reason why the hardware component spec does not meet the required hardware component spec

    Public Static Functions

    static const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &getSystemHardwareSpec()
    :   Get system hardware specification.

        Returns:
        :   System hardware specification

    static void updateSystemHardwareSpecs()
    :   Updates the system hardware specifications.

    static [SystemCompatibilityInfo](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpec23SystemCompatibilityInfoE "mv::util::HardwareSpec::SystemCompatibilityInfo") getSystemCompatibility(const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &minimumHardwareSpec, const [HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &recommendedHardwareSpec)
    :   Get system compatibility with the minimum and recommended hardware specifications.

        Parameters:
        :   - **minimumHardwareSpec** – Minimum hardware specification
            - **recommendedHardwareSpec** – Recommended hardware specification

        Returns:
        :   System compatibility info with the minimum and recommended hardware specifications

    struct SystemCompatibilityInfo
    :   System compatibility information.

        Public Members

        QString \_message
        :   System compatibility.

        QIcon \_icon
        :   Compatibility/incompatibility message.
