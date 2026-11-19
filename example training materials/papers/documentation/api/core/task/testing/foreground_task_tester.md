# ForegroundTaskTester

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/testing/foreground_task_tester.html

**Documentation path:** `api/core/task/testing/foreground_task_tester.html`

---

# ForegroundTaskTester

**Qualified name:** `mv::ForegroundTaskTester`

class ForegroundTaskTester : public mv::[AbstractTaskTester](https://manivault.readthedocs.io/en/latest/api/core/task/testing/abstract_task_tester.html#_CPPv4N2mv18AbstractTaskTesterE "mv::AbstractTaskTester")
:   Foreground task tester class.

    Tests various foreground task scenarios.

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE ForegroundTaskTester(QObject \*parent, const QString &name)
    :   Initialize tester with pointer to \parent object and tester name.

        Parameters:
        :   - **parent** – Pointer to \parent object
            - **name** – Name of the tester
