# AbstractHelpManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_help_manager.html

**Documentation path:** `api/core/managers/abstract_help_manager.html`

---

# AbstractHelpManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the help manager
mv::help()->...
```

**Qualified name:** `mv::AbstractHelpManager`

class AbstractHelpManager : public mv::[AbstractManager](https://manivault.readthedocs.io/en/latest/api/core/managers/abstract_manager.html#_CPPv4N2mv15AbstractManagerE "mv::AbstractManager")
:   Abstract help manager class.

    Base abstract help manager class

    **Author**
    :   Thomas Kroes

    Public Functions

    inline AbstractHelpManager(QObject \*parent)
    :   Construct manager with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    virtual void addVideo(const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video) = 0
    :   Add `video`.

        Parameters:
        :   **video** – Pointer to video to add

    virtual util::LearningCenterVideos getVideos(const QStringList &tags) const = 0
    :   Get videos for `tags`.

        Parameters:
        :   **tags** – Filter tags (returns all videos if empty)

        Returns:
        :   Vector of videos

    virtual const [LearningCenterVideosModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/videos/learning_center_videos_model.html#_CPPv4N2mv25LearningCenterVideosModelE "mv::LearningCenterVideosModel") &getVideosModel() const = 0
    :   Get videos model.

        Returns:
        :   Const reference to videos model

    virtual QMenu \*getVideosMenu() const = 0
    :   Get videos menu (e.g.

        for use in the main menu)

        Returns:
        :   Pointer to videos menu

    virtual void addTutorial(const util::[LearningCenterTutorial](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_tutorial.html#_CPPv4N2mv4util22LearningCenterTutorialE "mv::util::LearningCenterTutorial") \*tutorial) = 0
    :   Add `tutorial`.

        Parameters:
        :   **tutorial** – Pointer to tutorial to add

    virtual util::LearningCenterTutorials getTutorials(const QStringList &includeTags, const QStringList &excludeTags = QStringList()) const = 0
    :   Get tutorials for `tags`.

        Parameters:
        :   - **includeTags** – Filter tags (returns all tutorials if empty)
            - **excludeTags** – Filter exclude tags

        Returns:
        :   Vector of tutorials

    virtual const [LearningCenterTutorialsModel](https://manivault.readthedocs.io/en/latest/api/core/models/learning_center/tutorials/learning_center_tutorials_model.html#_CPPv4N2mv28LearningCenterTutorialsModelE "mv::LearningCenterTutorialsModel") &getTutorialsModel() const = 0
    :   Get tutorials model.

        Returns:
        :   Const reference to tutorials model

    virtual const ThirdPartyLicensesListModel &getThirdPartyLicensesModel() const = 0
    :   Get aggregated third-party license model.

        Returns:
        :   Const reference to the third-party license model

    virtual QMenu \*getTutorialsMenu() const = 0
    :   Get tutorials menu (e.g.

        for use in the main menu)

        Returns:
        :   Pointer to tutorials menu

    virtual void addNotification(const QString &title, const QString &description, const QIcon &icon = QIcon(), const util::[Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification")::[DurationType](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12DurationTypeE "mv::util::Notification::DurationType") &durationType = util::[Notification](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12NotificationE "mv::util::Notification")::[DurationType](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12DurationTypeE "mv::util::Notification::DurationType")::[Calculated](https://manivault.readthedocs.io/en/latest/api/core/util/notifications/notification.html#_CPPv4N2mv4util12Notification12DurationType10CalculatedE "mv::util::Notification::DurationType::Calculated"), std::int32\_t delayMs = 0) = 0
    :   Add toaster notification in the main window.

        Parameters:
        :   - **title** – Message title (maybe HTML)
            - **description** – Message description (maybe HTML)
            - **icon** – Icon to display in the notification
            - **durationType** – Duration type of the notification
            - **delayMs** – Delay in milliseconds before the notification is shown

    virtual void addNotificationLinkHandler(const QString &route, const NotificationLinkHandler &handler) = 0
    :   Add notification link handler for `route`.

        Parameters:
        :   - **route** – Route to handle (e.g. “app://open/errors”)
            - **handler** – Handler function to invoke when a link with the specified route is clicked

    virtual void handleNotificationLink(const QUrl &url) = 0
    :   Handle notification link for `url`.

        Parameters:
        :   **url** – URL of the clicked link

    virtual void initializeNotifications(QWidget \*parentWidget) = 0
    :   Initialize notifications manager with `parentWidget` widget.

        Parameters:
        :   **parentWidget** – Pointer to parent widget

    void videosModelPopulatedFromWebsite()
    :   Invoked when the videos model has been successfully populated from the website.

    Protected Functions

    virtual void addNotification(QPointer<[Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task")> task) = 0
    :   Add toaster notification for `task` in the main window.

        Parameters:
        :   **task** – [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#classmv_1_1Task) containing the notification details
