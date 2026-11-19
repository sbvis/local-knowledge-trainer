# Script

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html

**Documentation path:** `api/core/util/script/script.html`

---

# Script

**Qualified name:** `mv::util::Script`

class Script : public QObject
:   [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) class.

    Contains information for running a script

    **Author**
    :   Thomas Kroes

    Public Types

    enum class Type
    :   [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) types.

        *Values:*

        enumerator None

        enumerator Loader
        :   Not a valid script type.

        enumerator Writer
        :   Data loading scripts.

        enumerator Analysis
        :   Data writer scripts.

        enumerator Transformation
        :   Data analysis scripts.

        enumerator View
        :   Data transformation scripts.

            Data view scripts

    enum class Language
    :   [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) language.

        *Values:*

        enumerator None

        enumerator Python
        :   Not a valid script language.

        enumerator R
        :   Python scripting.

            R scripting

    Public Functions

    explicit Script(const QString &title, const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script4TypeE "mv::util::Script::Type") &type, const [Language](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script8LanguageE "mv::util::Script::Language") &language, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &languageVersion, const QString &location, QObject \*parent = nullptr)
    :   Construct script with `type` and `language`.

        Parameters:
        :   - **title** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) title
            - **type** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) type
            - **language** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) language
            - **languageVersion** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the scripting language
            - **location** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) location
            - **datasets** – List of datasets that the script can work with
            - **parent** – Pointer to parent object (optional, default is nullptr)

    explicit Script(const QString &title, const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script4TypeE "mv::util::Script::Type") &type, const [Language](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script8LanguageE "mv::util::Script::Language") &language, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &languageVersion, const QString &location, const Datasets &datasets, QObject \*parent = nullptr)
    :   Construct script with `type` and `language`.

        Parameters:
        :   - **title** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) title
            - **type** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) type
            - **language** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) language
            - **languageVersion** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the scripting language
            - **location** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) location
            - **datasets** – List of datasets that the script can work with
            - **parent** – Pointer to parent object (optional, default is nullptr)

    explicit Script(const QString &title, const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script4TypeE "mv::util::Script::Type") &type, const [Language](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script8LanguageE "mv::util::Script::Language") &language, const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &languageVersion, const QString &location, const DataTypes &dataTypes, QObject \*parent = nullptr)
    :   Construct script with `type` and `language`.

        Parameters:
        :   - **title** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) title
            - **type** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) type
            - **language** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) language
            - **languageVersion** – [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#classmv_1_1util_1_1Version) of the scripting language
            - **location** – [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) location
            - **datasets** – List of datasets that the script can work with
            - **parent** – Pointer to parent object (optional, default is nullptr)

    virtual void run()
    :   Runs the script.

    inline [Type](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script4TypeE "mv::util::Script::Type") getType() const
    :   Get script title.

    inline QString getTypeName() const
    :   Get script type.

    inline [Language](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script8LanguageE "mv::util::Script::Language") getLanguage() const
    :   Get script type name.

    inline [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") getLanguageVersion() const
    :   Get script language.

    inline QString getLocation() const
    :   Get script language version.

    inline Datasets getDatasets() const
    :   Get script location.

    inline DataTypes getDataTypes() const
    :   Get script datasets.

    QIcon getLanguageIcon() const
    :   Get script compatible data types.

    inline void setTitle(const QString &title)
    :   Get icon representing the scripting language.

    inline void setType(const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script4TypeE "mv::util::Script::Type") &type)
    :   Set script title.

    inline void setLanguage(const [Language](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script8LanguageE "mv::util::Script::Language") &language)
    :   Set script type.

    inline void setLanguageVersion(const [Version](https://manivault.readthedocs.io/en/latest/api/core/util/internal/version.html#_CPPv4N2mv4util7VersionE "mv::util::Version") &languageVersion)
    :   Set script language.

    inline void setLocation(const QString &location)
    :   Set script language version.

    inline void setDatasets(const Datasets &datasets)
    :   Set script location.

    inline void setDataTypes(const DataTypes &dataTypes)
    :   Set script datasets.

    Public Static Functions

    static QString getTypeName(const [Type](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script4TypeE "mv::util::Script::Type") &type)
    :   Get the type name from `type`.

        Parameters:
        :   **type** – Type enum

        Returns:
        :   [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) type name

    static [Type](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script4TypeE "mv::util::Script::Type") getTypeEnum(const QString &typeName)
    :   Get type enum from `typeName`.

        Parameters:
        :   **typeName** – Type name

        Returns:
        :   [Script](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#classmv_1_1util_1_1Script) type enum

    static QString getLanguageName(const [Language](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script8LanguageE "mv::util::Script::Language") &language)
    :   Get the language name from `language`.

        Parameters:
        :   **language** – Language enum

        Returns:
        :   Language name

    static [Language](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script8LanguageE "mv::util::Script::Language") getLanguageEnum(const QString &languageName)
    :   Get language enum from `language` name.

        Parameters:
        :   **languageName** – Language name

        Returns:
        :   Language enum

    Public Static Attributes

    static QMap<[Type](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script4TypeE "mv::util::Script::Type"), QString> typeMap
    :   Maps type to type name.

    static QMap<[Language](https://manivault.readthedocs.io/en/latest/api/core/util/script/script.html#_CPPv4N2mv4util6Script8LanguageE "mv::util::Script::Language"), QString> languageMap
    :   Maps language enum to language name.
