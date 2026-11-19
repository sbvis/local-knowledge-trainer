# PropertiesSerializer

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/serialization/properties_serializer.html

**Documentation path:** `api/core/util/serialization/properties_serializer.html`

---

# PropertiesSerializer

**Qualified name:** `mv::PropertiesSerializer`

`PropertiesSerializer` provides workflow-based conversion for ManiVault property maps. Core uses it while persisting dataset and set properties so that potentially substantial property values participate in the surrounding serialization workflow.

Warning

This is a specialized, temporary Core helper and may be removed in a future release. Do not use it as the general persistence contract for a plugin. Implement [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html) and follow the [plugin persistence guide](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/index.html) instead.

class PropertiesSerializer : public QObject
:   [PropertiesSerializer](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/properties_serializer.html#classmv_1_1PropertiesSerializer) is a utility class that provides static methods for serializing and deserializing (dataset) properties.

    It uses optimized QVariant serialization that is more efficient than the default QVariant serialization, and it includes a format version in the serialized data to ensure compatibility between different versions of the software.

    The toVariantMap method takes a QVariantMap and returns a new QVariantMap that contains the serialized properties, while the fromVariantMap method takes a source QVariantMap and a reference to a destination QVariantMap, and it populates the destination map with the deserialized properties from the source map. If the format version in the source map is not supported, it throws a runtime error.

    **Author**
    :   T. Kroes

    Note

    This class is temporary; it will most likely be removed in the future when a more robust solution for properties serialization is implemented.

    Public Static Functions

    static workflow::UniqueWorkflowPlan fromVariantMapWorkflow(const QVariantMap &propertiesMap, QVariantMap &destinationPropertiesMap, workflow::SharedWorkflowExecutionContext parentContext = nullptr)
    :   Deserializes the given properties map into a workflow plan.

        Parameters:
        :   - **propertiesMap** – The properties map to deserialize.
            - **destinationPropertiesMap** – The map to populate with the deserialized properties.
            - **parentContext** – The parent workflow execution context.

        Returns:
        :   A unique pointer to the workflow plan that performs the deserialization.

    static workflow::UniqueWorkflowPlan toVariantMapWorkflow(const QVariantMap &propertiesMap)
    :   Creates a workflow plan that serializes the given properties map into a QVariantMap using the optimized serialization format.

        Parameters:
        :   **propertiesMap** – The properties map to serialize.

        Returns:
        :   A unique pointer to the workflow plan that performs the serialization.

    Public Static Attributes

    static constexpr quint32 FormatVersion = 2
    :   Format version for the serialized properties.
