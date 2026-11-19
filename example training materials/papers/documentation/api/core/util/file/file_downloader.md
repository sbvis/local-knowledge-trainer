# FileDownloader

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/file/file_downloader.html

**Documentation path:** `api/core/util/file/file_downloader.html`

---

# FileDownloader

**Qualified name:** `mv::util::FileDownloader`

class FileDownloader : public QObject
:   File downloader class.

    Helper class for simplifying file download

    **Author**
    :   Thomas Kroes

    Public Static Functions

    static [SecureNetworkAccessManager](https://manivault.readthedocs.io/en/latest/api/core/util/network/secure_network_access_manager.html#_CPPv4N2mv4util26SecureNetworkAccessManagerE "mv::util::SecureNetworkAccessManager") &sharedManager()
    :   Get the shared network access manager instance.

        Returns:
        :   Reference to the shared QNetworkAccessManager instance

    static QFuture<QByteArray> downloadToByteArrayAsync(const QUrl &url, [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task = nullptr)
    :   Download file to byte array asynchronously.

        Parameters:
        :   - **url** – URL of the file to download
            - **task** – Optional task to associate with the download operation (must live in the main/GUI thread)

        Returns:
        :   Future containing the downloaded data as byte array

    static QFuture<QString> downloadToFileAsync(const QUrl &url, const QString &targetDirectory = "", [Task](https://manivault.readthedocs.io/en/latest/api/core/task/task.html#_CPPv4N2mv4TaskE "mv::Task") \*task = nullptr, bool overwriteAllowed = true)
    :   Download file from `url` to `targetDirectory` asynchronously.

        Parameters:
        :   - **url** – URL of the file to download
            - **targetDirectory** – Directory where the file should be saved (OS temporary dir when empty)
            - **task** – Optional task to associate with the download operation (must live in the main/GUI thread)
            - **overwriteAllowed** – Whether it is ok to overwrite existing download

        Returns:
        :   Future containing the path to the downloaded file

    static QFuture<std::uint64\_t> getDownloadSizeAsync(const QUrl &url)
    :   Get the size of the file to be downloaded asynchronously.

        Parameters:
        :   **url** – URL of the file to be downloaded

        Returns:
        :   Size of the file to be downloaded in bytes, 0 if size cannot be determined

    static QFuture<QDateTime> getLastModifiedAsync(const QUrl &url)
    :   Get the last modified date of the file at `url` asynchronously.

        Parameters:
        :   **url** – URL of the file to check

        Returns:
        :   Last modified date of the file, QDateTime() if it cannot be determined

    static QFuture<QString> getFinalFileNameAsync(const QUrl &url)
    :   Get the final file name of the file at `url` asynchronously (works with redirected URL)

        Parameters:
        :   **url** – URL of the file to check

        Returns:
        :   QFuture that will contain the final file name of the file, or an empty string if it cannot be determined

    class ByteArraySink : public mv::util::[FileDownloader](https://manivault.readthedocs.io/en/latest/api/core/util/file/file_downloader.html#_CPPv4N2mv4util14FileDownloaderE "mv::util::FileDownloader")::[ISink](https://manivault.readthedocs.io/en/latest/api/core/util/file/file_downloader.html#_CPPv4I0EN2mv4util14FileDownloader5ISinkE "mv::util::FileDownloader::ISink")<QByteArray>
    :   Saves the download to a byte array.

        Public Functions

        virtual bool open(QNetworkReply \*reply, const QUrl &url, const QString &targetDirectory, bool overwriteAllowed, QString \*error) override
        :   Finalize successfully (e.g., commit QSaveFile)

            Parameters:
            :   - **reply** – Pointer to network reply (may not be nullptr)
                - **url** – Url to download
                - **targetDirectory** – Target directory where to put the download
                - **overwriteAllowed** – Whether it is allowed to overwrite an existing download
                - **error** – Pointer to error

            Returns:
            :   Whether successfully opened

        virtual bool write(const QByteArray &chunk, QString \*error) override
        :   Write `chunk` with `error`.

            Parameters:
            :   - **chunk** – Chunk of data
                - **error** – Pointer to error

            Returns:
            :   Whether successfully written

        virtual bool commit(QString \*error) override
        :   Finalize successfully (e.g., commit QSaveFile)

            Parameters:
            :   **error** – Pointer to error

            Returns:
            :   Whether commit was successful

        virtual void cancel() noexcept override
        :   Discards partial output.

        virtual QByteArray result() const override
        :   Get the resulting value to emit into the promise.

            Returns:
            :   The promise result

    class FileSink : public mv::util::[FileDownloader](https://manivault.readthedocs.io/en/latest/api/core/util/file/file_downloader.html#_CPPv4N2mv4util14FileDownloaderE "mv::util::FileDownloader")::[ISink](https://manivault.readthedocs.io/en/latest/api/core/util/file/file_downloader.html#_CPPv4I0EN2mv4util14FileDownloader5ISinkE "mv::util::FileDownloader::ISink")<QString>
    :   Saves the download to a file on disk.

        Public Functions

        virtual bool open(QNetworkReply \*reply, const QUrl &url, const QString &targetDirectory, bool overwriteAllowed, QString \*error) override
        :   Finalize successfully (e.g., commit QSaveFile)

            Parameters:
            :   - **reply** – Pointer to network reply (may not be nullptr)
                - **url** – Url to download
                - **targetDirectory** – Target directory where to put the download
                - **overwriteAllowed** – Whether it is allowed to overwrite an existing download
                - **error** – Pointer to error

            Returns:
            :   Whether successfully opened

        virtual bool write(const QByteArray &chunk, QString \*error) override
        :   Write `chunk` with `error`.

            Parameters:
            :   - **chunk** – Chunk of data
                - **error** – Pointer to error

            Returns:
            :   Whether successfully written

        virtual bool commit(QString \*error) override
        :   Finalize successfully (e.g., commit QSaveFile)

            Parameters:
            :   **error** – Pointer to error

            Returns:
            :   Whether commit was successful

        virtual void cancel() noexcept override
        :   Discards partial output.

        virtual QString result() const override
        :   Get the resulting value to emit into the promise.

            Returns:
            :   The promise result

    template<typename T> struct ISink
    :   Public Functions

        virtual bool open(QNetworkReply \*reply, const QUrl &url, const QString &targetDirectory, bool overwriteAllowed, QString \*error) = 0
        :   Finalize successfully (e.g., commit QSaveFile)

            Parameters:
            :   - **reply** – Pointer to network reply (may not be nullptr)
                - **url** – Url to download
                - **targetDirectory** – Target directory where to put the download
                - **overwriteAllowed** – Whether it is allowed to overwrite an existing download
                - **error** – Pointer to error

            Returns:
            :   Whether successfully opened

        virtual bool write(const QByteArray &chunk, QString \*error) = 0
        :   Write `chunk` with `error`.

            Parameters:
            :   - **chunk** – Chunk of data
                - **error** – Pointer to error

            Returns:
            :   Whether successfully written

        virtual bool commit(QString \*error) = 0
        :   Finalize successfully (e.g., commit QSaveFile)

            Parameters:
            :   **error** – Pointer to error

            Returns:
            :   Whether commit was successful

        virtual void cancel() noexcept = 0
        :   Discards partial output.

        virtual Result result() const = 0
        :   Get the resulting value to emit into the promise.

            Returns:
            :   The promise result
