# PixelSelectionAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/pixel_selection_action.html

**Documentation path:** `api/core/gui/actions/miscellaneous/pixel_selection_action.html`

---

# PixelSelectionAction

**Qualified name:** `mv::gui::PixelSelectionAction`

class PixelSelectionAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Pixel selection action class.

    Action class for pixel selection

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE PixelSelectionAction(QObject \*parent, const QString &title)
    :   Construct with `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title

    void initialize(QWidget \*targetWidget, util::[PixelSelectionTool](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection_tool.html#_CPPv4N2mv4util18PixelSelectionToolE "mv::util::PixelSelectionTool") \*pixelSelectionTool, const util::PixelSelectionTypes &pixelSelectionTypes = util::[defaultPixelSelectionTypes](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util26defaultPixelSelectionTypesE "mv::util::defaultPixelSelectionTypes"))
    :   Initialize the pixel selection action.

        Parameters:
        :   - **targetWidget** – Pointer to target widget (pixel selection tool will be drawn on top of it)
            - **pixelSelectionTool** – Pointer to pixel selection tool
            - **pixelSelectionTypes** – Allowed pixel selection types

    QMenu \*getContextMenu()
    :   Get the context menu for the action.

        Parameters:
        :   **parent** – Parent widget

        Returns:
        :   Context menu

    QWidget \*getTargetWidget()
    :   Get pointer to the target on which the pixel selection tool operates.

    util::[PixelSelectionTool](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection_tool.html#_CPPv4N2mv4util18PixelSelectionToolE "mv::util::PixelSelectionTool") \*getPixelSelectionTool()
    :   Get pointer to pixel selection tool.

    void setShortcutsEnabled(const bool &shortcutsEnabled)
    :   Enables/disables shortcuts.

        Parameters:
        :   **shortcutsEnabled** – Whether shortcuts are enabled or not

    bool eventFilter(QObject \*object, QEvent \*event) override
    :   Listens to the events of target `object`.

        Parameters:
        :   - **object** – Target object to watch for events
            - **event** – Event that occurred

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load selection action from variant.

        Parameters:
        :   **Variant** – representation of the selection action

    virtual QVariantMap toVariantMap() const override
    :   Save selection action to variant.

        Returns:
        :   Variant representation of the selection action

    Protected Functions

    virtual void connectToPublicAction([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive) override
    :   Connect this action to a public action.

        Parameters:
        :   - **publicAction** – Pointer to public action to connect to
            - **recursive** – Whether to also connect descendant child actions

    virtual void disconnectFromPublicAction(bool recursive) override
    :   Disconnect this action from its public action.

        Parameters:
        :   **recursive** – Whether to also disconnect descendant child actions
