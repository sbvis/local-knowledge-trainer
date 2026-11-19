# MultiSelectComboBox

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/widgets/internal/multi_select_combobox.html

**Documentation path:** `api/core/gui/widgets/internal/multi_select_combobox.html`

---

# MultiSelectComboBox

**Qualified name:** `mv::gui::MultiSelectComboBox`

class MultiSelectComboBox : public QComboBox
:   Multi-select combobox widget class.

    Allows to select multiple items during a single popup sessions.

    **Author**
    :   Thomas Kroes

    Public Functions

    explicit MultiSelectComboBox(QWidget \*parent = nullptr)
    :   Construct with pointer to `parent` widget.

        Parameters:
        :   **parent** – Pointer to parent widget

    void init()
    :   Call this post QComboBox::setView() to setup connections.

    Protected Functions

    void hidePopup() override
    :   Override to customize popup hide behaviour.

    bool eventFilter(QObject \*watched, QEvent \*event) override
    :   Called when `event` happens for `watched` object.

        Parameters:
        :   - **watched** – Pointer to watched object
            - **event** – Pointer to event that occurred

        Returns:
        :   Whether the event was handled or not
