# Workflow batching options

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_batching_options.html

**Documentation path:** `api/core/workflow/planning/workflow_batching_options.html`

---

# Workflow batching options

Conservative batch-size helpers for resource-intensive parallel operations.

struct WorkflowBatchingOptions
:   Configures workflow serialization batch sizes.

    These options bound how many datasets or data blocks may be processed in parallel during loading, saving, encoding, and decoding.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Members

    std::size\_t datasetLoadingBatchSize = [conservativeDatasetsSerializationBatchSize](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_batching_options.html#_CPPv4N2mv8workflow23WorkflowBatchingOptions42conservativeDatasetsSerializationBatchSizeEv "mv::workflow::WorkflowBatchingOptions::conservativeDatasetsSerializationBatchSize")()
    :   Number of datasets to load in parallel.

    std::size\_t datasetSavingBatchSize = [conservativeDatasetsSerializationBatchSize](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_batching_options.html#_CPPv4N2mv8workflow23WorkflowBatchingOptions42conservativeDatasetsSerializationBatchSizeEv "mv::workflow::WorkflowBatchingOptions::conservativeDatasetsSerializationBatchSize")()
    :   Number of datasets to save in parallel.

    std::size\_t dataBlockEncodingBatchSize = [conservativeBlockSerializationBatchSize](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_batching_options.html#_CPPv4N2mv8workflow23WorkflowBatchingOptions39conservativeBlockSerializationBatchSizeEv "mv::workflow::WorkflowBatchingOptions::conservativeBlockSerializationBatchSize")()
    :   Number of data blocks to encode in parallel.

    std::size\_t dataBlockDecodingBatchSize = [conservativeBlockSerializationBatchSize](https://manivault.readthedocs.io/en/latest/api/core/workflow/planning/workflow_batching_options.html#_CPPv4N2mv8workflow23WorkflowBatchingOptions39conservativeBlockSerializationBatchSizeEv "mv::workflow::WorkflowBatchingOptions::conservativeBlockSerializationBatchSize")()
    :   Number of data blocks to decode in parallel.

    Public Static Functions

    static std::size\_t conservativeDatasetsSerializationBatchSize()
    :   Returns the conservative dataset batch size.

        Returns:
        :   Number of datasets to process concurrently.

    static std::size\_t conservativeBlockSerializationBatchSize()
    :   Returns the conservative data-block batch size.

        Returns:
        :   Number of data blocks to process concurrently.
