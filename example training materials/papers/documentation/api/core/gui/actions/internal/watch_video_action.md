# WatchVideoAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/watch_video_action.html

**Documentation path:** `api/core/gui/actions/internal/watch_video_action.html`

---

# WatchVideoAction

**Qualified name:** `mv::gui::WatchVideoAction`

class WatchVideoAction : public mv::gui::[TriggerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/trigger/trigger_action.html#_CPPv4N2mv3gui13TriggerActionE "mv::gui::TriggerAction")
:   Watch video action class.

    Watch video trigger action class

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE WatchVideoAction(QObject \*parent, const QString &title, const util::[LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") \*video = nullptr)
    :   Construct with pointer to `parent` object, `title` and pointer to `video`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **video** – Pointer to video
