# ProgressAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/progress_action.html

**Documentation path:** `api/core/gui/actions/task/progress_action.html`

---

# ProgressAction

**Qualified name:** `mv::gui::ProgressAction`

class ProgressAction : public mv::gui::[WidgetAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/widget_action.html#_CPPv4N2mv3gui12WidgetActionE "mv::gui::WidgetAction")
:   Progress action class.

    Action class for displaying progress

    **Author**
    :   Thomas Kroes

    Public Types

    enum WidgetFlag
    :   Describes the widget flags.

        *Values:*

        enumerator HorizontalBar

        enumerator VerticalBar
        :   Widget includes a horizontal bar.

        enumerator Label
        :   Widget includes a vertical bar.

        enumerator LineEdit
        :   Widget includes a label widget.

        enumerator Default
        :   Widget includes a line edit widget.

    Public Functions

    Q\_INVOKABLE ProgressAction(QObject \*parent, const QString &title)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action

    int getMinimum() const
    :   Get progress range minimum.

        Returns:
        :   Progress range minimum

    void setMinimum(int minimum)
    :   Set progress range minimum to `minimum`.

        Parameters:
        :   **minimum** – Progress range minimum

    int getMaximum() const
    :   Get progress range maximum.

        Returns:
        :   Progress range maximum

    void setMaximum(int maximum)
    :   Set progress range maximum to `maximum`.

        Parameters:
        :   **maximum** – Progress range maximum

    void setRange(int minimum, int maximum)
    :   Set progress range from `minimum` to `maximum`.

        Parameters:
        :   - **minimum** – Progress range minimum
            - **maximum** – Progress range maximum

    int getProgress() const
    :   Get progress value.

        Returns:
        :   Progress value

    void setProgress(int value)
    :   Set progress value to `value`.

        Parameters:
        :   **value** – Progress value

    bool getTextVisible() const
    :   Get whether text is visible.

        Returns:
        :   Boolean determining whether text is visible

    void setTextVisible(bool textVisible)
    :   Set whether text is visible to `textVisible`.

        Parameters:
        :   **textVisible** – Boolean determining whether text is visible

    Qt::AlignmentFlag getTextAlignment() const
    :   Get text alignment.

        Returns:
        :   Text alignment flag

    void setTextAlignment(Qt::AlignmentFlag textAlignment)
    :   Set text alignment to `textAlignment`.

        Parameters:
        :   **textAlignment** – Text alignment flag

    QString getTextFormat() const
    :   Get text format.

        Returns:
        :   ProgressAction::\_textFormat when ProgressAction::\_overrideTextFormat is empty, otherwise ProgressAction::\_overrideTextFormat

    void setTextFormat(const QString &textFormat)
    :   Set text format to `textFormat` p - is replaced by the percentage completed v - is replaced by the current value m - is replaced by the total number of steps The default value is “%p%”.

        Parameters:
        :   **textFormat** – Text format string

    QString getOverrideTextFormat() const
    :   Get override text format.

        Returns:
        :   Override text format string

    void setOverrideTextFormat(const QString &overrideTextFormat)
    :   Set override text format to `overrideTextFormat` p - is replaced by the percentage completed v - is replaced by the current value m - is replaced by the total number of steps The default value is “%p%”.

        Parameters:
        :   **overrideTextFormat** – Override text format string

    int getNumberOfSteps() const
    :   Get number of steps.

        Returns:
        :   Number of steps

    float getPercentage() const
    :   Get percentage completed.

        Returns:
        :   Percentage

    QString getText() const
    :   Get text representation of the progress (using the text format)

        Returns:
        :   Text representation of the progress

    void minimumChanged(int minimum)
    :   Signals that the progress range minimum changed to `minimum`.

        Parameters:
        :   **minimum** – Updated progress range minimum

    void maximumChanged(int maximum)
    :   Signals that the progress range maximum changed to `maximum`.

        Parameters:
        :   **maximum** – Updated progress range maximum

    void numberOfStepsChanged(int numberOfSteps)
    :   Signals that the number of steps changed to `numberOfSteps`.

        Parameters:
        :   **numberOfSteps** – Number of steps

    void valueChanged(int value)
    :   Signals that the progress value changed to `value`.

        Parameters:
        :   **value** – Updated progress value

    void progressChanged(float progress)
    :   Signals that the progress changed to `percentage`.

        Parameters:
        :   **progress** – Updated progress

    void textVisibleChanged(bool textVisible)
    :   Signals that text visibility changed to `textVisible`.

        Parameters:
        :   **textVisible** – Updated text visibility

    void textAlignmentChanged(bool textAlignment)
    :   Signals that text alignment changed to `textAlignment`.

        Parameters:
        :   **textAlignment** – Updated text alignment

    void textFormatChanged(const QString &previousTextFormat, const QString &currentTextFormat)
    :   Signals that the text format changed from `previousTextFormat` to `currentTextFormat`.

        Parameters:
        :   - **previousTextFormat** – Previous text format
            - **currentTextFormat** – Current text format

    void overrideTextFormatChanged(const QString &previousOverrideTextFormat, const QString &currentOverrideTextFormat)
    :   Signals that the override text format changed from `previousOverrideTextFormat` to `currentOverrideTextFormat`.

        Parameters:
        :   - **previousOverrideTextFormat** – Previous override text format
            - **currentOverrideTextFormat** – Current override text format

    Protected Functions

    virtual QWidget \*getWidget(QWidget \*parent, const std::int32\_t &widgetFlags) override
    :   Get widget representation of the setEnabled action.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **widgetFlags** – Widget flags for the configuration of the widget (type)

    class BarWidget : public QProgressBar
    :   Bar widget for progress action.

        Public Functions

        BarWidget(QWidget \*parent, [ProgressAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/progress_action.html#_CPPv4N2mv3gui14ProgressActionE "mv::gui::ProgressAction") \*progressAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **progressAction** – Pointer to progress action
                - **widgetFlags** – Widget flags

        void paintEvent(QPaintEvent \*paintEvent) override
        :   Override the paint event to add text elidation.

            Parameters:
            :   **paintEvent** – Pointer to the paint event

        Friends

        *friend class* ProgressAction

    class LabelWidget : public QLabel
    :   Label widget for progress action.

        Protected Functions

        LabelWidget(QWidget \*parent, [ProgressAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/progress_action.html#_CPPv4N2mv3gui14ProgressActionE "mv::gui::ProgressAction") \*progressAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **progressAction** – Pointer to progress action
                - **widgetFlags** – Widget flags

        Friends

        *friend class* ProgressAction

    class LineEditWidget : public QLineEdit
    :   Line edit widget for progress action.

        Protected Functions

        LineEditWidget(QWidget \*parent, [ProgressAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/task/progress_action.html#_CPPv4N2mv3gui14ProgressActionE "mv::gui::ProgressAction") \*progressAction, const std::int32\_t &widgetFlags)
        :   Constructor.

            Parameters:
            :   - **parent** – Pointer to parent widget
                - **progressAction** – Pointer to progress action
                - **widgetFlags** – Widget flags

        Friends

        *friend class* ProgressAction
