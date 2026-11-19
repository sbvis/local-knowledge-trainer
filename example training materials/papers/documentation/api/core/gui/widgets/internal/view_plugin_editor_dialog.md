# ViewPluginEditorDialog

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/view_plugin_editor_dialog.html

**Documentation path:** `api/core/gui/widgets/internal/view_plugin_editor_dialog.html`

---

# ViewPluginEditorDialog

**Qualified name:** `mv::gui::ViewPluginEditorDialog`

class ViewPluginEditorDialog : public QDialog
:   View plugin editor dialog class.

    Dialog class for editing view plugin properties such as the actions and docking properties

    **Author**
    :   Thomas Kroes

    Public Functions

    ViewPluginEditorDialog(QWidget \*parent, mv::plugin::[ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin") \*viewPlugin)
    :   Constructor for plugin-attached actions.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **viewPlugin** – Pointer to view plugin to edit

    ViewPluginEditorDialog(QWidget \*parent, mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*rootAction)
    :   Constructor for dataset-attached actions.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **rootAction** – Pointer to parent action of all actions to be displayed

    inline QSize sizeHint() const override
    :   Get preferred size.

    inline QSize minimumSizeHint() const override
    :   Get minimum size hint.
