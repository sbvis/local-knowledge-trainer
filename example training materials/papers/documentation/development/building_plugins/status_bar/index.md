# Status-bar integration

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/index.html

**Documentation path:** `development/building_plugins/status_bar/index.html`

---

# Status-bar integration

The application status bar is appropriate for compact, persistent information or a small control that remains useful while users work. A plugin factory can register one `mv::gui::PluginStatusBarAction` shared by all instances of its plugin kind.

![Plugin status-bar action](https://manivault.readthedocs.io/en/latest/_images/plugin_status_bar_action.png)

The action can contain inline child actions, expose a richer popup action, or provide menu commands. `PluginStatusBarAction` additionally supports visibility based on whether its plugin kind has active instances.

Important

A plugin status-bar action is factory-wide, not instance-owned. When several instances exist, show aggregate state or provide a way to choose an instance; do not let whichever instance updated last silently represent the whole plugin kind.

- [Choosing status-bar content](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/choosing_content.html)
  - [Good status-bar content](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/choosing_content.html#good-status-bar-content)
  - [Avoid duplicate progress and errors](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/choosing_content.html#avoid-duplicate-progress-and-errors)
  - [Decide the scope](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/choosing_content.html#decide-the-scope)
- [Defining and registering an item](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/defining_and_registering.html)
  - [Derive a typed action](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/defining_and_registering.html#derive-a-typed-action)
  - [Register during factory initialization](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/defining_and_registering.html#register-during-factory-initialization)
  - [Registration timing](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/defining_and_registering.html#registration-timing)
- [Content and interaction](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/content_and_interaction.html)
  - [Inline actions](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/content_and_interaction.html#inline-actions)
  - [Popup content](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/content_and_interaction.html#popup-content)
  - [Menu actions](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/content_and_interaction.html#menu-actions)
  - [StatusAction](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/content_and_interaction.html#statusaction)
  - [Progress and long-running operations](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/content_and_interaction.html#progress-and-long-running-operations)
- [Lifecycle, visibility, and persistence](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/lifecycle_and_visibility.html)
  - [Conditional visibility](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/lifecycle_and_visibility.html#conditional-visibility)
  - [Application status-bar visibility](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/lifecycle_and_visibility.html#application-status-bar-visibility)
  - [Runtime updates](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/lifecycle_and_visibility.html#runtime-updates)
  - [Persistence](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/lifecycle_and_visibility.html#persistence)
- [Testing and pitfalls](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/testing_and_pitfalls.html)
  - [Verification checklist](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/testing_and_pitfalls.html#verification-checklist)
  - [Common pitfalls](https://manivault.readthedocs.io/en/latest/development/building_plugins/status_bar/testing_and_pitfalls.html#common-pitfalls)

For exact signatures, see the [PluginStatusBarAction API](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/plugin_status_bar_action.html), [StatusBarAction API](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_bar_action.html), and [StatusAction API](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/status_action.html).
