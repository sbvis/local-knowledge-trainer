# Event listener

**Source:** https://manivault.readthedocs.io/en/latest/api/core/data/events/event_listener.html

**Documentation path:** `api/core/data/events/event_listener.html`

---

# Event listener

`EventListener` registers with the core event manager and supports general callbacks plus callbacks filtered by `DataType`. Event types form an explicit allowlist: add at least one supported type before expecting delivery. Destruction unregisters the listener.

For ownership, filtering, and callback-lifetime examples, see [Listening across datasets](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/events/event_listener.html).

class EventListener
:   Public Types

    using DataEventHandler = std::function<void([DatasetEvent](https://manivault.readthedocs.io/en/latest/api/core/data/events/event_types.html#_CPPv4N2mv12DatasetEventE "mv::DatasetEvent")\*)>
    :   Event registration function signatures.

    Public Functions

    EventListener()
    :   Constructor, registers the event listener.

    virtual ~EventListener()
    :   Destructor, unregisters the event listener from the core.

    bool isEventTypeSupported(std::uint32\_t eventType) const
    :   Determines whether the listener should listen to a specific event type or not.

        Parameters:
        :   **eventType** – Type of event

        Returns:
        :   Boolean indicating whether the listener should listen to a specific event type or not

    void addSupportedEventType(std::uint32\_t eventType)
    :   Add supported event type.

        Parameters:
        :   **eventType** – Type of event that should be supported

    void removeSupportedEventType(std::uint32\_t eventType)
    :   Remove supported event type.

        Parameters:
        :   **eventType** – Type of event that should be not be supported anymore

    void setSupportedEventTypes(const QSet<std::uint32\_t> &eventTypes)
    :   Add supported event types.

        Parameters:
        :   **eventType** – Types of events that should be supported
