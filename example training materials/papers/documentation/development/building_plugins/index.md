# Building plugins

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/index.html

**Documentation path:** `development/building_plugins/index.html`

---

# Building plugins

Plugins are ManiVault’s primary extension mechanism. A plugin can introduce data storage, loading, analysis, transformation, visualization, or export while relying on the core for datasets, project state, execution, actions, and application integration.

## Choose a starting point

| Goal | Start here |
| --- | --- |
| Create a plugin and choose its type | [Plugin fundamentals](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/index.html) |
| Read, create, link, or observe datasets | [Working with data and datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/index.html) |
| Add persistent controls and settings | [Plugin actions and settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/actions/index.html) |
| Exchange state or request another plugin | [Plugin communication and creation triggers](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/index.html) |
| Run a long operation and report progress | [Long-running operations and task progress](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/index.html) |
| Save and restore plugin-owned state | [Project serialization and restoration](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/index.html) |
| Diagnose a failure or report it to the user | [Notifications, logging, errors, and diagnostics](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/index.html) |
| Integrate with application UI and help | See **Application integration** below |

If you are implementing a new plugin, follow Fundamentals first, then Data and Actions. Add the remaining sections when the plugin’s behavior requires them. Use the [core API reference](https://manivault.readthedocs.io/en/latest/api/core/index.html) for exact class and member signatures.

## Core plugin development

- [Plugin fundamentals](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/index.html)
- [Working with data and datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/index.html)
- [Plugin actions and settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/actions/index.html)
- [Plugin communication and creation triggers](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/index.html)

## Execution, state, and failures

- [Long-running operations and task progress](https://manivault.readthedocs.io/en/latest/development/building_plugins/tasks/index.html)
- [Project serialization and restoration](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/index.html)
- [Notifications, logging, errors, and diagnostics](https://manivault.readthedocs.io/en/latest/development/building_plugins/diagnostics/index.html)

## Application integration

- [Dataset drag and drop](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/index.html)
- [Icons](https://manivault.readthedocs.io/en/latest/development/building_plugins/icons.html)
- [Plugin creation policy and instance limits](https://manivault.readthedocs.io/en/latest/development/building_plugins/creation_policy/index.html)
- [Global plugin settings](https://manivault.readthedocs.io/en/latest/development/building_plugins/global_settings/index.html)
- [Status-bar integration](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/index.html)
- [Learning Center and shortcuts](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/index.html)
- [Qt plugin considerations](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/index.html)
