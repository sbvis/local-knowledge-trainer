# AnalysisPluginFactory

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin_factory.html

**Documentation path:** `api/core/plugin/analysis_plugin_factory.html`

---

# AnalysisPluginFactory

**Qualified name:** `mv::plugin::AnalysisPluginFactory`

`AnalysisPluginFactory` identifies a plugin kind as an analysis and narrows `produce()` to return an [AnalysisPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html). A concrete factory supplies plugin metadata, supported data types, and any dataset-sensitive creation triggers through the inherited [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html) API.

The Core assigns validated input datasets through the managed request path. Do not call `produce()` directly. See [Factory and plugin instance](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/factory_and_instance.html) and [Plugin creation policy](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/index.html).

class AnalysisPluginFactory : public mv::plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory")
:   Public Functions

    virtual [AnalysisPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html#_CPPv4N2mv6plugin14AnalysisPluginE "mv::plugin::AnalysisPlugin") \*produce() override = 0
    :   Produces the plugin.

        Returns:
        :   Pointer to the produced plugin
