# BrandingConfigurationAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/branding_configuration_action.html

**Documentation path:** `api/core/gui/actions/internal/branding_configuration_action.html`

---

# BrandingConfigurationAction

**Qualified name:** `mv::gui::BrandingConfigurationAction`

class BrandingConfigurationAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application) branding configuration action class.

    Bundles application branding settings

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE BrandingConfigurationAction(QObject \*parent, const QString &title)
    :   Construct with pointer to /p parent object and /p title.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load application configuration from variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the application configuration

    virtual QVariantMap toVariantMap() const override
    :   Save application configuration to variant maps.

        Returns:
        :   Variant representation of the application configuration
