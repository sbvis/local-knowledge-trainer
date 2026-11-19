# YouTubeVideoDialog

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/you_tube_video_dialog.html

**Documentation path:** `api/core/gui/widgets/internal/you_tube_video_dialog.html`

---

# YouTubeVideoDialog

**Qualified name:** `mv::gui::YouTubeVideoDialog`

class YouTubeVideoDialog : public QDialog
:   YouTube video dialog class.

    Dialog class for displaying a YouTube video (WIP)

    **Author**
    :   Thomas Kroes

    Public Functions

    YouTubeVideoDialog(const QString &videoId, QWidget \*parent = nullptr)
    :   Construct with `videoId` and pointer to `parent` widget.

        Parameters:
        :   - **videoId** – Globally unique identifier of the video
            - **parent** – Pointer to parent widget

    inline QSize sizeHint() const override
    :   Get preferred size.

    inline QSize minimumSizeHint() const override
    :   Get minimum size hint.

    Public Static Functions

    static void play(const QString &videoId)
    :   Create YouTube video dialog and play `videoUrl`.

        Parameters:
        :   **videoId** – Globally unique identifier of the video
