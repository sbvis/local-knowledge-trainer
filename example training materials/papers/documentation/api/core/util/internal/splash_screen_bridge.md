# SplashScreenBridge

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/internal/splash_screen_bridge.html

**Documentation path:** `api/core/util/internal/splash_screen_bridge.html`

---

# SplashScreenBridge

**Qualified name:** `mv::util::SplashScreenBridge`

class SplashScreenBridge : public QObject
:   Splash screen bridge utility class.

    For interaction between splash screen HTML and C++ code

    Note: This utility class is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit SplashScreenBridge(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** –

    int progress() const
    :   Get progress value.

        Returns:
        :   Progress value in range [0, 100]

    QString progressDescription() const
    :   Get progress description.

        Returns:
        :   Progress description

    void setProgress(int progress)
    :   Set progress value to `progress`.

        Parameters:
        :   **progress** – Progress value in range [0, 100]

    void setProgressDescription(const QString &progressDescription)
    :   Set progress description to `description`.

        Parameters:
        :   **progressDescription** – Progress description

    void requestInitial()
    :   called by JS at load

    void progressChanged(int progress)
    :   Signals that progress changed to `progress`.

        Parameters:
        :   **progress** – New progress value in range [0, 100]

    void progressDescriptionChanged(const QString &description)
    :   Signals that progress description changed to `description`.

        Parameters:
        :   **description** – New progress description
