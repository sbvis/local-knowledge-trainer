# CpuComponentSpec

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/cpu_component_spec.html

**Documentation path:** `api/core/util/hardware_spec/cpu_component_spec.html`

---

# CpuComponentSpec

**Qualified name:** `mv::util::CpuComponentSpec`

class CpuComponentSpec : public mv::util::[HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec")
:   CPU component spec class.

    For encapsulating a CPU hardware specification

    **Author**
    :   Thomas Kroes

    Public Functions

    CpuComponentSpec()
    :   Default constructor.

    virtual QString getFailureString(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const override
    :   Get the reason why the CPU component spec does not meet the `required` CPU component spec.

        Parameters:
        :   **required** – CPU component spec that is required

        Returns:
        :   String containing the reason why the CPU component spec does not meet the required CPU component spec

    inline bool operator==(const [CpuComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/cpu_component_spec.html#_CPPv4N2mv4util16CpuComponentSpecE "mv::util::CpuComponentSpec") &other) const
    :   Get whether the CPU component specification is equal to the `other` CPU component specification.

        Parameters:
        :   **other** – CPU component specification to compare with

        Returns:
        :   Boolean determining whether the CPU component specification is equal to the `other` CPU component specification

    inline bool operator!=(const [CpuComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/cpu_component_spec.html#_CPPv4N2mv4util16CpuComponentSpecE "mv::util::CpuComponentSpec") &other) const
    :   Get whether the CPU component specification is not equal to the `other` CPU component specification.

        Parameters:
        :   **other** – CPU component specification to compare with

        Returns:
        :   Boolean determining whether the CPU component specification is not equal to the `other` CPU component specification

    inline bool operator<(const [CpuComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/cpu_component_spec.html#_CPPv4N2mv4util16CpuComponentSpecE "mv::util::CpuComponentSpec") &other) const
    :   Get whether the CPU specification is smaller than the `other` CPU specification.

        Returns:
        :   Boolean determining whether the CPU specification is smaller than the `other` CPU specification

    inline bool operator>(const [CpuComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/cpu_component_spec.html#_CPPv4N2mv4util16CpuComponentSpecE "mv::util::CpuComponentSpec") &other) const
    :   Get whether the CPU specification is larger than the `other` CPU specification.

        Returns:
        :   Boolean determining whether the CPU specification is larger than the `other` CPU specification

    inline virtual bool lessThan(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const override
    :   Get whether the CPU component specification is smaller than the `other` CPU component specification.

        Parameters:
        :   **other** – CPU component specification to compare with

        Returns:
        :   Boolean determining whether the CPU component specification is smaller than the `other` CPU component specification

    inline virtual bool equals(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const override
    :   Get whether the CPU component specification is equal to the `other` CPU component specification.

        Parameters:
        :   **other** – CPU component specification to compare with

        Returns:
        :   Boolean determining whether the CPU component specification is equal to the `other` CPU component specification

    virtual bool meets(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const override
    :   Get whether the CPU component specification meets the `required` CPU component specification.

        Parameters:
        :   **required** – CPU component spec that is required

        Returns:
        :   Boolean determining whether the CPU component spec meets the required CPU component spec

    virtual QStandardItem \*getStandardItem() const override
    :   Get standard item.

        Returns:
        :   Pointer to standard item representing the hardware component spec

    Protected Functions

    virtual void fromSystem() override
    :   Load the hardware spec from current system.

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load the hardware spec from `variantMap`.

        Parameters:
        :   **variantMap** – Variant map containing the hardware spec properties
