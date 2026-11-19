# Workflow execution metrics

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_execution_metrics.html

**Documentation path:** `api/core/workflow/reporting/workflow_execution_metrics.html`

---

# Workflow execution metrics

The synchronized accumulator used to update and snapshot metrics during execution.

class WorkflowExecutionMetrics
:   Thread-safe accumulator for workflow execution metrics.

    Metrics are registered by name and then updated atomically during workflow execution. [snapshot()](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_execution_metrics.html#classmv_1_1workflow_1_1WorkflowExecutionMetrics_1ad7341ca0fc8e0d25e9e74839b7a6b76f) returns value objects suitable for reporting and notifications.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Functions

    void registerInteger(const QString &name, const QString &unit, QVariantMap metadata = {})
    :   Registers an integer metric.

        Parameters:
        :   - **name** – Metric name.
            - **unit** – Metric unit label.
            - **metadata** – Additional metric metadata.

    void registerDouble(const QString &name, const QString &unit, QVariantMap metadata = {})
    :   Registers a floating-point metric.

        Parameters:
        :   - **name** – Metric name.
            - **unit** – Metric unit label.
            - **metadata** – Additional metric metadata.

    void addInteger(const QString &name, std::uint64\_t amount)
    :   Adds to an integer metric.

        Parameters:
        :   - **name** – Metric name.
            - **amount** – Amount to add.

    void addDouble(const QString &name, double amount)
    :   Adds to a floating-point metric.

        Parameters:
        :   - **name** – Metric name.
            - **amount** – Amount to add.

    QVector<[WorkflowMetric](https://manivault.readthedocs.io/en/latest/api/core/workflow/reporting/workflow_metric.html#_CPPv4N2mv8workflow14WorkflowMetricE "mv::workflow::WorkflowMetric")> snapshot() const
    :   Returns all registered metrics.

        Returns:
        :   Snapshot of accumulated metric values.
