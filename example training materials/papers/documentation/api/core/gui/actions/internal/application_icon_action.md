# ApplicationIconAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/application_icon_action.html

**Documentation path:** `api/core/gui/actions/internal/application_icon_action.html`

---

# ApplicationIconAction

**Qualified name:** `mv::gui::ApplicationIconAction`

class ApplicationIconAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application) icon action class.

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE ApplicationIconAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void overrideMainWindowIcon() const
    :   Set the main window icon to the override application icon.

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load image action from variant.

        Parameters:
        :   **variantMap** – Variant map representation of the image action

    virtual QVariantMap toVariantMap() const override
    :   Save image action to variant.

        Returns:
        :   Variant representation of the image action

    void iconChanged(const QIcon &icon)
    :   Signals that the current icon changed to `icon`.

        Parameters:
        :   **icon** – Current icon that changed

    Public Static Functions

    static void resetApplicationIcon()
    :   Set the application icon to the default.
