# DatasetPickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/dataset_picker_action.html`

---

# DatasetPickerAction

**Qualified name:** `mv::gui::DatasetPickerAction`

class DatasetPickerAction : public mv::gui::[OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction")
:   Picks a dataset.

    [DatasetPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html#classmv_1_1gui_1_1DatasetPickerAction) presents datasets through an option action and keeps the available choices synchronized with the selected population mode.

    In automatic population mode, the action follows the global datasets model and applies the configured filter function. In manual population mode, the action uses the dataset list provided through [setDatasets()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html#classmv_1_1gui_1_1DatasetPickerAction_1a2a3d3d4732b8529dae1b84bd5801183a).

    The action tracks the selected dataset by identifier for serialization and emits dataset selection signals when the current dataset changes.

    [currentDatasetChanged()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html#classmv_1_1gui_1_1DatasetPickerAction_1a0da5812008f47cd163a2d908f925b9f7) is the complete state-change signal. It emits a valid dataset when a dataset is selected and an invalid dataset when the selection is cleared. [datasetPicked()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html#classmv_1_1gui_1_1DatasetPickerAction_1aa4221b0bf5d0bae33b56757d05909751) is retained as the selection-specific compatibility signal and is emitted only for valid datasets.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Functions

    Q\_INVOKABLE DatasetPickerAction(QObject \*parent, const QString &title)
    :   Constructs a dataset picker action.

        Parameters:
        :   - **parent** – Parent object.
            - **title** – Action title.

    mv::Datasets getDatasets() const
    :   Returns selectable datasets.

        Returns:
        :   Datasets currently visible through the picker after filtering.

    void setDatasets(mv::Datasets datasets, bool silent = false)
    :   Sets selectable datasets.

        Assigning datasets switches the action to manual population mode.

        Parameters:
        :   - **datasets** – Datasets that can be selected.
            - **silent** – Whether to suppress [datasetsChanged()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html#classmv_1_1gui_1_1DatasetPickerAction_1ab2449279c678d4b086f71f8f450ab830) while replacing the list.

    void setFilterFunction(const [DatasetsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/datasets_filter_model.html#_CPPv4N2mv19DatasetsFilterModelE "mv::DatasetsFilterModel")::[FilterFunction](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/datasets_filter_model.html#_CPPv4N2mv19DatasetsFilterModel14FilterFunctionE "mv::DatasetsFilterModel::FilterFunction") &filterFunction)
    :   Sets the dataset filter function.

        Parameters:
        :   **filterFunction** – Function used by the filter model to decide which datasets are selectable.

    mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset") getCurrentDataset() const
    :   Returns the current dataset.

        Returns:
        :   Currently selected dataset, or an invalid dataset when no dataset is selected.

    template<typename DatasetType> inline mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html#_CPPv4I0ENK2mv3gui19DatasetPickerAction17getCurrentDatasetEN2mv7DatasetI11DatasetTypeEEv "mv::gui::DatasetPickerAction::getCurrentDataset::DatasetType")> getCurrentDataset() const
    :   Returns the current dataset as a typed dataset.

        Template Parameters:
        :   **DatasetType** – Target dataset implementation type.

        Returns:
        :   Currently selected dataset cast to `DatasetType`.

    void setCurrentDataset(mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<mv::[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> currentDataset)
    :   Sets the current dataset.

        Parameters:
        :   **currentDataset** – [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) to select, or an invalid dataset to clear the selection.

    void setCurrentDataset(const QString &datasetId)
    :   Sets the current dataset by identifier.

        Parameters:
        :   **datasetId** – Globally unique identifier of the dataset to select, or an empty string to clear the selection.

    QString getCurrentDatasetId() const
    :   Returns the current dataset identifier.

        Returns:
        :   Globally unique identifier of the selected dataset, or an empty string when no dataset is selected.

    QStringList getCurrentDatasetIds() const
    :   Returns selectable dataset identifiers.

        Returns:
        :   Globally unique identifiers of all currently selectable datasets.

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getDataset(const QString &datasetId) const
    :   Returns a dataset by identifier.

        Parameters:
        :   **datasetId** – Globally unique dataset identifier to look up.

        Returns:
        :   [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#classmv_1_1Dataset) with the requested identifier, or an invalid dataset when it is not selectable.

    void invalidateFilter()
    :   Refreshes the dataset filter.

        Invalidates the internal filter model so the selectable dataset list is recomputed. This is primarily useful in automatic population mode.

    [AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationModeE "mv::AbstractDatasetsModel::PopulationMode") getPopulationMode() const
    :   Returns the population mode.

        Returns:
        :   Current population mode.

    void setPopulationMode([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationModeE "mv::AbstractDatasetsModel::PopulationMode") populationMode)
    :   Sets the population mode.

        Parameters:
        :   **populationMode** – Population mode to use for selectable datasets.

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Loads the action from a variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the action.

    virtual QVariantMap toVariantMap() const override
    :   Saves the action to a variant map.

        Returns:
        :   Variant map representation of the action.

    void datasetAboutToBePicked(mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<> currentDataset)
    :   Signals that the current dataset is about to change.

        The signal carries the previously selected dataset. The dataset can be invalid when no dataset was selected.

        Parameters:
        :   **currentDataset** – Previously selected dataset, or an invalid dataset when no dataset was selected.

    void datasetPicked(mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<> pickedDataset)
    :   Signals that a valid dataset has been picked.

        This compatibility signal is emitted only for valid dataset selections. Code that also needs to react to cleared selections should use [currentDatasetChanged()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/dataset_picker_action.html#classmv_1_1gui_1_1DatasetPickerAction_1a0da5812008f47cd163a2d908f925b9f7).

        Parameters:
        :   **pickedDataset** – Newly selected dataset. The dataset is guaranteed to be valid.

    void currentDatasetChanged([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset)
    :   Signals that the current dataset changed.

        This is the canonical state-change signal. A valid dataset means a dataset is selected; an invalid dataset means the selection was cleared or could no longer be resolved.

        Parameters:
        :   **dataset** – Newly selected dataset, or an invalid dataset when the selection was cleared.

    void datasetsChanged(mv::Datasets datasets)
    :   Signals that selectable datasets changed.

        Parameters:
        :   **datasets** – Current selectable datasets.

    void populationModeChanged([AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationModeE "mv::AbstractDatasetsModel::PopulationMode") previousPopulationMode, [AbstractDatasetsModel](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModelE "mv::AbstractDatasetsModel")::[PopulationMode](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/abstract_datasets_model.html#_CPPv4N2mv21AbstractDatasetsModel14PopulationModeE "mv::AbstractDatasetsModel::PopulationMode") currentPopulationMode)
    :   Signals that the population mode changed.

        Parameters:
        :   - **previousPopulationMode** – Previous population mode.
            - **currentPopulationMode** – Current population mode.

    Protected Functions

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive) override
    :   Connects this action to a public action.

        Parameters:
        :   - **publicAction** – Public action to connect to.
            - **recursive** – Whether to also connect descendant child actions.

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnects this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions.
