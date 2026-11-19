# Serialization

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/serialization/index.html

**Documentation path:** `api/core/util/serialization/index.html`

---

# Serialization

ManiVault persistence has three related layers:

1. **Object state** — a [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html) object converts its state to and from a `QVariantMap`.
2. **Binary payloads** — the [serialization helpers](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html) partition large byte buffers into blocks and represent those blocks in the object’s variant map.
3. **Encoding** — the active project’s [compression settings](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_compression_action.html) select a codec through the [CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html). A [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html) then encodes or decodes each block.

This separation lets a plugin describe *what* must be persisted without taking responsibility for project-archive layout or the concrete compression implementation. On restoration, each blob records the codec needed to decode it; the registry supplies the matching implementation.

Start with [Project serialization and restoration](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/index.html) for the plugin contract, workflow boundary, identity rules, and compatibility guidance. The pages below provide the exact low-level APIs.

## Which API should I use?

| If you are… | Start with… |
| --- | --- |
| Persisting plugin or model state | [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html) and the plugin persistence guide |
| Storing a large binary buffer | [Blob serialization functions](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html) |
| Configuring project compression | [ProjectCompressionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_compression_action.html) and [CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html) |
| Integrating another codec into the application | [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html), [BlobCodecFactory](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec_factory.html), and [CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html) |

Prefer the workflow forms of serialization and blob processing for long-running operations. They integrate with ManiVault’s workflow execution, progress reporting, and cancellation. The synchronous APIs remain useful for small, bounded state.

## Blob encoding pipeline

The blob helpers obtain the current project’s codec settings, divide the input into blocks, and create codecs through the registry. `BlobStorageLocation` explicitly chooses whether `bytesToBlobVariantMap()` and `bytesToBlobVariantMapWorkflow()` store the encoded blocks as project-archive files or as base64 payloads inside the project JSON. File storage is the default. Decoding recognizes both representations and follows the codec metadata stored with the blob rather than assuming the project’s current selection.

For an end-to-end plugin example and guidance on choosing a storage location, see [Persisting binary data as blob variant maps](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/binary_blob_data.html).

`CodecActionBinding` is the ownership bridge between a codec and its GUI settings action. It avoids unsafe cross-thread `QObject` parenting when codec work runs outside the GUI thread.

`PropertiesSerializer` is a specialized internal workflow helper for property maps. It is not the general entry point for plugin persistence.

## Reference

- [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html)
- [Serialization](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html)
- [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html)
- [BlobCodecFactory](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec_factory.html)
- [CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html)
- [CodecActionBinding](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_action_binding.html)
- [PropertiesSerializer](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/properties_serializer.html)
