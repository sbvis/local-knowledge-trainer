# Project serialization and restoration

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/index.html

**Documentation path:** `development/building_plugins/persistence/index.html`

---

# Project serialization and restoration

Project persistence reconstructs datasets, hierarchy state, plugin instances, views, and settings as one coordinated operation. Plugin code contributes only the state it owns; the project manager controls the file operation, ordering, workflows, progress, and final lifecycle signals.

- [Defining plugin-owned state](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/plugin_state.html)
- [Persisting binary data as blob variant maps](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/binary_blob_data.html)
- [Synchronous and workflow serialization](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/synchronous_and_workflow.html)
- [Identity and persistent relationships](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/identity_and_relationships.html)
- [Project lifecycle](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/project_lifecycle.html)
- [Compatibility and round-trip testing](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/compatibility_and_testing.html)

For exact signatures, see [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html), the [blob serialization utilities](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serialization.html), and the [project manager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_project_manager.html).
