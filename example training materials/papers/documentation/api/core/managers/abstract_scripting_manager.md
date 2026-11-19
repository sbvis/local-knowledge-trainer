# AbstractScriptingManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_scripting_manager.html

**Documentation path:** `api/core/managers/abstract_scripting_manager.html`

---

# AbstractScriptingManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the scripting manager
mv::scripting()->...
```

## Related

- Scripts [models](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/index.html)

**Qualified name:** `mv::AbstractScriptingManager`

class AbstractScriptingManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract scripting manager class.

    Base abstract scripting manager class

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractScriptingManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual gui::ScriptTriggerActions getScriptTriggerActions(const Datasets &datasets) const = 0
    :   Get script trigger actions for `datasets`.

        Parameters:
        :   **datasets** – Sequence of input datasets (order in which they were selected in the data hierarchy)

        Returns:
        :   Vector of script trigger actions
