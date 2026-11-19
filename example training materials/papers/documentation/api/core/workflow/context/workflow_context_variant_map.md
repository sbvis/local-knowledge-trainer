# Workflow context variant map

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_context_variant_map.html

**Documentation path:** `api/core/workflow/context/workflow_context_variant_map.html`

---

# Workflow context variant map

A general-purpose context payload providing synchronized access to named variant values.

class WorkflowContextVariantMap : public mv::workflow::[WorkflowContextBase](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_context_base.html#_CPPv4N2mv8workflow19WorkflowContextBaseE "mv::workflow::WorkflowContextBase")
:   Shares QVariantMap data between workflow stages.

    This context provides a thread-safe key/value store that can be used by workflow stages to exchange intermediate data during (serialization or deserialization) workflows.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Functions

    QVariantMap getMap() const
    :   Returns the complete map.

        Returns:
        :   Copy of the stored QVariantMap.

    void setMap(const QVariantMap &map)
    :   Replaces the complete map with the provided one.

        Parameters:
        :   **map** – Map to store.

    bool contains(const QString &key) const
    :   Checks whether a value exists for the specified key.

        Parameters:
        :   **key** – Key to test for existence.

        Returns:
        :   True if the key exists, otherwise false.

    QVariant value(const QString &key, const QVariant &defaultValue = {}) const
    :   Returns a value from the map.

        Parameters:
        :   - **key** – Key to retrieve.
            - **defaultValue** – Value returned when the key is not present.

        Returns:
        :   Stored value, or the provided default value.

    QVariantMap mapValue(const QString &key) const
    :   Returns a QVariantMap value from the map.

        Parameters:
        :   **key** – Key to retrieve.

        Returns:
        :   The stored value converted to QVariantMap, or an empty map if the key does not exist or cannot be converted.

    void setValue(const QString &key, const QVariant &value)
    :   Stores a value in the map.

        Parameters:
        :   - **key** – Key to store.
            - **value** – Value to associate with the key.

    QVariant takeValue(const QString &key)
    :   Removes and returns a value from the map.

        Parameters:
        :   **key** – Key to remove.

        Returns:
        :   The removed value or an invalid QVariant if the key was not found.

    void merge(const QVariantMap &values)
    :   Merges key/value pairs into the map.

        Parameters:
        :   **values** – Map containing values to merge.

    void clear()
    :   Clears all stored values.
