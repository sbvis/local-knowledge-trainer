# CustomAssetsUrlSchemeHandler

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/network/custom_assets_url_scheme_handler.html

**Documentation path:** `api/core/util/network/custom_assets_url_scheme_handler.html`

---

# CustomAssetsUrlSchemeHandler

**Qualified name:** `mv::util::CustomAssetsUrlSchemeHandler`

class CustomAssetsUrlSchemeHandler : public QWebEngineUrlSchemeHandler
:   Custom assets URL scheme handler class.

    Gives restricted access to custom assets located in the application directory

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit CustomAssetsUrlSchemeHandler(QObject \*parent = nullptr)
    :   Construct with optional parent.

        Parameters:
        :   **parent** –

    void requestStarted(QWebEngineUrlRequestJob \*job) override
    :   Invoked when a request is started.

        Parameters:
        :   **job** – Request job
