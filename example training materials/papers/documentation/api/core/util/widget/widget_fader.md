# WidgetFader

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/widget/widget_fader.html

**Documentation path:** `api/core/util/widget/widget_fader.html`

---

# WidgetFader

**Qualified name:** `mv::util::WidgetFader`

class WidgetFader : public QObject
:   Widget fader utility class.

    Helper class for fading in/out a target widget.

    **Author**
    :   Thomas Kroes

    Public Functions

    WidgetFader(QObject \*parent, QWidget \*targetWidget, float opacity = 0.0f, float minimumOpacity = 0.0f, float maximumOpacity = 1.0f, std::int32\_t fadeInDuration = 150, std::int32\_t fadeOutDuration = 150)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **targetWidget** – Pointer to target widget to fade
            - **opacity** – Initial opacity [0, 1]
            - **minimumOpacity** – Target fade in opacity [0, 1]
            - **maximumOpacity** – Target fade out opacity [0, 1]
            - **fadeInDuration** – Duration of the fade in animation
            - **fadeOutDuration** – Duration of the fade out animation

    void fadeIn(std::int32\_t duration = -1)
    :   Fade in the target widget.

        Parameters:
        :   **duration** – Only used if duration >= 0, otherwise uses \_fadeInDuration

    void fadeOut(std::int32\_t duration = -1, bool autoHideAfterFade = false)
    :   Fade out the target widget.

        Parameters:
        :   - **duration** – Only used if duration >= 0, otherwise uses \_fadeOutDuration
            - **autoHideAfterFade** – The widget automatically hides itself once the fade-out process completes

    void setOpacity(float opacity, std::uint32\_t duration = 0, std::uint32\_t delay = 0)
    :   Set opacity.

        Parameters:
        :   - **opacity** – Opacity
            - **duration** – Animation duration in milliseconds
            - **delay** – Animation delay in milliseconds

    bool isFadedIn() const
    :   Get whether the target widget is faded in.

        Returns:
        :   Boolean determining whether the target widget is faded in

    bool isFadedOut() const
    :   Get whether the target widget is faded out.

        Returns:
        :   Boolean determining whether the target widget is faded out

    float getMinimumOpacity() const
    :   Get minimum opacity.

    float getMaximumOpacity() const
    :   Get maximum opacity.

    void setMinimumOpacity(float minimumOpacity)
    :   Set minimum opacity.

        Parameters:
        :   **minimumOpacity** – Minimum opacity

    void setMaximumOpacity(float maximumOpacity)
    :   Set maximum opacity.

        Parameters:
        :   **maximumOpacity** – Maximum opacity

    std::int32\_t getFadeInDuration() const
    :   Get fade-in duration.

    std::int32\_t getFadeOutDuration() const
    :   Get fade-out duration.

    void setFadeInDuration(std::int32\_t fadeInDuration)
    :   Set fade-in duration.

        Parameters:
        :   **fadeInDuration** – Fade-in duration in milliseconds

    void setFadeOutDuration(std::int32\_t fadeOutDuration)
    :   Set fade-out duration.

        Parameters:
        :   **fadeOutDuration** – Fade-out duration in milliseconds

    QGraphicsOpacityEffect &getOpacityEffect()
    :   Get opacity effect.

        Returns:
        :   Reference to opacity effect

    void fadedIn()
    :   Signals that the animation has faded in.

    void fadedOut()
    :   Signals that the animation has faded out.

    void opacityChanged(float opacity)
    :   Signals that the opacity changed to `opacity`.

        Parameters:
        :   **opacity** – Current opacity
