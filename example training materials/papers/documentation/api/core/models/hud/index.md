# Heads-up-display

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/hud/index.html

**Documentation path:** `api/core/models/hud/index.html`

---

# Heads-up-display

A **heads-up-display** is used by **ManiVault** to overlay (textual) information on view plugins. The model classes below are for storing and filtering [`mv::util::HeadsUpDisplayItem`](https://manivault.readthedocs.io/en/latest/api/core/util/heads_up_display_item/heads_up_display_item.html#_CPPv4N2mv4util18HeadsUpDisplayItemE "mv::util::HeadsUpDisplayItem").

Note

This API is considered a **WIP**. Plugin developers typically do not need to interact with the models directly as it is wrapped by the [`mv::gui::ViewPluginHeadsUpDisplayAction`](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_heads_up_display.html#_CPPv4N2mv3gui30ViewPluginHeadsUpDisplayActionE "mv::gui::ViewPluginHeadsUpDisplayAction"). This action is a member of the [`mv::plugin::ViewPlugin`](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html#_CPPv4N2mv6plugin10ViewPluginE "mv::plugin::ViewPlugin"): `mv::plugin::ViewPlugin::getHeadsUpDisplayAction()`.

- [AbstractHeadsUpDisplayModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/abstract_heads_up_display_model.html)
- [HeadsUpDisplayTreeModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/heads_up_display_tree_model.html)
- [HeadsUpDisplayFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/hud/heads_up_display_filter_model.html)
