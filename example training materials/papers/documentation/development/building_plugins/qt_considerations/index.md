# Qt plugin considerations

**Source:** https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/index.html

**Documentation path:** `development/building_plugins/qt_considerations/index.html`

---

# Qt plugin considerations

ManiVault plugins are Qt components loaded into a long-running GUI application. Correct plugin code must account for both C++ object lifetime and Qt’s additional contracts: QObject parentage, thread affinity, queued delivery, meta-object generation, widget ownership, and event-loop-driven destruction.

This section incorporates the former **QObject Lifetime & Ownership Guidelines** and places those rules alongside the related threading, connection, build, UI, and teardown guidance.

- [QObject lifetime and ownership](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/qobject_ownership.html)
  - [Common patterns](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/qobject_ownership.html#common-patterns)
  - [QObject members in ManiVault](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/qobject_ownership.html#qobject-members-in-manivault)
  - [Association is not necessarily ownership](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/qobject_ownership.html#association-is-not-necessarily-ownership)
  - [Heap allocation](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/qobject_ownership.html#heap-allocation)
- [Connections and deferred callbacks](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/connections_and_callbacks.html)
  - [Always provide a context object](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/connections_and_callbacks.html#always-provide-a-context-object)
  - [Timers and delayed work](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/connections_and_callbacks.html#timers-and-delayed-work)
  - [QPointer and stable identities](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/connections_and_callbacks.html#qpointer-and-stable-identities)
  - [Queued delivery during teardown](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/connections_and_callbacks.html#queued-delivery-during-teardown)
- [Threads and the event loop](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/threads_and_event_loop.html)
  - [GUI objects stay on the GUI thread](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/threads_and_event_loop.html#gui-objects-stay-on-the-gui-thread)
  - [Connection types](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/threads_and_event_loop.html#connection-types)
  - [Moving QObjects](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/threads_and_event_loop.html#moving-qobjects)
  - [Event-loop assumptions](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/threads_and_event_loop.html#event-loop-assumptions)
- [Meta-object and build integration](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/meta_object_and_build.html)
  - [Q\_OBJECT](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/meta_object_and_build.html#q-object)
  - [AUTOMOC and target sources](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/meta_object_and_build.html#automoc-and-target-sources)
  - [Custom types in signals and QVariant](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/meta_object_and_build.html#custom-types-in-signals-and-qvariant)
- [Widgets, models, and presentation](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/widgets_models_and_presentation.html)
  - [Actions and widget representations](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/widgets_models_and_presentation.html#actions-and-widget-representations)
  - [Layout and widget ownership](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/widgets_models_and_presentation.html#layout-and-widget-ownership)
  - [Model/view updates](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/widgets_models_and_presentation.html#model-view-updates)
  - [Themes, icons, and high DPI](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/widgets_models_and_presentation.html#themes-icons-and-high-dpi)
  - [OpenGL widgets](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/widgets_models_and_presentation.html#opengl-widgets)
- [Teardown and testing](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/teardown_and_testing.html)
  - [Teardown sequence](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/teardown_and_testing.html#teardown-sequence)
  - [Plugin destruction](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/teardown_and_testing.html#plugin-destruction)
  - [deleteLater()](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/teardown_and_testing.html#deletelater)
  - [Avoid shutdown deadlocks](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/teardown_and_testing.html#avoid-shutdown-deadlocks)
  - [Verification checklist](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/teardown_and_testing.html#verification-checklist)
  - [Review questions](https://manivault.readthedocs.io/en/latest/development/building_plugins/qt_considerations/teardown_and_testing.html#review-questions)

Domain-specific pages still describe their own contracts. In particular, see [Action ownership](https://manivault.readthedocs.io/en/latest/development/building_plugins/actions/lifecycle.html), [Dataset removal](https://manivault.readthedocs.io/en/latest/development/building_plugins/data/events/removal_and_lifetime.html), [Plugin lifecycle](https://manivault.readthedocs.io/en/latest/development/building_plugins/fundamentals/lifecycle.html), and [Workflow threading](https://manivault.readthedocs.io/en/latest/development/workflows/threading_and_parallelism.html).
