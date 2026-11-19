# JSON

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/file/json.html

**Documentation path:** `api/core/util/file/json.html`

---

# JSON

## Functions

bool mv::util::isValidJson(const std::string &input)
:   Check if a string is valid JSON.

    Parameters:
    :   **input** – String to check

    Returns:
    :   True if the string is valid JSON, false otherwise

std::string mv::util::loadJsonFromResource(const std::string &resourcePath)
:   Load JSON from a resource file.

    Parameters:
    :   **resourcePath** – Path to the JSON resource file

    Returns:
    :   Parsed JSON content as a QString

void mv::util::validateJson(const std::string &jsonString, const std::string &jsonLocation, const std::string &jsonSchemaString, const std::string &publicJsonSchemaLocation)
:   Validate JSON string content against a schema defined in a resource file as a JSON string.

    Parameters:
    :   - **jsonString** – JSON content string to validate
        - **jsonLocation** – Location of the JSON file
        - **jsonSchemaString** – JSON schema content string
        - **publicJsonSchemaLocation** – Location of the public JSON schema
