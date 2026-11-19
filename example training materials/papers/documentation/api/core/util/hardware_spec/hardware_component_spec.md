# HardwareComponentSpec

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html

**Documentation path:** `api/core/util/hardware_spec/hardware_component_spec.html`

---

# HardwareComponentSpec

**Qualified name:** `mv::util::HardwareComponentSpec`

class HardwareComponentSpec
:   Hardware component specification class Base class for encapsulating a component specification.

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::util::CpuComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/cpu_component_spec.html#classmv_1_1util_1_1CpuComponentSpec), [mv::util::DisplayComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/display_component_spec.html#classmv_1_1util_1_1DisplayComponentSpec), [mv::util::RamComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/ram_component_spec.html#classmv_1_1util_1_1RamComponentSpec), [mv::util::StorageComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/storage_component_spec.html#classmv_1_1util_1_1StorageComponentSpec)

    Public Functions

    HardwareComponentSpec(const QString &title)
    :   Construct with hardware component specification `title`.

        Parameters:
        :   **title** – hardware component specification title

    inline QString getTitle() const
    :   Get the title of the hardware component specification.

        Returns:
        :   String containing the title of the hardware component specification

    virtual void fromVariantMap(const QVariantMap &variantMap)
    :   Load the hardware component spec from `variantMap`.

        Parameters:
        :   **variantMap** – Variant map containing the hardware component spec properties

    virtual QVariantMap toVariantMap() const
    :   Convert the hardware component spec to a variant map.

        Returns:
        :   Variant map containing the hardware component spec properties

    virtual QString getFailureString(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const = 0
    :   Get the reason why the hardware component spec does not meet the `required` hardware component spec.

        Parameters:
        :   **required** – Hardware component spec that is required

        Returns:
        :   String containing the reason why the hardware component spec does not meet the required hardware component spec

    inline bool isInitialized() const
    :   Get whether the hardware component spec has been initialized.

        Returns:
        :   Boolean determining whether the hardware component spec has been initialized

    virtual bool lessThan(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const = 0
    :   Get whether the hardware component specification is smaller than the `other` hardware component specification.

        Parameters:
        :   **other** – Hardware component specification to compare with

        Returns:
        :   Boolean determining whether the hardware component specification is smaller than the `other` hardware component specification

    virtual bool equals(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const = 0
    :   Get whether the hardware component specification is equal to the `other` hardware component specification.

        Parameters:
        :   **other** – Hardware component specification to compare with

        Returns:
        :   Boolean determining whether the hardware component specification is equal to the `other` hardware component specification

    virtual bool meets(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const = 0
    :   Get whether the hardware component specification meets the `required` hardware component specification.

        Parameters:
        :   **required** – Hardware component specification that is required

        Returns:
        :   Boolean determining whether the hardware component spec meets the required hardware component spec

    virtual QStandardItem \*getStandardItem() const
    :   Get standard item.

        Returns:
        :   Pointer to standard item representing the hardware component spec

    Public Static Functions

    static QList<QStandardItem\*> getParameterRow(const QString &parameterName, const QString &systemValue = "", const QString &requiredValue = "", bool valid = true)
    :   Get row representing the hardware component spec parameter.

        Parameters:
        :   - **parameterName** – Name of the parameter
            - **systemValue** – String containing the system value of the parameter
            - **requiredValue** – String containing the required value of the parameter
            - **valid** – Boolean determining whether the parameter condition is valid

        Returns:
        :   List of pointers to standard items representing the parameter

    Protected Functions

    virtual void fromSystem() = 0
    :   Load the hardware component spec from current system.

    inline void setInitialized(bool initialized = true)
    :   Set whether the hardware spec has been initialized to `initialized`.

        Parameters:
        :   **initialized** – Boolean determining whether the hardware spec has been initialized
