# AbstractActionsManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_actions_manager.html

**Documentation path:** `api/core/managers/abstract_actions_manager.html`

---

# AbstractActionsManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the actions manager
mv::actions()->...
```

## Related

- Actions [models](https://manivault.readthedocs.io/en/latest/api/core/models/actions/index.html)

**Qualified name:** `mv::AbstractActionsManager`

class AbstractActionsManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract actions manager.

    Base abstract actions manager class for managing widget actions.

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractActionsManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    inline const gui::WidgetActions &getActions() const
    :   Get all actions in the manager.

        Returns:
        :   List of all actions in the manager

    inline const gui::WidgetActions &getPublicActions() const
    :   Get all public actions in the manager.

        Returns:
        :   List of all public actions in the manager

    inline gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*getAction(const QString &id)
    :   Get action with `id`.

        Returns:
        :   Pointer to widget action (may return nullptr)

    template<typename ActionType> inline void addAction([ActionType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_actions_manager.html#_CPPv4I0EN2mv22AbstractActionsManager9addActionEvP10ActionType "mv::AbstractActionsManager::addAction::ActionType") \*action)
    :   Add `action` of action type to the manager.

        Parameters:
        :   **action** – Pointer to action

    template<typename ActionType> inline void removeAction([ActionType](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_actions_manager.html#_CPPv4I0EN2mv22AbstractActionsManager12removeActionEvP10ActionType "mv::AbstractActionsManager::removeAction::ActionType") \*action)
    :   Remove `action` of action type from the manager.

        Parameters:
        :   **action** – Pointer to action

    virtual bool publishPrivateAction(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*privateAction, const QString &name = "", bool recursive = true, bool allowDuplicateName = false) = 0
    :   Publish `privateAction` so that other private actions can connect to it.

        Parameters:
        :   - **privateAction** – Pointer to private action to publish
            - **name** – Name of the published widget action (if empty, a name choosing dialog will popup)
            - **recursive** – Whether to also publish the child actions recursively
            - **allowDuplicateName** – Boolean determining whether publishing will take place when a public with the same name already exists in the public actions database

        Returns:
        :   Boolean determining whether the action is successfully published or not

    inline void connectPrivateActionToPublicAction(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*privateAction, gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction, bool recursive)
    :   Connect `privateAction` to `publicAction`.

        Parameters:
        :   - **privateAction** – Pointer to private action
            - **publicAction** – Pointer to public action
            - **recursive** – Whether to also connect descendant child actions

    inline void connectPrivateActions(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*privateSourceAction, gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*privateTargetAction, const QString &publicActionName = "")
    :   Connect `privateSourceAction` to `privateTargetAction`.

        Parameters:
        :   - **privateSourceAction** – Pointer to private source action
            - **privateTargetAction** – Pointer to private target action (private source action will be connected to published private target action)
            - **publicActionName** – Name of the public action (ask for name if empty)

    inline void disconnectPrivateActionFromPublicAction(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*privateAction, bool recursive)
    :   Disconnect `privateAction` from public action.

        Parameters:
        :   - **privateAction** – Pointer to private action
            - **recursive** – Whether to also disconnect descendant child actions

    inline QStringList getActionTypes() const
    :   Get set of action types.

        Returns:
        :   List of action types

    inline QStringList getActionTypesHumanFriendly() const
    :   Get set of human-friendly action types (without prefixes)

        Returns:
        :   List of human-friendly action types

    void actionAdded(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Signals that `action` is added to the manager.

        Parameters:
        :   **action** – Pointer to action that is added to the manager

    void actionAboutToBeRemoved(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Signals that `action` is about to be removed from the manager.

        Parameters:
        :   **action** – Pointer to action that is about to be removed from the manager

    void actionRemoved(const QString &actionId)
    :   Signals that action with `actionId` was removed from the manager.

        Parameters:
        :   **actionId** – Globally unique identifier of the action that was removed from the manager

    void publicActionAdded(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction)
    :   Signals that `publicAction` is added to the manager.

        Parameters:
        :   **publicAction** – Pointer to public action that is added to the manager

    void publicActionAboutToBeRemoved(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction)
    :   Signals that `publicAction` is about to be removed from the manager.

        Parameters:
        :   **publicAction** – Pointer to public action that is about to be removed from the manager

    void publicActionRemoved(const QString &publicActionId)
    :   Signals that public action with `publicActionId` was removed from the manager.

        Parameters:
        :   **publicActionId** – Globally unique identifier of the public action that was removed from the manager

    void actionTypeAdded(const QString &actionType)
    :   Signals that a new `actionType` has been added to the manager.

        Parameters:
        :   **actionType** – Action type

    void actionTypeRemoved(const QString &actionType)
    :   Signals that the last instance of `actionType` has been removed from the manager.

        Parameters:
        :   **actionType** – Action type

    void actionTypesChanged(const QStringList &actionTypes)
    :   Signals that the `actionTypes` changed.

        Parameters:
        :   **actionTypes** – Action types

    void actionTypesHumanFriendlyChanged(const QStringList &actionTypesHumanFriendly)
    :   Signals that the human-friendly `actionTypes` changed.

        Parameters:
        :   **actionTypesHumanFriendly** – Human-friendly action types

    Protected Functions

    inline void addPrivateActionToPublicAction(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*privateAction, gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction)
    :   Add `privateAction` to the list of connected actions in the `publicAction` and notify listeners.

        Parameters:
        :   - **privateAction** – Pointer to private action
            - **publicAction** – Pointer to public action

    inline void removePrivateActionFromPublicAction(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*privateAction, gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*publicAction)
    :   Remove `privateAction` from the list of connected actions in the `publicAction` and notify listeners.

        Parameters:
        :   - **privateAction** – Pointer to private action
            - **publicAction** – Pointer to public action

    inline void addActionType(const QString &actionType)
    :   Add `actionType` string.

        Parameters:
        :   **actionType** – Action type string to add

    inline void removeActionType(const QString &actionType)
    :   Remove `actionType` string.

        Parameters:
        :   **actionType** – Action type string to remove

    inline void makeActionPublic(gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction") \*action)
    :   Make widget `action` public.

        Parameters:
        :   **action** – Pointer to action

    Protected Attributes

    gui::WidgetActions \_publicActions
    :   List of actions that are instantiated in the plugin system.

    QMap<QString, ActionType> \_actionTypes
    :   List of public actions that are instantiated in the plugin system.

    Friends

    *friend class* gui::WidgetAction
