# DimensionsPickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html

**Documentation path:** `api/core/gui/actions/point_data/dimensions_picker_action.html`

---

# DimensionsPickerAction

**Qualified name:** `DimensionsPickerAction`

class DimensionsPickerAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Dimensions picker action class.

    Action class for picking one or more points dimensions

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE DimensionsPickerAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    ~DimensionsPickerAction()
    :   Destructor.

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant.

        Parameters:
        :   **Variant** – representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant.

        Returns:
        :   Variant representation of the widget action

    void setDimensions(const std::uint32\_t numDimensions, const std::vector<QString> &names)
    :   Set dimensions.

        Parameters:
        :   - **numDimensions** – Number of dimensions
            - **names** – Dimension names

    const QVector<std::int32\_t> getSelectedDimensions() const
    :   Get indices of the currently selected dimensions.

        Returns:
        :   Indices of the currently selected dimensions

    std::vector<bool> getEnabledDimensions() const
    :   Get enabled dimension.

        Returns:
        :   Vector of booleans where each boolean indicates whether the dimension is enabled or not

    mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> getPointsDataset() const
    :   Get the input points dataset.

    void setPointsDataset(const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &points)
    :   Set the input points dataset.

        Parameters:
        :   **points** – Smart pointer to points dataset

    mv::[DimensionsPickerHolder](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_holder.html#_CPPv4N2mv22DimensionsPickerHolderE "mv::DimensionsPickerHolder") &getHolder()
    :   Get selection picker holder.

        Returns:
        :   Reference to dimensions picker holder

    mv::[DimensionsPickerItemModel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_item_model.html#_CPPv4N2mv25DimensionsPickerItemModelE "mv::DimensionsPickerItemModel") &getItemModel()
    :   Get item model.

        Returns:
        :   Reference to item model

    mv::[DimensionsPickerProxyModel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_proxy_model.html#_CPPv4N2mv26DimensionsPickerProxyModelE "mv::DimensionsPickerProxyModel") &getProxyModel()
    :   Get selection proxy model.

        Returns:
        :   Reference to selection proxy model

    void setNameFilter(const QString &nameFilter)
    :   Set name filter.

        Parameters:
        :   **nameFilter** – Name filter

    void setShowOnlySelectedDimensions(const bool &showOnlySelectedDimensions)
    :   Set show only selected dimensions.

        Parameters:
        :   **showOnlySelectedDimensions** – Show only selected dimensions

    void setApplyExclusionList(const bool &applyExclusionList)
    :   Set apply exclusion list.

        Parameters:
        :   **applyExclusionList** – Apply exclusion list

    void setIgnoreZeroValues(const bool &ignoreZeroValues)
    :   Set ignore zero values.

        Parameters:
        :   **ignoreZeroValues** – Ignore zero values

    void loadSelectionFromFile(const QString &fileName)
    :   Load selection from file.

        Parameters:
        :   **fileName** – Selection file name

    void loadExclusionFromFile(const QString &fileName)
    :   Load exclusion from file.

        Parameters:
        :   **fileName** – Exclusion file name

    void saveSelectionToFile(const QString &fileName)
    :   Save selection from file.

        Parameters:
        :   **fileName** – Selection file name

    void selectDimension(const QString &dimensionName, bool clearExisiting = false)
    :   Select a single dimension by name (and possibly clear the selection)

        Parameters:
        :   - **dimensionName** – Name of the dimension to select
            - **clearExisiting** – Whether to clear the current selection

    void selectDimension(const std::int32\_t &dimensionIndex, bool clearExisiting = false)
    :   Select a single dimension by index (and possibly clear the selection)

        Parameters:
        :   - **dimensionIndex** – Index of the dimension to select
            - **clearExisiting** – Whether to clear the current selection

    void selectDimensions(const QVector<std::int32\_t> &dimensionIndices, bool clearExisiting = true)
    :   Select one or more dimensions by index (and possibly clear the selection)

        Parameters:
        :   - **dimensionIndices** – Indices of the dimensions to select
            - **clearExisiting** – Whether to clear the current selection

    template<bool selectVisible> inline void selectDimensionsBasedOnVisibility()
    :   Select dimensions based on visibility.

    void proxyModelChanged(mv::[DimensionsPickerProxyModel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_proxy_model.html#_CPPv4N2mv26DimensionsPickerProxyModelE "mv::DimensionsPickerProxyModel") \*dimensionsPickerProxyModel)
    :   Signals that the proxy model changed.

        Parameters:
        :   **dimensionsPickerProxyModel** – Pointer to dimensions picker proxy model

    void selectedDimensionsChanged(const QVector<std::int32\_t> &selectedDimensionIndices)
    :   Signals that the selected dimensions changed.

        Parameters:
        :   **selectedDimensionIndices** – Indices of the currently selected dimensions

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the dimension selection action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#classDimensionsPickerAction_1_1Widget) flags for the configuration of the widget

    void computeStatistics()
    :   Compute dimension statistics.

    void updateSlider()
    :   Update the slider.

    void updateSummary()
    :   Update the dimension selection summary.

    void scheduleSummaryUpdate()
    :   Schedule a deferred dimension selection summary update.

    void connectToPublicAction(WidgetAction \*publicAction, bool recursive) override
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions

    Protected Attributes

    mv::[DimensionsPickerHolder](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_holder.html#_CPPv4N2mv22DimensionsPickerHolderE "mv::DimensionsPickerHolder") \_holder
    :   Smart pointer to points set.

    std::unique\_ptr<mv::[DimensionsPickerItemModel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_item_model.html#_CPPv4N2mv25DimensionsPickerItemModelE "mv::DimensionsPickerItemModel")> \_itemModel
    :   Selection holder.

    std::unique\_ptr<mv::[DimensionsPickerProxyModel](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_proxy_model.html#_CPPv4N2mv26DimensionsPickerProxyModelE "mv::DimensionsPickerProxyModel")> \_proxyModel
    :   Selection item model.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_summaryAction
    :   Selection proxy model for filtering etc.

    mv::gui::[DimensionsPickerFilterAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_filter_action.html#_CPPv4N2mv3gui28DimensionsPickerFilterActionE "mv::gui::DimensionsPickerFilterAction") \_filterAction
    :   Summary action.

    mv::gui::[DimensionsPickerSelectAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_select_action.html#_CPPv4N2mv3gui28DimensionsPickerSelectActionE "mv::gui::DimensionsPickerSelectAction") \_selectAction
    :   Filter action.

    mv::gui::[DimensionsPickerMiscellaneousAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_miscellaneous_action.html#_CPPv4N2mv3gui35DimensionsPickerMiscellaneousActionE "mv::gui::DimensionsPickerMiscellaneousAction") \_miscellaneousAction
    :   Select action.

    bool \_summaryUpdatePending = {false}
    :   Miscellaneous settings action.

    Friends

    *friend class* Widget

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#classDimensionsPickerAction_1_1Widget) class for dimension selection action.

        Public Functions

        Widget(QWidget \*parent, [DimensionsPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#_CPPv422DimensionsPickerAction "DimensionsPickerAction") \*dimensionsPickerAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **dimensionsPickerAction** – Pointer to dimensions picker action
                - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimensions_picker_action.html#classDimensionsPickerAction_1_1Widget) flags for the configuration of the widget

        Protected Functions

        void updateTableViewModel(QAbstractItemModel \*model)
        :   Update the table view source model.

            Parameters:
            :   **model** – Pointer to table view source model
