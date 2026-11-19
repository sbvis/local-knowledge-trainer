# ProjectCompressionAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_compression_action.html

**Documentation path:** `api/core/gui/actions/project/project_compression_action.html`

---

# ProjectCompressionAction

**Qualified name:** `mv::ProjectCompressionAction`

This action owns the compression choice for the active project and exposes its [codec settings](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html). The blob serialization helpers use it to create a configured codec; ordinary plugin serializers should normally call those helpers rather than instantiate codecs themselves.

See [Serialization](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/index.html) for the complete object-state, blob-storage, and codec pipeline.

class ProjectCompressionAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   [Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project) compression class.

    Group action class for compression parameters

    **Author**
    :   Thomas Kroes

    Public Functions

    ProjectCompressionAction(QObject \*parent = nullptr)
    :   Constructs from `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    util::SharedCodec createCodec(QObject \*parent) const
    :   Create a new codec instance based on the current codec type and the associated settings action.

        Parameters:
        :   **parent** – Pointer to parent object

        Returns:
        :   Shared pointer to the created codec instance

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load compression action from variant.

        Parameters:
        :   **variantMap** – Variant representation of the compression action

    virtual QVariantMap toVariantMap() const override
    :   Save compression action to variant.

        Returns:
        :   Variant representation of the compression action

    Public Static Attributes

    static constexpr bool DEFAULT\_ENABLE\_COMPRESSION = false
    :   Maps codec display names to codec settings actions.

    Protected Types

    using CodecSettingsActionMap = std::unordered\_map<QString, gui::[CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html#_CPPv4N2mv3gui19CodecSettingsActionE "mv::gui::CodecSettingsAction")\*>
    :   Maps codec display names to codec instances.
