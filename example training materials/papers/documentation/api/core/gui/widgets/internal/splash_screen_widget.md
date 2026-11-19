# SplashScreenWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/splash_screen_widget.html

**Documentation path:** `api/core/gui/widgets/internal/splash_screen_widget.html`

---

# SplashScreenWidget

**Qualified name:** `mv::gui::SplashScreenWidget`

class SplashScreenWidget : public QWidget
:   Splash screen widget class.

    For displaying a splash screen using an [mv::gui::SplashScreenAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#classmv_1_1gui_1_1SplashScreenAction)

    **Author**
    :   Thomas Kroes

    Public Functions

    SplashScreenWidget([SplashScreenAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#_CPPv4N2mv3gui18SplashScreenActionE "mv::gui::SplashScreenAction") &splashScreenAction, QWidget \*parent = nullptr)
    :   Construct with reference to owning `splashScreenAction` and optional pointer to `parent` widget.

        Parameters:
        :   - **splashScreenAction** – Reference to owning splashScreenAction
            - **parent** – Pointer to parent widget

    ~SplashScreenWidget() override
    :   Destructor.

    void showEvent(QShowEvent \*event) override
    :   Override the show event to initialize the widget once, wraps QWidget::showEvent()

        Parameters:
        :   **event** – Pointer to show event

    void hideEvent(QHideEvent \*event) override
    :   Override the hide event to stop the event processing timer, wraps QWidget::hideEvent()

        Parameters:
        :   **event** – Pointer to hide event

    void showAnimated()
    :   Show the splash screen widget animated, wraps QWidget::show()

    void closeAnimated()
    :   Animate the splash screen widget and close it, wraps QWidget::close()
