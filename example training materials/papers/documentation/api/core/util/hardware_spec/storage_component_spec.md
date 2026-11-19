# StorageComponentSpec

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/storage_component_spec.html

**Documentation path:** `api/core/util/hardware_spec/storage_component_spec.html`

---

# StorageComponentSpec

**Qualified name:** `mv::util::StorageComponentSpec`

class StorageComponentSpec : public mv::util::[HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec")
:   Storage component spec class.

    For encapsulating a storage hardware specification.

    **Author**
    :   Thomas Kroes

    Public Functions

    StorageComponentSpec()
    :   Default constructor.

    virtual QString getFailureString(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const override
    :   Get the reason why the storage component spec does not meet the `required` storage component spec.

        Parameters:
        :   **required** – Storage component spec that is required

        Returns:
        :   String containing the reason why the storage component spec does not meet the required storage component spec

    inline std::uint64\_t getNumberOfBytesAvailableInAppData() const
    :   Get the number of available bytes in app data folder.

        Returns:
        :   Number of bytes of available disk space in app data folder

    inline bool operator==(const [StorageComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/storage_component_spec.html#_CPPv4N2mv4util20StorageComponentSpecE "mv::util::StorageComponentSpec") &other) const
    :   Get whether the storage component specification is equal to the `other` storage component specification.

        Parameters:
        :   **other** – Storage component specification to compare with

        Returns:
        :   Boolean determining whether the storage component specification is equal to the `other` storage component specification

    inline bool operator!=(const [StorageComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/storage_component_spec.html#_CPPv4N2mv4util20StorageComponentSpecE "mv::util::StorageComponentSpec") &other) const
    :   Get whether the storage component specification is not equal to the `other` storage component specification.

        Parameters:
        :   **other** – Storage component specification to compare with

        Returns:
        :   Boolean determining whether the storage component specification is not equal to the `other` storage component specification

    inline bool operator<(const [StorageComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/storage_component_spec.html#_CPPv4N2mv4util20StorageComponentSpecE "mv::util::StorageComponentSpec") &other) const
    :   Get whether the storage component specification is smaller than the `other` storage component specification.

        Returns:
        :   Boolean determining whether the storage component specification is smaller than the `other` storage component specification

    inline bool operator>(const [StorageComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/storage_component_spec.html#_CPPv4N2mv4util20StorageComponentSpecE "mv::util::StorageComponentSpec") &other) const
    :   Get whether the storage component specification is larger than the `other` storage component specification.

        Returns:
        :   Boolean determining whether the storage component specification is larger than the `other` storage component specification

    inline virtual bool lessThan(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const override
    :   Get whether the storage component specification is smaller than the `other` storage component specification.

        Parameters:
        :   **other** – Hardware component specification to compare with

        Returns:
        :   Boolean determining whether the hardware component specification is smaller than the `other` hardware component specification

    inline virtual bool equals(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const override
    :   Get whether the storage component specification is equal to the `other` storage component specification.

        Parameters:
        :   **other** – Storage component specification to compare with

        Returns:
        :   Boolean determining whether the storage component specification is equal to the `other` storage component specification

    virtual bool meets(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const override
    :   Get whether the storage component specification meets the `required` storage component specification.

        Parameters:
        :   **required** – storage component spec that is required

        Returns:
        :   Boolean determining whether the storage component spec meets the required storage component spec

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
