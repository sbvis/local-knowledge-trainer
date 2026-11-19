# Serialization

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html

**Documentation path:** `api/core/util/serialization/serialization.html`

---

# Serialization

This section documents utility functions for encoding byte buffers as project blobs, restoring those buffers, and serializing Qt variant maps. Large encode and decode operations can be expressed as workflow plans so that they use the core workflow execution, progress, and cancellation infrastructure.

Blob encoding uses the active project’s [compression configuration](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_compression_action.html) and creates the selected [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html) through the [CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html). Use these helpers instead of coupling plugin serialization directly to a concrete compression library or archive layout.

The encode helpers require an open project because the project supplies the codec settings and persistence context. A serialized blob carries the codec information required for restoration.

## Storage location

`BlobStorageLocation` controls where each encoded block is stored:

- `FileInProject` writes block files into the project archive and stores relative references in the blob map. It is the default and is normally the better choice for large payloads.
- `InlineInProjectJson` stores the encoded bytes as base64 data directly in the project JSON. It produces a self-contained variant-map representation, at the cost of a larger JSON document and base64 overhead.

Both forms use the active project’s codec and block-size settings. The restore helpers accept either representation without a separate storage-location argument. Treat the returned blob map as opaque rather than depending on its internal block fields.

For plugin-oriented examples, see [Persisting binary data as blob variant maps](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/binary_blob_data.html).

enum class mv::util::BlobStorageLocation
:   Location used to store encoded blob payloads during project serialization.

    *Values:*

    enumerator FileInProject

    enumerator InlineInProjectJson
    :   Store each encoded block as a file in the project archive.

        Store each encoded block inline in the project JSON.

## Functions

QVariantMap mv::util::bytesToBlobVariantMap(const char \*bytes, std::uint64\_t numberOfBytes, [BlobStorageLocation](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html#_CPPv4N2mv4util19BlobStorageLocationE "mv::util::BlobStorageLocation") storageLocation = [BlobStorageLocation](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html#_CPPv4N2mv4util19BlobStorageLocationE "mv::util::BlobStorageLocation")::[FileInProject](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html#_CPPv4N2mv4util19BlobStorageLocation13FileInProjectE "mv::util::BlobStorageLocation::FileInProject"))
:   Serialize a raw byte buffer into a blob variant map.

    The buffer is partitioned into blocks, encoded using the active project compression settings, and described by a variant map that can later be restored using [populateBytesFromBlobMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html#namespacemv_1_1util_1af1fae4961a16710891d100617aa9608b) or [bytesFromBlobVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html#namespacemv_1_1util_1a8b47b092d5bfb84869d4138248bd4e37).

    Parameters:
    :   - **bytes** – Source byte buffer.
        - **numberOfBytes** – Number of bytes in the source buffer.
        - **storageLocation** – Location used to store the encoded blob payloads.

    Returns:
    :   Serialized blob variant map.

workflow::UniqueWorkflowPlan mv::util::bytesToBlobVariantMapWorkflow(const char \*bytes, std::uint64\_t numberOfBytes, [BlobStorageLocation](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html#_CPPv4N2mv4util19BlobStorageLocationE "mv::util::BlobStorageLocation") storageLocation = [BlobStorageLocation](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html#_CPPv4N2mv4util19BlobStorageLocationE "mv::util::BlobStorageLocation")::[FileInProject](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html#_CPPv4N2mv4util19BlobStorageLocation13FileInProjectE "mv::util::BlobStorageLocation::FileInProject"))
:   Create a workflow that serializes a raw byte buffer into a blob variant map.

    The workflow performs block encoding in parallel and publishes the resulting blob variant map as its output.

    Parameters:
    :   - **bytes** – Source byte buffer.
        - **numberOfBytes** – Number of bytes in the source buffer.
        - **storageLocation** – Location used to store the encoded blob payloads.

    Returns:
    :   Workflow that produces a blob variant map.

void mv::util::populateBytesFromBlobMap(QVariantMap variantMap, char \*destination, std::uint64\_t destinationSize)
:   Populate a destination buffer from a serialized blob variant map.

    All encoded blocks described by the variant map are decoded and written into the destination buffer at their recorded offsets.

    Parameters:
    :   - **variantMap** – Serialized blob variant map.
        - **destination** – Destination buffer.
        - **destinationSize** – Size of the destination buffer in bytes.

workflow::UniqueWorkflowPlan mv::util::populateBytesFromBlobMapWorkflow(QVariantMap variantMap, char \*destination, std::uint64\_t destinationSize, const workflow::[WorkflowOptions](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_options.html#_CPPv4N2mv8workflow15WorkflowOptionsE "mv::workflow::WorkflowOptions") &options = {})
:   Create a workflow that populates a destination buffer from a serialized blob variant map.

    The workflow decodes blocks in parallel according to the supplied workflow execution options.

    Parameters:
    :   - **variantMap** – Serialized blob variant map.
        - **destination** – Destination buffer.
        - **destinationSize** – Size of the destination buffer in bytes.
        - **options** – Workflow options used to determine decode batching behavior.

    Returns:
    :   Workflow that populates the destination buffer.

QByteArray mv::util::bytesFromBlobVariantMap(QVariantMap variantMap)
:   Deserialize a blob variant map into a byte array.

    The required storage is allocated automatically and all encoded blocks are decoded into the returned byte array.

    Parameters:
    :   **variantMap** – Serialized blob variant map.

    Returns:
    :   Decoded byte array.

void mv::util::variantMapMustContain(const QVariantMap &variantMap, const QString &key, std::source\_location sourceLocation = std::source\_location::current())
:   Ensure that a variant map contains a required key.

    Parameters:
    :   - **variantMap** – Variant map to inspect.
        - **key** – Required key.
        - **sourceLocation** – Source location used to report errors.

    Throws:
    :   [ManiVaultException](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv18ManiVaultExceptionE "mv::ManiVaultException") – If the key is not present.

std::uint64\_t mv::util::estimateRawBlockTotalSize(const QVariant &value)
:   Estimate the total decoded size of all serialized blob objects contained within a variant hierarchy.

    Parameters:
    :   **value** – Variant value to inspect recursively.

    Returns:
    :   Estimated total decoded size in bytes.

QByteArray mv::util::serializeVariantMap(const QVariantMap &map)
:   Serialize a variant map to a binary byte array.

    Parameters:
    :   **map** – Variant map to serialize.

    Returns:
    :   Serialized byte array.

QVariantMap mv::util::deserializeVariantMap(const QByteArray &bytes)
:   Deserialize a variant map from a binary byte array.

    Parameters:
    :   **bytes** – Serialized byte array.

    Returns:
    :   Deserialized variant map.

QVariantMap mv::util::storeOnDisk(const QStringList &list)
:   Serialize a string list using the blob serialization format.

    Parameters:
    :   **list** – String list to serialize.

    Returns:
    :   Serialized representation.

QVariantMap mv::util::storeOnDisk(const QVector<uint32\_t> &vector)
:   Serialize a vector using the blob serialization format.

    Parameters:
    :   **vector** – Vector to serialize.

    Returns:
    :   Serialized representation.

void mv::util::loadFromDisk(const QVariantMap &variantMap, QStringList &list)
:   Restore a string list from a serialized blob representation.

    Parameters:
    :   - **variantMap** – Serialized representation.
        - **list** – Destination string list.

void mv::util::loadFromDisk(const QVariantMap &variantMap, QVector<uint32\_t> &vec)
:   Restore a vector from a serialized blob representation.

    Parameters:
    :   - **variantMap** – Serialized representation.
        - **vec** – Destination vector.
