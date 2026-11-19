# HttpsErrorReply

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/network/https_error_reply.html

**Documentation path:** `api/core/util/network/https_error_reply.html`

---

# HttpsErrorReply

**Qualified name:** `mv::util::HttpsErrorReply`

class HttpsErrorReply : public QNetworkReply
:   HTTPS error reply class.

    Custom reply class for non-HTTPS requests.

    **Author**
    :   Thomas Kroes

    Public Functions

    HttpsErrorReply(const QNetworkRequest &request, QObject \*parent = nullptr)
    :   Construct with a network `request` and an optional `parent`.

        Parameters:
        :   - **request** – The network request that caused the error
            - **parent** – The parent object (optional)

    void abort() override
    :   Abort the reply (this method is called when the reply is aborted).

    qint64 readData(char \*data, qint64 maxlen) override
    :   Read data from the reply.

        Parameters:
        :   - **data** – Pointer to the data buffer where the read data will be stored
            - **maxlen** – Maximum length of data to read

        Returns:
        :   The number of bytes read, or -1 if no data is available
