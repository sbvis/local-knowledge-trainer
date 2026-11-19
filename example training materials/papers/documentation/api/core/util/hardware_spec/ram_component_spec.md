# RamComponentSpec

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/ram_component_spec.html

**Documentation path:** `api/core/util/hardware_spec/ram_component_spec.html`

---

# RamComponentSpec

**Qualified name:** `mv::util::RamComponentSpec`

class RamComponentSpec : public mv::util::[HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec")
:   RAM component spec class.

    For encapsulating a RAM hardware component specification.

    **Author**
    :   Thomas Kroes

    Public Functions

    RamComponentSpec()
    :   Default constructor.

    virtual QString getFailureString(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const override
    :   Get the reason why the RAM component spec does not meet the `required` RAM component spec.

        Parameters:
        :   **required** – RAM component spec that is required

        Returns:
        :   String containing the reason why the RAM component spec does not meet the required RAM component spec

    inline std::uint64\_t getNumberOfBytes() const
    :   Get the amount of available RAM in bytes.

        Returns:
        :   Number of bytes of available RAM

    inline bool operator==(const [RamComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/ram_component_spec.html#_CPPv4N2mv4util16RamComponentSpecE "mv::util::RamComponentSpec") &other) const
    :   Get whether the RAM component specification is equal to the `other` RAM component specification.

        Parameters:
        :   **other** – RAM component specification to compare with

        Returns:
        :   Boolean determining whether the RAM component specification is equal to the `other` RAM component specification

    inline bool operator!=(const [RamComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/ram_component_spec.html#_CPPv4N2mv4util16RamComponentSpecE "mv::util::RamComponentSpec") &other) const
    :   Get whether the RAM component specification is not equal to the `other` RAM component specification.

        Parameters:
        :   **other** – RAM component specification to compare with

        Returns:
        :   Boolean determining whether the RAM component specification is not equal to the `other` RAM component specification

    inline bool operator<(const [RamComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/ram_component_spec.html#_CPPv4N2mv4util16RamComponentSpecE "mv::util::RamComponentSpec") &other) const
    :   Get whether the RAM component specification is smaller than the `other` RAM component specification.

        Returns:
        :   Boolean determining whether the RAM component specification is smaller than the `other` RAM component specification

    inline bool operator>(const [RamComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/ram_component_spec.html#_CPPv4N2mv4util16RamComponentSpecE "mv::util::RamComponentSpec") &other) const
    :   Get whether the RAM component specification is larger than the `other` RAM component specification.

        Returns:
        :   Boolean determining whether the RAM component specification is larger than the `other` RAM component specification

    inline virtual bool lessThan(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const override
    :   Get whether the RAM component specification is smaller than the `other` RAM component specification.

        Parameters:
        :   **other** – RAM component specification to compare with

        Returns:
        :   Boolean determining whether the RAM component specification is smaller than the `other` RAM component specification

    inline virtual bool equals(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const override
    :   Get whether the RAM component specification is equal to the `other` RAM component specification.

        Parameters:
        :   **other** – RAM component specification to compare with

        Returns:
        :   Boolean determining whether the RAM component specification is equal to the `other` RAM component specification

    virtual bool meets(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const override
    :   Get whether the RAM component specification meets the `required` RAM component specification.

        Parameters:
        :   **required** – RAM component spec that is required

        Returns:
        :   Boolean determining whether the RAM component spec meets the required RAM component spec

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
