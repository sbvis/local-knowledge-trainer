# Notification

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html

**Documentation path:** `api/core/util/notifications/notification.html`

---

# Notification

**Qualified name:** `mv::util::Notification`

class Notification : public QWidget
:   Toast-style notification widget.

    [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) renders one transient message in a stacked notification area. [Notifications](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notifications.html#classmv_1_1util_1_1Notifications) can either show a title, description, and icon for a fixed or calculated duration, or stay visible while an associated [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) is running.

    Instances are linked to previous and next notifications so stacked widgets can reposition when one is shown or dismissed. [Notifications](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notifications.html#classmv_1_1util_1_1Notifications) owns the lifecycle of these widgets.

    @maintainer Thomas Kroes (BioVault - Biomedical Visual Analytics Unit LUMC - TU Delft)

    Note

    This class is intended for internal use by [Notifications](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notifications.html#classmv_1_1util_1_1Notifications).

    Public Types

    enum class DurationType
    :   Duration policy for a notification.

        *Values:*

        enumerator Fixed
        :   Uses the standard fixed display duration.

        enumerator Calculated
        :   Estimates display duration from message length.

        enumerator Task
        :   Stays visible while the associated task is running.

    Public Functions

    explicit Notification(const QString &title, const QString &description, const QIcon &icon, [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12NotificationERK7QStringRK7QStringRK5QIconP12NotificationRK12DurationTypeP7QWidget "mv::util::Notification::Notification") \*previousNotification, const [DurationType](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12DurationTypeE "mv::util::Notification::DurationType") &durationType, QWidget \*parent = nullptr)
    :   Constructs a message notification.

        Parameters:
        :   - **title** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) title.
            - **description** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) description, optionally rich text.
            - **icon** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) icon.
            - **previousNotification** – Previous notification in the stack, or nullptr.
            - **durationType** – Display duration policy.
            - **parent** – Optional parent widget.

    explicit Notification(QPointer<[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")> task, [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12NotificationE8QPointerI4TaskEP12NotificationP7QWidget "mv::util::Notification::Notification") \*previousNotification, QWidget \*parent = nullptr)
    :   Constructs a task notification.

        Parameters:
        :   - **task** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) whose state is displayed by the notification.
            - **previousNotification** – Previous notification in the stack, or nullptr.
            - **parent** – Optional parent widget.

    bool isClosing() const
    :   Returns whether the notification is closing.

        Returns:
        :   True if the notification is currently closing.

    [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification") \*getPreviousNotification() const
    :   Returns the previous notification in the stack.

        Returns:
        :   Previous notification, or nullptr.

    void setPreviousNotification([Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification") \*previousNotification)
    :   Sets the previous notification in the stack.

        Parameters:
        :   **previousNotification** – Previous notification, or nullptr.

    [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification") \*getNextNotification() const
    :   Returns the next notification in the stack.

        Returns:
        :   Next notification, or nullptr.

    void setNextNotification([Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification") \*nextNotification)
    :   Sets the next notification in the stack.

        Parameters:
        :   **nextNotification** – Next notification, or nullptr.

    QIcon getIcon() const
    :   Returns the notification icon.

        Returns:
        :   [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) icon.

    void setIcon(const QIcon &icon)
    :   Sets the notification icon.

        Parameters:
        :   **icon** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) icon.

    QString getTitle() const
    :   Returns the notification title.

        Returns:
        :   [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) title.

    void setTitle(const QString &title)
    :   Sets the notification title.

        Parameters:
        :   **title** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) title.

    QString getDescription() const
    :   Returns the notification description.

        Returns:
        :   [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) description.

    void setDescription(const QString &description)
    :   Sets the notification description.

        Parameters:
        :   **description** – [Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#classmv_1_1util_1_1Notification) description.

    QSize minimumSizeHint() const override
    :   Returns the preferred minimum notification size.

        Returns:
        :   Minimum size hint.

    QSize sizeHint() const override
    :   Returns the preferred notification size.

        Returns:
        :   Size hint.

    void finished()
    :   Emitted when this notification has finished displaying.

    void linkActivated(const QUrl &url)
    :   Emitted when a hyperlink in the notification is clicked.

        Parameters:
        :   **url** – Activated hyperlink URL.

    Protected Functions

    void showEvent(QShowEvent \*event) override
    :   Handles initial positioning and slide-in animation when shown.

        Parameters:
        :   **event** – Show event.

    void updatePosition()
    :   Updates this notification and following notifications in the stack.

    class NotificationWidget : public QWidget
    :   Inner widget used to paint the notification background.

        Public Functions

        void paintEvent(QPaintEvent \*event) override
        :   Paints the rounded notification background.

            Parameters:
            :   **event** – Paint event.

        QSize sizeHint() const override
        :   Returns the preferred inner notification size.

            Returns:
            :   Size hint for the notification background widget.
