# ElidedLabel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/elided_label.html

**Documentation path:** `api/core/gui/widgets/elided_label.html`

---

# ElidedLabel

**Qualified name:** `mv::gui::ElidedLabel`

class ElidedLabel : public QLabel
:   Elided label class.

    Truncates label text when text does not fit in the label

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit ElidedLabel(const QString &text, QWidget \*parent = nullptr, const Qt::TextElideMode &textElideMode = Qt::ElideMiddle)
    :   Construct with initial \text, pointer to `parent` widget and `textElideMode`.

        Parameters:
        :   - **parent** – Pointer to parent widget
            - **textElideMode** – Where to truncate the text; left, middle or right

    void setText(const QString &fullText)
    :   Set text to `fullText`.

        Parameters:
        :   **fullText** – Non-elided text

    void resizeEvent(QResizeEvent \*resizeEvent) override
    :   Invoked when the label is resized.

        Parameters:
        :   **resizeEvent** – Pointer to the resize event

    Qt::TextElideMode getTextElideMode() const
    :   Gets the text elide mode.

    void setTextElideMode(const Qt::TextElideMode &textElideMode)
    :   Set whether label elide is enabled or not.

        Parameters:
        :   **textElideMode** – Where to truncate the text; left, middle or right

    bool getElide() const
    :   Gets whether label elide is enabled or not.

    void setElide(bool elide)
    :   Set whether label elide is enabled or not.

        Parameters:
        :   **labelElide** – Whether label elide is enabled or not
