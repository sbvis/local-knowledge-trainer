# ColorMapAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html

**Documentation path:** `api/core/gui/actions/colormap/color_map_action.html`

---

# ColorMapAction

**Qualified name:** `mv::gui::ColorMapAction`

class ColorMapAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Color map action class.

    Color map selection and settings action

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::gui::ColorMap1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_1d_action.html#classmv_1_1gui_1_1ColorMap1DAction), [mv::gui::ColorMap2DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_2d_action.html#classmv_1_1gui_1_1ColorMap2DAction)

    Public Types

    enum WidgetFlag
    :   Describes the widget configurations (a color map combobox always exists)

        *Values:*

        enumerator Settings

        enumerator EditRange
        :   Widgets have a settings popup to adjust range and other settings.

        enumerator Default
        :   Users are allowed to change the color map range.

    enum class Axis
    :   Axis enum for distinguishing between x- and y axis part of the color map (range)

        *Values:*

        enumerator X

        enumerator Y
        :   Along x-axis.

        enumerator Count
        :   Along y-axis.

    Public Functions

    void initialize(const QString &colorMap)
    :   Initialize the color map action.

        Parameters:
        :   **colorMap** – Current color map

    util::[ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") getColorMapType() const
    :   Gets the current color map type.

    QString getColorMap() const
    :   Gets the current color map name.

    QImage getColorMapImage() const
    :   Gets the current color map.

    void setColorMap(const QString &colorMap)
    :   Sets the current color map name.

        Parameters:
        :   **colorMap** – Name of the current color map

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load widget action from variant map.

        Parameters:
        :   **Variant** – map representation of the widget action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void typeChanged(const util::[ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") &colorMapType)
    :   Signals that the current color map type changed.

        Parameters:
        :   **colorMapType** – Current color map type

    void imageChanged(const QImage &image)
    :   Signals that the current color map image changed.

        Parameters:
        :   **image** – Current color map image

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the color map action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    Q\_INVOKABLE ColorMapAction(QObject \*parent, const QString &title, const util::[ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") &colorMapType = util::[ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type")::[OneDimensional](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4Type14OneDimensionalE "mv::util::ColorMap::Type::OneDimensional"), const QString &colorMap = "RdYlBu")
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **colorMapType** – Type of color map (1D/2D)
            - **colorMap** – Current color map

    void setColorMapType(const util::[ColorMap](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMapE "mv::util::ColorMap")::[Type](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_map.html#_CPPv4N2mv4util8ColorMap4TypeE "mv::util::ColorMap::Type") &colorMapType)
    :   Sets the current color map type.

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive) override
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions

    Protected Attributes

    [OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") \_currentColorMapAction
    :   The filtered color map model (contains either 1D or 2D color maps)

    [DecimalRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeActionE "mv::gui::DecimalRangeAction") \_rangeAction[static\_cast<int>([Axis](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapAction4AxisE "mv::gui::ColorMapAction::Axis")::[Count](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapAction4Axis5CountE "mv::gui::ColorMapAction::Axis::Count"))]
    :   Current color map selection action.

    [DecimalRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeActionE "mv::gui::DecimalRangeAction") \_dataRangeAction[static\_cast<int>([Axis](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapAction4AxisE "mv::gui::ColorMapAction::Axis")::[Count](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapAction4Axis5CountE "mv::gui::ColorMapAction::Axis::Count"))]
    :   Color map range action (1D/2D color map)

    [DecimalRangeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/decimal_range_action.html#_CPPv4N2mv3gui18DecimalRangeActionE "mv::gui::DecimalRangeAction") \_sharedDataRangeAction[static\_cast<int>([Axis](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapAction4AxisE "mv::gui::ColorMapAction::Axis")::[Count](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapAction4Axis5CountE "mv::gui::ColorMapAction::Axis::Count"))]
    :   Range of the associated dataset (1D/2D color map)

    [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_lockToSharedDataRangeAction
    :   Shared range (1D/2D color map) of all connected color maps (if the color map is connected to a public color map)

    [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_mirrorAction[static\_cast<int>([Axis](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapAction4AxisE "mv::gui::ColorMapAction::Axis")::[Count](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapAction4Axis5CountE "mv::gui::ColorMapAction::Axis::Count"))]
    :   Lock to shared data range action.

    [HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction") \_mirrorGroupAction
    :   Mirror along the horizontal/vertical axis action.

    [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_discretizeAction
    :   Group action for mirroring along horizontal/vertical axis.

    [IntegralAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/numerical/integral_action.html#_CPPv4N2mv3gui14IntegralActionE "mv::gui::IntegralAction") \_numberOfDiscreteStepsAction
    :   Discretize setEnabled action.

    [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_discretizeAlphaAction
    :   Number of discrete steps action.

    [ColorMapSettings1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_1d_action.html#_CPPv4N2mv3gui24ColorMapSettings1DActionE "mv::gui::ColorMapSettings1DAction") \_settings1DAction
    :   Whether to also discretize the alpha channel of the color map.

    [ColorMapSettings2DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_2d_action.html#_CPPv4N2mv3gui24ColorMapSettings2DActionE "mv::gui::ColorMapSettings2DAction") \_settings2DAction
    :   One-dimensional settings action.

    [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") \_customColorMapAction
    :   Two-dimensional settings action.

    [ColorMapEditor1DAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_action.html#_CPPv4N2mv3gui22ColorMapEditor1DActionE "mv::gui::ColorMapEditor1DAction") \_editor1DAction
    :   Toggle custom color map action.

    [HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction") \_customColorMapGroupAction
    :   One-dimensional editor action.

    [ColorMapSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_settings_action.html#_CPPv4N2mv3gui22ColorMapSettingsActionE "mv::gui::ColorMapSettingsAction") \_settingsAction
    :   Groups the custom color map and editor action.

    Friends

    *friend class* AbstractActionsManager

    class ComboBoxWidget : public mv::gui::[OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction")::[ComboBoxWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionAction14ComboBoxWidgetE "mv::gui::OptionAction::ComboBoxWidget")
    :   Combobox widget class for display of a color map.

        Protected Functions

        ComboBoxWidget(QWidget \*parent, [OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") \*optionAction, [ColorMapAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_action.html#_CPPv4N2mv3gui14ColorMapActionE "mv::gui::ColorMapAction") \*colorMapAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **optionAction** – Pointer to option action
                - **colorMapAction** – Pointer to color map action

        void paintEvent(QPaintEvent \*paintEvent) override
        :   Paint event to override default paint.

            Parameters:
            :   **paintEvent** – Pointer to paint event

        Friends

        *friend class* ColorMapAction
