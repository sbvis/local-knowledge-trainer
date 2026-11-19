# CodecActionBinding

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_action_binding.html

**Documentation path:** `api/core/util/serialization/codec_action_binding.html`

---

# CodecActionBinding

**Qualified name:** `mv::util::CodecActionBinding`

`CodecActionBinding` safely associates a [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html) with its [CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html). It deliberately avoids making the GUI action a child of a codec that may live or be destroyed on a worker thread. When the codec is destroyed, the action is scheduled for deletion in the GUI thread.

This is primarily an ownership utility for codec implementations and factories; ordinary serializers do not need to create bindings themselves.

class CodecActionBinding : public QObject
:   Binds a [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#classmv_1_1util_1_1BlobCodec) instance to its corresponding GUI CodecSettingsAction.

    [CodecActionBinding](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_action_binding.html#classmv_1_1util_1_1CodecActionBinding) provides a safe bridge between the runtime codec layer and the GUI layer. It ensures that a [gui::CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html#classmv_1_1gui_1_1CodecSettingsAction) is properly cleaned up when the associated [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#classmv_1_1util_1_1BlobCodec) is destroyed, without introducing direct ownership or parent-child relationships between objects that may live in different threads.

    This class exists to avoid common pitfalls:

    - Prevents dangling pointers to GUI actions when codecs are destroyed
    - Avoids illegal QObject parenting across threads
    - Decouples GUI lifetime management from codec runtime logic

    The binding listens to the destruction of the [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#classmv_1_1util_1_1BlobCodec) and schedules the deletion of the associated CodecSettingsAction using deleteLater(), ensuring that deletion occurs safely in the GUI thread.

    **Author**
    :   Thomas Kroes

    Public Functions

    CodecActionBinding([BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#_CPPv4N2mv4util9BlobCodecE "mv::util::BlobCodec") \*codec, gui::[CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html#_CPPv4N2mv3gui19CodecSettingsActionE "mv::gui::CodecSettingsAction") \*action)
    :   Constructs a [CodecActionBinding](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_action_binding.html#classmv_1_1util_1_1CodecActionBinding) that binds a [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#classmv_1_1util_1_1BlobCodec) to a CodecSettingsAction.

        Parameters:
        :   - **codec** – The [BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#classmv_1_1util_1_1BlobCodec) instance to bind
            - **action** – The CodecSettingsAction instance to bind
