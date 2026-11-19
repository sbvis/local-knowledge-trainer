# Logger

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/logging/logger.html

**Documentation path:** `api/core/util/logging/logger.html`

---

# Logger

**Qualified name:** `mv::util::Logger`

`Logger` is the application-owned store behind ManiVault’s global Qt message handler. It maintains structured [MessageRecord](https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html) entries, provides synchronized access to them, and supports the models that present newly captured records in the interface.

Application startup initializes the logger. Plugin code should emit Qt log messages rather than construct or initialize another `Logger`. The record-access and mutex APIs primarily support Core presentation and integration code.

class Logger
:   Global application logger.

    Class for recording log messages

    **Author**
    :   Niels Dekker (original design) and Thomas Kroes (re-design and refactor)

    Friends

    *friend class* mv::Application
