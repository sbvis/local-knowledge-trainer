# Raw data

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/raw_data/index.html

**Documentation path:** `api/core/models/raw_data/index.html`

---

# Raw data

Raw data is a crucial part of the dataset API. During its lifetime, raw data is tracked by the global [`mv::AbstractDataManager`](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_data_manager.html#_CPPv4N2mv19AbstractDataManagerE "mv::AbstractDataManager") with the use of dedicated models. The classes below are used to store, present and filter raw data.

Note

This API is **stable** and intended for use by **core developers**. Plugin developers should not interact with it directly, as it is fully wrapped by the data manager.

- [RawDataModel](https://manivault.readthedocs.io/en/latest/api/core/models/raw_data/raw_data_model.html)
- [RawDataFilterModel](https://manivault.readthedocs.io/en/latest/api/core/models/raw_data/raw_data_filter_model.html)
