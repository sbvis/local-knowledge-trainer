# WidgetActionMimeData

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_mime_data.html

**Documentation path:** `api/core/gui/actions/internal/widget_action_mime_data.html`

---

# WidgetActionMimeData

**Qualified name:** `mv::gui::WidgetActionMimeData`

class WidgetActionMimeData : public QMimeData
:   Widget action mime data class.

    Class for drag-and-drop of a widget action

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetActionMimeData([WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Construct with `action`.

        Parameters:
        :   **action** – Pointer to action for dropping

    ~WidgetActionMimeData()
    :   Destructor.

    QStringList formats() const override
    :   Get supported mime types.

        Returns:
        :   List of string of supported mime types

    inline [WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction() const
    :   Get stored action.

        Returns:
        :   Pointer to stored widget action

    Public Static Functions

    static inline QString format()
    :   Supported mime type.
