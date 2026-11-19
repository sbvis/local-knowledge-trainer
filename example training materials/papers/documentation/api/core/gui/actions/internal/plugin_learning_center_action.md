# PluginLearningCenterAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_learning_center_action.html

**Documentation path:** `api/core/gui/actions/internal/plugin_learning_center_action.html`

---

# PluginLearningCenterAction

Plugin instances use the core-managed instance returned by `Plugin::getLearningCenterAction()` to associate tutorials and videos and configure view-overlay placement. For practical guidance, see [Learning Center and shortcuts](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/index.html).

**Qualified name:** `mv::gui::PluginLearningCenterAction`

class PluginLearningCenterAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Plugin learning center action.

    All plugin-related action interface

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE PluginLearningCenterAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    void initialize([plugin](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_learning_center_action.html#_CPPv4N2mv3gui26PluginLearningCenterAction10initializeEPN6plugin6PluginE "mv::gui::PluginLearningCenterAction::initialize::plugin")::Plugin \*plugin)
    :   Initialize with pointer to `plugin` and `parent` object.

        Parameters:
        :   **plugin** – Pointer to plugin

    virtual QMenu \*getContextMenu(QWidget \*parent = nullptr) override
    :   Get the context menu for the action.

        Parameters:
        :   **parent** – Parent widget

        Returns:
        :   Context menu

    QMenu \*getAlignmentContextMenu(QWidget \*parent = nullptr)
    :   Get the context menu for the alignment.

        Parameters:
        :   **parent** – Parent widget

        Returns:
        :   Pointer to alignment context menu

    [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*getViewPluginOverlayWidget() const
    :   Get view plugin overlay widget.

        Returns:
        :   Pointer to plugin overlay widget (maybe nullptr)

    Qt::Alignment getAlignment() const
    :   Get view plugin overlay alignment as a Qt flag.

        Returns:
        :   Alignment flag

    void setAlignment(const Qt::Alignment &alignment)
    :   Set view plugin overlay alignment to `alignment`.

        Parameters:
        :   **alignment** – Alignment flag

    plugin::[PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadataE "mv::plugin::PluginMetadata") &getPluginMetadata()
    :   Get plugin metadata.

        Returns:
        :   Reference to plugin metadata

    const plugin::[PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html#_CPPv4N2mv6plugin14PluginMetadataE "mv::plugin::PluginMetadata") &getPluginMetaData() const
    :   Get plugin meta data.

        Returns:
        :   Reference to plugin meta data

    bool hasHelp() const
    :   Get whether the plugin has help information or not.

        Returns:
        :   Boolean determining whether the plugin has help information or not

    void addVideo(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video)
    :   Add `video`.

        Parameters:
        :   **video** – Pointer to video

    void addVideos(const util::LearningCenterVideos &videos)
    :   Add `videos`.

        Parameters:
        :   **videos** – Videos

    void addVideos(const QString &tag)
    :   Add video by `tag`.

        Parameters:
        :   **tag** – Video tag (from global learning center video)

    void addVideos(const QStringList &tags)
    :   Add videos by `tags`.

        Parameters:
        :   **tags** – Video tags (from global learning center video)

    const util::LearningCenterVideos &getVideos() const
    :   Get videos.

        Returns:
        :   Videos

    void addTutorial(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial)
    :   Add `tutorial`.

        Parameters:
        :   **tutorial** – Pointer to tutorial

    void addTutorials(const util::LearningCenterTutorials &tutorials)
    :   Add `tutorials`.

        Parameters:
        :   **tutorials** – Tutorials

    void addTutorials(const QString &tag)
    :   Add tutorial by `tag`.

        Parameters:
        :   **tag** – tutorial tag (from global learning center tutorial)

    void addTutorials(const QStringList &tags)
    :   Add tutorials by `tags`.

        Parameters:
        :   **tags** – Tutorial tags (from global learning center tutorial)

    const util::LearningCenterTutorials &getTutorials() const
    :   Get tutorials.

        Returns:
        :   tutorials

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load action from variant.

        Parameters:
        :   **variantMap** – variantMap Variant representation of the action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant.

        Returns:
        :   Variant representation of the widget action

    Public Static Attributes

    static const std::vector<Qt::Alignment> alignmentFlags
    :   Names of the supported alignments in the case of a view plugin.

    Protected Functions

    void createViewPluginOverlayWidget()
    :   Create the view plugin overlay widget (should only be called by the view plugin)

    Friends

    *friend class* plugin::ViewPlugin
