# Selection map

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/selection_map.html

**Documentation path:** `api/core/data/selection_map.html`

---

# Selection map

`SelectionMap` maps selected indices between linked datasets using explicit index mappings or image-pyramid geometry.

class SelectionMap : public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   Public Types

    enum class Type
    :   Type of selection mapping.

        *Values:*

        enumerator Indexed

        enumerator ImagePyramid
        :   Using mapped indices.

            Using image pyramids

    Public Functions

    SelectionMap([Type](https://manivault.readthedocs.io/en/latest/api/core/data/selection_map.html#_CPPv4N2mv12SelectionMap4TypeE "mv::SelectionMap::Type") type = [Type](https://manivault.readthedocs.io/en/latest/api/core/data/selection_map.html#_CPPv4N2mv12SelectionMap4TypeE "mv::SelectionMap::Type")::[Indexed](https://manivault.readthedocs.io/en/latest/api/core/data/selection_map.html#_CPPv4N2mv12SelectionMap4Type7IndexedE "mv::SelectionMap::Type::Indexed"))
    :   Constructs a selection mapping of `type`.

        Parameters:
        :   **type** – Type of selection mapping

    SelectionMap(const QSize &sourceImageSize, const QSize &targetImageSize)
    :   Constructs an image pyramid selection mapping.

        Parameters:
        :   - **sourceImageSize** – Resolution of the source image
            - **targetImageSize** – Resolution of the target image

    void populateMappingIndices(std::uint32\_t pointIndex, Indices &indices) const
    :   Populate mapping `indices` for `pointIndex`.

        Parameters:
        :   - **pointIndex** – Point index for which to populate
            - **indices** – Mapping indices

    inline Map &getMap()
    :   Get map for indexed pixels.

        Returns:
        :   Index map

    inline const Map &getMap() const
    :   Get map for indexed pixels.

        Returns:
        :   Index map

    bool hasMappingForPointIndex(std::uint32\_t pointIndex) const
    :   Establishes whether a mapping exists for `pointIndex`.

        Parameters:
        :   **pointIndex** – Point index to check for

        Returns:
        :   Boolean indicating whether a mapping exists for `pointIndex`

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load from variant map.

        Parameters:
        :   **variantMap** – Variant map

    virtual QVariantMap toVariantMap() const override
    :   Save to variant map.

        Returns:
        :   Variant map
