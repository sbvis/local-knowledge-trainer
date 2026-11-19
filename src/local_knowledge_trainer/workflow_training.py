"""Conservative task-oriented SFT examples from explicit user documentation.

These examples are *extractive*, not synthetic guesses about undocumented UI
behaviour. Sections without identifiable interaction steps produce no examples.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit

from .workflow_search import _clean_line, _START_STEP, _CONTEXTUAL_STEP, document_headings

_HEADING = re.compile(r'^\s*#{2,5}\s+(.+?)\s*#*\s*$')
_GERUNDS = {'exploring': 'explore', 'identifying': 'identify',
            'comparing': 'compare', 'selecting': 'select',
            'adjusting': 'adjust', 'changing': 'change',
            'creating': 'create', 'loading': 'load',
            'finding': 'find', 'filtering': 'filter',
            'exporting': 'export', 'importing': 'import',
            'visualizing': 'visualize', 'analyzing': 'analyze',
            'sorting': 'sort', 'using': 'use', 'viewing': 'view',
            'select': 'select', 'identify': 'identify', 'compare': 'compare',
            'find': 'find', 'open': 'open', 'adjust': 'adjust',
            'change': 'change', 'create': 'create', 'export': 'export'}


def _question(heading: str, source: str, path: str) -> str:
    words = heading.split()
    if words:
        action = _GERUNDS.get(words[0].lower())
        if action:
            task = action + (' ' + ' '.join(words[1:]) if len(words) > 1 else '')
        else:
            task = 'use the ' + heading + ' feature'
    else:
        task = 'use this feature'
    # If a heading already names the application, reuse that name instead of
    # appending a duplicate derived from a tutorial filename.
    named_context = re.search(r'\b(?:in|for|within)\s+([A-Z][\w-]*(?:\s+[A-Z][\w-]*)*)$', heading)
    project = named_context.group(1) if named_context else Path(path).stem
    if not named_context:
        project = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', project)
    project = re.sub(r'[-_]+', ' ', project).strip()
    if not project or project.casefold() in {'readme', 'index', 'guide', 'tutorial'}:
        candidate = urlsplit(source).path.rstrip('/').rsplit('/', 1)[-1]
        project = candidate.removesuffix('.git').replace('-', ' ').replace('_', ' ') or 'the application'
    project = ' '.join(word if word.isupper() else word.capitalize() for word in project.split())
    suffix = '' if task.casefold().rstrip('?').endswith('in ' + project.casefold()) else f' in {project}'
    return f'How do I {task}{suffix}?'


def extract_workflow_examples(chunks, *, limit: int = 250) -> list[dict]:
    """Only numbered or imperative steps inside a named Markdown section.

    Source grouping preserves the line numbers and avoids a train/validation
    leak when a generated workflow and a documentation summary share a file.
    """
    files = defaultdict(list)
    for chunk in chunks:
        if chunk.kind != 'document' or Path(chunk.location).suffix.lower() not in {'.md', '.markdown', '.html', '.htm', ''}:
            continue
        files[(chunk.source, chunk.location)].append(chunk)
    results = []
    for (source, path), segments in sorted(files.items()):
        # Chunks overlap. Rebuild exact source line numbers before sectioning.
        numbered = {}
        for segment in segments:
            for offset, raw in enumerate(segment.text.splitlines()):
                numbered.setdefault(segment.start_line + offset, raw)
        sections = []
        current = None
        indexed_lines = sorted(numbered.items())
        headings = document_headings(indexed_lines)
        for index, (number, raw) in enumerate(indexed_lines):
            if index in headings:
                if current:
                    sections.append(current)
                current = (headings[index], number, [])
            elif current:
                current[2].append((number, raw))
        if current:
            sections.append(current)
        for heading, title_line, lines in sections:
            # A title alone is insufficient; extract actual numbered UI actions.
            steps = []
            for number, raw in lines:
                text = _clean_line(raw)
                if not 9 <= len(text) <= 320 or text.startswith(('//', '#include')):
                    continue
                if _START_STEP.match(text) or _CONTEXTUAL_STEP.match(text):
                    if re.search(r'\b(?:source code|implementation|compile|import os|git clone|pip install)\b', text, re.I):
                        continue
                    if text not in [t for _, t in steps]:
                        steps.append((number, text))
                if len(steps) >= 6:
                    break
            # Some published tutorials document a complete task with one
            # explicit action (e.g. 'Click Species Appearance to rank genes').
            # Requiring two steps silently discards those high-value examples.
            specific_heading = bool(re.search(
                r'\b(?:select|identify|find|explor|zoom|rank|sort|filter|export|'
                r'import|change|adjust|view|color|compar|open|load|toggl)\w*\b',
                heading, re.I))
            if not steps or (len(steps) == 1 and not specific_heading):
                continue
            # Reject generic headings and huge script dumps as task examples.
            if len(heading) < 6 or len(heading) > 100 or re.search(r'\b(?:installation|dependencies|build system|development)\b', heading, re.I):
                continue
            place = f'{path}:L{steps[0][0]}-L{steps[-1][0]}'
            answer = ('Follow these documented steps:\n' +
                      '\n'.join(f'{i}. {step}' for i, (_, step) in enumerate(steps, 1)) +
                      f'\nSource: {source} :: {place}')
            questions = [_question(heading, source, path)]
            for question in questions:
                results.append({
                    'messages': [
                        {'role': 'user', 'content': question},
                        {'role': 'assistant', 'content': answer},
                    ],
                    '_source': f'{source}::{path}', '_split_group': f'{source}::{path}',
                    '_location': place, '_evidence_type': 'documented_workflow',
                })
    # Preserve coverage across sources and avoid a huge tutorial monopolizing SFT.
    from collections import deque
    grouped = defaultdict(list)
    for row in results:
        grouped[row['_source'].split('::', 1)[0]].append(row)
    pending = deque(iter(grouped[source]) for source in sorted(grouped))
    ordered = []
    while pending and len(ordered) < limit:
        it = pending.popleft()
        item = next(it, None)
        if item is not None:
            ordered.append(item)
            pending.append(it)
    return ordered
