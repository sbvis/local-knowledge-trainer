"""Conservative, dependency-free multi-repository source analysis.

Extracts *observable* source facts (definitions, includes, Qt labels, and signal/
slot wiring). Resolves cross-repository links only when a referenced header or
qualified symbol has a unique definition. This is not a compiler/AST and does
not claim to infer runtime UI layout from source fragments.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import re
from pathlib import PurePosixPath
from urllib.parse import urlsplit

from .prepare import Chunk, location_for

CPP_EXTS = ('.c', '.cc', '.cpp', '.cxx', '.h', '.hh', '.hpp', '.hxx')
UI_TERMS = ('action', 'widget', 'button', 'slider', 'menu', 'toolbar', 'layout',
            'dialog', 'checkbox', 'spinbox', 'combobox', 'dock', 'tab')
QT_PROPERTIES = {'setText': 'label', 'setTitle': 'title',
                 'setToolTip': 'tooltip', 'setStatusTip': 'tooltip',
                 'setWhatsThis': 'help_text', 'setPlaceholderText': 'placeholder'}
_DEFINITION = re.compile(r'\b(?:class|struct)\s+([A-Za-z_]\w*)\b')
_FUNCTION = re.compile(r'\b([A-Za-z_]\w*(?:::[A-Za-z_~]\w*)+)\s*\([^;{}]{0,160}\)\s*(?:const\s*)?(?:\{|$)')
_INCLUDE = re.compile(r'^\s*#\s*include\s*[<"]([^>"]+)[>"]')
_QT_PROPERTY = re.compile(r'\b([A-Za-z_]\w*)\s*(?:->|\.)\s*(setText|setTitle|setToolTip|setStatusTip|setWhatsThis|setPlaceholderText)\s*\(\s*(?:QStringLiteral\s*\()?\s*"((?:[^"\\]|\\.){1,160})"')
_QT_INIT = re.compile(r'\b(_?[A-Za-z_]\w*(?:Action|Widget|Button|Slider|Group|Settings))\s*\(\s*(?:this|parent)\s*,\s*(?:QStringLiteral\s*\()?\s*"((?:[^"\\]|\\.){1,130})"')
_QT_CTOR = re.compile(r'\b([A-Za-z_]\w*)\s*=\s*new\s+(Q[A-Za-z_]\w*(?:Action|Widget|Button|Slider|Menu|Dialog|Box))\s*\(\s*(?:QStringLiteral\s*\()?\s*"((?:[^"\\]|\\.){1,130})"')
_QT_REGISTER = re.compile(r'\b([A-Za-z_]\w*)\s*(?:->|\.)\s*(addWidget|addAction|addMenu|addTab|addSubAction|setCentralWidget)\s*\(\s*([&*]?[A-Za-z_]\w*)')
_SIGNAL_SLOT = re.compile(r'\bconnect\s*\(\s*([\w.>\-]+)\s*,\s*&[\w:]+\s*,\s*(?:[\w.>\-]+\s*,\s*)?&([A-Za-z_]\w*(?:::[A-Za-z_]\w*)+)')
_TOKEN = re.compile(r'\b[A-Za-z_][A-Za-z_0-9]*\b')
_IGNORE_SYMBOLS = {'Plugin', 'Action', 'Widget', 'View', 'Data', 'Points', 'QString',
                   'QObject', 'QWidget', 'QAction', 'QMenu', 'QDialog', 'QObjectList'}


@dataclass(frozen=True)
class Fact:
    source: str
    location: str
    subject: str
    predicate: str
    object: str
    evidence: str
    target_source: str = ''
    target_location: str = ''
    confidence: str = 'observed'  # observed or resolved_unique


def _file(chunk: Chunk) -> str:
    return chunk.location.replace('\\', '/')


def _location(chunk: Chunk, line_offset: int) -> str:
    # Chunk location can be a many-line excerpt; give precise original line.
    line = chunk.start_line + line_offset
    return f'{_file(chunk)}:L{line}-L{line}'


def _fact(chunk, offset, subject, predicate, value, evidence) -> Fact:
    return Fact(chunk.source, _location(chunk, offset), subject, predicate,
                value.strip(), evidence.strip()[:600])


def analyze_chunks(chunks: list[Chunk], *, max_facts: int = 25000) -> list[Fact]:
    """Analyze lines, then link unique cross-file references across all repositories.

    Restrained parsing is deliberate: an observed include/signal/property is
    evidence, but it is not proof of final runtime behavior or screen location.
    """
    observed: list[Fact] = []
    definitions: dict[str, list[Fact]] = defaultdict(list)
    references: list[Fact] = []
    files: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for chunk in chunks:
        if chunk.kind != 'code' or not _file(chunk).lower().endswith(CPP_EXTS):
            continue
        files[PurePosixPath(_file(chunk)).name.lower()].add((chunk.source, _file(chunk)))
        lines = chunk.text.splitlines()
        for offset, line in enumerate(lines):
            if len(observed) >= max_facts:
                break
            stripped = line.strip()
            if len(stripped) > 500 or stripped.startswith(('//', '*', '/*')):
                continue
            inc = _INCLUDE.match(line)
            if inc:
                references.append(_fact(chunk, offset, inc.group(1), 'includes',
                                        inc.group(1), stripped))
            for match in _DEFINITION.finditer(line):
                definition = _fact(chunk, offset, match.group(1), 'defines_class',
                                   match.group(1), stripped)
                observed.append(definition)
                definitions[match.group(1)].append(definition)
            fun = _FUNCTION.search(line)
            if fun:
                definition = _fact(chunk, offset, fun.group(1), 'defines_function',
                                   fun.group(1), stripped)
                observed.append(definition)
                definitions[fun.group(1)].append(definition)
            for match in _QT_PROPERTY.finditer(line):
                observed.append(_fact(chunk, offset, match.group(1), QT_PROPERTIES[match.group(2)],
                                      match.group(3), stripped))
            for match in _QT_INIT.finditer(line):
                observed.append(_fact(chunk, offset, match.group(1), 'label',
                                      match.group(2), stripped))
            for match in _QT_CTOR.finditer(line):
                observed.append(_fact(chunk, offset, match.group(1), 'ui_constructs',
                                      match.group(2), stripped))
                observed.append(_fact(chunk, offset, match.group(1), 'label',
                                      match.group(3), stripped))
            reg = _QT_REGISTER.search(line)
            if reg:
                observed.append(_fact(chunk, offset, reg.group(3).lstrip('*&'),
                                      'registered_with', f'{reg.group(1)}.{reg.group(2)}', stripped))
            connected = _SIGNAL_SLOT.search(line)
            if connected:
                observed.append(_fact(chunk, offset, connected.group(1).lstrip('*&_'),
                                      'connected_to', connected.group(2), stripped))
            # Capture multi-line typed signal -> handler relationship. Never infer
            # a click-path or hidden UI position from a callback alone.
            if re.search(r'\bconnect\s*\(', line):
                statement = ' '.join(lines[offset:offset + 8])[:1200]
                action_match = re.search(r'connect\s*\(\s*&?(_?[A-Za-z_]\w*Action)\s*,\s*&[A-Za-z_:]+::([A-Za-z_]\w*)', statement)
                if action_match:
                    action, signal = action_match.groups()
                    observed.append(_fact(chunk, offset, action, 'signal', signal, statement))
                    setter = re.search(r'\b([A-Za-z_]\w*)\s*(?:->|\.)\s*(set[A-Z][A-Za-z_0-9]*)\s*\(', statement)
                    if setter:
                        observed.append(_fact(chunk, offset, action, 'callback_invokes',
                                              setter.group(1) + '.' + setter.group(2), statement))
        if len(observed) >= max_facts:
            break

    # Extract classes referenced from another repository only when an exact class
    # name has a single defining file across the whole corpus (avoid common words).
    unique_definitions = {}
    for name, found in definitions.items():
        if name in _IGNORE_SYMBOLS or len(name) < 5:
            continue
        keys = {(f.source, f.location.split(':L')[0]) for f in found}
        if len(keys) == 1:
            unique_definitions[name] = found[0]

    links: list[Fact] = []
    edge_keys: set[tuple[str, str, str, str]] = set()
    # Include paths are a strong source-level relationship when the basename
    # uniquely identifies a file. Ambiguity is intentionally not resolved.
    for inc in references:
        basename = PurePosixPath(inc.object).name.lower()
        targets = files.get(basename, set())
        target = next(iter(targets)) if len(targets) == 1 else None
        if target is None or target[0] == inc.source:
            continue
        edge = (inc.source, inc.location, 'imports_file', target[0] + '/' + target[1])
        if edge in edge_keys:
            continue
        edge_keys.add(edge)
        links.append(Fact(inc.source, inc.location, inc.subject, 'imports_file',
                          inc.object, inc.evidence, target[0], f'{target[1]}:L1-L1',
                          'resolved_unique'))

    # Cross-repository mentions are a weaker relationship. Evidence means only
    # that the symbol is referenced, not that a function calls another function.
    for chunk in chunks:
        if chunk.kind != 'code' or not _file(chunk).lower().endswith(CPP_EXTS):
            continue
        for offset, line in enumerate(chunk.text.splitlines()):
            if len(links) >= max_facts // 2:
                break
            if line.strip().startswith(('//', '*', '/*')):
                continue
            candidates = set(_TOKEN.findall(line)) & unique_definitions.keys()
            for name in sorted(candidates)[:4]:
                target = unique_definitions[name]
                if target.source == chunk.source:
                    continue
                loc = _location(chunk, offset)
                key = (chunk.source, loc, 'references_class', name)
                if key in edge_keys:
                    continue
                edge_keys.add(key)
                links.append(Fact(chunk.source, loc, name, 'references_class', name,
                                  line.strip()[:450], target.source, target.location,
                                  'resolved_unique'))

    result = []
    seen = set()
    for fact in observed + links:
        key = (fact.source, fact.location, fact.subject, fact.predicate, fact.object,
               fact.target_source, fact.target_location)
        if key not in seen:
            seen.add(key)
            result.append(fact)
    return result[:max_facts]


def ui_controls(facts: list[Fact]) -> list[dict]:
    """Combine labels, tooltips, registrations and signals for the same object.

    Only join facts scoped to the *same source and source file*. No speculation
    about screen placement; registration records the actual receiving object.
    """
    by_object: dict[tuple[str, str, str], list[Fact]] = defaultdict(list)
    for fact in facts:
        if fact.predicate not in {'label', 'title', 'tooltip', 'help_text', 'placeholder',
                                  'ui_constructs', 'registered_with', 'connected_to', 'signal', 'callback_invokes'}:
            continue
        if not fact.subject or fact.subject in {'this', 'self'}:
            continue
        by_object[(fact.source, fact.location.split(':L')[0], fact.subject)].append(fact)
    controls = []
    for (source, file, obj), related in sorted(by_object.items()):
        labels = [f for f in related if f.predicate in {'label', 'title', 'tooltip', 'help_text'}]
        if not labels:
            continue
        registration = [f for f in related if f.predicate == 'registered_with']
        wiring = [f for f in related if f.predicate in {'connected_to', 'callback_invokes', 'signal'}]
        controls.append({'source': source, 'file': file, 'object': obj,
                         'label': next((f.object for f in labels if f.predicate in {'label', 'title'}), labels[0].object),
                         'hints': [f.object for f in labels if f.predicate in {'tooltip', 'help_text'}][:3],
                         'registrations': [(f.object, f.location) for f in registration][:4],
                         'connections': [(f.object, f.location) for f in wiring][:4],
                         'evidence': [(f.predicate, f.location, f.evidence) for f in related][:10]})
    return controls


def graph_summary(facts: list[Fact]) -> dict:
    """Stable, auditable organization summary for repositories and UI features."""
    counts: dict[str, int] = defaultdict(int)
    profiles: dict[str, dict] = {}
    edges: dict[tuple[str, str], dict] = {}
    for fact in facts:
        counts[fact.predicate] += 1
        profile = profiles.setdefault(fact.source, {
            'facts': 0, 'observed_ui_properties': 0, 'cross_repo_outgoing': 0,
        })
        profile['facts'] += 1
        if fact.predicate in {'label', 'title', 'tooltip', 'help_text', 'signal', 'callback_invokes'}:
            profile['observed_ui_properties'] += 1
        if fact.target_source and fact.target_source != fact.source:
            profile['cross_repo_outgoing'] += 1
            key = (fact.source, fact.target_source)
            edge = edges.setdefault(key, {'from': fact.source, 'to': fact.target_source,
                                          'observed_links': 0, 'types': set(),
                                          'example_evidence': f'{fact.location}: {fact.evidence[:180]}'})
            edge['observed_links'] += 1
            edge['types'].add(fact.predicate)
    # A compact, navigable map; bounded to keep manifests portable.
    links = [{**edge, 'types': sorted(edge['types'])}
             for _, edge in sorted(edges.items())][:250]
    return {'facts': len(facts), 'by_type': dict(sorted(counts.items())),
            'cross_repository_pairs': len(edges),
            'repository_profiles': dict(sorted(profiles.items())),
            'cross_repository_links': links,
            'ui_controls_with_labels': len(ui_controls(facts)),
            'method': 'conservative static source-pattern analysis, not compiler-verified behavior'}
