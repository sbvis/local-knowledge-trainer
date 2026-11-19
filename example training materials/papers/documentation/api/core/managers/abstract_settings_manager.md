# AbstractSettingsManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_settings_manager.html

**Documentation path:** `api/core/managers/abstract_settings_manager.html`

---

# AbstractSettingsManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the settings manager reference
mv::settings().getPluginGlobalSettingsGroupAction(...);
```

**Qualified name:** `mv::AbstractSettingsManager`

`AbstractSettingsManager` exposes the application’s built-in settings groups and looks up global settings registered by plugin factories. Plugin-owned groups, defaults, and persistence are described in [Global plugin settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/index.html).

class AbstractSettingsManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract settings manager.

    Base abstract settings manager class for managing global settings

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractSettingsManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void edit() = 0
    :   Opens the settings editor dialog.

    virtual gui::[PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#_CPPv4N2mv3gui31PluginGlobalSettingsGroupActionE "mv::gui::PluginGlobalSettingsGroupAction") \*getPluginGlobalSettingsGroupAction(const QString &kind) = 0
    :   Get plugin global settings for plugin `kind`.

        Parameters:
        :   **kind** – Plugin kind

        Returns:
        :   Pointer to plugin global settings (if available, otherwise returns a nullptr)

    template<typename ActionType> inline [ActionType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_settings_manager.html#_CPPv4I0EN2mv23AbstractSettingsManager34getPluginGlobalSettingsGroupActionEP10ActionTypeRK7QString "mv::AbstractSettingsManager::getPluginGlobalSettingsGroupAction::ActionType") \*getPluginGlobalSettingsGroupAction(const QString &kind)
    :   Get plugin global settings `ActionType` for plugin `kind`.

        Parameters:
        :   **kind** – Plugin kind

        Returns:
        :   Pointer to plugin global settings of `ActionType` (if available, otherwise returns a nullptr)

    virtual gui::[PluginGlobalSettingsGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/plugin_global_settings_group_action.html#_CPPv4N2mv3gui31PluginGlobalSettingsGroupActionE "mv::gui::PluginGlobalSettingsGroupAction") \*getPluginGlobalSettingsGroupAction(const [plugin](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_settings_manager.html#_CPPv4N2mv23AbstractSettingsManager34getPluginGlobalSettingsGroupActionEPKN6plugin6PluginE "mv::AbstractSettingsManager::getPluginGlobalSettingsGroupAction::plugin")::Plugin \*plugin) = 0
    :   Get plugin global settings for `plugin`.

        Parameters:
        :   **plugin** – Pointer to plugin

        Returns:
        :   Pointer to plugin global settings (if available, otherwise returns a nullptr)

    template<typename ActionType> inline [ActionType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_settings_manager.html#_CPPv4I0EN2mv23AbstractSettingsManager34getPluginGlobalSettingsGroupActionEP10ActionTypePKN6plugin6PluginE "mv::AbstractSettingsManager::getPluginGlobalSettingsGroupAction::ActionType") \*getPluginGlobalSettingsGroupAction(const [plugin](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_settings_manager.html#_CPPv4I0EN2mv23AbstractSettingsManager34getPluginGlobalSettingsGroupActionEP10ActionTypePKN6plugin6PluginE "mv::AbstractSettingsManager::getPluginGlobalSettingsGroupAction::plugin")::Plugin \*plugin)
    :   Get plugin global settings of `ActionType` for `plugin`.

        Parameters:
        :   **plugin** – Pointer to plugin

        Returns:
        :   Pointer to plugin global settings of `ActionType` (if available, otherwise returns a nullptr)
