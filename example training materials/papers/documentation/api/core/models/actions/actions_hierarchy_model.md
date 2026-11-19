# ActionsHierarchyModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_hierarchy_model.html

**Documentation path:** `api/core/models/actions/actions_hierarchy_model.html`

---

# ActionsHierarchyModel

**Qualified name:** `mv::ActionsHierarchyModel`

class ActionsHierarchyModel : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")
:   Actions hierarchy model class.

    Hierarchical actions model class

    **Author**
    :   Thomas Kroes

    Public Functions

    ActionsHierarchyModel(QObject \*parent, gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*rootAction = nullptr)
    :   Construct with `parent` object and `rootAction`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **rootAction** – When set, only list the root action and its descendants

    virtual void initialize() override
    :   Initializes the model from the current state of the actions manager.

    Protected Functions

    virtual void actionAddedToManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) override
    :   Invoked when `action` is added to the actions manager.

        Parameters:
        :   **action** – Pointer to action that was added

    virtual void actionAboutToBeRemovedFromManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) override
    :   Invoked when `action` is about to be removed from the actions manager.

        Parameters:
        :   **action** – Pointer to action that was removed

    virtual void publicActionAddedToManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction) override
    :   Invoked when `publicAction` is added to the actions manager.

        Parameters:
        :   **publicAction** – Pointer to public action that was added

    virtual void publicActionAboutToBeRemovedFromManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction) override
    :   Invoked when `publicAction` is about to be removed from the actions manager.

        Parameters:
        :   **publicAction** – Pointer to public action to remove
