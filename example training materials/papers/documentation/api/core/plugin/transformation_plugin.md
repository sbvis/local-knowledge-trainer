# TransformationPlugin

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin.html

**Documentation path:** `api/core/plugin/transformation_plugin.html`

---

# TransformationPlugin

**Qualified name:** `mv::plugin::TransformationPlugin`

A transformation plugin performs a focused transformation over one or more input datasets through `transform()`. The managed creation path assigns its input datasets before initialization.

Pair a transformation instance with a [TransformationPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin_factory.html). See [Choosing a plugin type](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/choosing_a_type.html) for the boundary between transformations and larger analyses.

class TransformationPlugin : public mv::plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")
:   Transformation plugin base class.

    **Author**
    :   T. Kroes

    Public Functions

    TransformationPlugin(const [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*factory)
    :   Constructor.

        Parameters:
        :   **factory** – Pointer to transformation plugin factory

    virtual void transform() = 0
    :   Performs the data transformation.

    Datasets getInputDatasets() const
    :   Get input datasets.

        Returns:
        :   Input datasets

    template<typename DatasetType = [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin.html#_CPPv4I0EN2mv6plugin20TransformationPlugin15getInputDatasetE7DatasetI11DatasetTypeEv "mv::plugin::TransformationPlugin::getInputDataset::DatasetType")> getInputDataset()
    :   Get first input dataset.

        Returns:
        :   First input dataset

    void setInputDatasets(const Datasets &inputDatasets)
    :   Set input datasets @inputDatasets Input datasets.

    void setInputDataset(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &inputDataset)
    :   Set a single input dataset.

        Parameters:
        :   **inputDataset** – Smart pointer to the input dataset

    gui::[OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") &getTypeAction()
    :   Get type action.

        Returns:
        :   Reference to type action
