# ProxyDatasetsAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/proxy_datasets_action.html

**Documentation path:** `api/core/gui/actions/point_data/proxy_datasets_action.html`

---

# ProxyDatasetsAction

**Qualified name:** `ProxyDatasetsAction`

class ProxyDatasetsAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Proxy datasets action class.

    Action class for displaying the number of proxy datasets and providing an edit function

    **Author**
    :   Thomas Kroes

    Public Functions

    ProxyDatasetsAction(QObject \*parent, const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &points)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **points** – Smart pointer to points dataset

    void dimensionNamesChanged(const QStringList &dimensionNames)
    :   Signals that the dimension names changed.

        Parameters:
        :   **dimensionNames** – Dimension names

    Protected Functions

    inline virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the proxy datasets action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/proxy_datasets_action.html#classProxyDatasetsAction_1_1Widget) flags for the configuration of the widget (type)

    Protected Attributes

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_countAction
    :   Points dataset reference.

    [EditProxyDatasetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/edit_proxy_datasets_action.html#_CPPv423EditProxyDatasetsAction "EditProxyDatasetsAction") \_editProxyDatasetsAction
    :   Number of proxy datasets action.

    class Widget : public mv::gui::[WidgetActionWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/widget_action_widget.html#_CPPv4N2mv3gui18WidgetActionWidgetE "mv::gui::WidgetActionWidget")
    :   [Widget](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/proxy_datasets_action.html#classProxyDatasetsAction_1_1Widget) class for proxy datasets action.

        Public Functions

        Widget(QWidget \*parent, [ProxyDatasetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/proxy_datasets_action.html#_CPPv419ProxyDatasetsAction "ProxyDatasetsAction") \*proxyDatasetsAction)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **proxyDatasetsAction** – Pointer to proxy datasets action
