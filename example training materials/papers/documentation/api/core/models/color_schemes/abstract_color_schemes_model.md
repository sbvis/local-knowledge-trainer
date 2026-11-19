# AbstractColorSchemesModel

**Source:** https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html

**Documentation path:** `api/core/models/color_schemes/abstract_color_schemes_model.html`

---

# AbstractColorSchemesModel

**Qualified name:** `mv::AbstractColorSchemesModel`

class AbstractColorSchemesModel : public mv::[StandardItemModel](https://manivault.readthedocs.io/en/latest/api/core/models/common/standard_item_model.html#_CPPv4N2mv17StandardItemModelE "mv::StandardItemModel")
:   Color schemes model class.

    Base standard item model for color schemes (application palette)

    **Author**
    :   Thomas Kroes

    Subclassed by [mv::ColorSchemesListModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/color_schemes_list_model.html#classmv_1_1ColorSchemesListModel)

    Public Types

    enum class Column
    :   Model columns.

        *Values:*

        enumerator Name

        enumerator Description
        :   Color scheme name.

        enumerator Palette
        :   Color scheme description.

        enumerator Mode
        :   Color palette.

        enumerator Count
        :   Whether it is a built-in color scheme, or user-added.

    Public Functions

    AbstractColorSchemesModel(QObject \*parent = nullptr)
    :   Construct with pointer to `parent` object.

        Parameters:
        :   **parent** – Pointer to parent object

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override
    :   Get header data for `section`, `orientation` and display `role`.

        Parameters:
        :   - **section** – Section
            - **orientation** – Orientation
            - **role** – Data role

        Returns:
        :   Header

    class DescriptionItem : public mv::[AbstractColorSchemesModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModelE "mv::AbstractColorSchemesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModel4ItemE "mv::AbstractColorSchemesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel_1_1Item) class for displaying the color scheme description version.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &colorScheme)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Item : public QStandardItem
    :   Base standard model item class for the color scheme item.

        Subclassed by [mv::AbstractColorSchemesModel::DescriptionItem](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel_1_1DescriptionItem), [mv::AbstractColorSchemesModel::ModeItem](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel_1_1ModeItem), [mv::AbstractColorSchemesModel::NameItem](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel_1_1NameItem), [mv::AbstractColorSchemesModel::PaletteItem](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel_1_1PaletteItem)

        Public Functions

        Item(util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &colorScheme)
        :   Construct with reference to the `colorScheme`.

            Parameters:
            :   **colorScheme** – Reference to the color scheme

        util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &getColorScheme()
        :   Get color scheme.

            Returns:
            :   Reference to the color scheme

        const util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &getColorScheme() const
        :   Get color scheme.

            Returns:
            :   Reference to the color scheme

    class ModeItem : public mv::[AbstractColorSchemesModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModelE "mv::AbstractColorSchemesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModel4ItemE "mv::AbstractColorSchemesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel_1_1Item) class for displaying the color scheme mode.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &colorScheme)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class NameItem : public mv::[AbstractColorSchemesModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModelE "mv::AbstractColorSchemesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModel4ItemE "mv::AbstractColorSchemesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel_1_1Item) class for displaying the color scheme name.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &colorScheme)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class PaletteItem : public mv::[AbstractColorSchemesModel](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModelE "mv::AbstractColorSchemesModel")::[Item](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#_CPPv4N2mv25AbstractColorSchemesModel4ItemE "mv::AbstractColorSchemesModel::Item")
    :   [Item](https://manivault.readthedocs.io/en/latest/api/core/models/color_schemes/abstract_color_schemes_model.html#classmv_1_1AbstractColorSchemesModel_1_1Item) class for displaying the color scheme palette.

        Public Functions

        QVariant data(int role = Qt::UserRole + 1) const override
        :   Get model data for `role`.

            Returns:
            :   Data for `role` in variant form

        Item(util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &colorScheme)
        :   No need for specialized constructor.

        Public Static Functions

        static inline QVariant headerData(Qt::Orientation orientation, int role)
        :   Get header data for `orientation` and `role`.

            Parameters:
            :   - **orientation** – Horizontal/vertical
                - **role** – Data role

            Returns:
            :   Header data

    class Row : public QList<QStandardItem\*>
    :   Convenience class for combining items in a row.

        Public Functions

        inline Row(util::[ColorScheme](https://manivault.readthedocs.io/en/latest/api/core/util/color/color_scheme.html#_CPPv4N2mv4util11ColorSchemeE "mv::util::ColorScheme") &colorScheme)
        :   Construct with reference to `colorScheme`.

            Parameters:
            :   **colorScheme** – Reference to colorScheme
