# Hardware Specs

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/index.html

**Documentation path:** `api/core/models/hardware_spec/index.html`

---

# Hardware Specs

A [`mv::util::HardwareSpec`](https://manivault.readthedocs.io/en/latest/api/core/util/hardware_spec/hardware_spec.html#_CPPv4N2mv4util12HardwareSpecE "mv::util::HardwareSpec") is used by **ManiVault** to describe the system requirements of a project, including CPU capabilities, available memory, and disk capacity.

This specification can be extended to define both minimum and recommended hardware requirements. When a project is loaded, ManiVault can evaluate the current system against these requirements and notify the user if the available hardware does not meet the minimum specification, or if it falls below the recommended level.

The model classes below are for storing and filtering hardware specs.

- [AbstractHardwareSpecModel](https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/abstract_hardware_spec_model.html)
- [HardwareSpecTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/hardware_spec_tree_model.html)
- [HardwareSpecFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/hardware_spec_filter_model.html)
