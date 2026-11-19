# MessageRecord

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/logging/message_record.html

**Documentation path:** `api/core/util/logging/message_record.html`

---

# MessageRecord

**Qualified name:** `mv::util::MessageRecord`

`MessageRecord` is the structured representation of one captured Qt log message. In addition to the message text and `QtMsgType`, it retains sequence, source-location, function, category, and format-version information for presentation and support diagnostics.

Records are owned by the application [Logger](https://manivault.readthedocs.io/en/latest/api/core/util/logging/logger.html). Consumers such as `LoggingModel` retain references to those records, so callers should not treat record pointers as independently owned objects.

struct MessageRecord
