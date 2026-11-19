# DimensionPickerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimension_picker_action.html

**Documentation path:** `api/core/gui/actions/point_data/dimension_picker_action.html`

---

# DimensionPickerAction

**Qualified name:** `DimensionPickerAction`

class DimensionPickerAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Dimension picker action class.

    Action class for picking a dimension from a points dataset Also support searching for a dimension

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE DimensionPickerAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void setPointsDataset(const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &points)
    :   Set the points dataset from which the dimension will be picked.

        Parameters:
        :   **points** – Dataset reference to points dataset

    QStringList getDimensionNames() const
    :   Get the names of the dimensions.

    std::uint32\_t getNumberOfDimensions() const
    :   Get the number of currently loaded dimensions.

    std::int32\_t getCurrentDimensionIndex() const
    :   Get the current dimension index.

    QString getCurrentDimensionName() const
    :   Get the current dimension name.

    void setCurrentDimensionIndex(const std::int32\_t &dimensionIndex)
    :   Set the current dimension by index.

        Parameters:
        :   **dimensionIndex** – Index of the current dimension

    void setCurrentDimensionName(const QString &dimensionName)
    :   Set the current dimension by name.

        Parameters:
        :   **dimensionName** – Name of the current dimension

    std::uint32\_t getSearchThreshold() const
    :   Get search threshold.

    void setSearchThreshold(const std::uint32\_t &searchThreshold)
    :   Set search threshold.

        Parameters:
        :   **searchThreshold** – Search threshold

    bool maySearch() const
    :   Establishes whether the dimensions can be searched (number of options exceeds the search threshold)

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void currentDimensionIndexChanged(const std::int32\_t &currentDimensionIndex)
    :   Signals that the current dimension index changed.

        Parameters:
        :   **currentDimensionIndex** – Index of the current dimension

    void currentDimensionNameChanged(const QString &currentDimensionName)
    :   Signals that the current dimension name changed.

        Parameters:
        :   **currentDimensionName** – Name of the current dimension

    inline mv::gui::[OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") &getCurrentDimensionAction()
    :   Action getters.

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the dimension picker action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimension_picker_action.html#classDimensionPickerAction_1_1Widget) flags for the configuration of the widget (type)

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

    mv::gui::[OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") \_currentDimensionAction
    :   Smart pointer to points dataset from which the dimension will be picked.

    std::uint32\_t \_searchThreshold
    :   Current dimension action.

    Protected Static Attributes

    static constexpr std::uint32\_t DEFAULT\_SEARCH\_THRESHOLD = 1000
    :   Select from a drop-down below the threshold and above use a search bar.

    Friends

    *friend class* AbstractActionsManager

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimension_picker_action.html#classDimensionPickerAction_1_1Widget) class for points dimension picker action.

        Protected Functions

        Widget(QWidget \*parent, [DimensionPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/dimension_picker_action.html#_CPPv421DimensionPickerAction "DimensionPickerAction") \*dimensionPickerAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **dimensionPickerAction** – Smart pointer to dimension picker action
