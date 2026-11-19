# SortFilterProxyModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html

**Documentation path:** `api/core/models/common/sort_filter_proxy_model.html`

---

# SortFilterProxyModel

**Qualified name:** `mv::SortFilterProxyModel`

class SortFilterProxyModel : public QSortFilterProxyModel, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   Filter model class.

    Base MV filter model class

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::ActionsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_filter_model.html#classmv_1_1ActionsFilterModel), [mv::ColorSchemesFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/color_schemes_filter_model.html#classmv_1_1ColorSchemesFilterModel), [mv::DataHierarchyFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/data_hierarchy_filter_model.html#classmv_1_1DataHierarchyFilterModel), [mv::DatasetsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/datasets_filter_model.html#classmv_1_1DatasetsFilterModel), [mv::HardwareSpecFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/hardware_spec/hardware_spec_filter_model.html#classmv_1_1HardwareSpecFilterModel), [mv::HeadsUpDisplayFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/heads_up_display_filter_model.html#classmv_1_1HeadsUpDisplayFilterModel), [mv::LearningCenterTutorialsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_filter_model.html#classmv_1_1LearningCenterTutorialsFilterModel), [mv::LearningCenterVideosFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_filter_model.html#classmv_1_1LearningCenterVideosFilterModel), [mv::LoggingFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/logging/logging_filter_model.html#classmv_1_1LoggingFilterModel), [mv::PluginFactoriesFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugin_factories/plugin_factories_filter_model.html#classmv_1_1PluginFactoriesFilterModel), [mv::PluginsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/plugins/plugins_filter_model.html#classmv_1_1PluginsFilterModel), [mv::ProjectsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/projects/projects_filter_model.html#classmv_1_1ProjectsFilterModel), [mv::RawDataFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/raw_data/raw_data_filter_model.html#classmv_1_1RawDataFilterModel), [mv::RecentFilesFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/recent_files/recent_files_filter_model.html#classmv_1_1RecentFilesFilterModel), [mv::ScriptsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/scripts/scripts_filter_model.html#classmv_1_1ScriptsFilterModel), [mv::SelectionsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/selections/selections_filter_model.html#classmv_1_1SelectionsFilterModel), [mv::TasksFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/tasks/tasks_filter_model.html#classmv_1_1TasksFilterModel), mv::ThirdPartyLicensesFilterModel, [mv::WorkflowMessagesFilterModel](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_messages_filter_model.html#classmv_1_1WorkflowMessagesFilterModel)

    Public Functions

    SortFilterProxyModel(QObject \*parent = nullptr, const QString &title = "SortFilterProxyModel")
    :   Construct with parent `parent` object.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the model

    void setSourceModel(QAbstractItemModel \*sourceModel) override
    :   Set source model to `sourceModel`.

        Parameters:
        :   **sourceModel** – Pointer to source model

    void setRowTypeName(const QString &rowTypeName)
    :   Set row type name to `rowTypeName`.

        Parameters:
        :   **rowTypeName** – Type name by which to identify a row

    QString getRowTypeName() const
    :   Get row type name.

        Returns:
        :   Type name by which to identify a row

    void setFilterColumn(int column)
    :   Set filter column to `column`.

        Parameters:
        :   **column** – Column index

    void rowTypeNameChanged(const QString &rowTypeName)
    :   Signals that the row type name changed to `rowTypeName`.

        Parameters:
        :   **rowTypeName** – Type name by which to identify a row

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load from variant map.

        Parameters:
        :   **variantMap** – Variant map

    virtual QVariantMap toVariantMap() const override
    :   Save to variant map.

        Returns:
        :   Variant map
