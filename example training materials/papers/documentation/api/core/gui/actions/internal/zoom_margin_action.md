# ZoomMarginAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/zoom_margin_action.html

**Documentation path:** `api/core/gui/actions/internal/zoom_margin_action.html`

---

# ZoomMarginAction

**Qualified name:** `mv::gui::ZoomMarginAction`

class ZoomMarginAction : public mv::gui::[VerticalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html#_CPPv4N2mv3gui19VerticalGroupActionE "mv::gui::VerticalGroupAction")
:   Zoom margin action class.

    Provides interface for setting the zoom margins

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE ZoomMarginAction(QObject \*parent, const QString &title)
    :   Construct with pointer to `parent` object and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load navigation action from variant map.

        Parameters:
        :   **variantMap** – Variant map representation of the navigation action

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action
