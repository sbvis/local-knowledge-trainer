# Timer

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/timer/timer.html

**Documentation path:** `api/core/util/timer/timer.html`

---

# Timer

**Qualified name:** `Timer`

class Timer
:   [Timer](https://manivault.readthedocs.io/en/latest/api/core/util/timer/timer.html#classTimer) utility class.

    Helper class for timing events When an instance of this class goes out of scope, it prints the elapsed time (prefixed by the event name)

    Code inspired by: <https://stackoverflow.com/questions/2808398/easily-measure-elapsed-time>

    **Author**
    :   Thomas Kroes

    Public Functions

    Timer(const QString &event = "")
    :   Constructor.

        Parameters:
        :   **event** – Name of the event to measure (when empty, elapsed time is not printed when this object goes out of scope)

    ~Timer()
    :   Destructor.

    std::int64\_t elapsedTime(const SteadyClock &start) const
    :   Returns the elapsed time.

        Parameters:
        :   **start** – The start time of the time interval

        Returns:
        :   Elapsed time

    float elapsedTimeMilliseconds(const SteadyClock &start) const
    :   Returns the elapsed time.

        Parameters:
        :   **start** – The start time of the time interval

        Returns:
        :   Elapsed time in milliseconds

    void printElapsedTime(const QString &event, const bool &reset = false)
    :   Prints the elapsed time since the timer was created.

        Parameters:
        :   - **event** – Name of the event
            - **reset** – Whether to reset the start time

    void reset()
    :   Resets the start time of the timer.

    Protected Functions

    void printTotalTime()
    :   Prints the elapsed time since the timer was created.
