# BlobCodec

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html

**Documentation path:** `api/core/util/serialization/blob_codec.html`

---

# BlobCodec

**Qualified name:** `mv::util::BlobCodec`

`BlobCodec` is the abstract binary encoder and decoder used by project blob storage. A codec can encode to memory or a file, decode into a new or existing buffer, declare its file extension, and indicate whether its encoded data may be stored inline.

Codecs are created from settings by the [CodecRegistry](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_registry.html) rather than constructed directly by plugin serialization code. The associated [CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html) remains a GUI object; [CodecActionBinding](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/codec_action_binding.html) manages the lifetime boundary when codec work runs on another thread.

class BlobCodec : public QObject
:   Interface for encoding and decoding binary blobs.

    A blob codec transforms raw binary data into a stored representation and back again. Concrete implementations may perform no compression, Qt compression, Zstandard compression, etc.

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Type
    :   Blob codec type.

        *Values:*

        enumerator None

        enumerator QtCompress
        :   No compression.

        enumerator Zstd
        :   Qt compression.

        enumerator Count
        :   Zstandard compression.

    Public Functions

    BlobCodec(QObject \*parent, const gui::CodecSettingsActionPtr &codecSettingsAction)
    :   Constructs a codec with a codec settings action.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **codecSettingsAction** – Codec settings action for this codec (must be a valid pointer)

    virtual [Type](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#_CPPv4N2mv4util9BlobCodec4TypeE "mv::util::BlobCodec::Type") getType() const = 0
    :   Returns the codec type.

    virtual QString getName() const = 0
    :   Returns the codec name used for serialization/debugging.

    virtual QByteArray encode(const QByteArray &input) const = 0
    :   Encode a block of raw bytes and return the encoded data.

        Note

        This method will throw an exception if encoding fails. The returned QByteArray is only valid if the encoding was successful.

        Parameters:
        :   **input** – Raw input bytes

        Returns:
        :   Encoded bytes

    virtual QByteArray encode(const char \*data, qsizetype size) const = 0
    :   Encode a block of raw bytes and return the encoded data.

        Note

        This method will throw an exception if encoding fails. The returned QByteArray is only valid if the encoding was successful.

        Parameters:
        :   - **data** – Pointer to raw input bytes
            - **size** – Size of the raw input bytes in bytes

        Returns:
        :   Encoded bytes

    virtual QByteArray decode(const QByteArray &input, qsizetype expectedSize = -1) const = 0
    :   Decode a previously encoded block of bytes and return the decoded data.

        Note

        This method will throw an exception if decoding fails. The returned QByteArray is only valid if the decoding was successful.

        Parameters:
        :   - **input** – Encoded input bytes
            - **expectedSize** – Expected decoded size in bytes, or -1 if unknown

        Returns:
        :   Decoded bytes

    virtual void decodeTo(const QByteArray &encodedData, char \*destination, std::uint64\_t destinationSize) const
    :   Decode a previously encoded block of bytes directly to a provided output buffer.

        The default implementation may allocate a temporary decoded buffer and copy it into the destination. Codecs should override this method when they can decode directly into the destination buffer.

        Parameters:
        :   - **encodedData** – Encoded input bytes.
            - **destination** – Output buffer that receives the decoded bytes.
            - **destinationSize** – Size of the output buffer in bytes.

    virtual QString getFileExtension() const = 0
    :   Get file extension for this codec (without leading dot, e.g.

        “zstd” for Zstandard codec)

        Returns:
        :   File extension for this codec

    inline virtual bool supportsInlineData() const
    :   Check if this codec supports inline data (i.e.

        storing encoded data directly in the database instead of as separate files on disk)

        Returns:
        :   True if this codec supports inline data, false otherwise

    gui::[CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html#_CPPv4N2mv3gui19CodecSettingsActionE "mv::gui::CodecSettingsAction") \*getSettingsAction() const
    :   Get codec settings action for this codec (returns nullptr if no settings are needed)

        Returns:
        :   Codec settings action for this codec (returns nullptr if no settings are needed)

    Public Static Functions

    static QString typeToString([Type](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#_CPPv4N2mv4util9BlobCodec4TypeE "mv::util::BlobCodec::Type") type)
    :   Convert codec type to persistent string.

    static [Type](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec.html#_CPPv4N2mv4util9BlobCodec4TypeE "mv::util::BlobCodec::Type") typeFromString(const QString &typeString)
    :   Convert persistent string to codec type.
