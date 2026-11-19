# LearningCenterVideo

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html

**Documentation path:** `api/core/util/learning_center/learning_center_video.html`

---

# LearningCenterVideo

For global registration, plugin association, YouTube identifiers, GIF resources, and ownership, see [Tutorials and videos](https://manivault.readthedocs.io/en/latest/development/building_plugins/learning_center/tutorials_and_videos.html).

**Qualified name:** `mv::util::LearningCenterVideo`

class LearningCenterVideo : public QObject
:   Learning center video class.

    Contains video properties

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Type
    :   Type of video.

        *Values:*

        enumerator YouTube

        enumerator GIF
        :   Youtube video.

            GIF animation

    Public Functions

    explicit LearningCenterVideo(const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideo4TypeE "mv::util::LearningCenterVideo::Type") &type, const QString &title, const QStringList &tags, const QString &date, const QString &summary, const QString &resource)
    :   Construct video from individual properties.

        Parameters:
        :   - **type** – Type of video
            - **title** – Video title
            - **tags** – Video tags for filtering
            - **date** – Issue date
            - **summary** – Brief video description
            - **resource** – Identifier of the YouTube or GIF

    explicit LearningCenterVideo(const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideo4TypeE "mv::util::LearningCenterVideo::Type") &type, const QVariantMap &variantMap)
    :   Construct video from `variantMap`.

        Parameters:
        :   - **type** – Type of video
            - **variantMap** – Variant map containing the video properties

    const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideo4TypeE "mv::util::LearningCenterVideo::Type") &getType() const
    :   Get video type.

        Returns:
        :   Video type

    const QString &getTitle() const
    :   Get video title.

        Returns:
        :   Video title

    const QStringList &getTags() const
    :   Get video tags.

        Returns:
        :   Video tags

    const QString &getDate() const
    :   Get video date.

        Returns:
        :   Video date

    const QString &getSummary() const
    :   Get video summary (brief description)

        Returns:
        :   Video summary

    const QString &getResource() const
    :   Get video resource.

        Returns:
        :   Video resource

    QImage getThumbnailImage() const
    :   Get thumbnail image.

        Returns:
        :   Thumbnail image

    void setThumbnailImage(const QImage &thumbnailImage)
    :   Set thumbnail image to /p thumbnailImage.

        Parameters:
        :   **thumbnailImage** – Thumbnail image

    bool hasThumbnailImage() const
    :   Get whether there is a valid thumbnail image.

        Returns:
        :   Boolean determining whether there is a valid thumbnail image

    inline [LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") &operator=(const [LearningCenterVideo](https://manivault.readthedocs.io/en/latest/api/core/util/learning_center/learning_center_video.html#_CPPv4N2mv4util19LearningCenterVideoE "mv::util::LearningCenterVideo") &rhs)
    :   Overload assignment operator.

        Parameters:
        :   **rhs** – Right hand side video

        Returns:
        :   Assigned video

    void thumbnailImageReady(const QImage &thumbnailImage)
    :   Signals that /p thumbnailImage is ready for use.

        Parameters:
        :   **thumbnailImage** – Thumbnail image

    Public Static Functions

    static QString getYouTubeThumbnailUrl(const QString &videoId, const QString &quality = "mqdefault")
    :   Get youTube thumbnail for `videoId` with `quality`.

        Parameters:
        :   - **videoId** – Globally unique identifier of the video
            - **quality** – String determining the quality: “default”, “hqdefault”, “mqdefault”, “sddefault”, “maxresdefault”
