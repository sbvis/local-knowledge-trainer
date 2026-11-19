# CodecRegistry

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html

**Documentation path:** `api/core/util/serialization/codec_registry.html`

---

# CodecRegistry

**Qualified name:** `mv::util::CodecRegistry`

`CodecRegistry` maps stable codec types and keys to [BlobCodecFactory](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec_factory.html) instances. Project restoration uses this mapping to recreate the codec named in stored blob metadata, while project compression settings use it to enumerate and create available codecs.

Registration belongs to the application/Core integration layer. Plugin persistence code should use the [blob serialization helpers](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html) and should not depend on a particular registered codec.

class CodecRegistry

[CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html#_CPPv4N2mv4util13CodecRegistryE "mv::util::CodecRegistry") &mv::util::codecRegistry()
