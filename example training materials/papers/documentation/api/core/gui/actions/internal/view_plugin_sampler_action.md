# ViewPluginSamplerAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html

**Documentation path:** `api/core/gui/actions/internal/view_plugin_sampler_action.html`

---

# ViewPluginSamplerAction

**Qualified name:** `mv::gui::ViewPluginSamplerAction`

class ViewPluginSamplerAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   View plugin sampler action class.

    Provides sampling support in view plugins

    Sampling is based on either:

    - The current selection ([SamplingMode::Selection](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1aac2b3ba572e01687f0c8cc60aac9cca1a6ff9dd0d34f65181173c1e4bc39939de)) In this mode, the view plugin updates the sample context whenever its selection changes, it calls [ViewPluginSamplerAction::setSampleContext(const SampleContext& sampleContext)](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1af218b028881cd43f0b6dffd8f0e4f5be). The sample context is a QVariantMap and depends on the type of view plugin.
    - Focus region (circular) around the mouse cursor ([SamplingMode::FocusRegion](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1aac2b3ba572e01687f0c8cc60aac9cca1a22aadb477436272ac3375b16ea6ec5e2)) In this mode, the [ViewPluginSamplerAction::sampleContextRequested()](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1ad09f2848fcbd501c7cacb125cecfb2d5) signal is called periodically. The view plugin collects the samples in response to the signal and calls [ViewPluginSamplerAction::setSampleContext(const SampleContext& sampleContext)](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1af218b028881cd43f0b6dffd8f0e4f5be) to update the current sample context.

    When the current sample context changes, the current ViewPluginSamplerAction::\_viewGeneratorType determines whether the HTML or widget view generator function is called to update the view:

    - ViewPluginSamplerAction::\_htmlViewGeneratorFunction, see ViewPluginSamplerAction::setHtmlViewGeneratorFunction(…)
    - ViewPluginSamplerAction::\_widgetViewGeneratorFunction, see ViewPluginSamplerAction::setWidgetViewGeneratorFunction(…) The generated view is then either:
    - Not shown at all ([ViewingMode::None](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1af40073b9f1830debd562ff8717047815a6adf97f83acf6453d4a6a4b1070f3754))
    - Shown in a tooltip ([ViewingMode::Tooltip](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1af40073b9f1830debd562ff8717047815ac983077ca27977bb5cb4b6398f144166))
    - Shown in a window ([ViewingMode::Windowed](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1af40073b9f1830debd562ff8717047815ab13311ab51c4c34757f67f26580018dd))

    Note: ViewPluginSamplerAction::initialize(…) needs to be called for this action to work properly. In addition to a pointer to a view plugin, it requires two pointers to pixel selection actions:

    - Normal pixel selection action
    - Sampling pixel selection action (enabled when selection is idle)

    The scatter plot plugin is a good example of how this view plugin sampler can be integrated into a view plugin class.

    Special considerations:

    - ViewPluginSamplerAction::setWidgetViewGeneratorFunction(…) does not work reliably together with QWebEngineView and QLabel for HTML-based view, use QTextBrowser instead
    - This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Types

    enum class SamplingMode
    :   Sampling modes.

        *Values:*

        enumerator Selection

        enumerator FocusRegion
        :   Sampling is based on the current selection.

    enum class ViewingMode
    :   Viewing modes.

        *Values:*

        enumerator None

        enumerator Windowed
        :   Do not show samples.

        enumerator Tooltip
        :   Force sample scope view plugin based view.

            Force tooltip view (regardless of the size of the tooltip)

    enum class ViewGeneratorType
    :   Type of view generator.

        *Values:*

        enumerator HTML

        enumerator Widget
        :   HTML formatted string.

            Widget

    using SampleContext = QVariantMap
    :   Context with which the tooltip is created.

    using HtmlViewGeneratorFunction = std::function<QString(const [SampleContext](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction13SampleContextE "mv::gui::ViewPluginSamplerAction::SampleContext")&)>
    :   View generator function which is called periodically when the mouse moves in the view (should return an HTML formatted string)

    using WidgetViewGeneratorFunction = std::function<QWidget\*(const [SampleContext](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction13SampleContextE "mv::gui::ViewPluginSamplerAction::SampleContext")&)>
    :   Widget view generator function ()

    Public Functions

    Q\_INVOKABLE ViewPluginSamplerAction(QObject \*parent, const QString &title, const [ViewingMode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction11ViewingModeE "mv::gui::ViewPluginSamplerAction::ViewingMode") &viewingMode = [ViewingMode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction11ViewingModeE "mv::gui::ViewPluginSamplerAction::ViewingMode")::[None](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction11ViewingMode4NoneE "mv::gui::ViewPluginSamplerAction::ViewingMode::None"))
    :   Construct with pointer to `parent` object and title.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **viewingMode** – Viewing mode

    void initialize(plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [PixelSelectionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/pixel_selection_action.html#_CPPv4N2mv3gui20PixelSelectionActionE "mv::gui::PixelSelectionAction") \*pixelSelectionAction, [PixelSelectionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/pixel_selection_action.html#_CPPv4N2mv3gui20PixelSelectionActionE "mv::gui::PixelSelectionAction") \*samplerPixelSelectionAction)
    :   Initializes the action and enables tooltip display.

        Parameters:
        :   - **viewPlugin** – Pointer to view plugin (may not be nullptr)
            - **pixelSelectionAction** – Pointer to pixel selection action to use (may not be nullptr)
            - **samplerPixelSelectionAction** – Pointer to sampler pixel selection action to use (may not be nullptr)

    [ViewingMode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction11ViewingModeE "mv::gui::ViewPluginSamplerAction::ViewingMode") getViewingMode() const
    :   Get viewing mode.

        Returns:
        :   Viewing mode

    void setViewingMode(const [ViewingMode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction11ViewingModeE "mv::gui::ViewPluginSamplerAction::ViewingMode") &viewingMode)
    :   Set viewing mode to `viewingMode`.

        Parameters:
        :   **viewingMode** – Viewing mode

    [SamplingMode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction12SamplingModeE "mv::gui::ViewPluginSamplerAction::SamplingMode") getSamplingMode() const
    :   Get sampling mode.

        Returns:
        :   Sampling mode

    void setSamplingMode(const [SamplingMode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction12SamplingModeE "mv::gui::ViewPluginSamplerAction::SamplingMode") &samplingMode)
    :   Set sampling mode to `samplingMode`.

        Parameters:
        :   **samplingMode** – Viewing mode

    bool canView() const
    :   Whether this sampler can be viewed, three criteria must be met:

        - ViewPluginSamplerAction.\_enabledAction must be checked
        - ViewPluginSamplerAction::\_viewingMode must be either Mode::Tooltip or Mode::Windowed
        - ViewPluginSamplerAction::\_viewGeneratorFunction must be valid

        Returns:

    [ViewGeneratorType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction17ViewGeneratorTypeE "mv::gui::ViewPluginSamplerAction::ViewGeneratorType") getViewGeneratorType() const
    :   Get the view generator type.

        Returns:
        :   View generator type

    void setViewGeneratorType(const [ViewGeneratorType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction17ViewGeneratorTypeE "mv::gui::ViewPluginSamplerAction::ViewGeneratorType") &viewGeneratorType)
    :   Set the generated view type to `generatedViewType`.

        Parameters:
        :   **viewGeneratorType** – View generator type

    void setHtmlViewGeneratorFunction(const [HtmlViewGeneratorFunction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction25HtmlViewGeneratorFunctionE "mv::gui::ViewPluginSamplerAction::HtmlViewGeneratorFunction") &htmlViewGeneratorFunction)
    :   Sets the HTML view generator function to `htmlViewGeneratorFunction` (automatically sets the viewing type to [ViewGeneratorType::HTML](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1ad3fac9df6b1b9ad0beadad745bc51b7aa4c4ad5fca2e7a3f74dbb1ced00381aa4))

        Parameters:
        :   **htmlViewGeneratorFunction** – HTML view generator function

    void setWidgetViewGeneratorFunction(const [WidgetViewGeneratorFunction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction27WidgetViewGeneratorFunctionE "mv::gui::ViewPluginSamplerAction::WidgetViewGeneratorFunction") &widgetViewGeneratorFunction)
    :   Sets the widget view generator function to `widgetViewGeneratorFunction` (automatically sets the viewing type to [ViewGeneratorType::Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction_1ad3fac9df6b1b9ad0beadad745bc51b7aa6ed562a0d4381eef12d92c87520f3208))

        Parameters:
        :   **widgetViewGeneratorFunction** – Widget view generator function

    [SampleContext](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction13SampleContextE "mv::gui::ViewPluginSamplerAction::SampleContext") getSampleContext() const
    :   Get sample context.

        Returns:
        :   Sample variant map

    void setSampleContext(const [SampleContext](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction13SampleContextE "mv::gui::ViewPluginSamplerAction::SampleContext") &sampleContext)
    :   Set the sample context and flag request an update.

        Parameters:
        :   **sampleContext** – Sample context

    QString getViewString() const
    :   Get view string.

        Returns:
        :   HTML formatted string

    const QWidget \*getViewWidget() const
    :   Get view widget.

        Returns:
        :   Pointer to view widget (maybe nullptr)

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load view plugin from variant.

        Parameters:
        :   **variantMap** – Variant representation of the view plugin

    virtual QVariantMap toVariantMap() const override
    :   Save view plugin to variant.

        Returns:
        :   Variant representation of the view plugin

    void viewingModeChanged(const [ViewingMode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction11ViewingModeE "mv::gui::ViewPluginSamplerAction::ViewingMode") &previousViewingMode, const [ViewingMode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction11ViewingModeE "mv::gui::ViewPluginSamplerAction::ViewingMode") &currentViewingMode)
    :   Signals that the viewing mode changed from `previousViewingMode` to `currentViewingMode`.

        Parameters:
        :   - **previousViewingMode** – Previous viewing mode
            - **currentViewingMode** – Current viewing mode

    void viewGeneratorTypeChanged(const [ViewGeneratorType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction17ViewGeneratorTypeE "mv::gui::ViewPluginSamplerAction::ViewGeneratorType") &previousViewGeneratorType, const [ViewGeneratorType](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction17ViewGeneratorTypeE "mv::gui::ViewPluginSamplerAction::ViewGeneratorType") &currentViewGeneratorType)
    :   Signals that the generated view type changed from `previousViewGeneratorType` to `currentViewGeneratorType`.

        Parameters:
        :   - **previousViewGeneratorType** – Previous generated view type
            - **currentViewGeneratorType** – Current generated view type

    void viewStringChanged(const QString &previousViewString, const QString &currentViewString)
    :   Signals that the view HTML string changed from `previousViewString` to `currentViewString`.

        Parameters:
        :   - **previousViewString** – Previous view HTML string
            - **currentViewString** – Current view HTML string

    void viewWidgetChanged(const QWidget \*previousViewWidget, const QWidget \*currentViewWidget)
    :   Signals that the view widget changed from `previousViewWidget` to `currentViewWidget`.

        Parameters:
        :   - **previousViewWidget** – Previous view widget
            - **currentViewWidget** – Current view widget

    void sampleContextRequested()
    :   Signals that a new sample context is required.

    void sampleContextChanged(const [SampleContext](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction13SampleContextE "mv::gui::ViewPluginSamplerAction::SampleContext") &previousSampleContext, const [SampleContext](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#_CPPv4N2mv3gui23ViewPluginSamplerAction13SampleContextE "mv::gui::ViewPluginSamplerAction::SampleContext") &currentSampleContext)
    :   Signals that the sample context changed from `previousSampleContext` to `currentSampleContext`.

        Parameters:
        :   - **previousSampleContext** – Previous sample context
            - **currentSampleContext** – Current sample context

    void canViewChanged(bool canView)
    :   Signals that the view-ability changed to `canView`.

        Parameters:
        :   **canView** – Current view-ability
