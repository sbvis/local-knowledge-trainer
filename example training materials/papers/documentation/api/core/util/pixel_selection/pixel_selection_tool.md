# PixelSelectionTool

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection_tool.html

**Documentation path:** `api/core/util/pixel_selection/pixel_selection_tool.html`

---

# PixelSelectionTool

**Qualified name:** `mv::util::PixelSelectionTool`

class PixelSelectionTool : public QObject
:   Pixel selection tool class.

    Class for pixel selection using various tools (e.g. brush, rectangle and lasso) It handles mouse/keyboard events to switch between tools and perform the selection itself It draws an overlay of the selection shape `_shapePixmap` and the selected area `_areaPixmap`

    **Author**
    :   Thomas Kroes

    Public Functions

    PixelSelectionTool(QWidget \*targetWidget, const bool &enabled = true)
    :   Constructor.

        Parameters:
        :   - **targetWidget** – Target widget on which the pixel selection tool operates
            - **enabled** – Whether the tool is enabled or not

    bool isEnabled() const
    :   Get whether the tool is enabled or not.

    void setEnabled(const bool &enabled)
    :   Set whether the tool is enabled or not.

        Parameters:
        :   **enabled** – Whether the tool is enabled or not

    [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType") getType() const
    :   Get the current pixel selection type.

    void setType(const [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType") &type)
    :   Set the current pixel selection type.

        Parameters:
        :   **type** – Pixel selection type

    [PixelSelectionModifierType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util26PixelSelectionModifierTypeE "mv::util::PixelSelectionModifierType") getModifier() const
    :   Get the current pixel selection modifier.

    void setModifier(const [PixelSelectionModifierType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util26PixelSelectionModifierTypeE "mv::util::PixelSelectionModifierType") &modifier)
    :   Set the current pixel selection modifier.

        Parameters:
        :   **modifier** – Pixel selection modifier

    bool isNotifyDuringSelection() const
    :   Get whether notifications should be fired continuously or only at the end of selection.

    void setNotifyDuringSelection(const bool &notifyDuringSelection)
    :   Set whether notifications should be fired continuously or only at the end of selection.

        Parameters:
        :   **notifyDuringSelection** – Whether notifications should be fired continuously or only at the end of selection

    float getBrushRadius() const
    :   Get brush radius.

    float getLineWidth() const
    :   Get line width.

    float getLineAngle() const
    :   Get line width.

    void setBrushRadius(const float &brushRadius)
    :   Set brush radius.

        Parameters:
        :   **brushRadius** – Brush radius

    void setLineWidth(const float &lineWidth)
    :   Set line width.

        Parameters:
        :   **lineWidth** – Line width

    void setLineAngle(const float &lineAngle)
    :   Set line width.

        Parameters:
        :   **lineAngleLine** – width

    Qt::KeyboardModifier getFixedBrushRadiusModifier() const
    :   Get fixed brush radius modifier.

    void setFixedBrushRadiusModifier(Qt::KeyboardModifier fixedBrushRadiusModifier)
    :   Set fixed brush radius modifier.

    Qt::KeyboardModifier getFixedLineWidthModifier() const
    :   Get fixed line width modifier.

    void setFixedLineWidthModifier(Qt::KeyboardModifier fixedLineWidthModifier)
    :   Set fixed brush radius modifier.

    Qt::KeyboardModifier getFixedLineAngleModifier() const
    :   Get fixed line width modifier.

    void setFixedLineAngleModifier(Qt::KeyboardModifier fixedLineAngleModifier)
    :   Set fixed brush radius modifier.

    QColor getMainColor() const
    :   Get main drawing color.

    void setMainColor(const QColor &mainColor)
    :   Set main drawing color.

        Parameters:
        :   **color** – Drawing color

    void setChanged()
    :   Trigger signals.

    inline bool isActive() const
    :   Get whether the selection process is currently active.

        Returns:
        :   Boolean indicating whether the selection process is currently active

    inline bool isAborted() const
    :   Get whether the selection process is aborted.

        Returns:
        :   Boolean indicating whether the selection process is aborted

    inline QPixmap getShapePixmap()
    :   Get the pixmap overlay that contains the selection tool visualization.

    inline QPixmap getAreaPixmap()
    :   Get the pixmap overlay that contains the selected pixels.

    void update()
    :   Updates the pixel selection tool (wraps internal paint method)

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Listens to the events of `target`.

        Parameters:
        :   - **target** – Target object to watch for events
            - **event** – Event that occurred

    void typeChanged(const [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType") &type)
    :   Signals that the type has changed.

    void modifierChanged(const [PixelSelectionModifierType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util26PixelSelectionModifierTypeE "mv::util::PixelSelectionModifierType") &modifier)
    :   Signals that the selection modifier has changed.

    void notifyDuringSelectionChanged(const bool &notifyDuringSelection)
    :   Signals that the notify during selection property has changed.

    void brushRadiusChanged(const float &brushRadius)
    :   Signals that the brush radius has changed.

    void lineWidthChanged(const float &lineWidth)
    :   Signals that the brush radius has changed.

    void lineAngleChanged(const float &lineAngle)
    :   Signals that the brush radius has changed.

    void shapeChanged()
    :   Signals that the selection shape changed.

    void areaChanged()
    :   Signals that the selection area changed.

    void started()
    :   Signals that the selection process has started.

    void ended()
    :   Signals that the selection process has ended.

    Public Static Attributes

    static constexpr float BRUSH\_RADIUS\_MIN = 10.0f
    :   Closing point pen (e.g.

        for finishing polygon selection)

    static constexpr float BRUSH\_RADIUS\_MAX = 500.0f
    :   Minimum radius.

    static constexpr float BRUSH\_RADIUS\_DEFAULT = 50.0f
    :   Maximum radius.

    static constexpr float BRUSH\_RADIUS\_DELTA = 10.0f
    :   Default radius.

    static constexpr float LINE\_WIDTH\_MIN = 1.0f
    :   Radius increment.

    static constexpr float LINE\_WIDTH\_MAX = 1000.0f
    :   Minimum width.

    static constexpr float LINE\_WIDTH\_DEFAULT = 10.0f
    :   Maximum width.

    static constexpr float LINE\_WIDTH\_DELTA = 1.0f
    :   Default width.

    static constexpr float LINE\_ANGLE\_MIN = 0.0f
    :   Width increment.

    static constexpr float LINE\_ANGLE\_MAX = 360.0f
    :   Minimum angle.

    static constexpr float LINE\_ANGLE\_DEFAULT = 0.0f
    :   Maximum angle.

    static constexpr float LINE\_ANGLE\_DELTA = 0.1f
    :   Default angle.

    static constexpr float CP\_RADIUS\_LINE = 8.0f
    :   Angle increment.

    static constexpr float CP\_RADIUS\_CLOSING = 2.5f \* [CP\_RADIUS\_LINE](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection_tool.html#_CPPv4N2mv4util18PixelSelectionTool14CP_RADIUS_LINEE "mv::util::PixelSelectionTool::CP_RADIUS_LINE")
    :   Radius of line control points.

    Protected Attributes

    std::int32\_t \_drawFlags
    :   Whether the tool is enabled or not.

    [PixelSelectionType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util18PixelSelectionTypeE "mv::util::PixelSelectionType") \_type
    :   Draw options.

    [PixelSelectionModifierType](https://manivault.readthedocs.io/en/latest/api/core/util/pixel_selection/pixel_selection.html#_CPPv4N2mv4util26PixelSelectionModifierTypeE "mv::util::PixelSelectionModifierType") \_modifier
    :   Current selection type.

    bool \_active
    :   Current selection modifier.

    bool \_notifyDuringSelection
    :   Whether the selection process is active.

    float \_brushRadius
    :   Whether the selection is published continuously or at the end.

    float \_lineWidth
    :   Brush radius.

    float \_lineAngle
    :   Line width.

    Qt::KeyboardModifier \_fixedBrushRadiusModifier
    :   Line angle.

    Qt::KeyboardModifier \_fixedLineWidthModifier
    :   Do not change brush radius when fixed by pressing a key (e.g.

        for navigation)

    Qt::KeyboardModifier \_fixedLineAngleModifier
    :   Do not change line width when fixed by pressing a key (e.g.

        for navigation)

    QPoint \_mousePosition
    :   Do not change line angle when fixed by pressing a key (e.g.

        for navigation)

    QVector<QPoint> \_mousePositions
    :   Current mouse position.

    int \_mouseButtons
    :   Recorded mouse positions.

    QPixmap \_shapePixmap
    :   State of the left, middle and right mouse buttons.

    QPixmap \_areaPixmap
    :   Pixmap for the selection tool shape.

    bool \_preventContextMenu
    :   Pixmap for the selection area.

    bool \_aborted
    :   Whether to prevent a context menu.

    QColor \_fillColor
    :   Main drawing color.

    QBrush \_areaBrush
    :   [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) area fill color (based on main color)

    QPen \_penLineForeGround
    :   [Selection](https://manivault.readthedocs.io/en/latest/api/core/graphics/helpers/selection.html#classmv_1_1Selection) area brush.

    QPen \_penLineBackGround
    :   Foreground pen.

    QPen \_penControlPoint
    :   Background pen.

    QPen \_penClosingPoint
    :   Control point pen.

    Protected Static Attributes

    static const std::int32\_t LAZY\_UPDATE\_INTERVAL = 10
    :   Whether the selection process was aborted.
