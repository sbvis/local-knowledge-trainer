# MarkdownDocument

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/markdown_document.html

**Documentation path:** `api/core/gui/widgets/internal/markdown_document.html`

---

# MarkdownDocument

**Qualified name:** `mv::util::MarkdownDocument`

class MarkdownDocument : public QObject
:   Markdown document class.

    Callback object class for relaying markdown content

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit MarkdownDocument(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    void setText(const QString &text)
    :   Set text to `text`.

        Parameters:
        :   **text** – Text

    void textChanged(const QString &text)
    :   Signals that the text changed to `text` @parent text New text.
