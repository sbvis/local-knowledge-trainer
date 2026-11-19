# Dataset drag and drop

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/index.html

**Documentation path:** `development/building_plugins/drag_and_drop/index.html`

---

# Dataset drag and drop

Drag and drop lets users connect datasets to a plugin directly from the data hierarchy. `mv::gui::DropWidget` adds this interaction to an existing widget and presents one or more temporary regions describing what a drop will do.

![Drag-and-drop behaviour in action](https://manivault.readthedocs.io/en/latest/_images/drag_and_drop.gif)

The normal flow is:

1. Enable drops on the target widget and attach a `DropWidget` to it.
2. Inspect the incoming `QMimeData` as `mv::DatasetsMimeData`.
3. Validate the number, type, and state of the dragged datasets.
4. Return regions for the operations that make sense for that drag.
5. Retain dataset handles, update actions, or start work from the selected region’s callback.

The callback that supplies regions is a negotiation step, not the place to perform the operation. It runs when a drag enters the target; the selected region’s callback runs only when the user drops onto it.

- [Accepting datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/accepting_datasets.html)
  - [Set up the target](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/accepting_datasets.html#set-up-the-target)
  - [Inspect and validate the payload](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/accepting_datasets.html#inspect-and-validate-the-payload)
  - [Retain the handle, not a raw pointer](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/accepting_datasets.html#retain-the-handle-not-a-raw-pointer)
- [Designing drop regions](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/drop_regions.html)
  - [Rejection and explanation](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/drop_regions.html#rejection-and-explanation)
  - [Custom region widgets](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/drop_regions.html#custom-region-widgets)
  - [One drag, multiple datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/drop_regions.html#one-drag-multiple-datasets)
- [Indicators, events, and lifetime](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/indicators_and_lifetime.html)
  - [Empty-state indicator](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/indicators_and_lifetime.html#empty-state-indicator)
  - [Event sequence](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/indicators_and_lifetime.html#event-sequence)
  - [Ownership](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/indicators_and_lifetime.html#ownership)
- [Recipes and testing](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/recipes_and_testing.html)
  - [Replace or add](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/recipes_and_testing.html#replace-or-add)
  - [Accept compatible derived datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/recipes_and_testing.html#accept-compatible-derived-datasets)
  - [Start long-running work](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/recipes_and_testing.html#start-long-running-work)
  - [Testing checklist](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/recipes_and_testing.html#testing-checklist)
  - [Common pitfalls](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/recipes_and_testing.html#common-pitfalls)

For exact signatures, see the [DropWidget API reference](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html) and [DatasetsMimeData API reference](https://manivault.readthedocs.io/en/latest/api/core/data/datasets_mime_data.html).
