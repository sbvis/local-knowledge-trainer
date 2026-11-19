# MarkdownDialog

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/markdown_dialog.html

**Documentation path:** `api/core/gui/widgets/internal/markdown_dialog.html`

---

# MarkdownDialog

**Qualified name:** `mv::util::MarkdownDialog`

class MarkdownDialog : public QDialog
:   Plugin read me dialog class.

    Dialog class for displaying plugin read me markdown content

    **Author**
    :   Thomas Kroes

    Public Functions

    MarkdownDialog(const QUrl &markdownUrl, QWidget \*parent = nullptr)
    :   Construct with `readmeUrl` and pointer to `parent` widget.

        Parameters:
        :   - **markdownUrl** – URL of the plugin markdown URL
            - **parent** – Pointer to parent widget

    inline QSize sizeHint() const override
    :   Get preferred size.

    inline QSize minimumSizeHint() const override
    :   Get minimum size hint.
