# DropWidget

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html

**Documentation path:** `api/core/gui/widgets/drop_widget.html`

---

# DropWidget

**Qualified name:** `mv::gui::DropWidget`

`DropWidget` adds dataset-aware drag-and-drop regions to an existing Qt widget without requiring a custom widget subclass. The target supplies a callback that inspects the incoming MIME data and returns the operations applicable to that drag.

For setup, validation, ownership, and complete plugin-side patterns, begin with [Dataset drag and drop](https://manivault.readthedocs.io/en/latest/development/building_plugins/drag_and_drop/index.html). Dataset hierarchy drags are represented by [DatasetsMimeData](https://manivault.readthedocs.io/en/latest/api/core/data/datasets_mime_data.html).

class DropWidget : public QWidget
:   Advanced drop widget class.

    This class adds advanced drag and drop support to arbitrary (parent) widget without having to change it Depending on the data being dragged, an overlay is presented with one or more drop regions Each region has its own visual representation and drop behaviour (with custom lambda function)

    Note: Add the following line to the parent widget to enabled drag and drop: setAcceptDrops(true);

    **Author**
    :   Thomas Kroes

    Public Types

    using DropRegions = QList<[DropRegion](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget10DropRegionE "mv::gui::DropWidget::DropRegion")\*>
    :   Alias for dropping regions list.

    using GetDropRegionsFunction = std::function<[DropRegions](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget11DropRegionsE "mv::gui::DropWidget::DropRegions")(const QMimeData\*)>
    :   Function for obtaining a list of available drop regions.

    Public Functions

    DropWidget(QWidget \*parent)
    :   Constructor.

        Parameters:
        :   **parent** – Parent widget

    bool eventFilter(QObject \*target, QEvent \*event) override
    :   Respond to `target` events.

        Parameters:
        :   - **target** – Object of which an event occurred
            - **event** – The event that took place

    void initialize(const [GetDropRegionsFunction](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget22GetDropRegionsFunctionE "mv::gui::DropWidget::GetDropRegionsFunction") &getDropRegions)
    :   Initialize the drop widget.

        Parameters:
        :   **getDropRegions** – Function that (based on mime data) returns a list of drop regions

    bool getShowDropIndicator() const
    :   Get/set whether to show the drop indicator widget.

    void setDropIndicatorWidget(QWidget \*dropIndicatorWidget)
    :   Sets the drop indicator widget.

        Parameters:
        :   **dropIndicatorWidget** – Drop indicator widget

    Protected Attributes

    bool \_showDropIndicator
    :   Function that (based on mime data) returns a list of drop regions.

    QWidget \*\_dropIndicatorWidget
    :   Whether to show a drop indicator widget overlay.

    class DropIndicatorWidget : public QWidget
    :   Drop indicator widget class.

        Convenience (standard) class for a drop indicator (some visual cues that something can be dropped)

        **Author**
        :   Thomas Kroes

        Public Functions

        DropIndicatorWidget(QWidget \*parent, const QString &title, const QString &description)
        :   Constructor.

            Parameters:
            :   - **parent** – Parent widget
                - **title** – Title
                - **description** – Description

    class DropRegion : public QObject
    :   Drop region class.

        This class represents a drop region (a region where mime data can be dropped) It has a visual representation `widget` and a callback function `dropped` when dropping takes place

        **Author**
        :   Thomas Kroes

        Public Types

        using Dropped = std::function<void(void)>
        :   Callback function when mime data is dropped.

        Public Functions

        DropRegion(QObject \*parent, QWidget \*widget, const [Dropped](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget10DropRegion7DroppedE "mv::gui::DropWidget::DropRegion::Dropped") &dropped = [Dropped](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget10DropRegion7DroppedE "mv::gui::DropWidget::DropRegion::Dropped")())
        :   Constructs a drop region object with a custom widget.

            Parameters:
            :   - **parent** – Parent widget to enable drag and drop behavior for
                - **widget** – Widget for the visual representation of the region
                - **iconName** – Name of the icon
                - **dropped** – Callback function when mime data is dropped

        DropRegion(QObject \*parent, const QString &title, const QString &description, const QString &iconName = "file-import", const bool &dropAllowed = true, const [Dropped](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget10DropRegion7DroppedE "mv::gui::DropWidget::DropRegion::Dropped") &dropped = [Dropped](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget10DropRegion7DroppedE "mv::gui::DropWidget::DropRegion::Dropped")())
        :   Constructs a drop region object with a standard widget.

            Parameters:
            :   - **parent** – Parent widget to enable drag and drop behavior for
                - **title** – Title of the drop region
                - **description** – Description of the drop region
                - **iconName** – Name of the icon
                - **dropAllowed** – Whether dropping is allowed in the region
                - **dropped** – Callback function when mime data is dropped

        QWidget \*getWidget() const
        :   Get visual representation of the region.

        void drop()
        :   Initiate the dropping process.

        Protected Attributes

        const [Dropped](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget10DropRegion7DroppedE "mv::gui::DropWidget::DropRegion::Dropped") \_dropped
        :   visual representation of the region

        class StandardWidget : public QWidget
        :   Standard widget class.

            Drop region widget class for standardized visual representation

            **Author**
            :   Thomas Kroes

            Public Functions

            StandardWidget(QWidget \*parent, const QString &title, const QString &description, const QString &iconName = "file-import", const bool &dropAllowed = true)
            :   Constructor.

                Parameters:
                :   - **parent** – Parent widget
                    - **title** – Title of the drop region
                    - **description** – Description of the drop region
                    - **iconName** – Name of the icon
                    - **dropAllowed** – Whether dropping is allowed in the region

    class DropRegionContainerWidget : public QWidget
    :   Drop region container widget class.

        This class is the widget representation that is added to the layout of the drop widget

        **Author**
        :   Thomas Kroes

        Public Functions

        DropRegionContainerWidget([DropRegion](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget10DropRegionE "mv::gui::DropWidget::DropRegion") \*dropRegion, QWidget \*parent)
        :   Constructor.

            Parameters:
            :   - **dropRegion** – Drop region
                - **parent** – Parent widget

        [DropRegion](https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/drop_widget.html#_CPPv4N2mv3gui10DropWidget10DropRegionE "mv::gui::DropWidget::DropRegion") \*getDropRegion()
        :   Get the drop region.

        Protected Functions

        void setHighLight(const bool &highlight = false)
        :   Sets the highlight state of the widget.

            Parameters:
            :   **highlight** – Whether to highlight the widget or not

        Protected Attributes

        util::[WidgetFader](https://manivault.readthedocs.io/en/latest/api/core/util/widget/widget_fader.html#_CPPv4N2mv4util11WidgetFaderE "mv::util::WidgetFader") \_widgetFader
        :   Drop region.

        Friends

        *friend class* DropWidget
