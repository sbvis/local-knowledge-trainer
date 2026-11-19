# Workflow result future

**Source:** https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html

**Documentation path:** `api/core/workflow/execution/workflow_result_future.html`

---

# Workflow result future

A future-like handle for observing asynchronous workflow completion and retrieving its result.

class WorkflowResultFuture
:   Represents an asynchronous workflow result.

    [WorkflowResultFuture](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html#classmv_1_1workflow_1_1WorkflowResultFuture) wraps the shared future returned by asynchronous workflow execution together with its optional GUI task and captured exception state.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Public Functions

    WorkflowResultFuture()
    :   Constructs an empty workflow result future.

    explicit WorkflowResultFuture(std::shared\_ptr<[State](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html#_CPPv4N2mv8workflow20WorkflowResultFuture5StateE "mv::workflow::WorkflowResultFuture::State")> state)
    :   Constructs a workflow result future from shared state.

        Parameters:
        :   **state** – Shared asynchronous execution state.

    SharedWorkflowResult get() const
    :   Returns the completed workflow result.

        This call blocks until the asynchronous execution has finished and rethrows any exception captured by the shared state.

        Returns:
        :   Completed workflow result.

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*getTask() const
    :   Returns the associated GUI task.

        Returns:
        :   [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) associated with execution, or nullptr.

    inline std::shared\_ptr<[State](https://manivault.readthedocs.io/en/latest/api/core/workflow/execution/workflow_result_future.html#_CPPv4N2mv8workflow20WorkflowResultFuture5StateE "mv::workflow::WorkflowResultFuture::State")> getState() const
    :   Returns the shared asynchronous execution state.

        Returns:
        :   Shared state object.

    void onFinished(QObject \*receiver, std::function<void(SharedWorkflowResult)> callback)
    :   Registers a callback for workflow completion.

        Parameters:
        :   - **receiver** – QObject that owns the callback connection lifetime.
            - **callback** – Function invoked with the completed workflow result.

    struct State
    :   Shared state for an asynchronous workflow execution.

        Public Functions

        void setException(std::exception\_ptr e)
        :   Stores an asynchronous execution exception.

            Parameters:
            :   **e** – Exception pointer to store.

        std::exception\_ptr getException() const
        :   Returns the stored asynchronous execution exception.

            Returns:
            :   Stored exception pointer.

        bool hasException() const
        :   Returns whether an exception has been stored.

            Returns:
            :   True if an exception is stored.

        void rethrowExceptionIfAny() const
        :   Rethrows the stored exception.

            If no exception has been stored, the function returns without doing anything.

        Public Members

        std::shared\_future<SharedWorkflowResult> future
        :   Future that produces the workflow result.

        QPointer<[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")> task
        :   Optional task associated with execution.

        mutable QMutex mutex
        :   Protects stored exception state.

        std::exception\_ptr exception
        :   Exception captured from asynchronous execution.
