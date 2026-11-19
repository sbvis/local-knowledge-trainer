# BlobCodecFactory

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec_factory.html

**Documentation path:** `api/core/util/serialization/blob_codec_factory.html`

---

# BlobCodecFactory

**Qualified name:** `mv::util::BlobCodecFactory`

A factory describes one codec type, creates its default GUI settings, and creates configured codec instances. Factories are registered with the [CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html) by the application integration layer.

Factory objects are expected to live on the main thread because they create [CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html) instances. The codecs they produce may subsequently perform encoding or decoding in workflow worker threads.

class BlobCodecFactory : public QObject
:   Factory interface for creating codec instances.

    This factory is expected to live in the main thread

    **Author**
    :   Thomas Kroes

    Public Functions

    virtual const gui::[CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html#_CPPv4N2mv3gui19CodecSettingsActionE "mv::gui::CodecSettingsAction") \*getDefaultCodecSettingsAction() const = 0
    :   Get default codec settings action for this codec (returns nullptr if no settings are needed)

        Returns:
        :   Default codec settings action for this codec (returns nullptr if no settings are needed)

    Protected Functions

    virtual std::shared\_ptr<[BlobCodec](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#_CPPv4N2mv4util9BlobCodecE "mv::util::BlobCodec")> createCodec(QObject \*parent, gui::[CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html#_CPPv4N2mv3gui19CodecSettingsActionE "mv::gui::CodecSettingsAction") \*codecSettingsAction = nullptr) const = 0
    :   Create a new codec instance with the provided codec settings action.

        If no codec settings action is provided, the default codec settings action is used (if available).

        Parameters:
        :   - **parent** – Pointer to parent object for the created codec instance
            - **codecSettingsAction** – Codec settings action for the created codec instance (optional)

        Returns:
        :   A new codec instance
