# What actions are

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/actions/what_are_actions.html

**Documentation path:** `development/building_plugins/actions/what_are_actions.html`

---

# What actions are

An action combines parameter or command state with the ability to create a user-interface representation. Plugins work with the action API; ManiVault supplies the standard Qt widgets and keeps multiple representations synchronized.

Common action families include:

- `StringAction` and `StringsAction` for text;
- `DecimalAction` and `IntegralAction` for numerical values;
- `OptionAction` and `OptionsAction` for choices;
- `ToggleAction` for boolean state;
- `TriggerAction` for commands;
- color and color-map actions;
- file and directory picker actions;
- dataset, plugin, dimension, and dimensions picker actions;
- group and toolbar actions for composition.

An action has a display title, globally unique ID, serialization name, QObject owner, enabled and visible state, widget configuration, and private or public scope. Concrete action types add their own value, range, options, and typed signals.

Use the narrowest concrete type that represents the setting. This provides suitable validation, serialization, signals, parameter compatibility, and standard widgets without custom plumbing.

The [actions API reference](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/index.html) lists the supported concrete types.
