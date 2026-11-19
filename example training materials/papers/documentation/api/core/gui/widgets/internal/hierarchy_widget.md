# HierarchyWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/hierarchy_widget.html

**Documentation path:** `api/core/gui/widgets/internal/hierarchy_widget.html`

---

# HierarchyWidget

**Qualified name:** `mv::gui::HierarchyWidget`

class HierarchyWidget : public QWidget, public mv::util::[Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable")
:   Base widget for displaying a hierarchical model in a tree view.

    It sets up the tree view and links up the filter and selection models.

    Features a toolbar for interaction with the model built with actions:

    - Filter by name (possibly with regular expression)
    - Expanding all items
    - Collapsing all items
    - Selecting all items
    - De-selecting all items
    - Edit settings

    In addition, it shows an overlay widget (with icon, title and description) when no items are loaded or filtering did not yield any items.

    **Author**
    :   Thomas Kroes

    Public Functions

    HierarchyWidget(QWidget \*parent, const QString &itemTypeName, const QAbstractItemModel &model, QSortFilterProxyModel \*filterModel = nullptr, bool showToolbar = true, bool showOverlay = true)
    :   Constructor.

        Parameters:
        :   - **parent** – Parent widget
            - **itemTypeName** – Type name of the item (e.g. dataset or action)
            - **model** – Reference to input model
            - **filterModel** – Pointer to input filter model (if present)
            - **showToolbar** – Whether to add a default toolbar for filtering and expand/collapse
            - **showOverlay** – Whether to show an overlay when the (filter) model is empty

    QString getItemTypeName() const
    :   Get item type name.

        Returns:
        :   Item type name

    void setItemTypeName(const QString &itemTypeName)
    :   Set item type name to `itemTypeName`.

        Returns:
        :   Item type name

    void setWindowIcon(const QIcon &icon)
    :   Override set window icon to update the overlay icons as well.

        Parameters:
        :   **icon** – Window icon

    void setNoItemsDescription(const QString &noItemsDescription)
    :   Set overlay widget description when no items are loaded.

        Parameters:
        :   **noItemsDescription** – Overlay widget description when no items are loaded

    bool getHeaderHidden() const
    :   Get whether the header view is visible or not.

        Returns:
        :   Boolean determining whether the header view is visible or not

    void setHeaderHidden(bool headerHidden)
    :   Set whether the header view is visible or not.

        Parameters:
        :   **headerHidden** – Boolean determining whether the header view is visible or not

    inline const QAbstractItemModel &getModel()
    :   Get input model.

        Returns:
        :   Input model

    inline QSortFilterProxyModel \*getFilterModel()
    :   Set input model to `model`.

        Parameters:
        :   **model** – Input model Get input filter model

        Returns:
        :   Pointer to input filter model

    inline QItemSelectionModel &getSelectionModel()
    :   Get selection model.

        Returns:
        :   Reference to selection model

    inline HierarchyWidgetTreeView &getTreeView()
    :   Get tree view widget.

        Returns:
        :   Reference to tree view widget

    inline [InfoOverlayWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/info_overlay_widget.html#_CPPv4N2mv3gui17InfoOverlayWidgetE "mv::gui::InfoOverlayWidget") \*getInfoOverlayWidget()
    :   Get overlay widget.

        Returns:
        :   Pointer to overlay widget

    inline [StringAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/textual/string_action.html#_CPPv4N2mv3gui12StringActionE "mv::gui::StringAction") &getFilterNameAction()
    :   Get filter name action.

        Returns:
        :   Reference to filter name action

    inline [OptionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/option_action.html#_CPPv4N2mv3gui12OptionActionE "mv::gui::OptionAction") &getFilterColumnAction()
    :   Get filter column action.

        Returns:
        :   Reference to filter column action

    inline [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") &getFilterGroupAction()
    :   Get filter group action.

        Returns:
        :   Reference to filter group action

    inline [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getFilterRegularExpressionAction()
    :   Get filter regular expression action.

        Returns:
        :   Reference to filter regular expression action

    inline [ToggleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/toggle/toggle_action.html#_CPPv4N2mv3gui12ToggleActionE "mv::gui::ToggleAction") &getFilterCaseSensitiveAction()
    :   Get filter case sensitive action.

        Returns:
        :   Reference to filter case sensitive action

    inline [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") &getExpandAllAction()
    :   Get expand all action.

        Returns:
        :   Reference to expand all action

    inline [TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction") &getCollapseAllAction()
    :   Get collapse all action.

        Returns:
        :   Reference to collapse all action

    inline [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") &getSelectionGroupAction()
    :   Get selection group action.

        Returns:
        :   Reference to selection group action

    inline [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") &getColumnsGroupAction()
    :   Get columns group action.

        Returns:
        :   Reference to columns group action

    inline [GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction") &getSettingsGroupAction()
    :   Get selection group action.

        Returns:
        :   Reference to selection group

    QModelIndex toSourceModelIndex(const QModelIndex &modelIndex) const
    :   Maps a model index to source model index.

        Parameters:
        :   **modelIndex** – Model index to map

        Returns:
        :   The mapped model index if a filter model is present, other wise the input model index

    QModelIndexList getSelectedRows() const
    :   Get selected rows.

        Returns:
        :   Model indices of the selected rows

    QModelIndexList fetchFilterModelIndices(QModelIndex filterModelIndex = QModelIndex()) const
    :   Fetches filter model indices of `filterModelIndex` and its children recursively.

        Parameters:
        :   **filterModelIndex** – Filter model index

        Returns:
        :   Fetched filter model indices

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load from variant map.

        Parameters:
        :   **variantMap** – Variant map

    virtual QVariantMap toVariantMap() const override
    :   Save to variant map.

        Returns:
        :   Variant map

    Protected Functions

    bool mayExpandAll() const
    :   Get whether one or more items may be expanded.

        Returns:
        :   Boolean indicating whether one or more items may be expanded

    void expandAll()
    :   Expand all items in the hierarchy.

    bool mayCollapseAll() const
    :   Get whether one or more items may be collapse.

        Returns:
        :   Boolean indicating whether one or more items may be collapse

    void collapseAll()
    :   Collapse all items in the hierarchy.

    bool maySelectAll() const
    :   Get whether all items may be selected.

        Returns:
        :   Boolean determining whether all items may be selected

    void selectAll()
    :   Select all items in the hierarchy.

    bool maySelectNone() const
    :   Get whether one (or more) items can be de-selected.

        Returns:
        :   Boolean determining whether one (or more) items can be de-selected

    void selectNone()
    :   Deselect all selected items in the hierarchy.

    void updateHeaderVisibility()
    :   Updates the visibility of the header.
