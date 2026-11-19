# ViewPlugin

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html

**Documentation path:** `api/core/plugin/view_plugin.html`

---

# ViewPlugin

**Qualified name:** `mv::plugin::ViewPlugin`

A view plugin owns an interactive widget and the actions integrated into its title bar, dock areas, and overlays. It can receive datasets during managed creation and later through `loadData()`.

Pair a view instance with a [ViewPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin_factory.html), which supplies the view’s system-view and initial-placement policy. See [Choosing a plugin type](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/choosing_a_type.html) for keeping reusable computation separate from presentation.

class ViewPlugin : public mv::plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")
:   Subclassed by DataHierarchyPlugin, DataPropertiesPlugin, LoggingPlugin, SampleScopePlugin, SharedParametersPlugin, TasksPlugin, TutorialPlugin

    Public Functions

    ViewPlugin(const [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory") \*factory)
    :   Constructor.

        Parameters:
        :   **factory** – Pointer to plugin factory

    virtual void init() override
    :   Perform startup initialization.

    virtual void loadData(const Datasets &datasets)
    :   Load one (or more) datasets in the view.

        Parameters:
        :   **datasets** – Dataset(s) to load

    QWidget &getWidget()
    :   Get widget representation of the plugin.

        Returns:
        :   Widget representation of the plugin

    bool isSystemViewPlugin() const
    :   Get whether this plugin is a system view plugin or not.

        Returns:
        :   Boolean determining whether this plugin is a system view plugin or not

    virtual void createScreenshot()
    :   Create screenshot from the view plugin Base implementation grabs the widget and saves it in a user-chosen location.

    QKeySequence getTriggerShortcut() const
    :   Get shortcut for triggering the plugin.

        Returns:
        :   Shortcut key sequence

    void setTriggerShortcut(const QKeySequence &keySequence)
    :   Set shortcut for triggering the plugin.

        Parameters:
        :   **keySequence** – Shortcut key sequence

    void addTitleBarMenuAction(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Add action to the title bar menu.

        Parameters:
        :   **action** – Pointer to widget action

    void removeTitleBarMenuAction(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Remove action from the title bar menu.

        Parameters:
        :   **action** – Pointer to widget action

    gui::WidgetActions getTitleBarMenuActions()
    :   Get title bar actions.

        Returns:
        :   List of pointers to title bar actions

    void addDockingAction(WidgetAction \*dockingAction, WidgetAction \*dockToDockingAction = nullptr, gui::DockAreaFlag dockArea = gui::DockAreaFlag::Right, bool autoHide = false, const gui::AutoHideLocation &autoHideLocation = gui::AutoHideLocation::Left, const QSize &minimumDockWidgetSize = QSize(256, 256))
    :   Add a docking action to the view (the action widget will be docked in the view)

        Parameters:
        :   - **dockingAction** – Pointer to docking action to add
            - **dockToDockingAction** – Pointer to the settings action to dock to (docked top-level if nullptr)
            - **dockArea** – Dock area in which `dockToViewPlugin` will be docked
            - **autoHide** – Whether to pin the settings action to the border of the view plugin
            - **autoHideLocation** – Location to pin the settings action in case auto-hide is active
            - **minimumDockWidgetSize** – Minimum dock widget size

    gui::WidgetActions getDockingActions() const
    :   Get vector of pointers to docking actions.

    void addOverlayAction(WidgetAction \*overlayAction, const Qt::Alignment &alignment = Qt::AlignTop | Qt::AlignLeft)
    :   Add `overlayAction` to the view (the action widget will be overlaid on top of the view)

        Parameters:
        :   - **overlayAction** – Pointer to overlay action to add (may not be nullptr)
            - **alignment** – Alignment of the overlay action in the view

    void removeOverlayAction(WidgetAction \*overlayAction)
    :   Remove `overlayAction` from the view.

        Parameters:
        :   **overlayAction** – Pointer to overlay action to remove (may not be nullptr)

    gui::WidgetActions getOverlayActions() const
    :   Get all overlay actions.

        Returns:
        :   List of pointers to overlay actions

    void setOverlayActionsTargetWidget(QWidget \*targetWidget)
    :   Set target widget for overlay actions to `targetWidget` (default is the view plugin widget)

        Parameters:
        :   **targetWidget** – Pointer to target widget (may not be nullptr)

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*getProgressTask()
    :   Get progress task.

        Returns:
        :   Pointer to progress task (maybe nullptr)

    void setProgressTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*progressTask)
    :   Set progress task to `progressTask`.

        Parameters:
        :   **progressTask** – Pointer to progress task (maybe nullptr)

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load view plugin from variant.

        Parameters:
        :   **variantMap** – Variant map representation of the view plugin

    virtual QVariantMap toVariantMap() const override
    :   Save view plugin to variant.

        Returns:
        :   Variant representation of the view plugin

    void progressTaskChanged([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*progressTask)
    :   Signals that the progress task changed to `progressTask`.

        Parameters:
        :   **progressTask** – Pointer to progress task (maybe nullptr)

    void dockingActionAdded(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Signals that `action` was added as a docking action.

        Parameters:
        :   **action** – Pointer to the added docking action
