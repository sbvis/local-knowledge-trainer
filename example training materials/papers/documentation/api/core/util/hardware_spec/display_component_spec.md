# DisplayComponentSpec

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/display_component_spec.html

**Documentation path:** `api/core/util/hardware_spec/display_component_spec.html`

---

# DisplayComponentSpec

**Qualified name:** `mv::util::DisplayComponentSpec`

class DisplayComponentSpec : public mv::util::[HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec")
:   Display component spec class.

    For encapsulating a display hardware specification

    **Author**
    :   Thomas Kroes

    Public Functions

    DisplayComponentSpec()
    :   Default constructor.

    virtual QString getFailureString(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const override
    :   Get the reason why the display component spec does not meet the `required` display component spec.

        Parameters:
        :   **required** – Display component spec that is required

        Returns:
        :   String containing the reason why the display component spec does not meet the required display component spec

    [Resolution](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/display_component_spec.html#_CPPv4N2mv4util20DisplayComponentSpec10ResolutionE "mv::util::DisplayComponentSpec::Resolution") getResolution() const
    :   Get the display resolution.

        Returns:
        :   Pair of integers representing the display resolution (width, height)

    inline bool operator==(const [DisplayComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/display_component_spec.html#_CPPv4N2mv4util20DisplayComponentSpecE "mv::util::DisplayComponentSpec") &other) const
    :   Get whether the display component specification is equal to the `other` display component specification.

        Parameters:
        :   **other** – Display component specification to compare with

        Returns:
        :   Boolean determining whether the display component specification is equal to the `other` display component specification

    inline bool operator!=(const [DisplayComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/display_component_spec.html#_CPPv4N2mv4util20DisplayComponentSpecE "mv::util::DisplayComponentSpec") &other) const
    :   Get whether the display component specification is not equal to the `other` display component specification.

        Parameters:
        :   **other** – Display component specification to compare with

        Returns:
        :   Boolean determining whether the display component specification is not equal to the `other` display component specification

    inline bool operator<(const [DisplayComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/display_component_spec.html#_CPPv4N2mv4util20DisplayComponentSpecE "mv::util::DisplayComponentSpec") &other) const
    :   Get whether the display component specification is smaller than the `other` display component spec.

        Returns:
        :   Boolean determining whether the display component specification is smaller than the `other` display component spec

    inline bool operator>(const [DisplayComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/display_component_spec.html#_CPPv4N2mv4util20DisplayComponentSpecE "mv::util::DisplayComponentSpec") &other) const
    :   Get whether the display component specification is larger than the `other` display component spec.

        Returns:
        :   Boolean determining whether the display component specification is larger than the `other` display component spec

    inline virtual bool lessThan(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const override
    :   Get whether the display component specification is smaller than the `other` display component specification.

        Parameters:
        :   **other** – Display component specification to compare with

        Returns:
        :   Boolean determining whether the display component specification is smaller than the `other` display component specification

    inline virtual bool equals(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &other) const override
    :   Get whether the display component specification is equal to the `other` display component specification.

        Parameters:
        :   **other** – Display component specification to compare with

        Returns:
        :   Boolean determining whether the display component specification is equal to the `other` display component specification

    virtual bool meets(const [HardwareComponentSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_component_spec.html#_CPPv4N2mv4util21HardwareComponentSpecE "mv::util::HardwareComponentSpec") &required) const override
    :   Get whether the display component specification meets the `required` display component specification.

        Parameters:
        :   **required** – Display component spec that is required

        Returns:
        :   Boolean determining whether the display component spec meets the required display component spec

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

    struct Resolution
