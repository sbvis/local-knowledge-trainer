# ViewPluginHeadsUpDisplayAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_heads_up_display.html

**Documentation path:** `api/core/gui/actions/internal/view_plugin_heads_up_display.html`

---

# ViewPluginHeadsUpDisplayAction

**Qualified name:** `mv::gui::ViewPluginHeadsUpDisplayAction`

class ViewPluginHeadsUpDisplayAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   View plugin heads up display action class.

    For displaying a heads-up display action in the view plugin (as an overlay action)

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE ViewPluginHeadsUpDisplayAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title` of the action.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    [HeadsUpDisplayTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/heads_up_display_tree_model.html#_CPPv4N2mv23HeadsUpDisplayTreeModelE "mv::HeadsUpDisplayTreeModel") &getHeadsUpDisplayTreeModel()
    :   Get heads up display tree model.

        Returns:
        :   Heads up display tree model

    util::HeadsUpDisplayItemSharedPtr addHeadsUpDisplayItem(const QString &title, const QString &value, const QString &description, const util::HeadsUpDisplayItemSharedPtr &sharedParent = nullptr)
    :   Add heads-up display item.

        Parameters:
        :   - **title** – Title
            - **value** – Value
            - **description** – Description
            - **sharedParent** – Shared pointer to parent item (default: nullptr)

    void removeHeadsUpDisplayItem(const util::HeadsUpDisplayItemSharedPtr &headsUpDisplayItem)
    :   Remove `headsUpDisplayItem`.

        Parameters:
        :   **headsUpDisplayItem** – Heads-up display item to remove

    void removeAllHeadsUpDisplayItems()
    :   Remove all heads-up display items.

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load image action from variant.

        Parameters:
        :   **variantMap** – Variant representation of the image action

    virtual QVariantMap toVariantMap() const override
    :   Save image action to variant.

        Returns:
        :   Variant map representation of the image action

    void contentChanged(const QString &previousContent, const QString &currentContent)
    :   Signals that the content changed from `previousContent` to `currentContent`.

        Parameters:
        :   - **previousContent** – Previous string content of the HUD action
            - **currentContent** – Current string content of the HUD action

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    class HeadsUpDisplayWidget : public QWidget
    :   Widget class for displaying HUD entries.

        Protected Functions

        HeadsUpDisplayWidget(QWidget \*parent, [ViewPluginHeadsUpDisplayAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_heads_up_display.html#_CPPv4N2mv3gui30ViewPluginHeadsUpDisplayActionE "mv::gui::ViewPluginHeadsUpDisplayAction") \*viewPluginHeadsUpDisplayAction, const std::int32\_t &widgetFlags)
        :   Construct with pointer to `parent` widget, `viewPluginHeadsUpDisplayAction` and `widgetFlags`.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **viewPluginHeadsUpDisplayAction** – Pointer to view plugin heads up display action
                - **widgetFlags** – Widget flags

        Protected Attributes

        [ViewPluginHeadsUpDisplayAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_heads_up_display.html#_CPPv4N2mv3gui30ViewPluginHeadsUpDisplayActionE "mv::gui::ViewPluginHeadsUpDisplayAction") \*\_viewPluginHeadsUpDisplayAction
        :   Get minimum size hint for the widget.

            Return:
            :   Minimum size hint for the widget

        std::int32\_t \_widgetFlags
        :   Pointer to view plugin heads up display action.

        QTreeView \_treeView
        :   Widget flags.

        Friends

        *friend class* ViewPluginHeadsUpDisplayAction
