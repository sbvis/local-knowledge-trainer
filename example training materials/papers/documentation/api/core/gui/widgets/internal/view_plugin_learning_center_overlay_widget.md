# ViewPluginLearningCenterOverlayWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html

**Documentation path:** `api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html`

---

# ViewPluginLearningCenterOverlayWidget

`ViewPlugin` creates this overlay automatically. Plugin implementations may retarget it to their central content widget; see [View-plugin Learning Center overlay](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/view_overlay.html).

**Qualified name:** `mv::gui::ViewPluginLearningCenterOverlayWidget`

class ViewPluginLearningCenterOverlayWidget : public mv::gui::[OverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/overlay_widget.html#_CPPv4N2mv3gui13OverlayWidgetE "mv::gui::OverlayWidget")
:   View plugin learning center overlay widget class.

    Overlays the source widget with a view plugin learning center icon popup

    **Author**
    :   Thomas Kroes

    Public Functions

    ViewPluginLearningCenterOverlayWidget(QWidget \*target, const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin)
    :   Construct with pointer to `target` widget and pointer to `viewPlugin`.

        Parameters:
        :   - **target** – Pointer to parent widget (overlay widget will be layered on top of this widget)
            - **viewPlugin** – Pointer to the view plugin for which to create the overlay

    void setTargetWidget(QWidget \*targetWidget)
    :   Set target widget to `targetWidget`.

        Parameters:
        :   **targetWidget** – Pointer to target widget

    [ToolbarWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget13ToolbarWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::ToolbarWidget") &getToolbarWidget()
    :   Get toolbar widget.

        Returns:
        :   Reference to toolbar widget

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Respond to `target` events.

        Parameters:
        :   - **target** – Object of which an event occurred
            - **event** – The event that took place

    void expanded()
    :   Signals that the toolbar got expanded.

    void collapsed()
    :   Signals that the toolbar got collapsed.

    Protected Functions

    void collapse()
    :   Collapse all visible items in the toolbar.

    void expand()
    :   Expand all visible items in the toolbar.

    bool isExpanded()
    :   Get whether all displayable items in the toolbar are visible.

        Returns:
        :   Boolean determining whether all displayable items in the toolbar are visible

    bool isCollapsed()
    :   Get whether all displayable items in the toolbar are hidden.

        Returns:
        :   Boolean determining whether all displayable items in the toolbar are hidden

    void toolbarItemWidgetShown(QWidget \*toolbarItemWidget)
    :   Invoked when `toolbarItemWidget` is shown.

        Parameters:
        :   **toolbarItemWidget** – Pointer to toolbar item widget which is shown

    void toolbarItemWidgetHidden(QWidget \*toolbarItemWidget)
    :   Invoked when `toolbarItemWidget` is hidden.

        Parameters:
        :   **toolbarItemWidget** – Pointer to toolbar item widget which is hidden

    class AboutToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for showing the about information.

        Public Functions

        AboutToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class AbstractToolbarItemWidget : public QWidget
    :   Base class for toolbar item widgets.

        Subclassed by [mv::gui::ViewPluginLearningCenterOverlayWidget::AboutToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1AboutToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::AlignmentToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1AlignmentToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::HideToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1HideToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::LearningCenterToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1LearningCenterToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::ShortcutsToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1ShortcutsToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::ShowDocumentationToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1ShowDocumentationToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::ToLearningCenterToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1ToLearningCenterToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::TutorialsToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1TutorialsToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::VideosToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1VideosToolbarItemWidget), [mv::gui::ViewPluginLearningCenterOverlayWidget::VisitGithubRepoToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1VisitGithubRepoToolbarItemWidget)

        Public Functions

        AbstractToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget, const QSize &iconSize = QSize(16, 16))
        :   Construct with pointer to `overlayWidget` and `icon`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget
                - **iconSize** – Size of the item icon

        void showConditionally()
        :   Show only when required (when [AbstractToolbarItemWidget::shouldDisplay()](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#classmv_1_1gui_1_1ViewPluginLearningCenterOverlayWidget_1_1AbstractToolbarItemWidget_1abe457a7ef378e221ccf7711338f191e3) returns true)

        void showEvent(QShowEvent \*event) override
        :   Invoked when the widget is shown.

            Parameters:
            :   **event** – Pointer to show event

        void hideEvent(QHideEvent \*event) override
        :   Invoked when the widget is hidden.

            Parameters:
            :   **event** – Pointer to hide event

        virtual QIcon getIcon() const = 0
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const = 0
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

        virtual void updateIcon()
        :   Updates the item icon (for badge update)

        util::[WidgetFader](https://manivault.readthedocs.io/en/latest/api/core/util/widget/widget_fader.html#_CPPv4N2mv4util11WidgetFaderE "mv::util::WidgetFader") &getWidgetFader()
        :   Get widget fader.

            Returns:
            :   Reference to widget fader

        Protected Functions

        const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*getViewPlugin() const
        :   Get view plugin.

            Returns:
            :   Pointer to view plugin

        plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*getViewPlugin()
        :   Get non-const pointer to view plugin.

            Returns:
            :   Non-const pointer to view plugin

        [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*getOverlayWidget() const
        :   Get non-const pointer to overlay widget.

            Returns:
            :   Non-const pointer to overlay widget

        Protected Attributes

        [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*\_overlayWidget
        :   Const pointer to source view plugin.

        const QSize \_iconSize
        :   Pointer to overlay widget.

        QHBoxLayout \_layout
        :   Size of the item icon.

        QLabel \_iconLabel
        :   For placing the icon label.

        util::[WidgetFader](https://manivault.readthedocs.io/en/latest/api/core/util/widget/widget_fader.html#_CPPv4N2mv4util11WidgetFaderE "mv::util::WidgetFader") \_widgetFader
        :   Icon label.

    class AlignmentToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for configuring the alignment.

        Public Functions

        AlignmentToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class HideToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for hiding the toolbar.

        Public Functions

        HideToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class LearningCenterToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for the learning center.

        Public Functions

        LearningCenterToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class ShortcutsToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for showing the shortcut map.

        Public Functions

        ShortcutsToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class ShowDocumentationToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for showing the documentation.

        Public Functions

        ShowDocumentationToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class ToLearningCenterToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for visiting the global learning center.

        Public Functions

        ToLearningCenterToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class ToolbarWidget : public QWidget
    :   Toolbar widget to align items horizontally or vertically.

        Public Functions

        ToolbarWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget, bool alwaysVisible = false)
        :   Construct with pointer to `viewPlugin` and pointer to parent `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to the view plugin
                - **overlayWidget** – Pointer to parent overlay widget
                - **alwaysVisible** – Whether the toolbar widget should always be visible, regardless of the view plugin overlay visibility setting

        void addWidget(QWidget \*widget)
        :   Add `widget` to the toolbar.

            Parameters:
            :   **widget** – Pointer to widget to add

        Protected Functions

        bool eventFilter(QObject \*target, QEvent \*event) override
        :   Respond to `target` events.

            Parameters:
            :   - **target** – Object of which an event occurred
                - **event** – The event that took place

        void showEvent(QShowEvent \*event) override
        :   Invoked when the widget is shown.

            Parameters:
            :   **event** – Pointer to show event that occurred

        void alignmentChanged()
        :   Invoked when the plugin learning center alignment changes.

        Protected Static Attributes

        static constexpr std::int32\_t margin = 4
        :   The number of times the widget has been shown.

        Friends

        *friend class* ViewPluginLearningCenterOverlayWidget

    class TutorialsToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for showing the view plugin tutorials.

        Public Functions

        TutorialsToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class VideosToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for showing the view plugin related videos.

        Public Functions

        VideosToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not

    class VisitGithubRepoToolbarItemWidget : public mv::gui::[ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget")::[AbstractToolbarItemWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidget25AbstractToolbarItemWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget::AbstractToolbarItemWidget")
    :   Toolbar item widget for visiting the Github repository website.

        Public Functions

        VisitGithubRepoToolbarItemWidget(const plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin, [ViewPluginLearningCenterOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget.html#_CPPv4N2mv3gui37ViewPluginLearningCenterOverlayWidgetE "mv::gui::ViewPluginLearningCenterOverlayWidget") \*overlayWidget)
        :   Construct with pointer to `viewPlugin` and `overlayWidget`.

            Parameters:
            :   - **viewPlugin** – Pointer to view plugin
                - **overlayWidget** – Pointer to overlay widget

        void mousePressEvent(QMouseEvent \*event) override
        :   Invoked when the mouse button is pressed.

            Parameters:
            :   **event** – Pointer to mouse event

        virtual QIcon getIcon() const override
        :   Get icon.

            Returns:
            :   Icon

        virtual bool shouldDisplay() const override
        :   Determine whether the item should be visible or not.

            Returns:
            :   Boolean determining whether the item should be visible or not
