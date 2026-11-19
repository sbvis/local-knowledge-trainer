# HardwareSpecTreeModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/hardware_spec_tree_model.html

**Documentation path:** `api/core/models/hardware_spec/hardware_spec_tree_model.html`

---

# HardwareSpecTreeModel

**Qualified name:** `mv::HardwareSpecTreeModel`

class HardwareSpecTreeModel : public mv::[AbstractHardwareSpecModel](https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/abstract_hardware_spec_model.html#_CPPv4N2mv25AbstractHardwareSpecModelE "mv::AbstractHardwareSpecModel")
:   Hardware specs tree model class.

    Contains hardware specifications in a tree model.

    **Author**
    :   Thomas Kroes

    Public Functions

    HardwareSpecTreeModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    void setHardwareSpec(const util::[HardwareSpec](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") &hardwareSpec)
    :   Set the hardware specification to be displayed in the model.

        Parameters:
        :   **hardwareSpec** – The hardware specification to set
