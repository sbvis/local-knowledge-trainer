# RecentFile

**Source:** https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html

**Documentation path:** `api/core/util/file/recent_file.html`

---

# RecentFile

**Qualified name:** `mv::util::RecentFile`

class RecentFile
:   Recent file class.

    Utility class for recent file (contains file path and date time).

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    RecentFile(const QString &filePath = "", const QDateTime &dateTime = QDateTime::currentDateTime())
    :   Construct with `filePath` and `dateTime`.

        Parameters:
        :   - **filePath** – File path of the recent file
            - **dateTime** – Date and time the recent file was last opened

    QString getFilePath() const
    :   Get file path.

        Returns:
        :   File path of the recent file

    QDateTime getDateTime() const
    :   Get date and time.

        Returns:
        :   Date and time the recent file was last opened

    inline bool operator==(const [RecentFile](https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html#_CPPv4N2mv4util10RecentFileE "mv::util::RecentFile") &other) const
    :   Compare equality with \other recent files.

        Parameters:
        :   **other** – Other recent file to compare with

        Returns:
        :   Boolean whether equal to the other recent file

    inline bool operator<(const [RecentFile](https://manivault.readthedocs.io/en/latest/api/core/util/file/recent_file.html#_CPPv4N2mv4util10RecentFileE "mv::util::RecentFile") &other) const
    :   Establish whether smaller than the `other` recent file.

        Parameters:
        :   **other** – Other recent file to compare with

        Returns:
        :   Boolean whether smaller than the other recent file
