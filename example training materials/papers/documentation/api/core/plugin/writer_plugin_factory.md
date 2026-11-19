# WriterPluginFactory

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin_factory.html

**Documentation path:** `api/core/plugin/writer_plugin_factory.html`

---

# WriterPluginFactory

**Qualified name:** `mv::plugin::WriterPluginFactory`

`WriterPluginFactory` identifies a plugin kind as a writer and narrows `produce()` to return a [WriterPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin.html). Concrete factories use the common [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html) input declarations and dataset-sensitive triggers to offer export operations for valid selections.

The managed request path assigns the selected datasets and initializes the instance. `produce()` should only allocate the matching writer and must not be called directly by plugin code.

class WriterPluginFactory : public mv::plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory")
:   Public Functions

    ~WriterPluginFactory() override = default
    :   No need for custom destructor.

    inline void setObjectName(const QString &name)
    :   Set name of the object.

        Parameters:
        :   **name** – Name of the object

    virtual [WriterPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin.html#_CPPv4N2mv6plugin12WriterPluginE "mv::plugin::WriterPlugin") \*produce() override = 0
    :   Produces the plugin.

        Returns:
        :   Pointer to the produced plugin
