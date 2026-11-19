# Linked data

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/linked_data.html

**Documentation path:** `api/core/data/linked_data.html`

---

# Linked data

`LinkedData` associates source and target datasets with a serializable selection mapping used to propagate corresponding selections.

class LinkedData : public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   Public Functions

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load from variant map.

        Parameters:
        :   **variantMap** – Variant map

    virtual QVariantMap toVariantMap() const override
    :   Save to variant map.

        Returns:
        :   Variant map
