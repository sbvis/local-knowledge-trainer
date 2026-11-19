# ActionsListModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_list_model.html

**Documentation path:** `api/core/models/actions/actions_list_model.html`

---

# ActionsListModel

**Qualified name:** `mv::ActionsListModel`

class ActionsListModel : public mv::[AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html#_CPPv4N2mv20AbstractActionsModelE "mv::AbstractActionsModel")
:   Actions list model class.

    List model for actions derived from abstract actions model class

    When initialized with a root action, it lists the root action and its descendants, otherwise it just lists all the actions from the actions manager.

    **Author**
    :   Thomas Kroes

    Public Functions

    ActionsListModel(QObject \*parent = nullptr, gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*rootAction = nullptr)
    :   Construct with `parent` object and `rootAction`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **rootAction** – When set, only list the root action and its descendants

    virtual void initialize() override
    :   Initializes the model from the current state of the actions manager.

    gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getRootAction()
    :   Get root action.

        Returns:
        :   Pointer to root action (if any)

    void setRootAction(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*rootAction)
    :   Set root action to `rootAction`.

        Parameters:
        :   **rootAction** – When set, only list the root action and its descendants

    void rootActionChanged(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*rootAction)
    :   Signals that the root action changed to `rootAction`.

        Parameters:
        :   **rootAction** – Pointer to root action (if any)

    Protected Functions

    virtual void actionAddedToManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) override
    :   Helper method which is invoked when `action` is added to the actions manager.

        Parameters:
        :   **action** – Pointer to action that was added

    virtual void actionAboutToBeRemovedFromManager(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action) override
    :   Helper method which is invoked when `action` is about to be removed from the actions manager.

        Parameters:
        :   **action** – Pointer to action that was removed
