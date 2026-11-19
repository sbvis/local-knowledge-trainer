# IconPickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/icon_picker_action.html

**Documentation path:** `api/core/gui/actions/internal/icon_picker_action.html`

---

# IconPickerAction

**Qualified name:** `mv::gui::IconPickerAction`

class IconPickerAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   Icon picker action class (WIP)

    For picking and displaying an icon

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE IconPickerAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    QIcon getIcon() const
    :   Get the current icon Facade for IconAction::getLanguageIcon()

        Returns:
        :   Icon

    void setIcon(const QIcon &icon)
    :   Set the current icon to `icon` Facade for IconAction::setIcon(…)

        Parameters:
        :   **icon** – Current icon

    void setIconFromImage(const QImage &image)
    :   Set the current icon from `image` Facade for IconAction::setIconFromImage(…)

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

    void iconChanged(const QIcon &icon)
    :   Signals that the current icon changed to `icon`.

        Parameters:
        :   **icon** – Current icon that changed
