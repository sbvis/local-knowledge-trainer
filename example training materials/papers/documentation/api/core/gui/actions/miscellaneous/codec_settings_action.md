# CodecSettingsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/codec_settings_action.html`

---

# CodecSettingsAction

**Qualified name:** `mv::gui::CodecSettingsAction`

This action contains the user-facing settings for one blob codec: its codec key and block size. A [BlobCodecFactory](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/blob_codec_factory.html) creates the appropriate settings action, and [ProjectCompressionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_compression_action.html) exposes it as part of the project’s compression configuration.

See [Serialization](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/index.html) for the complete persistence pipeline and the distinction between plugin serialization and application-level codec integration.

class CodecSettingsAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE CodecSettingsAction(QObject \*parent, const QString &title)
    :   Construct with `parent` and `project`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
