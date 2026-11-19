# AnalysisPlugin

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html

**Documentation path:** `api/core/plugin/analysis_plugin.html`

---

# AnalysisPlugin

**Qualified name:** `mv::plugin::AnalysisPlugin`

An analysis plugin consumes one or more input datasets and may publish one or more output datasets. Its input and output handles are assigned through the managed plugin lifecycle and are persisted by the base implementation.

Pair an analysis instance with an [AnalysisPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin_factory.html). For choosing analysis rather than transformation or view, and for long-running execution guidance, see [Choosing a plugin type](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/choosing_a_type.html).

class AnalysisPlugin : public mv::plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")
:   Public Functions

    void setObjectName(const QString &name)
    :   Set name of the object.

        Parameters:
        :   **name** – Name of the object

    void setInputDataset(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &inputDataset)
    :   Set input dataset smart pointer.

        Parameters:
        :   **inputDataset** – Smart pointer to the input dataset

    void setInputDatasets(const Datasets &inputDatasets)
    :   Set input datasets smart pointers.

        Parameters:
        :   **inputDatasets** – Vector of smart pointers to the input datasets

    template<typename DatasetType = [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html#_CPPv4I0EN2mv6plugin14AnalysisPlugin15getInputDatasetE7DatasetI11DatasetTypeEv "mv::plugin::AnalysisPlugin::getInputDataset::DatasetType")> getInputDataset()
    :   Get input dataset smart pointer.

    inline Datasets getInputDatasets()
    :   Get input dataset smart pointer vector.

    void setOutputDataset(const [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &outputDataset)
    :   Set output dataset smart pointer.

        Parameters:
        :   **outputDataset** – Smart pointer to output dataset

    void setOutputDatasets(const Datasets &outputDatasets)
    :   Set output datasets smart pointers.

        Parameters:
        :   **outputDatasets** – Vector of smart pointers to output datasets

    template<typename DatasetType = [DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html#_CPPv4I0EN2mv6plugin14AnalysisPlugin16getOutputDatasetE7DatasetI11DatasetTypeEv "mv::plugin::AnalysisPlugin::getOutputDataset::DatasetType")> getOutputDataset()
    :   Get output dataset smart pointer.

    inline Datasets getOutputDatasets()
    :   Get output dataset smart pointers.

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load analysis plugin from variant.

        Parameters:
        :   **Variant** – representation of the analysis plugin

    virtual QVariantMap toVariantMap() const override
    :   Save analysis plugin to variant.

        Parameters:
        :   **Variant** – representation of the analysis plugin

    Protected Functions

    inline bool outputDataInit() const
    :   Returns whether any output dataset is given.

    Protected Attributes

    Datasets \_output
    :   Input datasets smart pointers.
