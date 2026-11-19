# VerticalGroupAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/vertical_group_action.html

**Documentation path:** `api/core/gui/actions/grouping/vertical_group_action.html`

---

# VerticalGroupAction

**Qualified name:** `mv::gui::VerticalGroupAction`

class VerticalGroupAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Vertical group action class.

    Convenience group action for displaying child actions vertically

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::ProjectMetaAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/project/project_meta_action.html#classmv_1_1ProjectMetaAction), [mv::gui::BrandingConfigurationAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/branding_configuration_action.html#classmv_1_1gui_1_1BrandingConfigurationAction), [mv::gui::CodecSettingsAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/codec_settings_action.html#classmv_1_1gui_1_1CodecSettingsAction), [mv::gui::EditColorSchemeAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/edit_color_scheme_action.html#classmv_1_1gui_1_1EditColorSchemeAction), [mv::gui::EventAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/event_action.html#classmv_1_1gui_1_1EventAction), [mv::gui::HorizontalHeaderAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/horizontal_header_action.html#classmv_1_1gui_1_1HorizontalHeaderAction), [mv::gui::PaletteAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/palette_action.html#classmv_1_1gui_1_1PaletteAction), [mv::gui::ProjectsConfigurationAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/projects_configuration_action.html#classmv_1_1gui_1_1ProjectsConfigurationAction), [mv::gui::StartPageConfigurationAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/start_page_configuration_action.html#classmv_1_1gui_1_1StartPageConfigurationAction), [mv::gui::TableAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/miscellaneous/table_action.html#classmv_1_1gui_1_1TableAction), [mv::gui::ZoomMarginAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/zoom_margin_action.html#classmv_1_1gui_1_1ZoomMarginAction)

    Public Functions

    Q\_INVOKABLE VerticalGroupAction(QObject \*parent, const QString &title, const bool &expanded = false)
    :   Construct with `parent` and `title`.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **title** – Title of the action
            - **expanded** – Whether the group is initially expanded/collapsed
