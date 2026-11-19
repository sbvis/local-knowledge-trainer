# Preset

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/preset/preset.html

**Documentation path:** `api/core/util/preset/preset.html`

---

# Preset

**Qualified name:** `mv::util::Preset`

class Preset
:   [Preset](https://manivault.readthedocs.io/en/latest/api/core/util/preset/preset.html#classmv_1_1util_1_1Preset) class.

    Class for storing preset properties

    **Author**
    :   Thomas Kroes

    Public Functions

    QString getName() const
    :   Get preset name.

        Returns:
        :   [Preset](https://manivault.readthedocs.io/en/latest/api/core/util/preset/preset.html#classmv_1_1util_1_1Preset) name

    QString getDescription() const
    :   Get preset description.

        Returns:
        :   [Preset](https://manivault.readthedocs.io/en/latest/api/core/util/preset/preset.html#classmv_1_1util_1_1Preset) description

    QIcon getIcon() const
    :   Get icon.

        Returns:
        :   Icon

    bool isDivergent() const
    :   Get is divergent.

        Returns:
        :   Whether the preset is divergent from current widget action settings

    void isDivergent(bool isDivergent)
    :   Set is divergent.

        Parameters:
        :   **isDivergent** – Whether the preset is divergent from current widget action settings

    Protected Functions

    Preset(const QString &name, const QString &description, const PresetType &presetType = PresetType::Normal)
    :   Constructor.

        Parameters:
        :   - **name** – Name of the preset
            - **description** – [Preset](https://manivault.readthedocs.io/en/latest/api/core/util/preset/preset.html#classmv_1_1util_1_1Preset) description
            - **presetType** – Type of preset
