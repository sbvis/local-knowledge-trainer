# StandardItemModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html

**Documentation path:** `api/core/models/common/standard_item_model.html`

---

# StandardItemModel

**Qualified name:** `mv::StandardItemModel`

class StandardItemModel : public QStandardItemModel, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   Standard item model class.

    Base MV standard item model class

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#classmv_1_1AbstractActionsModel), [mv::AbstractColorSchemesModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel), [mv::AbstractDataHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/abstract_data_hierarchy_model.html#classmv_1_1AbstractDataHierarchyModel), [mv::AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#classmv_1_1AbstractDatasetsModel), [mv::AbstractHardwareSpecModel](https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/abstract_hardware_spec_model.html#classmv_1_1AbstractHardwareSpecModel), [mv::AbstractHeadsUpDisplayModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html#classmv_1_1AbstractHeadsUpDisplayModel), [mv::AbstractPluginFactoriesModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/abstract_plugin_factories_model.html#classmv_1_1AbstractPluginFactoriesModel), [mv::AbstractPluginsModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/abstract_plugins_model.html#classmv_1_1AbstractPluginsModel), [mv::AbstractProjectsModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/abstract_projects_model.html#classmv_1_1AbstractProjectsModel), [mv::AbstractRecentFilesModel](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/abstract_recent_files_model.html#classmv_1_1AbstractRecentFilesModel), [mv::AbstractScriptsModel](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/abstract_scripts_model.html#classmv_1_1AbstractScriptsModel), [mv::AbstractTasksModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/abstract_tasks_model.html#classmv_1_1AbstractTasksModel), mv::AbstractThirdPartyLicensesModel, [mv::AbstractWorkflowMessagesModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/abstract_workflow_messages_model.html#classmv_1_1AbstractWorkflowMessagesModel), [mv::LoggingModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_model.html#classmv_1_1LoggingModel), [mv::RawDataModel](https://manivault.readthedocs.io/en/latest/api/core/models/raw_data/raw_data_model.html#classmv_1_1RawDataModel), [mv::SelectionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/selections/selections_model.html#classmv_1_1SelectionsModel)

    Public Types

    enum class PopulationMode
    :   Model population modes.

        *Values:*

        enumerator Automatic

        enumerator AutomaticSynchronous
        :   Automatically populate the model from the Data Source Names (DSNs)

        enumerator Manual
        :   Automatically populate the model from the DSNs in a synchronous manner.

            Manually populate the model from a JSON file or byte array

    Public Functions

    StandardItemModel(QObject \*parent = nullptr, const QString &title = "StandardItemModel", const [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModel14PopulationModeE "mv::StandardItemModel::PopulationMode") &populationMode = [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModel14PopulationModeE "mv::StandardItemModel::PopulationMode")::[Automatic](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModel14PopulationMode9AutomaticE "mv::StandardItemModel::PopulationMode::Automatic"))
    :   Construct with pointer to `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the model
            - **populationMode** – Population mode of the model (automatic/manual)

    [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModel14PopulationModeE "mv::StandardItemModel::PopulationMode") getPopulationMode() const
    :   Get the population mode of the model.

        Returns:
        :   Population mode (automatic/manual) of the model

    void setPopulationMode(const [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModel14PopulationModeE "mv::StandardItemModel::PopulationMode") &populationMode)
    :   Set the population mode of the model to `populationMode`.

        Parameters:
        :   **populationMode** – Population mode (automatic/manual) of the model

    inline virtual QString getSettingsPrefix() const
    :   Get settings prefix (Models/<serialization\_name>)

        Returns:
        :   Settings prefix for the model, used for saving/loading settings

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load from variant map.

        Parameters:
        :   **variantMap** – Variant map

    virtual QVariantMap toVariantMap() const override
    :   Save to variant map.

        Returns:
        :   Variant map

    void populationModeChanged(const [PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModel14PopulationModeE "mv::StandardItemModel::PopulationMode") &populationMode)
    :   Signals that the population mode changed to `populationMode`.

        Parameters:
        :   **populationMode** – New population mode of the model
