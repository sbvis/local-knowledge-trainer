# TransformationPluginFactory

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin_factory.html

**Documentation path:** `api/core/plugin/transformation_plugin_factory.html`

---

# TransformationPluginFactory

**Qualified name:** `mv::plugin::TransformationPluginFactory`

`TransformationPluginFactory` identifies a plugin kind as a transformation and narrows `produce()` to return a [TransformationPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin.html). Use the inherited [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html) capabilities to declare supported data, construct contextual triggers, and configure creation policy.

Inputs are assigned by the managed plugin request path before instance initialization. `produce()` should only allocate the matching concrete instance; it should not perform the transformation or bypass manager ownership.

class TransformationPluginFactory : public mv::plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory")
:   Transformation plugin factory class.

    **Author**
    :   T. Kroes

    Public Functions

    TransformationPluginFactory()
    :   Default constructor.

    ~TransformationPluginFactory() override = default
    :   Destructor.

    virtual [TransformationPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin.html#_CPPv4N2mv6plugin20TransformationPluginE "mv::plugin::TransformationPlugin") \*produce() override = 0
    :   Produces an instance of a transformation plugin.
