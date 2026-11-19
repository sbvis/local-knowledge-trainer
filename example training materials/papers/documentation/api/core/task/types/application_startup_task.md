# ApplicationStartupTask

**Source:** https://manivault.readthedocs.io/en/latest/api/core/task/types/application_startup_task.html

**Documentation path:** `api/core/task/types/application_startup_task.html`

---

# ApplicationStartupTask

**Qualified name:** `mv::ApplicationStartupTask`

Note

This part of the API is intended for use by **core developers**. Plugin developers should not interact with it, as it is fully managed by the **core**.

class ApplicationStartupTask : public mv::[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")
:   [Application](https://manivault.readthedocs.io/en/latest/api/core/application/application.html#classmv_1_1Application) startup task class.

    Defines a startup application task with all the necessary descendant tasks.

    **Author**
    :   Thomas Kroes

    Public Functions

    ApplicationStartupTask(QObject \*parent, const QString &name, const Status &status = Status::Undefined, bool mayKill = false)
    :   Construct task with `parent` object, `name` and initial `status`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **name** – Name of the task
            - **status** – Initial status of the task
            - **mayKill** – Boolean determining whether the task may be killed or not

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") &getLoadCoreManagersTask()
    :   Get aggregate task for loading the core.

    [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") &getLoadGuiTask()
    :   Get aggregate task for loading the core managers.
