# HorizontalGroupAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/horizontal_group_action.html

**Documentation path:** `api/core/gui/actions/grouping/horizontal_group_action.html`

---

# HorizontalGroupAction

**Qualified name:** `mv::gui::HorizontalGroupAction`

class HorizontalGroupAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Horizontal group action class.

    Convenience group action for displaying child actions horizontally

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::ProjectCompressionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_compression_action.html#classmv_1_1ProjectCompressionAction), [mv::gui::ApplicationIconAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/application_icon_action.html#classmv_1_1gui_1_1ApplicationIconAction), [mv::gui::ColorSchemeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/color_scheme_action.html#classmv_1_1gui_1_1ColorSchemeAction), [mv::gui::IconPickerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/icon_picker_action.html#classmv_1_1gui_1_1IconPickerAction), [mv::gui::ModelFilterAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/model_filter_action.html#classmv_1_1gui_1_1ModelFilterAction), [mv::gui::ModelSelectionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/model_selection_action.html#classmv_1_1gui_1_1ModelSelectionAction), [mv::gui::OptionsAction::FileAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/option/options_action.html#classmv_1_1gui_1_1OptionsAction_1_1FileAction), [mv::gui::PaletteColorAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/palette_color_action.html#classmv_1_1gui_1_1PaletteColorAction), [mv::gui::PaletteColorRoleAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/palette_color_role_action.html#classmv_1_1gui_1_1PaletteColorRoleAction), [mv::gui::SplashScreenAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/splash_screen_action.html#classmv_1_1gui_1_1SplashScreenAction), [mv::gui::VersionAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/version_action.html#classmv_1_1gui_1_1VersionAction), [mv::gui::ViewPluginSamplerAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/view_plugin_sampler_action.html#classmv_1_1gui_1_1ViewPluginSamplerAction)

    Public Functions

    Q\_INVOKABLE HorizontalGroupAction(QObject \*parent, const QString &title, const bool &expanded = false)
    :   Construct with `parent` and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **expanded** – Whether the group is initially expanded/collapsed
