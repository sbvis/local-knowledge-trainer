# AbstractHardwareSpecModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/abstract_hardware_spec_model.html

**Documentation path:** `api/core/models/hardware_spec/abstract_hardware_spec_model.html`

---

# AbstractHardwareSpecModel

**Qualified name:** `mv::AbstractHardwareSpecModel`

class AbstractHardwareSpecModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Abstract hardware spec model class.

    Base standard item model for hardware specification.

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::HardwareSpecTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/hardware_spec_tree_model.html#classmv_1_1HardwareSpecTreeModel)

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Title

        enumerator SystemValue
        :   Title of the hardware component (parameter) item.

        enumerator RequiredValue
        :   System value of the hardware component (parameter) item.

        enumerator Count
        :   Required value of the hardware component (parameter) item.

            Number of columns in the model

    Public Functions

    AbstractHardwareSpecModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object
