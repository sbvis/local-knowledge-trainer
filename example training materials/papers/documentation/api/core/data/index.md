# Data and datasets

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/index.html

**Documentation path:** `api/core/data/index.html`

---

# Data and datasets

The data API defines ManiVault’s central runtime data model. `Dataset<T>` is the event-aware handle used by consumers, `DatasetImpl` is the common implementation base, and raw-data plugins provide concrete data kinds. Supporting types describe identity, hierarchy placement, linked selections, and dataset lifecycle events.

For ownership rules, relationship semantics, and examples, begin with [Working with data and datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/index.html).

## Dataset model

- [Dataset](https://manivault.readthedocs.io/en/latest/api/core/data/dataset.html)
- [Dataset implementation](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_impl.html)
- [Dataset handle state](https://manivault.readthedocs.io/en/latest/api/core/data/dataset_private.html)
- [Data type](https://manivault.readthedocs.io/en/latest/api/core/data/data_type.html)
- [Data hierarchy item](https://manivault.readthedocs.io/en/latest/api/core/data/data_hierarchy_item.html)
- [DatasetsMimeData](https://manivault.readthedocs.io/en/latest/api/core/data/datasets_mime_data.html)

## Data plugins

- [Raw data plugin](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data.html)
- [Raw data factory](https://manivault.readthedocs.io/en/latest/api/core/data/raw_data_factory.html)

## Relationships and events

- [Linked data](https://manivault.readthedocs.io/en/latest/api/core/data/linked_data.html)
- [Selection map](https://manivault.readthedocs.io/en/latest/api/core/data/selection_map.html)
- [Dataset events](https://manivault.readthedocs.io/en/latest/api/core/data/events/index.html)
  - [Event listener](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_listener.html)
  - [Event types](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html)

## Related managers and models

- [AbstractDataManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html) owns and manages registered datasets.
- [AbstractDataHierarchyManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_hierarchy_manager.html) manages hierarchy items and hierarchy selection.
- Dataset [models](https://manivault.readthedocs.io/en/latest/api/core/models/datasets/index.html) expose registered datasets to Qt views.
- Data-hierarchy [models](https://manivault.readthedocs.io/en/latest/api/core/models/data_hierarchy/index.html) expose the hierarchy to Qt views.
