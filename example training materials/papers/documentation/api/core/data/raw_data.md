# Raw data plugin

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/raw_data.html

**Documentation path:** `api/core/data/raw_data.html`

---

# Raw data plugin

`plugin::RawData` is the plugin base for a registered data kind. It creates concrete dataset implementations and reports the storage associated with its raw-data instance.

class RawData : public mv::plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")
:   Subclassed by ClusterData, ColorData, ImageData, PointData, TextData

    Public Functions

    inline RawData(const [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*factory, const [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") &dataType)
    :   Constructor.

        Parameters:
        :   - **factory** – Pointer to the plugin factory
            - **dataType** – Type of data

    inline ~RawData() override
    :   Destructor.

    inline const [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") &getDataType() const
    :   Get the type of raw data.

    virtual [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> createDataSet(const QString &guid = "") const = 0
    :   Create dataset for raw data.

        Parameters:
        :   **guid** – Globally unique dataset identifier (use only for deserialization)

        Returns:
        :   Smart pointer to dataset

    inline virtual std::uint64\_t getRawDataSize() const
    :   Get amount of data occupied by the raw data.

        Returns:
        :   Size of the raw data in bytes
