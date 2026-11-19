"""Evidence-based end-user help from a local SQLite knowledge index.

This deliberately does not use free-form LLM generation for UI procedures. Small
models can confidently invent menus and C++ edits; controls and exact guide lines
are much more dependable. It works with existing knowledge.db releases.
"""
from __future__ import annotations

import re
import sqlite3
from collections import defaultdict
from contextlib import closing
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

from .index import _fact_table_exists, _named_repositories, search_ui_guides
from .ui_semantics import resolve_action_type, interaction_for
from .workflow_search import search_workflows

_STOP = {"how", "can", "do", "i", "to", "the", "a", "an", "in", "on", "of", "for", "my",
         "with", "change", "adjust", "increase", "decrease", "set", "find", "where",
         "click", "use", "open", "show", "hide", "navigate", "control", "settings",
         "setting", "app", "application", "plugin", "software", "interface", "ui",
         "using", "please", "want", "would", "like", "me"}
_ACTION = re.compile(r"\b(?:open|click|select|choose|adjust|drag|move|increase|decrease|"
                     r"toggle|check|uncheck|press|enter|set|use|find|locate|switch|"
                     r"expand|collapse|scroll|enable|disable)\b", re.I)
_CODE_LINE = re.compile(r"^\s*(?:#include|import\s|connect\s*\(|(?:void|auto|class|struct)\s|"
                        r"\w+(?:::|->)\w+\s*\(|\{\s*$|\}\s*;?\s*$)")


@dataclass(frozen=True)
class UserHelp:
    answer: str
    references: tuple[dict, ...]
    level: str  # 'documented', 'control', or 'insufficient'


def _terms(text: str) -> list[str]:
    """Map common end-user phrases to the actual concepts named in Qt actions."""
    lower = text.casefold()
    words = re.findall(r"[A-Za-z][A-Za-z0-9]*", lower)
    # Treat natural phrases as an alias for a control, not a hard-coded answer.
    # Only use these aliases when the words unambiguously indicate point size.
    point_words = {'point', 'points', 'dot', 'dots', 'marker', 'markers'}
    size_words = {'size', 'sizes', 'bigger', 'larger', 'smaller', 'small',
                  'enlarge', 'enlarging', 'shrink', 'resize', 'resizing'}
    if point_words.intersection(words) and size_words.intersection(words):
        return ['point', 'size']
    if 'transparency' in words or 'transparent' in words:
        return ['opacity']
    return list(dict.fromkeys(
        (w[:-1] if w.endswith('s') and len(w) > 4 else w)
        for w in words if len(w) >= 3 and w not in _STOP
    ))


def _repo_title(source: str) -> str:
    parts = urlsplit(source)
    if parts.hostname == 'github.com':
        return parts.path.rstrip('/').split('/')[-1] or source
    return Path(source).name or source


def _quote_locations(hits: list[dict]) -> str:
    return '\n'.join(f"[{i}] {h['source']} :: {h['location']}" for i, h in enumerate(hits, 1))


def _guide_steps(hit: dict, terms: list[str]) -> list[str]:
    lines = hit['content'].splitlines()
    snippets: list[str] = []
    in_fence = False
    for line in lines:
        if line.strip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        cleaned = re.sub(r'^\s*(?:[-*]\s+|\d+[.)]\s+)', '', line).strip()
        if not cleaned or len(cleaned) > 320 or _CODE_LINE.search(cleaned):
            continue
        if not _ACTION.search(cleaned):
            continue
        lower = cleaned.casefold()
        if terms and sum(w in lower for w in terms) < min(2, len(terms)):
            continue
        snippets.append(cleaned)
        if len(snippets) == 3:
            break
    return snippets


def _controls(db_path: Path, question: str, terms: list[str]) -> list[dict]:
    with closing(sqlite3.connect(db_path)) as db:
        db.row_factory = sqlite3.Row
        if not _fact_table_exists(db):
            return []
        scope_sources = _named_repositories(db, question)
        rows = db.execute('''SELECT source, location, subject, predicate, object
                             FROM facts WHERE predicate IN
                             ('label','title','tooltip','help_text',
                              'registered_with','connected_to','callback_invokes','signal')''').fetchall()
    groups: dict[tuple, list] = defaultdict(list)
    for row in rows:
        r = dict(row)
        if scope_sources and r['source'] not in scope_sources:
            continue
        groups[(r['source'], r['location'].split(':L', 1)[0], r['subject'])].append(r)
    candidates = []
    for (source, file, subject), related in groups.items():
        labels = [r for r in related if r['predicate'] in ('label', 'title')]
        for label in labels:
            value = label['object'].strip()
            if len(value) < 3 or len(value) > 100:
                continue
            label_terms = set(_terms(value))
            # A control must match *every* topic term in a compact query like
            # 'point size', not just the word 'point' in a random repository.
            matched = sum(t in label_terms for t in terms)
            if not matched or (len(terms) <= 3 and matched < min(len(terms), 2)):
                continue
            score = matched * 8 + (8 if ' '.join(terms) in value.casefold() else 0)
            score += 5 if any('setPointSize' in r['object'] for r in related) else 0
            if scope_sources:
                score += 10
            evidence = [label] + [r for r in related if r is not label]
            # Walk only explicit addSubAction/addWidget/addAction edges, and
            # only if the parent has a real label. Never invent a menu path.
            hierarchy = []
            current = (source, file, subject)
            visited = {current}
            for _ in range(3):
                links = groups.get(current, ())
                registration = next((r for r in links if r['predicate'] == 'registered_with'
                                     and re.fullmatch(r'[A-Za-z_]\w*\.(?:addSubAction|addAction|addWidget|addMenu|addTab)',
                                                      r['object'])), None)
                if not registration:
                    break
                parent = registration['object'].split('.', 1)[0]
                key = (source, file, parent)
                if key in visited:
                    break
                visited.add(key)
                parent_label = next((r['object'] for r in groups.get(key, ())
                                     if r['predicate'] in ('label','title')), None)
                if not parent_label:
                    break
                hierarchy.insert(0, parent_label)
                current = key
            candidates.append((score, {
                'source': source, 'file': file, 'subject': subject, 'label': value,
                'evidence': evidence, 'location': label['location'], 'hierarchy': hierarchy,
            }))
    candidates.sort(key=lambda v: (-v[0], v[1]['source'], v[1]['file']))
    # Prefer a single best label; identical labels may appear in several views.
    if not candidates:
        return []
    best = candidates[0][0]
    selected = [v for score, v in candidates if score >= best - 5][:3]
    for item in selected:
        item['action_type'], item['type_location'] = resolve_action_type(
            db_path, item['source'], item['subject'])
    return selected


def answer_ui_question(db_path: Path | str, question: str) -> UserHelp:
    """Produce end-user instructions only to the extent the indexed sources allow.

    Documentation takes precedence. With code-only evidence, describe the
    existing control but *never* infer a menu path or output code instructions.
    If nothing relevant is found, say so explicitly instead of hallucinating.
    """
    db_path = Path(db_path)
    terms = _terms(question)
    # Reconstruct neighboring tutorial chunks before extracting instructions.
    # Project names are context filters, not mandatory words in every step.
    workflows = search_workflows(db_path, question, limit=3)
    if workflows:
        best = workflows[0]
        references = ({'source': best.source, 'location': best.location},)
        if best.steps:
            details = ('\n'.join(best.details[:1]) + '\n\n') if best.details else ''
            answer = (f"According to **{best.title}** in the "
                      f"**{_repo_title(best.source)}** documentation:\n\n"
                      + details + '\n'.join(f'{n}. {step}' for n, step in enumerate(best.steps, 1))
                      + '\n\nSource: ' + _quote_locations(list(references)))
            return UserHelp(answer, references, 'documented')
        if best.details:
            answer = (f"The **{_repo_title(best.source)}** documentation discusses "
                      f"this topic under **{best.title}**:\n\n" +
                      ' '.join(best.details[:2]) +
                      '\n\nIt does not give enough verified interaction steps here to identify a full click path.'
                      '\n\nSource: ' + _quote_locations(list(references)))
            return UserHelp(answer, references, 'documented')
    docs = search_ui_guides(db_path, question, limit=8)
    for doc in docs:
        steps = _guide_steps(doc, terms)
        if steps:
            refs = ({'source': doc['source'], 'location': doc['location']},)
            answer = (f"According to the **{_repo_title(doc['source'])}** documentation:\n" + '\n'.join(
                f'{i}. {step}' for i, step in enumerate(steps, 1)
            )) + '\n\nSource: ' + _quote_locations(list(refs))
            return UserHelp(answer, refs, 'documented')
    controls = _controls(db_path, question, terms)
    if controls:
        refs = []
        descriptions = []
        for control in controls:
            hint = next((r['object'] for r in control['evidence']
                         if r['predicate'] in ('tooltip', 'help_text')), '')
            refs.append({'source': control['source'], 'location': control['location']})
            app = _repo_title(control['source'])
            parent = (' → '.join('**' + p + '**' for p in control['hierarchy']) + ' → ') if control['hierarchy'] else ''
            text = f"In **{app}**, look for {parent}**{control['label']}**. "
            if control['action_type']:
                text += interaction_for(control['action_type'], question, control['label'])
                if control['type_location']:
                    refs.append({'source': control['source'], 'location': control['type_location']})
            if hint:
                text += f'The control description says: “{hint}”. '
            descriptions.append(text.strip())
        answer = '\n'.join(descriptions)
        answer += ('\n\nThe names and grouping above come from source code. '
                   'The exact panel or toolbar can depend on the application version and workspace, '
                   'so I cannot verify a more specific click path without corresponding '
                   'user documentation or a runtime view.')
        answer += '\n\nSources:\n' + _quote_locations(refs)
        return UserHelp(answer, tuple(refs), 'control')
    return UserHelp(
        'I cannot verify how to perform that operation in the application UI from '
        'the indexed material. I will not suggest editing source files or invent '
        'a menu path. The available documents may not describe this user workflow.',
        (), 'insufficient'
    )
