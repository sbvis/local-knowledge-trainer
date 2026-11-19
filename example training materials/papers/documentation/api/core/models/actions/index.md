# Actions

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/actions/index.html

**Documentation path:** `api/core/models/actions/index.html`

---

# Actions

Actions are re-usable GUI building blocks. During their lifetime, actions are tracked in a global [`mv::AbstractActionsManager`](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_actions_manager.html#_CPPv4N2mv22AbstractActionsManagerE "mv::AbstractActionsManager") with the use of dedicated actions models. The classes below are used to store, present and filter actions.

Note

This API is **stable** and intended for use by **core developers**. Plugin developers typically do not need to interact with it directly, as it is fully wrapped by the actions manager.

- [AbstractActionsModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/abstract_actions_model.html)
- [ActionsHierarchyModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_hierarchy_model.html)
- [ActionsListModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_list_model.html)
- [ActionsFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/actions/actions_filter_model.html)
