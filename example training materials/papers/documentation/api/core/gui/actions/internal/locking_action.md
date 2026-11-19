# LockingAction

**Source:** https://manivault.readthedocs.io/en/latest/api/core/gui/actions/internal/locking_action.html

**Documentation path:** `api/core/gui/actions/internal/locking_action.html`

---

# LockingAction

**Qualified name:** `mv::gui::LockingAction`

class LockingAction : public mv::gui::[GroupAction](https://manivault.readthedocs.io/en/latest/api/core/gui/actions/grouping/group_action.html#_CPPv4N2mv3gui11GroupActionE "mv::gui::GroupAction")
:   Locked action class.

    Action class for locking status (internal use only).

    Note: This action is developed for internal use only

    **Author**
    :   Thomas Kroes

    Public Functions

    Q\_INVOKABLE LockingAction(QObject \*parent, const QString &what = "", bool locked = false)
    :   Constructor.

        Parameters:
        :   - **parent** – Pointer to parent object
            - **what** – What is to be locked
            - **locked** – Locked

    void initialize(bool locked = false)
    :   Initialize the setEnabled action.

        Parameters:
        :   **locked** – Locked

    QString getWhat() const
    :   Get what.

        Returns:
        :   What is locked

    void setWhat(QString what)
    :   Set what to `whatB`.

        Parameters:
        :   **what** – What is locked

    bool isLocked() const
    :   Get locked status.

        Returns:
        :   Boolean determining the locked status

    void setLocked(bool locked)
    :   Set locked status to `locked`.

        Parameters:
        :   **locked** – Boolean determining the locked status

    virtual void fromVariantMap(const QVariantMap &variantMap) override
    :   Load locked action from variant map.

        Parameters:
        :   **Variant** – map representation of the locked action

    virtual QVariantMap toVariantMap() const override
    :   Save locked action to variant map.

        Returns:
        :   Variant map representation of the locked action

    void lockedChanged(bool locked)
    :   Signals that the locked status changed.

        Parameters:
        :   **locked** – Locked status
