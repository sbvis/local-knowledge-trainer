# Dataset events

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/events/index.html

**Documentation path:** `api/core/data/events/index.html`

---

# Dataset events

The dataset event API broadcasts lifecycle, content, dimensional, selection, hierarchy, and locking changes. `Dataset<T>` translates these events into per-handle Qt signals; `EventListener` supports broader observation and filtering.

Start with the [developer guide](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/events/index.html) to choose between per-handle signals and a broad listener. The pages below provide the exact API after that choice is clear.

- [Event listener](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_listener.html)
- [Event types](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html)
