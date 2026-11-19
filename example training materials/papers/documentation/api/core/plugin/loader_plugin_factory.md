# LoaderPluginFactory

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin_factory.html

**Documentation path:** `api/core/plugin/loader_plugin_factory.html`

---

# LoaderPluginFactory

**Qualified name:** `mv::plugin::LoaderPluginFactory`

`LoaderPluginFactory` identifies a plugin kind as a loader and narrows `produce()` to return a [LoaderPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin.html). Its standard contextual trigger represents loading an external source and therefore does not depend on the currently selected datasets or data types.

A concrete loader factory still uses the inherited [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html) API for metadata, instance limits, and application integration. Request instances through the plugin manager instead of calling `produce()` directly.

class LoaderPluginFactory : public mv::plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory")
:   Public Functions

    inline void setObjectName(const QString &name)
    :   Set name of the object.

        Parameters:
        :   **name** – Name of the object

    virtual [LoaderPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin.html#_CPPv4N2mv6plugin12LoaderPluginE "mv::plugin::LoaderPlugin") \*produce() override = 0
    :   Produces an instance of a loader plugin.

        This function gets called by the plugin manager.

    virtual gui::PluginTriggerActions getPluginTriggerActions(const mv::Datasets &datasets) const override
    :   Get plugin trigger actions given `datasets`.

        Parameters:
        :   **datasets** – Vector of input datasets

        Returns:
        :   Vector of plugin trigger actions

    virtual gui::PluginTriggerActions getPluginTriggerActions(const mv::DataTypes &dataTypes) const override
    :   Get plugin trigger actions given `dataTypes`.

        Parameters:
        :   **datasetTypes** – Vector of input data types

        Returns:
        :   Vector of plugin trigger actions
