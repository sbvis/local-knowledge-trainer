# Workflow progress node

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html

**Documentation path:** `api/core/workflow/progress/workflow_progress_node.html`

---

# Workflow progress node

A hierarchical progress node with weighted aggregation, status, and snapshot support.

class WorkflowProgressNode : public std::enable\_shared\_from\_this<[WorkflowProgressNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNodeE "mv::workflow::WorkflowProgressNode")>
:   Tracks progress for a workflow execution node.

    [WorkflowProgressNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#classmv_1_1workflow_1_1WorkflowProgressNode) mirrors the hierarchy created by [WorkflowExecutionContext](https://manivault.readthedocs.io/en/latest/api/core/workflow/context/workflow_execution_context.html#classmv_1_1workflow_1_1WorkflowExecutionContext). Leaf nodes store explicit progress values, while parent nodes derive their progress from the weighted average of their children. This allows the root node to represent aggregate progress for the entire workflow execution.

    The class is designed for concurrent workflow execution. Public accessors and mutators synchronize access internally, and [createSnapshot()](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#classmv_1_1workflow_1_1WorkflowProgressNode_1a02bfe06deff5373b82cbf7d48e181205) returns a value tree suitable for dashboards, console formatting, and diagnostics.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Types

    enum class Status
    :   Defines the lifecycle state of a progress node.

        *Values:*

        enumerator Pending
        :   Node has been created but has not started.

        enumerator Running
        :   Node is currently executing.

        enumerator Completed
        :   Node finished successfully.

        enumerator Failed
        :   Node finished with an error.

        enumerator Skipped
        :   Node was intentionally skipped.

    using Type = [WorkflowExecutionNodeType](https://manivault.readthedocs.io/en/latest/api/core/workflow/utilities/workflow_execution_node_type.html#_CPPv4N2mv8workflow25WorkflowExecutionNodeTypeE "mv::workflow::WorkflowExecutionNodeType")
    :   Semantic execution node type.

    using Ptr = std::shared\_ptr<[WorkflowProgressNode](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNodeE "mv::workflow::WorkflowProgressNode")>
    :   Shared pointer type for workflow progress nodes.

    Public Functions

    [Snapshot](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode8SnapshotE "mv::workflow::WorkflowProgressNode::Snapshot") createSnapshot() const
    :   Creates a recursive snapshot of this progress subtree.

        Returns:
        :   [Snapshot](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#structmv_1_1workflow_1_1WorkflowProgressNode_1_1Snapshot) containing the current node state and child snapshots.

    explicit WorkflowProgressNode([Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode4TypeE "mv::workflow::WorkflowProgressNode::Type") type, QString name, [Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode3PtrE "mv::workflow::WorkflowProgressNode::Ptr") parent, double weight = 1.0)
    :   Constructs a progress node.

        Prefer [createRoot()](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#classmv_1_1workflow_1_1WorkflowProgressNode_1a705c6d77026000cdf77726063e922bad) and [createChild()](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#classmv_1_1workflow_1_1WorkflowProgressNode_1aadab8afa20ce66773f0a6387e2167329) in workflow code so parent-child relationships are established consistently.

        Parameters:
        :   - **type** – Semantic workflow node type.
            - **name** – Human-readable node name.
            - **parent** – Parent progress node, or nullptr for a root node.
            - **weight** – Relative contribution to the parent node’s progress.

    [Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode3PtrE "mv::workflow::WorkflowProgressNode::Ptr") createChild([Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode4TypeE "mv::workflow::WorkflowProgressNode::Type") type, QString name, double weight = 1.0)
    :   Creates and registers a child progress node.

        Parameters:
        :   - **type** – Semantic workflow node type.
            - **name** – Human-readable child node name.
            - **weight** – Relative contribution to this node’s aggregate progress.

        Returns:
        :   Shared child progress node.

    bool hasChildren() const
    :   Returns whether this node has direct children.

        Returns:
        :   True if this node has at least one child.

    void setProgress(double value)
    :   Sets explicit progress for a leaf node.

        The value is clamped to [0.0, 1.0]. Calls on non-leaf nodes are ignored because parent progress is computed from child progress.

        Parameters:
        :   **value** – Normalized progress value.

    double getProgress() const
    :   Returns this node’s current progress.

        Leaf nodes return their explicit progress. Parent nodes return the weighted average of their children’s progress.

        Returns:
        :   Normalized progress value in the range [0.0, 1.0].

    double getWeight() const
    :   Returns this node’s relative contribution to its parent.

        Returns:
        :   Progress weight.

    [Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode4TypeE "mv::workflow::WorkflowProgressNode::Type") getType() const
    :   Returns the semantic workflow node type.

        Returns:
        :   Workflow execution node type.

    QString getName() const
    :   Returns the human-readable node name.

        Returns:
        :   Node name.

    [Status](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode6StatusE "mv::workflow::WorkflowProgressNode::Status") getStatus() const
    :   Returns the current lifecycle state.

        Returns:
        :   Node status.

    [Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode3PtrE "mv::workflow::WorkflowProgressNode::Ptr") getParent() const
    :   Returns the parent node.

        Returns:
        :   Shared parent node, or nullptr for a root node.

    QVector<[Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode3PtrE "mv::workflow::WorkflowProgressNode::Ptr")> getChildren() const
    :   Returns direct child nodes.

        Returns:
        :   Copy of the current child pointer list.

    int getChildCount() const
    :   Returns the number of direct child nodes.

        Returns:
        :   Child count.

    int getCompletedChildCount() const
    :   Returns the number of direct children with terminal status.

        Completed, failed, and skipped children are all considered finished.

        Returns:
        :   Finished child count.

    std::int64\_t getElapsedMilliseconds() const
    :   Returns elapsed runtime for this node.

        Pending nodes report zero. Running nodes report the active timer value. Terminal nodes report the elapsed time captured when they finished.

        Returns:
        :   Elapsed time in milliseconds.

    std::int64\_t getElapsedMillisecondsUnlocked() const
    :   Returns elapsed runtime without locking.

        This helper is intended for internal use by callers that already hold this node’s mutex.

        Returns:
        :   Elapsed time in milliseconds.

    void markRunning()
    :   Marks the node as running and starts elapsed-time tracking if needed.

    void markCompleted()
    :   Marks the node as completed and captures elapsed time if it was running.

    void markFailed()
    :   Marks the node as failed and captures elapsed time if it was running.

    void markSkipped()
    :   Marks the node as skipped and captures elapsed time if it was running.

    bool isRoot() const
    :   Returns whether this node has no parent.

        Returns:
        :   True if this node is a root progress node.

    Public Static Functions

    static [Ptr](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode3PtrE "mv::workflow::WorkflowProgressNode::Ptr") createRoot([Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode4TypeE "mv::workflow::WorkflowProgressNode::Type") type, const QString &name, double weight = 1.0)
    :   Creates a root progress node.

        Parameters:
        :   - **type** – Semantic workflow node type.
            - **name** – Human-readable root node name.
            - **weight** – Relative progress weight, normally 1.0 for roots.

        Returns:
        :   Shared root progress node.

    struct Snapshot
    :   Value copy of a progress node and its descendants.

        Snapshots decouple rendering and reporting code from the live progress tree. They capture the node’s current state, aggregate progress, elapsed time, child counts, and recursively captured child snapshots.

        Public Members

        [Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode4TypeE "mv::workflow::WorkflowProgressNode::Type") type = [Type](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode4TypeE "mv::workflow::WorkflowProgressNode::Type")::Undefined
        :   Semantic workflow node type.

        [Status](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode6StatusE "mv::workflow::WorkflowProgressNode::Status") status = [Status](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode6StatusE "mv::workflow::WorkflowProgressNode::Status")::[Pending](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode6Status7PendingE "mv::workflow::WorkflowProgressNode::Status::Pending")
        :   Current lifecycle state.

        QString name
        :   Human-readable node name.

        double progress = 0.0
        :   Normalized progress in the range [0.0, 1.0].

        double weight = 1.0
        :   Relative contribution to the parent node.

        int childCount = 0
        :   Number of direct child nodes.

        int completedChildCount = 0
        :   Number of direct children with a terminal status.

        qint64 elapsedMilliseconds = 0
        :   Elapsed runtime in milliseconds.

        QVector<[Snapshot](https://manivault.readthedocs.io/en/latest/api/core/workflow/progress/workflow_progress_node.html#_CPPv4N2mv8workflow20WorkflowProgressNode8SnapshotE "mv::workflow::WorkflowProgressNode::Snapshot")> children
        :   Snapshots of direct child nodes.
