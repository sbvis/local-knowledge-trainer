# Requesting plugin instances

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/requesting_plugins.html

**Documentation path:** `development/building_plugins/communication/requesting_plugins.html`

---

# Requesting plugin instances

Use the plugin manager rather than calling a factory’s `produce()` directly. The manager checks the kind, enforces instance limits, initializes type-specific inputs, registers the instance, and handles view placement.

```cpp
auto* analysis = mv::plugins().requestPlugin<MyAnalysisPlugin>(
    "MyAnalysisPlugin",
    inputDatasets);

if (!analysis)
    return;
```

The generic request accepts input and output datasets. For analysis plugins the manager assigns both; transformation and writer plugins receive supported input context. A request for a view plugin is delegated to view creation when the project is not currently being restored.

## View placement

Use `requestViewPlugin()` when docking relative to another view matters, or `requestViewPluginFloated()` for a floating view. Pass datasets through the request so initialization follows the normal view-plugin path.

The returned pointer is borrowed from the plugin system. Do not delete it. If it must be retained, use a lifecycle-aware strategy such as `QPointer` and react to QObject destruction.

## Check availability when optional

When integration is optional, call `isPluginLoaded(kind)` or `getPluginFactory(kind)` before presenting the operation. A missing optional plugin should normally remove or disable the integration point rather than fail only after user invocation.

Calling `requestPlugin()` with an unknown kind or after reaching an instance limit fails through the core exception path. See [Lifetime and error handling](https://manivault.readthedocs.io/en/latest/development/building_plugins/communication/lifetime_and_errors.html).
