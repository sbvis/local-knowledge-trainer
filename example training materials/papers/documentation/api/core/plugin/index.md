# Plugin

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/index.html

**Documentation path:** `api/core/plugin/index.html`

---

# Plugin

Plugins are the primary extension mechanism in ManiVault. They allow new functionality to be added to the platform without modifying the core application, enabling features such as data loading, analysis, transformation, visualization, and export to be developed and deployed independently.

Each plugin follows a common lifecycle defined by the plugin base class and is instantiated through a plugin factory. Depending on their role, plugins are categorized into specific types that determine how they integrate with the application and interact with data and user workflows.

The sections below describe the core building blocks of the plugin system, the available plugin types, and supporting classes used for metadata and shortcut configuration.

For lifecycle, ownership, input, and implementation guidance, start with [Plugin fundamentals](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/index.html). The pages below are the accompanying API reference.

## Base class and factory

All **ManiVault** plugins are derived from a generic **plugin** base class and are created by a **plugin factory**.

- [Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html)
- [PluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_factory.html)

## Types

ManiVault plugins are categorized by their primary role within the platform. There are plugins for reading, writing, analyzing, transforming and viewing data. The classes below are all derived from the [plugin base class](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html).

Each runtime role has a matching factory specialization. Derive the instance and factory from the same pair, and return the matching instance type from `produce()`. Creation must still be requested through the plugin manager; `produce()` is the factory hook used by that managed path, not a public construction shortcut.

| Role | Instance | Factory |
| --- | --- | --- |
| Analysis | [AnalysisPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html) | [AnalysisPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin_factory.html) |
| Loader | [LoaderPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin.html) | [LoaderPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin_factory.html) |
| Transformation | [TransformationPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin.html) | [TransformationPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin_factory.html) |
| View | [ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html) | [ViewPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin_factory.html) |
| Writer | [WriterPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin.html) | [WriterPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin_factory.html) |

The data-role pair, `RawData` and `RawDataFactory`, is documented with the [data API](https://manivault.readthedocs.io/en/latest/api/core/data/index.html) because it defines dataset storage rather than an operation over existing datasets.

- [AnalysisPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin.html)
- [AnalysisPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/analysis_plugin_factory.html)
- [LoaderPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin.html)
- [LoaderPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin_factory.html)
- [DataLoadException](https://manivault.readthedocs.io/en/latest/api/core/plugin/data_load_exception.html)
- [TransformationPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin.html)
- [TransformationPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/transformation_plugin_factory.html)
- [ViewPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin.html)
- [ViewPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/view_plugin_factory.html)
- [WriterPlugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin.html)
- [WriterPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/writer_plugin_factory.html)

## Miscellaneous

The class below are used to compose a plugin shortcut map and adding plugin metadata.

- [PluginShortcuts](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_shortcuts.html)
- [PluginMetadata](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin_metadata.html)
