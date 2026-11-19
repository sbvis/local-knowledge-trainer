# Serializable

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html

**Documentation path:** `api/core/util/serialization/serializable.html`

---

# Serializable

**Qualified name:** `mv::util::Serializable`

For choosing between synchronous and workflow overrides, see [Synchronous and workflow serialization](https://manivault.readthedocs.io/en/latest/development/building_plugins/persistence/synchronous_and_workflow.html).

class Serializable
:   [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) base class.

    [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) provides the serialization contract for persisting and restoring object state.

    Serialization is exposed through two layers:

    - the synchronous contract: [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf) / [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e)
    - the workflow contract: [fromVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a87b350d0d2e10960cb9e7d6f3a55e909) / [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf)

    The synchronous functions are intended for simple, immediate serialization work. They must complete all work before returning and must not start background work, execute workflows, or defer state changes.

    The workflow functions are intended for expensive, staged, parallelizable, or progress-reporting serialization work. They only construct workflow plans; they do not execute them. Execution, scheduling, nesting, progress reporting, cancellation, diagnostics, and output collection are the responsibility of the workflow executor and the caller that composes the workflow.

    The default workflow implementations delegate to the synchronous functions, so simple objects only need to override [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf) and [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e).

    Framework code that participates in a larger workflow should compose the workflow returned by [fromVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a87b350d0d2e10960cb9e7d6f3a55e909) or [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf), typically as a nested workflow. It should not call helper functions that hide blocking workflow execution.

    Convenience JSON and parent-map helpers are provided for simple synchronous use cases. They are not workflow orchestration APIs.

    Plugin developers should typically:

    - override [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf) and [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e) for simple objects
    - override [fromVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a87b350d0d2e10960cb9e7d6f3a55e909) and/or [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf) for expensive, staged, parallelizable, or progress-reporting operations

    In addition to the primary serialization contract, [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) provides helpers for:

    - working with parent QVariantMaps
    - inserting serialized child objects into QVariantMaps
    - reading and writing JSON documents and files
    - object identity management and serialization diagnostics

    Subclassed by [mv::AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#classmv_1_1AbstractManager), [mv::Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application), mv::BiMap, mv::CoreApplication, mv::KeyBasedSelectionGroup, [mv::LinkedData](https://manivault.readthedocs.io/en/latest/api/core/data/linked_data.html#classmv_1_1LinkedData), mv::OrderedMap, [mv::Project](https://manivault.readthedocs.io/en/latest/api/core/application/project.html#classmv_1_1Project), [mv::SelectionMap](https://manivault.readthedocs.io/en/latest/api/core/data/selection_map.html#classmv_1_1SelectionMap), [mv::SortFilterProxyModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/sort_filter_proxy_model.html#classmv_1_1SortFilterProxyModel), [mv::StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#classmv_1_1StandardItemModel), [mv::Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task), [mv::Workspace](https://manivault.readthedocs.io/en/latest/api/core/application/workspace.html#classmv_1_1Workspace), [mv::gui::ColorMapEditor1DNode](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/colormap/color_map_editor_1d_node.html#classmv_1_1gui_1_1ColorMapEditor1DNode), [mv::gui::HierarchyWidget](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/hierarchy_widget.html#classmv_1_1gui_1_1HierarchyWidget), [mv::gui::WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#classmv_1_1gui_1_1WidgetAction), [mv::util::Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version)

    Public Types

    enum class State
    :   Determines the state of the serializable object.

        *Values:*

        enumerator Idle

        enumerator Reading
        :   The serializable object is not being read or written.

        enumerator Writing
        :   The serializable object is being read.

            The serializable object is being written

    enum class Direction
    :   Describes the serialization direction.

        *Values:*

        enumerator From

        enumerator To
        :   From variant map to serializable object.

            From serializable object to variant map

    Public Functions

    Serializable(const QString &serializationName = "")
    :   Construct a serializable object.

        Parameters:
        :   **serializationName** – Serialization name used when storing and retrieving this object from parent variant maps and JSON documents.

    inline virtual ~Serializable()
    :   Destructor.

    QString getId(bool truncated = false) const
    :   Get this object’s globally unique identifier.

        The identifier represents the persistent identity of the object and is used by the equality operators.

        Parameters:
        :   **truncated** – Whether to return a shortened representation of the identifier for diagnostic or display purposes.

        Returns:
        :   Globally unique identifier of this object.

    void setId(const QString &id)
    :   Set this object’s globally unique identifier.

        Changing the identifier changes the logical identity of the object and should therefore only be done when the implications are fully understood.

        In most cases, [makeUnique()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3bb166d5843f4ef17791915334cc5353) should be preferred when a new identity is required.

        Parameters:
        :   **id** – Globally unique identifier to assign.

    QString getSerializationName() const
    :   Get this object’s serialization name.

        The serialization name is used as the key under which the object is stored in parent variant maps and JSON documents.

        Returns:
        :   Serialization name.

    void setSerializationName(const QString &serializationName)
    :   Set this object’s serialization name.

        The serialization name is used as the key under which the object is stored in parent variant maps and JSON documents.

        Changing the serialization name after serialized data has already been persisted may render that data unreadable by this object, because the expected serialization key no longer matches the key stored in the serialized representation.

        Changing the serialization name may also introduce collisions with other serialized objects or make existing serialized state unreachable.

        Use this function sparingly and only when the object’s serialization identity is intentionally being changed and the implications are fully understood.

        Parameters:
        :   **serializationName** – Serialization name to assign.

    virtual void fromVariantMap(const QVariantMap &variantMap)
    :   Load the object state from a variant map.

        This is the low-level synchronous loading implementation.

        When this function returns, all state represented by the variant map must have been fully applied to the object.

        Implementations must not:

        - start background work
        - schedule workflow jobs
        - return before restoration is complete

        Framework code that participates in workflow execution should generally compose the workflow returned by [fromVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a87b350d0d2e10960cb9e7d6f3a55e909) instead of calling this function directly.

        Override this function for simple objects whose state can be restored synchronously.

        Override [fromVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a87b350d0d2e10960cb9e7d6f3a55e909) instead when loading is expensive, staged, parallelizable, or requires progress reporting.

        Parameters:
        :   **variantMap** – Serialized object state.

    virtual workflow::UniqueWorkflowPlan fromVariantMapWorkflow(QVariantMap variantMap)
    :   Create a workflow that restores the object state.

        This function constructs a workflow but does not execute it.

        The returned workflow must fully restore the object when executed.

        Implementations may use sequential, parallel, nested, or batched stages and may publish progress, warnings, messages, and outputs.

        The default implementation creates a simple workflow that invokes [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf).

        Framework code may compose this workflow directly, for example as a nested workflow within a larger serialization workflow.

        Parameters:
        :   **variantMap** – Serialized object state.

        Returns:
        :   Workflow plan that restores the object state.

    virtual void fromParentVariantMap(const QVariantMap &parentVariantMap, bool ignoreLoadingErrors = false)
    :   Restore this object from a parent variant map.

        This convenience function looks up the child variant map associated with this object’s serialization name and forwards it to [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf).

        The function expects the parent variant map to contain an entry whose key matches [getSerializationName()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1ae0ff3065f78d2a8d406c703bd664f61a). The associated value must be a QVariantMap representing the serialized state of this object.

        This function uses the synchronous serialization contract and therefore invokes [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf) directly. It does not execute [fromVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a87b350d0d2e10960cb9e7d6f3a55e909) and does not participate in workflow execution, progress reporting, or parent workflow hierarchies.

        Use [fromVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a87b350d0d2e10960cb9e7d6f3a55e909) when deserialization needs to participate in a larger workflow hierarchy.

        Parameters:
        :   - **parentVariantMap** – Parent variant map containing serialized child objects.
            - **ignoreLoadingErrors** – Whether missing serialized data should be ignored. When false, missing entries result in an exception. When true, missing entries may be handled according to the application’s loading error policy.

        Throws:
        :   - std::runtime\_error – If the serialization name is empty.
            - [ManiVaultException](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv18ManiVaultExceptionE "mv::ManiVaultException") – If the required entry is not present.

    virtual void fromJsonDocument(const QJsonDocument &jsonDocument)
    :   Restore the object state from a JSON document.

        This function extracts the variant map associated with this object’s serialization name from the JSON document and forwards it directly to [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf).

        This function uses the synchronous serialization contract and does not execute [fromVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a87b350d0d2e10960cb9e7d6f3a55e909). As a result, custom workflow-based loading behavior, progress reporting, nested workflows, and parent workflow hierarchies are not used.

        Parameters:
        :   **jsonDocument** – JSON document containing the serialized object state.

        Throws:
        :   [ManiVaultException](https://manivault.readthedocs.io/en/latest/api/core/util/exception/mani_vault_exception.html#_CPPv4N2mv18ManiVaultExceptionE "mv::ManiVaultException") – If the required serialization entry is missing or invalid.

    virtual void fromJsonFile(const QString &filePath = "")
    :   Restore the object state from a JSON file.

        This function reads a JSON document from disk, validates that the file exists, can be opened, contains data, and contains a valid JSON document, then forwards the document to [fromJsonDocument()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a74d4ecb28946450b9b85c27c22cb63f7).

        This function performs synchronous file loading and delegates to [fromJsonDocument()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a74d4ecb28946450b9b85c27c22cb63f7) after validating and parsing the JSON document.

        Parameters:
        :   **filePath** – Path to the JSON file to load.

        Throws:
        :   - std::runtime\_error – If the file does not exist.
            - std::runtime\_error – If the file cannot be opened for reading.
            - std::runtime\_error – If no data could be read.
            - std::runtime\_error – If the JSON document is invalid or empty.
            - std::exception – Any exception propagated by [fromJsonDocument()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a74d4ecb28946450b9b85c27c22cb63f7).

    virtual QVariantMap toVariantMap() const
    :   Serialize the object state to a variant map.

        This is the low-level synchronous serialization implementation.

        The returned variant map must contain all information required to restore the object through [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf).

        The base implementation serializes only the object’s unique identifier and updates the serialization counter.

        Derived classes should extend the returned variant map with their own serialized state and should generally invoke the base implementation first.

        Implementations must not schedule asynchronous work, create workflows, or defer serialization beyond the lifetime of this call.

        Framework code that participates in workflow execution should generally compose the workflow returned by [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf) instead of calling this function directly.

        The default implementation of [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf) delegates to this function, allowing simple objects to participate in the workflow-based serialization contract without implementing a custom workflow.

        Returns:
        :   Complete variant map representation of the object state.

    virtual workflow::UniqueWorkflowPlan toVariantMapWorkflow() const
    :   Create a workflow that serializes the object state to a variant map.

        This is the workflow-based serialization hook.

        The function only constructs and returns a workflow plan. It does not execute the workflow.

        The returned workflow must publish the serialized QVariantMap as an output using this object’s serialization name.

        The base implementation creates a simple workflow that invokes [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e) and publishes the resulting variant map as an output.

        Derived classes may override this function when serialization is expensive, staged, parallelizable, or requires progress reporting.

        Implementations must not perform the serialization immediately unless that work is part of a job in the returned workflow.

        Framework code may compose this workflow directly, for example as a nested workflow within a larger serialization workflow.

        Returns:
        :   Workflow plan that serializes the object state when executed.

    void insertIntoVariantMap(QVariantMap &variantMap) const
    :   Insert this object’s serialized state into a parent variant map.

        This convenience function serializes the object using [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e) and stores the resulting child variant map under the object’s serialization name.

        The function requires:

        - a non-empty serialization name
        - that the parent variant map does not already contain an entry with that name

        This function uses the synchronous serialization contract and therefore invokes [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e) directly. It does not participate in workflow execution and does not invoke [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf).

        Use [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf) when serialization needs to participate in a larger workflow hierarchy.

        Example:

        ```
        QVariantMap parentMap;
        child.insertIntoVariantMap(parentMap);
        ```

        Result:

        ```
        {
            "ChildSerializationName" : { ... }
        }
        ```

        Parameters:
        :   **variantMap** – Parent variant map into which the serialized object state will be inserted.

        Throws:
        :   - std::runtime\_error – If the serialization name is empty.
            - std::runtime\_error – If the parent variant map already contains an entry with the same serialization name.

    virtual QJsonDocument toJsonDocument() const
    :   Serialize the object state to a JSON document.

        This convenience function serializes the object using the synchronous serialization contract and converts the resulting QVariantMap to a JSON document.

        This function invokes [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e) directly. It does not participate in workflow execution and does not invoke [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf).

        Use [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf) when serialization needs to participate in a larger workflow hierarchy.

        Returns:
        :   JSON document containing the serialized object state.

    virtual void toJsonFile(const QString &filePath = "") const
    :   Serialize the object state to a JSON file.

        This convenience function serializes the object using the synchronous serialization contract, converts the resulting variant map to a JSON document, and writes it to disk.

        This function invokes [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e) directly. It does not participate in workflow execution and does not invoke [toJsonFileWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a5cf0924302c71cd61df7509e8983771f) or [toVariantMapWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a4d7fa8d832c61fd3036addc804ad18bf).

        Use [toJsonFileWorkflow()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a5cf0924302c71cd61df7509e8983771f) when file serialization needs to participate in a larger workflow hierarchy.

        Parameters:
        :   **filePath** – Path of the JSON file to write.

        Throws:
        :   std::exception – Any exception raised during serialization, JSON conversion, or file writing.

    workflow::UniqueWorkflowPlan toJsonFileWorkflow(const QString &filePath = "") const
    :   Create a workflow that serializes the object state to a JSON file.

        This function only constructs and returns a workflow plan. It does not execute the workflow.

        The returned workflow must serialize the object state and write the resulting JSON document to the specified file when executed.

        The base implementation may compose existing serialization workflows and additional stages required to write the JSON file.

        Derived classes may override this function when JSON file serialization requires custom staging, progress reporting, or additional workflow integration.

        Implementations must not write the file immediately unless that work is part of a job in the returned workflow.

        Parameters:
        :   **filePath** – Path of the JSON file to write.

        Returns:
        :   Workflow plan that writes the serialized object state to disk when executed.

    void makeUnique()
    :   Assign a fresh globally unique identifier to this object.

        This function replaces the current identifier with a newly generated identifier produced by [createId()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1abc8b130bf9b037725fb6bc5b1b97f610).

        Use this function when creating a logically distinct copy of a serializable object that must not share identity with the original object.

    std::int32\_t getSerializationCount(const [Direction](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12Serializable9DirectionE "mv::util::Serializable::Direction") &direction) const
    :   Get the number of times this object has been serialized in the specified direction.

        Serialization counters are maintained automatically by the base [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) implementation and may be useful for debugging, diagnostics, and testing.

        Parameters:
        :   **direction** – Serialization direction to query.

        Returns:
        :   Number of serialization operations performed in the specified direction.

    std::int32\_t getSerializationCountFrom() const
    :   Get the number of times [fromVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a3966d0241455cc4550653495368221cf) has been invoked.

        This counter is maintained automatically by the base [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) implementation and may be useful for diagnostics and testing.

        Returns:
        :   Number of deserialization operations performed through the low-level deserialization implementation.

    std::int32\_t getSerializationCountTo() const
    :   Get the number of times [toVariantMap()](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable_1a7c7c63a0099cfdb650247fddc8b1c30e) has been invoked.

        This counter is maintained automatically by the base [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) implementation and may be useful for diagnostics and testing.

        Returns:
        :   Number of serialization operations performed through the low-level serialization implementation.

    QPointer<[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")> getTask() const
    :   Get the task associated with this object.

        Returns:
        :   Associated task, or a null pointer if no task is associated with this object.

    bool hasTask() const
    :   Determine whether this object is associated with a task.

        Returns:
        :   True if a task is associated with this object, false otherwise.

    void setTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task)
    :   Associate this object with a task.

        The task association may be used by higher-level infrastructure for ownership, lifecycle management, or contextual integration.

        Parameters:
        :   **task** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) to associate with this object, or nullptr to clear the association.

    inline bool operator==(const [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable") &rhs) const
    :   Compare two serializable objects for identity equality.

        Two [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) instances are considered equal when their globally unique identifiers are equal.

        Parameters:
        :   **rhs** – Object to compare against.

        Returns:
        :   True if both objects have the same identifier, false otherwise.

    inline bool operator!=(const [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable") &rhs) const
    :   Compare two serializable objects for identity inequality.

        Two [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) instances are considered different when their globally unique identifiers differ.

        Parameters:
        :   **rhs** – Object to compare against.

        Returns:
        :   True if the identifiers differ, false otherwise.

    Public Static Functions

    static QString createId()
    :   Create a new globally unique identifier.

        The returned identifier is suitable for use as the persistent identity of a [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) instance.

        Returns:
        :   Newly generated globally unique identifier.

    static void handleKeyNotFoundInVariantMap(const [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable") &serializable, const QVariantMap &map, const QString &key, std::source\_location sourceLocation = std::source\_location::current())
    :   Handle a missing required key in a variant map.

        This helper centralizes error reporting for serialization-related lookup failures and typically throws a descriptive exception that includes contextual information about the missing key and the available entries in the variant map.

        Parameters:
        :   - **serializable** – [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) object for which the lookup failed.
            - **map** – Variant map that was expected to contain the key.
            - **key** – Required key that could not be found.
            - **sourceLocation** – Source location of the call site, used for diagnostics. Defaults to the current source location.

    Protected Static Functions

    static void fromVariantMap([Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable") \*serializable, const QVariantMap &variantMap)
    :   Restore a serializable object from a variant map.

        This convenience helper forwards the supplied variant map to the object’s synchronous deserialization implementation.

        This function is not part of the primary serialization contract.

        Parameters:
        :   - **serializable** – [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) object to restore.
            - **variantMap** – Serialized object state.

    static void fromVariantMap([Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable") &serializable, const QVariantMap &variantMap, const QString &key)
    :   Restore a serializable object from a child variant map contained within a parent variant map.

        This convenience helper extracts the child variant map associated with the specified key and forwards it to the object’s synchronous deserialization implementation.

        This function is not part of the primary serialization contract.

        Parameters:
        :   - **serializable** – [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) object to restore.
            - **variantMap** – Parent variant map.
            - **key** – Key identifying the serialized child object.

    static QVariantMap toVariantMap(const [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable") \*serializable)
    :   Serialize a serializable object to a variant map.

        This convenience helper invokes the object’s synchronous serialization implementation.

        This function is not part of the primary serialization contract.

        Parameters:
        :   **serializable** – [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) object to serialize.

        Returns:
        :   Serialized object state.

    static void insertIntoVariantMap(const [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable") &serializable, QVariantMap &variantMap, const QString &key)
    :   Serialize a serializable object and insert the resulting child variant map into a parent variant map under the specified key.

        This convenience helper is not part of the primary serialization contract.

        Parameters:
        :   - **serializable** – [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) object to serialize.
            - **variantMap** – Parent variant map.
            - **key** – Key under which the serialized object state will be stored.

    static void insertIntoVariantMap(const [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#_CPPv4N2mv4util12SerializableE "mv::util::Serializable") &serializable, QVariantMap &variantMap)
    :   Serialize a serializable object and insert the resulting child variant map into a parent variant map using the object’s serialization name as the key.

        This convenience helper is not part of the primary serialization contract.

        Parameters:
        :   - **serializable** – [Serializable](https://manivault.readthedocs.io/en/latest/api/core/util/serialization/serializable.html#classmv_1_1util_1_1Serializable) object to serialize.
            - **variantMap** – Parent variant map.
