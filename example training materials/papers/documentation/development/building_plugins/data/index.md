# Working with data and datasets

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/data/index.html

**Documentation path:** `development/building_plugins/data/index.html`

---

# Working with data and datasets

Datasets are ManiVault’s central data abstraction. Plugins exchange `Dataset<T>` handles, while the core owns the corresponding `DatasetImpl` objects, registers them with the data manager, places them in the data hierarchy, maintains selections, and broadcasts lifecycle events.

This guide explains the model from a plugin developer’s perspective: how to safely retain and access datasets, create new data, represent derived data and subsets, react to changes and removal, and implement a new data type.

Important

Do not treat `Dataset<T>` as an owning smart pointer. It is an event-aware reference managed around a core-owned dataset. Always check `isValid()` before dereferencing it, particularly across event-loop turns and asynchronous work.

## Recommended path

Begin with the mental model and dataset handles. Continue with creation and hierarchy for ordinary plugin development. The final pages cover selection propagation, events, and implementing a new raw-data plugin.

- [Mental model](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/mental_model.html)
  - [The principal types](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/mental_model.html#the-principal-types)
  - [Ownership](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/mental_model.html#ownership)
  - [Three independent relationships](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/mental_model.html#three-independent-relationships)
  - [Storage and proxy datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/mental_model.html#storage-and-proxy-datasets)
- [Dataset handles](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/dataset_handles.html)
  - [Validity and access](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/dataset_handles.html#validity-and-access)
  - [Typed conversion](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/dataset_handles.html#typed-conversion)
  - [Retaining handles](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/dataset_handles.html#retaining-handles)
  - [Signals](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/dataset_handles.html#signals)
- [Accessing and finding data](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/accessing_data.html)
  - [By identifier](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/accessing_data.html#by-identifier)
  - [Enumerating datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/accessing_data.html#enumerating-datasets)
  - [Data types and kinds](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/accessing_data.html#data-types-and-kinds)
  - [Concrete data access](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/accessing_data.html#concrete-data-access)
  - [Properties](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/accessing_data.html#properties)
- [Creating and removing datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/creating_datasets.html)
  - [Hierarchy parent](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/creating_datasets.html#hierarchy-parent)
  - [Initialization order](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/creating_datasets.html#initialization-order)
  - [Removing data](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/creating_datasets.html#removing-data)
  - [Batch removal](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/creating_datasets.html#batch-removal)
- [Interacting with the data hierarchy](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/index.html)
  - [Choose the right abstraction](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy/index.html#choose-the-right-abstraction)
- [Hierarchy, derived data, and subsets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy_derived_and_subsets.html)
  - [Data hierarchy](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy_derived_and_subsets.html#data-hierarchy)
  - [Derived datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy_derived_and_subsets.html#derived-datasets)
  - [Subsets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy_derived_and_subsets.html#subsets)
  - [Proxy datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy_derived_and_subsets.html#proxy-datasets)
  - [Do not infer semantics from the tree](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/hierarchy_derived_and_subsets.html#do-not-infer-semantics-from-the-tree)
- [Selections and linked data](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/selections_and_linked_data.html)
  - [Selection datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/selections_and_linked_data.html#selection-datasets)
  - [Selection notifications](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/selections_and_linked_data.html#selection-notifications)
  - [Linked data](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/selections_and_linked_data.html#linked-data)
  - [Selection groups and proxies](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/selections_and_linked_data.html#selection-groups-and-proxies)
- [Dataset events and listeners](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/events/index.html)
  - [Choose the narrowest subscription](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/events/index.html#choose-the-narrowest-subscription)
- [Implementing a data type](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/implementing_a_data_type.html)
  - [Raw-data plugin](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/implementing_a_data_type.html#raw-data-plugin)
  - [Concrete dataset](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/implementing_a_data_type.html#concrete-dataset)
  - [Full data, selections, and subsets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/implementing_a_data_type.html#full-data-selections-and-subsets)
  - [Notifications](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/implementing_a_data_type.html#notifications)
  - [Serialization](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/implementing_a_data_type.html#serialization)
  - [Checklist](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/implementing_a_data_type.html#checklist)

For exact signatures, see the [core data API reference](https://manivault.readthedocs.io/en/latest/api/core/data/index.html).
