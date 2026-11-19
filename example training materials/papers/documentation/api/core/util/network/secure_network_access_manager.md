# SecureNetworkAccessManager

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/network/secure_network_access_manager.html

**Documentation path:** `api/core/util/network/secure_network_access_manager.html`

---

# SecureNetworkAccessManager

**Qualified name:** `mv::util::SecureNetworkAccessManager`

class SecureNetworkAccessManager : public QNetworkAccessManager
:   Secure network access manager class.

    For secure, HTTPS-based, network access management.

    **Author**
    :   Thomas Kroes

    Protected Functions

    QNetworkReply \*createRequest(Operation op, const QNetworkRequest &request, QIODevice \*outgoingData = nullptr) override
    :   Create a network request, but block non-HTTPS requests.

        Parameters:
        :   - **op** – Operation to perform
            - **request** – Network request to create
            - **outgoingData** – Optional data to send with the request

        Returns:
        :   Pointer to the created network reply, or nullptr if the request is blocked
