# Raw data factory

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/raw_data_factory.html

**Documentation path:** `api/core/data/raw_data_factory.html`

---

# Raw data factory

`plugin::RawDataFactory` creates raw-data plugin instances and identifies them as data plugins in the plugin system.

class RawDataFactory : public mv::plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory")
:   Subclassed by ClusterDataFactory, ColorDataFactory, ImageDataFactory, PointDataFactory, TextDataFactory

    Public Functions

    virtual [RawData](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data.html#_CPPv4N2mv6plugin7RawDataE "mv::plugin::RawData") \*produce() override = 0
    :   Produces the plugin.

        Returns:
        :   Pointer to the produced plugin
