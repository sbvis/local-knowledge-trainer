# WriterPlugin

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin.html

**Documentation path:** `api/core/plugin/writer_plugin.html`

---

# WriterPlugin

**Qualified name:** `mv::plugin::WriterPlugin`

A writer plugin exports one or more ManiVault datasets through `writeData()`. The managed creation path assigns its ordered input dataset selection before initialization.

Pair a writer instance with a [WriterPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin_factory.html). The factory advertises broad input support and contextual creation triggers through the common [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html) API.

class WriterPlugin : public mv::plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")
:   Public Functions

    WriterPlugin(const [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*factory)
    :   Construct with pointer to plugin factory.

        Parameters:
        :   **factory** – Pointer to plugin factory

    ~WriterPlugin() override = default
    :   No need for custom destructor.

    void setInputDataset(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &inputDataset)
    :   Set input dataset smart pointer.

        Parameters:
        :   **inputDataset** – Smart pointer to input dataset

    void setInputDatasets(const Datasets &inputDatasets)
    :   Set input datasets smart pointers.

        Parameters:
        :   **inputDatasets** – Vector of smart pointers to the input datasets

    template<typename DatasetType = [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin.html#_CPPv4I0EN2mv6plugin12WriterPlugin15getInputDatasetE7DatasetI11DatasetTypeEv "mv::plugin::WriterPlugin::getInputDataset::DatasetType")> getInputDataset()
    :   Get input dataset smart pointer.

    inline Datasets getInputDatasets()
    :   Get input dataset smart pointer vector.
