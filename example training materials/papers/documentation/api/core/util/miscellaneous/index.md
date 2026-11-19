# Miscellaneous

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/miscellaneous/index.html

**Documentation path:** `api/core/util/miscellaneous/index.html`

---

# Miscellaneous

This section documents a collection of general-purpose utility functions that do not fit into a single functional category. These functions support a wide range of tasks, including formatting, layout manipulation, string processing, image and CSS handling, timing utilities, and data conversion.

## Functions

QString mv::util::getIntegerCountHumanReadable(const double &count)
:   Formats an integer-like count for display.

    Parameters:
    :   **count** – Count to format.

    Returns:
    :   Human-readable count string.

std::uint64\_t mv::util::parseByteSize(const QString &input)
:   Parses a human-readable byte-size string.

    Parameters:
    :   **input** – Byte-size string to parse.

    Returns:
    :   Number of bytes represented by the input.

QString mv::util::getNoBytesHumanReadable(std::uint64\_t noBytes, bool useIEC = true)
:   Formats a byte count for display.

    Parameters:
    :   - **noBytes** – Number of bytes.
        - **useIEC** – Whether to use IEC base-1024 units instead of SI base-1000 units.

    Returns:
    :   Human-readable byte count.

template<typename ActionType> void mv::util::sortActions(QVector<QPointer<[ActionType](https://manivault.readthedocs.io/en/latest/api/core/util/miscellaneous/index.html#_CPPv4I0EN2mv4util11sortActionsEvR7QVectorI8QPointerI10ActionTypeEE "mv::util::sortActions::ActionType")>> &actions)
:   Sorts actions by their display text.

    Template Parameters:
    :   **ActionType** – Action pointer type stored in the vector.

    Parameters:
    :   **actions** – Actions to sort in place.

template<class WidgetClass> [WidgetClass](https://manivault.readthedocs.io/en/latest/api/core/util/miscellaneous/index.html#_CPPv4I0EN2mv4util10findParentEP11WidgetClassPK7QWidget "mv::util::findParent::WidgetClass") \*mv::util::findParent(const QWidget \*widget)
:   Finds the first parent widget of the requested type.

    Template Parameters:
    :   **WidgetClass** – Widget type to find.

    Parameters:
    :   **widget** – Widget whose parents should be searched.

    Returns:
    :   Matching parent widget, or nullptr when no parent matches.

inline QString mv::util::getTabIndentedMessage(QString message, const std::uint32\_t &tabIndex)
:   Adds tab indentation to a message.

    Parameters:
    :   - **message** – Message to indent.
        - **tabIndex** – Number of tab characters to prefix.

    Returns:
    :   Indented message.

QString mv::util::getColorAsCssString(const QColor &color, bool alpha = true)
:   Converts a QColor to a CSS color string.

    Parameters:
    :   - **color** – Color to convert.
        - **alpha** – Whether to include the alpha channel.

    Returns:
    :   CSS rgb(…) or rgba(…) color string.

bool mv::util::urlExists(const QString &urlString)
:   Returns whether a URL exists.

    Parameters:
    :   **urlString** – URL string to test.

    Returns:
    :   True when the URL can be reached.

void mv::util::replaceLayout(QWidget \*widget, QLayout \*newLayout, bool removeWidgets = false)
:   Replaces a widget layout.

    Parameters:
    :   - **widget** – Widget whose layout should be replaced.
        - **newLayout** – New layout to install.
        - **removeWidgets** – Whether to remove widgets from the previous layout.

void mv::util::clearLayout(QLayout \*layout, bool removeWidgets = false)
:   Clears a layout.

    Parameters:
    :   - **layout** – Layout to clear.
        - **removeWidgets** – Whether to delete contained widgets.

void mv::util::setLayoutContentsMargins(QLayout \*layout, std::int32\_t margin)
:   Sets equal contents margins on a layout.

    Parameters:
    :   - **layout** – Layout to update.
        - **margin** – Margin applied to all sides.

QIcon mv::util::getAlignmentIcon(const Qt::Alignment &alignment)
:   Returns an icon representing a Qt alignment.

    Parameters:
    :   **alignment** – Alignment to represent.

    Returns:
    :   Alignment icon.

QVariant mv::util::setValueByPath(QVariant root, const QString &path, const QVariant &value)
:   Sets a nested value in a QVariant tree by path.

    Parameters:
    :   - **root** – Root value to update.
        - **path** – Path to the nested value.
        - **value** – Value to set.

    Returns:
    :   Updated root value.

QVariant mv::util::getValueByPath(const QVariant &root, const QString &path, const QVariant &valueIfNotFound = QVariant())
:   Returns a nested value from a QVariant tree by path.

    Parameters:
    :   - **root** – Root value to inspect.
        - **path** – Path to the nested value.
        - **valueIfNotFound** – Value returned when the path is not found.

    Returns:
    :   Nested value, or valueIfNotFound when unavailable.

QString mv::util::gifToBase64(const QByteArray &gifByteArray)
:   Converts GIF bytes to a base64 string.

    Parameters:
    :   **gifByteArray** – GIF image bytes.

    Returns:
    :   Base64-encoded GIF data.

QString mv::util::embedGifFromBase64(const QString &gifBase64)
:   Embeds a base64 GIF in an HTML image tag.

    Parameters:
    :   **gifBase64** – Base64-encoded GIF data.

    Returns:
    :   HTML image tag containing the GIF.

QString mv::util::embedGifFromResource(const QString &resourcePath)
:   Embeds a GIF resource in an HTML image tag.

    Parameters:
    :   **resourcePath** – Resource path of the GIF image.

    Returns:
    :   HTML image tag containing the GIF.

void mv::util::waitForDuration(int milliSeconds)
:   Waits while keeping the application event loop responsive.

    Parameters:
    :   **milliSeconds** – Duration to wait in milliseconds.

void mv::util::disconnectRecursively(const QObject \*object)
:   Disconnects an object and all descendants.

    Parameters:
    :   **object** – Root object whose signal connections should be removed.

std::string mv::util::replaceAll(std::string inputString, const std::string &from, const std::string &to)
:   Replaces all occurrences of a substring.

    Parameters:
    :   - **inputString** – Input string.
        - **from** – Substring to replace.
        - **to** – Replacement substring.

    Returns:
    :   String with replacements applied.

std::string mv::util::stripNewLines(std::string inputString)
:   Removes CR/LF characters from a string.

    Parameters:
    :   **inputString** – Input string.

    Returns:
    :   String without newline characters.

std::string mv::util::escapeCssDq(std::string inputString)
:   Escapes text for use inside a CSS double-quoted string.

    Parameters:
    :   **inputString** – Input string.

    Returns:
    :   CSS-escaped string.

std::string mv::util::pixmapToCssSrc(const QPixmap &pixmap)
:   Converts a pixmap to a CSS data source string.

    Parameters:
    :   **pixmap** – Pixmap to encode.

    Returns:
    :   CSS url(…) data source string.

QString mv::util::mimeForFormat(const QByteArray &byteArray)
:   Detects an image MIME type from encoded bytes.

    Parameters:
    :   **byteArray** – Encoded image bytes.

    Returns:
    :   MIME type, when detected.

QByteArray mv::util::normalizeFormatFromSuffix(const QString &path)
:   Normalizes an image format from a file suffix.

    Parameters:
    :   **path** – File path whose suffix should be inspected.

    Returns:
    :   Normalized image format such as PNG or JPEG.

QByteArray mv::util::chooseFormatForImage(const QImage &img, const QByteArray &hinted)
:   Chooses an encoding format for an image.

    If the hinted format is empty, PNG is preferred for images with alpha and JPEG otherwise.

    Parameters:
    :   - **img** – Image to encode.
        - **hinted** – Optional hinted format.

    Returns:
    :   Chosen image format.

QString mv::util::pixmapToDataUrl(const QPixmap &pixmap, const QByteArray &fmt = "PNG", int quality = -1)
:   Converts a pixmap to a base64 data URL.

    Parameters:
    :   - **pixmap** – Pixmap to encode.
        - **fmt** – Encoding format.
        - **quality** – Encoding quality, or -1 for the Qt default.

    Returns:
    :   Data URL string.

QString mv::util::applyPixmapToCss(QString css, const QPixmap &pixmap, const QByteArray &format = "PNG", int quality = -1, const QString &token = QStringLiteral("{{BACKGROUND\_IMAGE}}"))
:   Replaces a CSS token with an encoded pixmap data URL.

    Parameters:
    :   - **css** – CSS text to update.
        - **pixmap** – Pixmap to encode.
        - **format** – Encoding format.
        - **quality** – Encoding quality, or -1 for the Qt default.
        - **token** – Token to replace in the CSS.

    Returns:
    :   CSS with the token replaced by a data URL.

QString mv::util::applyResourceImageToCss(QString css, const QString &pathOrResource, const QString &token, float scaleFactor = 0, int quality = 90)
:   Replaces a CSS token with an encoded image data URL.

    Parameters:
    :   - **css** – CSS text to update.
        - **pathOrResource** – Image file path or Qt resource path.
        - **token** – Token to replace in the CSS.
        - **scaleFactor** – Optional image scale factor, or 0 to keep the original size.
        - **quality** – Encoding quality, or -1 for the Qt default.

    Returns:
    :   CSS with the token replaced by a data URL.

QByteArray mv::util::ensureUtf8(QByteArray byteArray)
:   Ensures that a byte array is UTF-8 encoded.

    Parameters:
    :   **byteArray** – Input byte array.

    Returns:
    :   UTF-8 byte array, converting from UTF-16 when detected.

QByteArray mv::util::sanitizeJsonWhitespaceOutsideStrings(const QByteArray &utf8)
:   Removes whitespace outside JSON strings.

    Parameters:
    :   **utf8** – JSON text encoded as UTF-8.

    Returns:
    :   Sanitized UTF-8 JSON text.

QString mv::util::getFilenameFromContentDisposition(const QByteArray &contentDispositionRaw)
:   Extracts a filename from a Content-Disposition header.

    RFC 5987 filename\* values are preferred when present.

    Parameters:
    :   **contentDispositionRaw** – Raw Content-Disposition header value.

    Returns:
    :   Filename when found, otherwise an empty string.

QString mv::util::getFilenameFromUrlPath(const QUrl &effectiveUrl)
:   Extracts a filename from a URL path.

    Parameters:
    :   **effectiveUrl** – URL to inspect.

    Returns:
    :   Filename from the URL path.

QString mv::util::getFilenameFromWaterButlerMetadata(const QByteArray &raw)
:   Extracts a filename from OSF Waterbutler metadata JSON.

    Parameters:
    :   **raw** – Raw Waterbutler metadata JSON.

    Returns:
    :   Filename when found, otherwise an empty string.
