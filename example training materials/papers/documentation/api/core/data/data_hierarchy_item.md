# Data hierarchy item

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html

**Documentation path:** `api/core/data/data_hierarchy_item.html`

---

# Data hierarchy item

`DataHierarchyItem` represents a registered dataset in the application hierarchy. It maintains parentage, children, visibility, expansion, hierarchy selection, locking presentation, attached actions, and context-menu behavior.

For selection, presentation, attached-action, and lifetime patterns, see [Interacting with the data hierarchy](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/index.html).

class DataHierarchyItem : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Data hierarchy item class.

    Represents a dataset as an item in the data hierarchy, see the [AbstractDataHierarchyManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_hierarchy_manager.html#classmv_1_1AbstractDataHierarchyManager)

    **Author**
    :   Thomas Kroes

    Public Functions

    DataHierarchyItem([Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> dataset, [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> parentDataset, bool visible = true, bool selected = false)
    :   Construct with smart pointer to `dataset`, `parentDataset` and possible configure whether the item is `visible` and/or `selected`.

        Parameters:
        :   - **dataset** – Smart pointer to dataset
            - **parentDataset** – Smart pointer to parent dataset (if any)
            - **visible** – Whether the dataset is visible
            - **selected** – Whether the dataset is selected

    inline [DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*getParent() const
    :   Get parent item.

        Returns:
        :   Pointer to parent item (nullptr if the item has not parent item)

    inline void setParent([DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*parent)
    :   Set pointer to parent hierarchy item to `parent`.

        Parameters:
        :   **parent** – Pointer to parent hierarchy item (root item if nullptr)

    inline DataHierarchyItems getAncestors() const
    :   Get ancestors.

        Returns:
        :   Pointers to data hierarchy item ancestors (bottom-up)

    inline gui::WidgetActionsOfType<[DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem")> getChildren(bool recursively = false) const
    :   Get children, possibly `recursively`.

        Parameters:
        :   **recursively** – Get children recursively

        Returns:
        :   Vector of pointers to child items

    inline std::uint32\_t getNumberOfChildren(bool recursively = false) const
    :   Get number of children.

        Parameters:
        :   **recursively** – Count recursively @returm Number of children

    template<typename WidgetActionType = WidgetAction> inline bool hasChildren() const
    :   Establishes whether the item has any children.

        Returns:
        :   Boolean determining whether the item has any children

    inline std::int32\_t getDepth() const
    :   Get the depth of the item w.r.t.

        its furthest ancestor

        Returns:
        :   Item depth (root starts at zero)

    inline bool isChildOf([DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*item) const
    :   Determine whether the item is a child of `item`.

        Parameters:
        :   **item** – Item to check for

        Returns:
        :   Boolean determining whether `item` is an ancestor or not

    inline bool isChildOf(gui::WidgetActionsOfType<[DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem")> items) const
    :   Determine whether the item is a child of one of `items`.

        Parameters:
        :   **items** – Items to check for

        Returns:
        :   Boolean determining whether the action is child of one of `actions` or not

    void setVisible(bool visible, bool recursively = true)
    :   Set visibility to `visible` possibly `recursively`.

        Parameters:
        :   - **visible** – Whether the data hierarchy item is visible or not
            - **recursively** – Whether to set child data hierarchy items recursively or not

    bool isSelected() const
    :   Gets whether the hierarchy item is selected.

        Returns:
        :   Boolean determining whether the item is selected

    void setSelected(bool selected, bool clear = true)
    :   Sets the selection status to `selected` and possibly `clear` the global selection.

        Parameters:
        :   - **selected** – Whether the hierarchy item is selected
            - **clear** – Whether to clear the global data hierarchy selection

    void select(bool clear = true)
    :   Selects the data hierarchy item.

        Parameters:
        :   **clear** – Whether to clear the global data hierarchy selection

    void deselect()
    :   De-selects the hierarchy item.

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> getDataset()
    :   Get the dataset.

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4I0ENK2mv17DataHierarchyItem10getDatasetE7DatasetI11DatasetTypeEv "mv::DataHierarchyItem::getDataset::DatasetType")> getDataset() const
    :   Get the dataset as `DatasetType`.

    [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetImpl](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html#_CPPv4N2mv11DatasetImplE "mv::DatasetImpl")> &getDatasetReference()
    :   Get reference to dataset smart pointer.

        Returns:
        :   Reference to dataset smart pointer

    template<typename DatasetType> inline [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html#_CPPv4I0EN2mv7DatasetE "mv::Dataset")<[DatasetType](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4I0ENK2mv17DataHierarchyItem19getDatasetReferenceER7DatasetI11DatasetTypeEv "mv::DataHierarchyItem::getDatasetReference::DatasetType")> &getDatasetReference() const
    :   Get reference to dataset smart pointer of a specific type.

        Returns:
        :   Reference to dataset smart pointer of a specific type

    [DataType](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html#_CPPv4N2mv8DataTypeE "mv::DataType") getDataType() const
    :   Get the dataset type.

        Returns:
        :   The dataset type

    void addAction(mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") &widgetAction)
    :   Attach `widgetAction`.

        Parameters:
        :   **widgetAction** – Reference to widget action to attach

    mv::gui::WidgetActions getActions() const
    :   Returns list of shared action widgets.

    virtual QMenu \*getContextMenu(QWidget \*parent = nullptr) override
    :   Get the context menu.

        Parameters:
        :   **parent** – Parent widget

        Returns:
        :   Context menu

    void populateContextMenu(QMenu \*contextMenu)
    :   Populates existing menu with actions menus.

        Parameters:
        :   **contextMenu** – Context menu to populate

    void lock(bool cache = false)
    :   Lock the dataset and possibly `cache` the current lock state.

        Parameters:
        :   **cache** – Whether to cache the current lock state

    void unlock(bool cache = false)
    :   Unlock the dataset and possibly `cache` the current lock state.

        Parameters:
        :   **cache** – Whether to cache the current lock state

    bool isLocked() const
    :   Get whether the dataset is locked.

        Returns:
        :   Boolean indicating whether the dataset is locked

    void setLocked(bool locked, bool cache = false)
    :   Set whether the dataset is `locked` and possibly `cache` the current lock state.

        Parameters:
        :   - **locked** – Boolean indicating whether the dataset is locked
            - **cache** – Whether to cache the current lock state

    void restoreLockedFromCache()
    :   Restore the lock status to the cached value.

    bool isExpanded() const
    :   Get expanded status.

        Returns:
        :   Boolean indicating whether the item is expanded or not

    void setExpanded(bool expanded)
    :   Set expanded status to `expanded`.

        Parameters:
        :   **expanded** – Boolean determining whether the dataset is expanded or not

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Initialize the data hierarchy item from `variantMap`.

        Parameters:
        :   **variantMap** – Variant map representation of the data hierarchy item

    virtual QVariantMap toVariantMap() const override
    :   Save widget action to variant map.

        Returns:
        :   Variant map representation of the widget action

    void selectedChanged(bool selected)
    :   Signals that item selection changed to `selected`.

        Parameters:
        :   **selected** – Whether the item is selected or not

    void actionAdded(mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") &widgetAction)
    :   Signals that `widgetAction` was attached to the data hierarchy item.

        Parameters:
        :   **widgetAction** – Reference to the widget action that was added

    void iconChanged()
    :   Signals that the set icon has changed.

    void datasetNameChanged(const QString &datasetName)
    :   Signals that the dataset name changed to `datasetName`.

        Parameters:
        :   **datasetName** – New name of the dataset

    void lockedChanged(bool locked)
    :   Signals that the locked status changed to `locked`.

        Parameters:
        :   **locked** – Locked

    void visibilityChanged(bool visibility)
    :   Signals that the visibility changed to `visibility`.

        Parameters:
        :   **visibility** – Visibility

    void expandedChanged(bool expanded)
    :   Signals that the expansion changed `expanded`.

        Parameters:
        :   **expanded** – Whether the item is expanded or not

    void parentChanged([DataHierarchyItem](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html#_CPPv4N2mv17DataHierarchyItemE "mv::DataHierarchyItem") \*parent)
    :   Signals that the parent changed to `parent`.

        Parameters:
        :   **parent** – Pointer to parent data hierarchy item (might be nullptr)
