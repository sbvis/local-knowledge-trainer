# ApplicationConfigurationAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/application_configuration_action.html

**Documentation path:** `api/core/gui/actions/internal/application_configuration_action.html`

---

# ApplicationConfigurationAction

**Qualified name:** `mv::gui::ApplicationConfigurationAction`

class ApplicationConfigurationAction : public mv::gui::[GroupsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/groups_action.html#_CPPv4N2mv3gui12GroupsActionE "mv::gui::GroupsAction")
:   [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application) configuration action class.

    Bundles application settings

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE ApplicationConfigurationAction(QObject \*parent, const QString &title)
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

    void mayConfigureChanged(bool mayConfigure)
    :   Signals that the may configure state has changed to /p mayConfigure.

        Parameters:
        :   **mayConfigure** – New may configure state
