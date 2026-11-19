# SplashScreenAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html

**Documentation path:** `api/core/gui/actions/internal/splash_screen_action.html`

---

# SplashScreenAction

**Qualified name:** `mv::gui::SplashScreenAction`

class SplashScreenAction : public mv::gui::[HorizontalGroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html#_CPPv4N2mv3gui21HorizontalGroupActionE "mv::gui::HorizontalGroupAction")
:   Splash screen action class.

    For configuring and displaying a splash screen.

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    SplashScreenAction(QObject \*parent, bool mayCloseSplashScreenWidget = false)
    :   Construct with `parent` object and optional parameter to control whether the user can close the splash screen widget with a close tool button.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **mayCloseSplashScreenWidget** – Whether the user can close the splash screen widget with a close tool button

    ~SplashScreenAction() override = default
    :   Destructor A destructor is mandatory here because of the SplashScreenAction::\_splashScreenDialog QScopePointer <https://doc.qt.io/qt-6/qscopedpointer.html#forward-declared-pointers>.

    void addAlert(const [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#_CPPv4N2mv3gui18SplashScreenAction5AlertE "mv::gui::SplashScreenAction::Alert") &alert)
    :   Add `alert` to the splash screen.

        Parameters:
        :   **alert** – [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#classmv_1_1gui_1_1SplashScreenAction_1_1Alert) to add

    Alerts getAlerts() const
    :   Get alerts.

        Returns:
        :   Vector of alerts

    bool getMayCloseSplashScreenWidget() const
    :   Get may close splash screen widget.

        Returns:
        :   Whether the user can close the splash screen widget with a close tool button

    void setMayCloseSplashScreenWidget(bool mayCloseSplashScreenWidget)
    :   Set may close splash screen widget.

        Parameters:
        :   **mayCloseSplashScreenWidget** – Whether the user can close the splash screen widget with a close tool button

    QString getHtml() const
    :   Get HTML content.

        Returns:
        :   HTML content, empty string if not available

    [ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#_CPPv4N2mv17ProjectMetaActionE "mv::ProjectMetaAction") \*getProjectMetaAction() const
    :   Get project meta action.

        Returns:
        :   Pointer to project meta action, nullptr if not available

    void setProjectMetaAction([ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#_CPPv4N2mv17ProjectMetaActionE "mv::ProjectMetaAction") \*projectMetaAction)
    :   Get project meta action to `projectMetaAction`.

        Parameters:
        :   **projectMetaAction** – Pointer to project meta action

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load splash screen action from variant.

        Parameters:
        :   **variantMap** – Variant representation of the project

    virtual QVariantMap toVariantMap() const override
    :   Save splash screen action to variant.

        Returns:
        :   Variant representation of the project

    Public Static Functions

    static QString pixmapToBase64(const QPixmap &pixmap)
    :   Convert `pixmap` to base64 string.

        Parameters:
        :   **pixmap** – Pixmap to convert

        Returns:
        :   Base64 representation of the pixmap, empty string if not available

    Protected Functions

    void showSplashScreenWidget()
    :   Shows the splash screen widget.

    void closeSplashScreenWidget()
    :   Animates the splash screen widget’s opacity and position and afterwards closes it.

    bool shouldDisplayProjectInfo() const
    :   Establishes whether project information should be shown or not.

    QString getHtmlFromTemplate() const
    :   Get HTML from template (located in resources)

        Returns:
        :   HTML content from template, empty string if not available

    void setStartupTask([Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*startupTask)
    :   Set startup task to `startupTask`.

        Parameters:
        :   **startupTask** – Pointer to startup task

    Friends

    *friend class* mv::Application

    class Alert
    :   Basic class to add an alert on the splash screen.

        Public Functions

        inline Alert(const Type &type, const QString &iconName, const QString &message, const QColor &color = Qt::black)
        :   Construct from `type`, `iconName`, `message` and color.

            Parameters:
            :   - **type** – [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#classmv_1_1gui_1_1SplashScreenAction_1_1Alert) type
                - **iconName** – Name of the icon (FontAwesome web fonts)
                - **message** – Error message
                - **color** – Icon and error message color

        Type getType() const
        :   Get alert type.

            Returns:
            :   [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#classmv_1_1gui_1_1SplashScreenAction_1_1Alert) type

        QString getIconName() const
        :   Get alert icon name.

            Returns:
            :   [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#classmv_1_1gui_1_1SplashScreenAction_1_1Alert) icon name (FontAwesome web fonts)

        QString getMessage() const
        :   Get alert message.

            Returns:
            :   [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#classmv_1_1gui_1_1SplashScreenAction_1_1Alert) message

        QColor getColor() const
        :   Get alert color.

            Returns:
            :   [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#classmv_1_1gui_1_1SplashScreenAction_1_1Alert) color

        Public Static Functions

        static [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#_CPPv4N2mv3gui18SplashScreenAction5AlertE "mv::gui::SplashScreenAction::Alert") debug(const QString &message)
        :   Create information alert.

        static [Alert](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#_CPPv4N2mv3gui18SplashScreenAction5AlertE "mv::gui::SplashScreenAction::Alert") warning(const QString &message)
        :   Create debug alert.
