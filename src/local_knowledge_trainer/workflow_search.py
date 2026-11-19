"""Retrieve user tasks from complete, adjacent documentation passages.

No generation or extrapolation: a cited step must appear in the source. The
existing index uses overlapping 36-line chunks, so a tutorial section often
spans two or more indexed rows. Reconstruct nearby lines before scoring.
"""
from __future__ import annotations

import html
import math
import re
import sqlite3
from collections import defaultdict
from contextlib import closing
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit


@dataclass(frozen=True)
class Workflow:
    source: str
    location: str
    title: str
    details: tuple[str, ...]
    steps: tuple[str, ...]
    score: int


_GENERIC = {
    'how', 'can', 'may', 'could', 'do', 'does', 'is', 'to', 'the', 'my', 'in', 'on',
    'for', 'from', 'with', 'of', 'a', 'an', 'and', 'or', 'where', 'which', 'why',
    'please', 'me', 'i', 'we', 'you', 'your', 'using', 'use', 'find', 'locate', 'get',
    'see', 'show', 'view', 'open', 'change', 'adjust', 'increase', 'decrease',
    'identify', 'create', 'make', 'calculate', 'compare', 'display', 'inspect',
    'select', 'choose', 'navigate', 'add', 'remove', 'run', 'detect', 'enable',
    'software', 'application', 'app', 'gui', 'ui', 'interface', 'plugin', 'system',
    'studio', 'project', 'tutorial', 'steps', 'step', 'howto', 'window',
    'what', 'should', 'that', 'this', 'these', 'those',
    'together', 'selected', 'across', 'versus', 'every', 'exact', 'menu', 'path',
    'click', 'press', 'hold', 'save', 'csv', 'investigate', 'distinguish',
    'pattern', 'branch',
    'button', 'after', 'while', 'more', 'than', 'return', 'its', 'compute',
    'existing', 'by', 'into', 'it',
}
_NEGATION = re.compile(r'\b(?:not|never|unrelated|different\s+plugin|does\s+not|isn.t|cannot|can.t)\b', re.I)
_GUIDE_PATH = re.compile(r'(?:documentation|tutorial|guide|manual|help|walkthrough|how.to|usage|readme)', re.I)
_START_STEP = re.compile(
    r'^(?:(?:step\s*\d+\s*[:.\-]?\s*)|(?:then|next|finally|afterwards|first|now)\s*[:,]?\s*)?'
    r'(?:click|select|choose|open|drag|drop|move|adjust|increase|decrease|'
    r'enter|type|press|hold|check|uncheck|toggle|expand|collapse|load|import|export|'
    r'save|filter|highlight|switch|navigate|right.click|double.click|'
    r'go\s+to|set\s+the|use|examine|hover|sort|edit|read|restore|clear|look\s+for)\b', re.I)
_INSIDE_ACTION = re.compile(
    r'\b(?:click|select|choose|open|drag|adjust|press|check|toggle|expand|'
    r'load|import|filter|navigate|go\s+to|set\s+the|use\s+the)\b', re.I)
# Instructions often begin with a location, e.g. 'In the gene table, click X'.
# Accept the imperative only when its prefix is a short interface locator.
_CONTEXTUAL_STEP = re.compile(
    r'^(?:(?:in|on|from|within|under|at)\s+.{3,100}?,\s*|[\w][\w &/-]{1,60}:\s*)'
    r'(?:click|select|choose|open|drag|adjust|press|check|toggle|'
    r'expand|load|import|filter|sort|edit|use|hold|scroll|set)\b', re.I)


def _stem(token: str) -> str:
    """Light inflection support, not a semantic assertion."""
    if token == 'species':
        return token
    if token.endswith('ing') and len(token) > 5:
        root = token[:-3]
        return root[:-1] if len(root) > 2 and root[-1] == root[-2] else root
    if token.endswith('ies') and len(token) > 5:
        return token[:-3] + 'y'
    if token.endswith('s') and len(token) > 4 and not token.endswith('ss'):
        return token[:-1]
    return token


def query_topics(question: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    question = re.sub(r'\bseveral\b', 'multiple', question, flags=re.I)
    question = re.sub(r'\b(add|select|choose)\s+more\b', r'\1 multiple', question, flags=re.I)
    raw_words = re.findall(r'[A-Za-z][A-Za-z0-9]*', question)
    words = [word.casefold() for word in raw_words]
    # Recognize explicitly named products without maintaining a registry of
    # particular applications. CamelCase names, acronyms and title-cased names
    # can scope results to matching source paths; ordinary topic words remain
    # searchable across the full index.
    apps = tuple(dict.fromkeys(
        word for raw, word in zip(raw_words, words)
        if word not in _GENERIC and
        (re.search(r'[a-z][A-Z]|[A-Z]{2,}[a-z]', raw) or raw.isupper()
         or (raw.istitle() and word not in {'update', 'absolute', 'relative'}))
    ))
    expanded = []
    for word in words:
        # Handle common closed compounds such as `celltypes` without carrying
        # an application-specific vocabulary.
        if word.endswith('types') and len(word) > 5:
            expanded.extend((word[:-5], 'type'))
        else:
            expanded.append(word)
    topics = tuple(dict.fromkeys(_stem(word) for word in expanded
                                 if len(word) >= 3 and word not in _GENERIC and word not in apps))
    return topics[:6], apps


def document_headings(indexed_lines: list[tuple[int, str]]) -> dict[int, str]:
    """Recognize Markdown and HTML tutorial sections without losing source lines."""
    headings = {}
    summary_start = None
    summary_parts = []
    for index, (_, raw) in enumerate(indexed_lines):
        markdown = re.match(r'^\s*#{1,6}\s+(.+?)\s*#*\s*$', raw)
        if markdown:
            headings[index] = _clean_line(markdown.group(1))
        if re.fullmatch(r'\s*\*\*[^*]+\*\*\s*', raw):
            headings[index] = _clean_line(raw)
        if '<summary' in raw.lower():
            summary_start = index
            summary_parts = []
        if summary_start is not None:
            summary_parts.append(raw)
            if '</summary>' in raw.lower():
                title = _clean_line(' '.join(summary_parts))
                if title and not title.lower().startswith(('watch', 'demo', 'video', 'click to view')):
                    headings[summary_start] = title
                summary_start = None
        # Tutorials also use unadorned headings between HTML instruction blocks.
        text = _clean_line(raw)
        if (0 < index < len(indexed_lines) - 1 and raw.strip() == text
                and not indexed_lines[index - 1][1].strip()
                and not indexed_lines[index + 1][1].strip()
                and 8 <= len(text) <= 90 and text[0].isupper()
                and not re.search(r'[.!?:=;{}]', text)
                and not _START_STEP.match(text)):
            headings[index] = text
    return headings


def _clean_line(raw: str) -> str:
    raw = re.sub(r'\{%.*?%\}|\{\{.*?\}\}', '', raw)
    raw = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', raw)  # no image filenames as steps
    raw = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', raw)
    raw = re.sub(r'<(?:script|style|iframe)\b[^>]*>.*?</(?:script|style|iframe)>', '', raw, flags=re.I)
    raw = re.sub(r'<[^>]*>', ' ', raw)
    raw = html.unescape(raw).replace('**', '').replace('__', '').replace('`', '')
    raw = raw.strip()
    raw = re.sub(r'^(?:\s*[-*+]\s+|\s*\d+[.)]\s+)', '', raw)
    text = re.sub(r'\s+', ' ', raw).strip()
    if re.match(r'^(?:watch\b|click to view (?:the )?video|see the interface layout|this video shows)', text, re.I):
        return ''
    return text


def _key(text: str) -> set[str]:
    return {_stem(t) for t in re.findall(r'[a-z][a-z0-9]*', text.lower())}


def _match_count(text: str, topics: tuple[str, ...]) -> int:
    keys = _key(text)
    return sum(t in keys for t in topics)



def _tight_topic_match(lines: list[str], topics: tuple[str, ...]) -> bool:
    """All subject words must co-occur in one compact heading or sentence.

    Prevents unrelated instructions such as 'point color' + 'view size'
    being mistaken for an instruction to change *point size*.
    """
    for line in lines:
        for sentence in re.split(r'[.!?]+(?:\s+|$)', line):
            if _NEGATION.search(sentence):
                continue
            words = [_stem(w) for w in re.findall(r'[a-z][a-z0-9]*', sentence.lower())]
            for i in range(len(words)):
                if set(topics).issubset(words[i:i + 9]):
                    return True
    return False

def _file_and_start(location: str) -> tuple[str, int]:
    matched = re.fullmatch(r'(.+):L(\d+)-L\d+', location)
    return (matched.group(1), int(matched.group(2))) if matched else (location, 1)


def _rebuild(rows: list[sqlite3.Row]) -> list[tuple[int, str]]:
    numbered: dict[int, str] = {}
    for row in rows:
        _, start = _file_and_start(row['location'])
        for offset, raw in enumerate(row['content'].splitlines()):
            numbered.setdefault(start + offset, raw)
    return sorted(numbered.items())


def _context_match(path: str, source: str, apps: tuple[str, ...]) -> int:
    if not apps:
        return 0
    combined = (path + ' ' + urlsplit(source).path).lower()
    return sum(8 for term in apps if term in combined)


def _candidate_passages(source: str, path: str, indexed_lines: list[tuple[int, str]],
                        topics: tuple[str, ...], apps: tuple[str, ...], question: str = '') -> list[Workflow]:
    results: list[Workflow] = []
    if not topics:
        return results
    cleaned = [(line, _clean_line(raw)) for line, raw in indexed_lines]
    # Split by Markdown headings when available. For tutorials without headings,
    # the nearby-line window still keeps unrelated topics separated.
    titles = document_headings(indexed_lines)
    heads = list(titles)
    app_score = _context_match(path, source, apps)
    for idx, (line_no, text) in enumerate(cleaned):
        if not text or len(text) > 480:
            continue
        nearest_heading = max((h for h in heads if h <= idx), default=-1)
        next_heading = min((h for h in heads if h > idx), default=len(cleaned))
        # A 12-line bounded window can join adjacent original FTS chunks, but
        # cannot accidentally combine two distant sections of a long tutorial.
        if nearest_heading >= 0:
            heading = titles[nearest_heading]
        else:
            heading = ''
        if heading and (_match_count(heading, topics) == len(topics)
                        or _match_count(heading, topics[:1])):
            # A task heading anchors an entire documented workflow. Do not
            # truncate it to an arbitrary 10-line window.
            start = nearest_heading + 1
            end = min(next_heading, start + 42)
        else:
            start = max(nearest_heading + 1, idx - 3)
            end = min(next_heading, idx + 11)
        window = ' '.join(line for _, line in cleaned[start:end] if line)
        topic_count = _match_count(heading + ' ' + window, topics)
        if not _match_count(heading + ' ' + window, topics[:1]):
            continue
        required_topics = len(topics) if len(topics) <= 2 else math.ceil(len(topics) * 0.6)
        if topic_count < required_topics:
            continue
        if len(topics) == 2 and not _tight_topic_match(
                [heading, *(line for _, line in cleaned[start:end])], topics):
            continue
        # At least one topic must occur on the anchor line, otherwise the
        # same section can score dozens of unrelated windows.
        if not _match_count(text, topics) and not (idx == nearest_heading + 1 and _match_count(heading, topics)):
            continue
        actions: list[tuple[int, str]] = []
        descriptions: list[tuple[int, str]] = []
        for num, candidate in cleaned[start:end]:
            if not candidate or len(candidate) < 9 or len(candidate) > 320:
                continue
            if re.match(r'^(?:\w+\s*=|\#include|import\s|<|\}\s*;?|//|def\s|class\s)', candidate):
                continue
            if (' > ' in candidate or _START_STEP.match(candidate) or _CONTEXTUAL_STEP.match(candidate)
                    or (candidate.lower().startswith('to ') and
                        len(list(_INSIDE_ACTION.finditer(candidate))) >= 2)):
                actions.append((num, candidate))
            elif (' > ' in candidate or _match_count(candidate, topics)
                  or (heading and _match_count(heading, topics) == len(topics))):
                if not candidate.startswith('---') and not candidate.startswith('http'):
                    descriptions.append((num, candidate))
        # A matching keyword is not proof of a user workflow. Keep only the
        # most relevant sentences and never turn generic prose into clicks.
        if not actions and not descriptions:
            continue
        if actions:
            matches = [_match_count(action, topics) for _, action in actions]
            strongest = max(matches)
            if strongest:
                last_target = max(i for i, count in enumerate(matches) if count == strongest)
                target_verbs = {actions[i][1].split()[0].lower() for i, count in enumerate(matches)
                                if count == strongest}
                # A section can present parallel choices (e.g. export one
                # table or another). Keep shared setup, then omit weaker
                # alternatives expressed with the same action verb.
                actions = [action for i, action in enumerate(actions)
                           if i <= last_target or matches[i] == strongest
                           or action[1].split()[0].lower() not in target_verbs]
        anchor_topic = _match_count(text + ' ' + heading, topics)
        score = topic_count * 12 + anchor_topic * 3 + app_score
        score += _match_count(heading, topics) * 8
        if all(_stem(w) in _key(text) for w in topics):
            score += 12
        if _GUIDE_PATH.search(path):
            score += 7
        if _GUIDE_PATH.search(urlsplit(source).path):
            score += 30  # Directly sourced end-user documentation takes precedence
        if actions:
            score += 8
        if re.search(r'\b(?:select|choose)\b', question, re.I):
            if any(re.match(r'^(?:select|choose)\b', action, re.I)
                   and _match_count(action, topics) for _, action in actions):
                score += 8
        if heading and _match_count(heading, topics) == len(topics):
            score += 12
        # If the question names an app, prefer its matching tutorial and avoid
        # unrelated apps whose incidental text happens to contain the terms.
        if apps and not app_score:
            score -= 12
        selected = actions[:5]
        details = [d for d in descriptions if d[0] != selected[0][0]] if selected else descriptions
        used = selected or details
        low = min(n for n, _ in used)
        high = max(n for n, _ in used)
        results.append(Workflow(source, f'{path}:L{low}-L{high}', heading or Path(path).stem,
                                tuple(dict.fromkeys(s for _, s in details[:2])),
                                tuple(dict.fromkeys(s for _, s in actions[:5])), score))
    return results


def search_workflows(db_path: Path | str, question: str, *, limit: int = 3) -> list[Workflow]:
    """Reconstruct and rank docs from the existing FTS database (no rebuild)."""
    if not 1 <= limit <= 10:
        raise ValueError('limit must be 1..10')
    topics, apps = query_topics(question)
    if not topics:
        return []
    terms = []
    for word in topics:
        terms.extend([word, word + 's', word + 'es'])
    terms = list(dict.fromkeys(terms))[:18]
    query = ' OR '.join('"' + w.replace('"', '""') + '"' for w in terms)
    with closing(sqlite3.connect(db_path)) as db:
        db.row_factory = sqlite3.Row
        from .index import named_documents
        documents = named_documents(db, question)
        hits = db.execute(
            "SELECT source, location, content, bm25(chunks) AS score FROM chunks "
            "WHERE chunks MATCH ? AND kind='document' ORDER BY score LIMIT 850",
            (query,)).fetchall()
        files = defaultdict(list)
        for hit in hits:
            path, _ = _file_and_start(hit['location'])
            if documents and (hit['source'], path) not in documents:
                continue
            if not Path(path).suffix or path.lower().endswith(('.md','.markdown','.rst','.txt','.html','.htm','.pdf','.docx')):
                files[(hit['source'], path)].append(hit)
        # Score files using topic presence in a single chunk and explicit app
        # in path; do not rank by raw FTS alone (it favors incidental matches).
        ranked_files = []
        for (source, path), rows in files.items():
            relevance = max((_match_count(row['content'], topics) for row in rows), default=0)
            relevance = 12 * relevance + _context_match(path, source, apps)
            relevance += 5 if _GUIDE_PATH.search(path) else 0
            if apps and not _context_match(path, source, apps):
                relevance -= 8
            ranked_files.append((relevance, source, path))
        ranked_files.sort(reverse=True)
        passages = []
        for _, source, path in ranked_files[:45]:
            rows = db.execute(
                "SELECT location, content FROM chunks WHERE source=? AND kind='document' "
                "AND location LIKE ? LIMIT 350", (source, path + ':L%')).fetchall()
            passages.extend(_candidate_passages(source, path, _rebuild(rows), topics, apps, question))
    passages.sort(key=lambda w: (-w.score, -len(w.steps), w.source, w.location))
    # Same tutorial may contain several overlapping windows. Only show distinct
    # evidence, and prefer the window with the most support.
    selected: list[Workflow] = []
    seen = set()
    for passage in passages:
        key = (passage.source, _file_and_start(passage.location)[0], passage.title)
        if key in seen:
            continue
        seen.add(key)
        selected.append(passage)
        evidence = ' '.join((passage.title, *passage.details, *passage.steps))
        if (len(selected) == 1 and len(documents) == 1 and passage.steps
                and _match_count(evidence, topics) == len(topics)):
            # A self-contained match in an explicitly named document needs no
            # adjacent workflows that could introduce unrelated operations.
            break
        if len(selected) >= limit:
            break
    return selected
