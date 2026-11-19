# IconAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/icon_action.html

**Documentation path:** `api/core/gui/actions/internal/icon_action.html`

---

# IconAction

**Qualified name:** `mv::gui::IconAction`

class IconAction : public mv::gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction")
:   Icon action class (WIP)

    For icon storage

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE IconAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void setIconFromImage(const QImage &image)
    :   Set the current icon from `image`.

        Parameters:
        :   **image** – Image to convert to icon

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load image action from variant.

        Parameters:
        :   **Variant** – representation of the image action

    virtual QVariantMap toVariantMap() const override
    :   Save image action to variant.

        Returns:
        :   Variant representation of the image action
