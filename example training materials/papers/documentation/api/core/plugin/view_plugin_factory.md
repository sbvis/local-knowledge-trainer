# ViewPluginFactory

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin_factory.html

**Documentation path:** `api/core/plugin/view_plugin_factory.html`

---

# ViewPluginFactory

**Qualified name:** `mv::plugin::ViewPluginFactory`

`ViewPluginFactory` identifies a plugin kind as a view, narrows `produce()` to return a [ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html), and describes initial workspace placement.

The constructor records whether instances are system views and whether they initially float. System-view factories are limited to one live instance by default. A concrete factory may also choose the preferred dock area; the default is the right dock area. These are factory-level policies shared by every instance of the plugin kind.

Request views through the plugin manager so creation policy, input assignment, workspace placement, initialization, and instance accounting remain intact. See [Plugin creation policy](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/index.html).

class ViewPluginFactory : public mv::plugin::[PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html#_CPPv4N2mv6plugin13PluginFactoryE "mv::plugin::PluginFactory")
:   Subclassed by DataHierarchyPluginFactory, DataPropertiesPluginFactory, LoggingPluginFactory, SampleScopePluginFactory, SharedParametersPluginFactory, TasksPluginFactory, TutorialPluginFactory

    Public Functions

    ViewPluginFactory(bool producesSystemViewPlugins = false, bool startFloating = false)
    :   Constructor.

        Parameters:
        :   - **producesSystemViewPlugins** – Whether this factory generates system view plugins or not
            - **startFloating** – Whether the view plugin is initially floating rather than docker to other view plugins

    ~ViewPluginFactory() override = default
    :   Destructor.

    virtual [ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*produce() override = 0
    :   Produces the plugin.

        Returns:
        :   Pointer to the produced plugin

    bool producesSystemViewPlugins() const
    :   Get whether this factory produces system view plugins or not.

        Returns:
        :   Boolean determining whether this factory produces system view plugins or not

    gui::DockAreaFlag getPreferredDockArea() const
    :   Get preferred dock area.

        Returns:
        :   Preferred initial dock area when the view plugin is added to the workspace

    bool getStartFloating() const
    :   Get whether the view plugin is initially floating (not docked to other view plugins)

        Returns:
        :   Boolean determining whether the view plugin initially floats

    Protected Functions

    void setPreferredDockArea(const gui::DockAreaFlag &preferredDockArea)
    :   Set preferred dock area.

        Parameters:
        :   **preferredDockArea** – Preferred initial dock area when the view plugin is added to the workspace
