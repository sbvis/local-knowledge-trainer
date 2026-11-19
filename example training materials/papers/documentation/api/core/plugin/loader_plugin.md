# LoaderPlugin

**Source:** https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin.html

**Documentation path:** `api/core/plugin/loader_plugin.html`

---

# LoaderPlugin

**Qualified name:** `mv::plugin::LoaderPlugin`

A loader plugin imports an external source into ManiVault. Implement `loadData()` as the loader’s entry point; `AskForFileName()` is available when the loader uses an interactive file choice and remembers the last directory for that plugin kind.

Pair a loader instance with a [LoaderPluginFactory](https://manivault.readthedocs.io/en/latest/api/core/plugin/loader_plugin_factory.html). A loader that cannot parse or read a chosen file may report a [DataLoadException](https://manivault.readthedocs.io/en/latest/api/core/plugin/data_load_exception.html) through the appropriate user-facing failure boundary.

class LoaderPlugin : public mv::plugin::[Plugin](https://manivault.readthedocs.io/en/latest/api/core/plugin/plugin.html#_CPPv4N2mv6plugin6PluginE "mv::plugin::Plugin")
:   Public Functions

    virtual void loadData() = 0
    :   Should be implemented by loader plugins to parse their specific data.

        This function will be called when the user clicks on the menu item for this loader. The implementation is free to create file dialogs if desired.

    Protected Functions

    QString AskForFileName(const QString &fileNameFilter) const
    :   Asks the user for the name of a file to load data from.

        Opens a file dialog at the directory of the last loaded file. The path of this directory is stored with the application settings (in the registry, on Windows). `fileNameFilter` could be something like “Text Files (\*.txt)”.
