# InfoAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/info_action.html

**Documentation path:** `api/core/gui/actions/point_data/info_action.html`

---

# InfoAction

**Qualified name:** `InfoAction`

class InfoAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction"), public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction"), public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction"), public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Info action class.

    Action class for displaying basic clusters info

    Action class for displaying basic images info

    **Author**
    :   Thomas Kroes

    Action class for displaying basic points info

    **Author**
    :   Thomas Kroes

    Action class for displaying text data info

    **Author**
    :   Thomas Kroes

    **Author**
    :   Julian Thijssen and Thomas Kroes

    Public Functions

    InfoAction(QObject \*parent, Clusters &clusters)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **clusters** – Reference to clusters dataset

    InfoAction(QObject \*parent, Images &images)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **images** – Reference to images dataset

    InfoAction(QObject \*parent, const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Points> &points)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **points** – Smart pointer to points dataset

    InfoAction(QObject \*parent, const mv::[Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<Text> &dataset)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **points** – Smart pointer to points dataset

    Protected Attributes

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_numberOfClustersAction
    :   Clusters dataset smart pointer.

    ClustersAction \_clustersAction
    :   Number of points action.

    mv::[EventListener](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_listener.html#_CPPv4N2mv13EventListenerE "mv::EventListener") \_eventListener
    :   Clusters action.

        Number of components action.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_typeAction
    :   Points dataset reference.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_numberOfImagesAction
    :   Image collection type action.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_imageResolutionAction
    :   Number of images action.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_numberOfPixelsAction
    :   Image resolution action.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_numberComponentsPerPixelAction
    :   Number of pixels per image action.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_dataStorageAction
    :   Points dataset reference.

        Text dataset reference.

    [ProxyDatasetsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/proxy_datasets_action.html#_CPPv419ProxyDatasetsAction "ProxyDatasetsAction") \_proxyDatasetsAction
    :   Type of data storage action.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_numberOfPointsAction
    :   Proxy datasets action.

        Type of data storage action.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_numberOfDimensionsAction
    :   Number of points action.

    mv::gui::[StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") \_rawDataSizeAction
    :   Number of dimensions action.

        Number of points action.

    [NumberOfSelectedPointsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/number_of_selected_points_action.html#_CPPv428NumberOfSelectedPointsAction "NumberOfSelectedPointsAction") \_numberOfSelectedPointsAction
    :   Amount of memory for raw data.

    [SelectedIndicesAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/point_data/selected_indices_action.html#_CPPv421SelectedIndicesAction "SelectedIndicesAction") \_selectedIndicesAction
    :   Number of selected points action.

    CreateSetFromSelectionAction \_createSetFromSelection
    :   Selected indices action.
