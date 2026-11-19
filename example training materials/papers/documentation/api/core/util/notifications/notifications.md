# Notifications

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notifications.html

**Documentation path:** `api/core/util/notifications/notifications.html`

---

# Notifications

**Qualified name:** `mv::util::Notifications`

class Notifications : public QObject
:   Manager for stacked toast notifications.

    [Notifications](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notifications.html#classmv_1_1util_1_1Notifications) creates [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) widgets, stacks them above the main window status bar, repositions them when the parent window changes size, and forwards activated notification links to interested consumers.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Note

    This class is intended for internal use by the help manager.

    Public Functions

    explicit Notifications(QWidget \*parent = nullptr)
    :   Constructs a notifications manager.

        Note

        [Notifications](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notifications.html#classmv_1_1util_1_1Notifications) are positioned relative to the main window, above its status bar (the main window must be set up before creating a [Notifications](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notifications.html#classmv_1_1util_1_1Notifications) instance).

        Parameters:
        :   **parent** – Pointer to parent widget (if any).

    void showMessage(const QString &title, const QString &description, const QIcon &icon, const util::[Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification")::[DurationType](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12DurationTypeE "mv::util::Notification::DurationType") &durationType, std::int32\_t delayMs)
    :   Shows a message notification.

        Parameters:
        :   - **title** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) title.
            - **description** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) description, optionally rich text.
            - **icon** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) icon.
            - **durationType** – Display duration policy.
            - **delayMs** – Delay in milliseconds before the notification is shown.

    void showTask(QPointer<[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")> task)
    :   Shows a task notification.

        Parameters:
        :   **task** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) whose state is displayed by the notification.

    void setupMainWindowSynchronization()
    :   Sets up synchronization with the main window.

    void notificationLinkActivated(const QUrl &url)
    :   Emitted when a notification hyperlink is activated.

        Parameters:
        :   **url** – Activated hyperlink URL.

    Protected Functions

    bool eventFilter(QObject \*watched, QEvent \*event) override
    :   Repositions notifications when watched widgets resize.

        Parameters:
        :   - **watched** – Watched object.
            - **event** – Event to handle.

        Returns:
        :   True if the event was handled.
