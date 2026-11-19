# Learning Center and shortcuts

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/index.html

**Documentation path:** `development/building_plugins/learning_center/index.html`

---

# Learning Center and shortcuts

The Learning Center connects a plugin’s user-facing metadata, documentation, tutorials, videos, and shortcut reference to the places where users need them. View plugins receive an in-view overlay; the same global content is also available through ManiVault’s Learning Center and Help menu.

![Plugin Learning Center overlay](https://manivault.readthedocs.io/en/latest/_images/plugin_learning_center.gif)

Use this section to add discoverable help without implementing custom help menus or dialogs for every view.

- [Help, about information, and repository links](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/help_and_metadata.html)
- [Tutorials and videos](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/tutorials_and_videos.html)
- [Documenting plugin shortcuts](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/shortcuts.html)
- [View-plugin Learning Center overlay](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/view_overlay.html)
- [Testing and common pitfalls](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/testing_and_pitfalls.html)

## Mental model

| Layer | Responsibility | Ownership |
| --- | --- | --- |
| Global Help manager | Catalogs all tutorials and videos | Owns registered content objects through its models |
| Plugin factory and metadata | Description, about information, repository, README handling, shortcut map | One shared object per plugin kind |
| Plugin instance | Selects relevant tutorials and videos by pointer or tag | Holds non-owning associations |
| View-plugin overlay | Presents relevant help, counts, shortcuts, about information, and links | Created and managed by `ViewPlugin` |

Most plugin code should configure the factory metadata, register stable shortcut descriptions, and associate existing learning content through `getLearningCenterAction()`. The `PluginLearningCenterAction`, overlay widget, dialogs, and catalog models are core-managed implementation details; do not construct replacements unless developing the core itself.

For individual types and member signatures, use the [Learning Center API reference](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/index.html), [PluginShortcuts API reference](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_shortcuts.html), and [PluginLearningCenterAction API reference](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/plugin_learning_center_action.html).
