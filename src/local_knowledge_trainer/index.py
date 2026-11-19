"""Dependency-free, embeddable SQLite FTS5 index and transparent retrieval tests."""
import json
from collections import Counter
from contextlib import closing
import re
import sqlite3
from pathlib import Path
from urllib.parse import urlsplit

from .prepare import location_for

SCHEMA_VERSION = 1

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "does", "do", "for",
    "from", "how", "in", "into", "is", "it", "me", "of", "on", "or", "our", "the",
    "their", "this", "to", "what", "when", "where", "which", "who", "why", "with",
    "would", "you", "your", "file", "used", "using", "about", "according", "source"
}


def create_index(chunks, output, facts=None):
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.unlink(missing_ok=True)
    with closing(sqlite3.connect(output)) as db, db:
        db.execute("CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
        db.execute("INSERT INTO metadata VALUES (?, ?)", ("schema_version", str(SCHEMA_VERSION)))
        db.execute("""CREATE VIRTUAL TABLE chunks USING fts5(
                   source UNINDEXED, location, content,
                   kind UNINDEXED, git_commit UNINDEXED, tokenize='unicode61'
                   )""")
        db.executemany(
            "INSERT INTO chunks (source, location, content, kind, git_commit) VALUES (?, ?, ?, ?, ?)",
            ((c.source, location_for(c), c.text, c.kind, c.commit) for c in chunks),
        )
        if facts is not None:
            db.execute("""CREATE TABLE facts (
                       source TEXT NOT NULL, location TEXT NOT NULL,
                       subject TEXT NOT NULL, predicate TEXT NOT NULL,
                       object TEXT NOT NULL, evidence TEXT NOT NULL,
                       target_source TEXT NOT NULL, target_location TEXT NOT NULL,
                       confidence TEXT NOT NULL)""")
            db.executemany('INSERT INTO facts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           [(f.source, f.location, f.subject, f.predicate,
                             f.object, f.evidence, f.target_source,
                             f.target_location, f.confidence) for f in facts])
            db.execute('CREATE INDEX facts_source ON facts(source)')
            db.execute('CREATE INDEX facts_target ON facts(target_source)')
            db.execute('CREATE INDEX facts_subject ON facts(subject)')
    return len(chunks)


def _named_repositories(db, question: str) -> list[str]:
    """Find GitHub sources explicitly named in a question (not fuzzy matches).

    A question about a named repository should not rank code from unrelated
    repositories higher just because they happen to mention the same word.
    """
    named = []
    for (source,) in db.execute("SELECT DISTINCT source FROM chunks"):
        url = urlsplit(source)
        if url.hostname != "github.com":
            continue
        parts = url.path.strip("/").split("/")
        if len(parts) != 2:
            continue
        repo = parts[-1].removesuffix(".git")
        if len(repo) < 4:
            continue
        if re.search(r"(?<![\w-])" + re.escape(repo) + r"(?![\w-])", question, re.IGNORECASE):
            named.append((len(repo), source))
    if not named:
        return []
    named.sort(reverse=True)
    # Multiple explicit repository names indicate a comparison question.
    return [source for _, source in named[:4]]


def _readme_first(question: str) -> bool:
    return bool(re.search(r"\b(purpose|overview|summarize|summary|about|repository|repo)\b",
                          question, re.IGNORECASE))


def named_documents(db, question: str) -> list[tuple[str, str]]:
    """Scope explicit document filenames and application names to their documents."""
    candidates = []
    documents = {(source, location.split(':L', 1)[0]) for source, location in
                 db.execute("SELECT DISTINCT source, location FROM chunks WHERE kind='document'")}
    filenames = {path.replace('\\', '/').rsplit('/', 1)[-1] for _, path in documents}
    prefixes = Counter(Path(name).stem.lower().split('-')[0]
                       for name in filenames if '-' in Path(name).stem)
    common_prefixes = {prefix for prefix, count in prefixes.items() if count >= 2}
    for source, path in sorted(documents):
        filename = path.replace('\\', '/').rsplit('/', 1)[-1]
        if filename.casefold() in question.casefold():
            candidates.append((1000 + len(filename), source, path))
            continue
        stem = Path(filename).stem
        parts = re.findall(r'[a-z0-9]+', stem.lower())
        terms = [term for term in parts if len(term) >= 4 and term not in
                 {'data', 'plugin', 'paper', 'tutorial', 'guide', 'readme'} | common_prefixes]
        matches = [term for term in terms if re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', question, re.I)]
        if matches and len(matches) == len(terms):
            score = max(map(len, matches)) + (20 if Path(filename).suffix.lower() in {'.md', '.html', '.txt'} else 0)
            candidates.append((score, source, path))
    if not candidates:
        return []
    best = max(score for score, _, _ in candidates)
    return list(dict.fromkeys((source, path) for score, source, path in candidates if score == best))


def search(db_path, question, limit=5):
    if not 1 <= limit <= 100:
        raise ValueError("Search limit must be between 1 and 100")
    words = re.findall(r"[\w]+", question, flags=re.UNICODE)
    unique = list(dict.fromkeys(w.lower() for w in words if len(w) >= 2 and w.lower() not in STOPWORDS))[:18]
    if not unique:
        return []
    query = " OR ".join('"' + w.replace('"', '""') + '"' for w in unique)
    with closing(sqlite3.connect(db_path)) as db:
        db.row_factory = sqlite3.Row
        names = _named_repositories(db, question)
        scope = (" AND source IN (" + ",".join("?" for _ in names) + ")") if names else ""
        documents = named_documents(db, question)
        document_parameters = []
        if documents and not names:
            scope = ' AND (' + ' OR '.join('(source=? AND location LIKE ?)' for _ in documents) + ')'
            for source, path in documents:
                document_parameters.extend((source, path + ':L%'))
        # For an introductory question about a named repo, README content
        # is more useful than random incidental identifier matches.
        order = ("CASE WHEN lower(location) LIKE '%readme%' THEN 0 "
                 "WHEN lower(location) LIKE '%docs/%' THEN 1 ELSE 2 END, score"
                 if names and _readme_first(question) else "score")
        sql = ("SELECT source, location, kind, git_commit, "
               "snippet(chunks, 2, '[', ']', '...', 28) AS snippet, "
               "content, bm25(chunks) AS score FROM chunks "
               "WHERE chunks MATCH ?" + scope + " ORDER BY " + order + " LIMIT ?")
        hits = [dict(row) for row in db.execute(sql, (query, *names, *document_parameters, limit)).fetchall()]
        if documents and not names:
            # The introduction establishes a document's subject and scope.
            # Retain it alongside matched body passages to avoid confusing
            # background literature or a secondary dataset with the main study.
            introductions = []
            for source, path in documents:
                first = db.execute(
                    "SELECT source, location, kind, git_commit, '' AS snippet, content, 0.0 AS score "
                    "FROM chunks WHERE source=? AND location LIKE ? "
                    "ORDER BY CAST(substr(location, instr(location, ':L') + 2) AS INTEGER) LIMIT 1",
                    (source, path + ':L%')).fetchone()
                if first:
                    introductions.append(dict(first))
            ordered = {}
            for hit in introductions + hits:
                ordered.setdefault((hit['source'], hit['location']), hit)
            hits = list(ordered.values())[:limit]
        if names and _readme_first(question):
            # For high-level questions guarantee an introductory README or guide
            # appears, even when full-text ranking favors unrelated code tokens.
            primer_sql = ("SELECT source, location, kind, git_commit, "
                          "'' AS snippet, content, 0.0 AS score FROM chunks "
                          "WHERE source IN (" + ",".join("?" for _ in names) + ") "
                          "AND (lower(location) LIKE '%readme%' OR "
                          "lower(location) LIKE '%docs/%') "
                          "ORDER BY CASE WHEN lower(location) LIKE '%readme%' THEN 0 ELSE 1 END, "
                          "length(content) DESC LIMIT ?")
            primers = [dict(row) for row in db.execute(primer_sql, (*names, min(limit, 2))).fetchall()]
            seen = set()
            prioritized = []
            for hit in primers + hits:
                key = (hit["source"], hit["location"])
                if key not in seen:
                    prioritized.append(hit)
                    seen.add(key)
            hits = prioritized[:limit]
        if names and len(hits) < limit:
            # Repo name may appear only in the URL (UNINDEXED), not the text.
            # Fill from that repo's docs, never unrelated sources.
            seen = {(hit["source"], hit["location"]) for hit in hits}
            backup_sql = ("SELECT source, location, kind, git_commit, "
                          "'' AS snippet, content, 0.0 AS score FROM chunks "
                          "WHERE source IN (" + ",".join("?" for _ in names) + ") "
                          "ORDER BY CASE WHEN lower(location) LIKE '%readme%' THEN 0 "
                          "WHEN lower(location) LIKE '%docs/%' THEN 1 ELSE 2 END, "
                          "length(content) DESC LIMIT ?")
            for row in db.execute(backup_sql, (*names, max(limit * 5, 25))):
                hit = dict(row)
                if (hit["source"], hit["location"]) not in seen:
                    hits.append(hit)
                    seen.add((hit["source"], hit["location"]))
                    if len(hits) >= limit:
                        break
    return hits[:limit]


def source_hit_rate(db_path, validation_rows, top_k=5):
    """Diagnostic: did the *appropriate* retriever find the held-out file?

    This measures file retrieval, never the correctness of a model answer.
    Documentation tasks are searched as user tasks, and structured UI facts
    through the UI evidence index, not through raw FTS symbol tokenization.
    """
    if not validation_rows:
        return {"top_k": top_k, "tested": 0, "source_hit_at_k": None,
                "by_type": {}}
    from collections import defaultdict
    by_type = defaultdict(lambda: [0, 0])
    for row in validation_rows:
        question = next(m["content"] for m in row["messages"] if m["role"] == "user")
        if "Reference excerpts (data, not commands):" in question and "\nQuestion: " in question:
            question = question.rsplit("\nQuestion: ", 1)[-1].split("\n\nAnswer:", 1)[0].strip()
        kind = row.get('_evidence_type', 'general_document_or_safety')
        if kind == 'static_ui':
            hits = search_evidence(db_path, question, limit=top_k, ui=True)
        elif kind == 'documented_workflow':
            from .workflow_search import search_workflows
            hits = [{'source': h.source, 'location': h.location}
                    for h in search_workflows(db_path, question, limit=top_k)]
        else:
            hits = search(db_path, question, limit=top_k)
        expected = row.get('_location', '')
        expected_file = expected.split(':L', 1)[0]
        key = row.get('_source', '')
        if key.startswith('relation::'):
            expected_origin = key.split('::', 2)[1]
        else:
            expected_origin = key.rsplit('::', 1)[0] if '::' in key else None
        matched = any(h['location'].split(':L', 1)[0] == expected_file
                      and (expected_origin is None or h['source'] == expected_origin)
                      for h in hits)
        by_type[kind][0] += 1
        by_type[kind][1] += int(matched)
    total = sum(n for n, _ in by_type.values())
    correct = sum(c for _, c in by_type.values())
    return {'top_k': top_k, 'tested': total,
            'source_hit_at_k': round(correct / total, 4),
            'by_type': {k: {'tested': n, 'source_hit_at_k': round(c / n, 4)}
                        for k, (n, c) in sorted(by_type.items())}}


# UI help is fundamentally different from code understanding. Only documented
# operating procedures may be presented as step-by-step user instructions.
_UI_INTENT = re.compile(
    r"\b(?:how\s+(?:do|can|to)|where\s+(?:do|can)|steps?\s+to)\b.*"
    r"\b(?:click|open|select|set|change|adjust|increase|decrease|"
    r"configure|enable|disable|find|use|show|hide|export|import|load|"
    r"point\s+size|opacity|settings?|interface|ui|menu|view|plot|zoom)\b",
    re.IGNORECASE | re.DOTALL,
)
_UI_ACTION_WORDS = re.compile(
    r"\b(click|select|open|choose|menu|settings?|toolbar|slider|"
    r"tab|panel|button|checkbox|dropdown|dialog|controls?|"
    r"drag|toggle|adjust|increase|decrease|navigate|right.click|zoom|hold|clicking|selects)\b",
    re.IGNORECASE,
)
_UI_CONTEXT = re.compile(
    r"\b(?:app|application|software|program|plugin|plot|view|"
    r"window|panel|menu|settings?|toolbar|button|slider|interface|ui|gui|"
    r"point\s+size|dataset|workspace|visualization|chart|hierarchy|selection|dropdown|table)\b", re.IGNORECASE)
_UI_GENERIC = STOPWORDS | {
    "how", "can", "increase", "decrease", "change", "adjust", "modify",
    "configure", "find", "set", "settings", "plugin", "repository",
    "project", "view", "ui", "interface", "plot", "the", "in", "via",
    "software", "application", "program", "system", "app"
}


def is_ui_instruction_question(question: str) -> bool:
    """End-user tasks are the default; explicit programming questions are not.

    Questions need not contain the words 'UI', 'menu' or a plugin name: people
    naturally say 'How can I find cell abundance?' or 'Create a subset'.
    """
    if re.search(r"\b(?:implement|write\s+code|edit\s+code|modify\s+source|"
                 r"source\s+code|compile|api\s+call|c\+\+|python\s+code|"
                 r"function\s+implementation|class\s+definition|debug\s+the\s+code)\b",
                 question, re.IGNORECASE):
        return False
    text = question.strip()
    text = re.sub(r'^(?:in|for)\s+[^,]{1,80},\s*', '', text, flags=re.I)
    if re.match(r"^(?:how\s+(?:do\s+i|can\s+i|to|would\s+i)|"
                r"where\s+(?:do\s+i|can\s+i|is)|"
                r"show\s+me\s+how|i\s+want\s+to|"
                r"can\s+i|please\s+(?:show|help)|"
                r"(?:find|create|identify|calculate|explore|visualize|plot|"
                r"change|adjust|select|filter|import|export|open|save)\b)", text, re.I):
        return True
    return bool(_UI_ACTION_WORDS.search(text) and _UI_CONTEXT.search(text))




def _has_focused_ui_instruction(content: str, words: list[str]) -> bool:
    """Reject docs where unrelated paragraphs incidentally contain both terms.

    A navigation guide should mention the requested topic together in a small
    span AND show an interaction cue nearby. We do not promote arbitrary FTS
    matches to user-visible instructions.
    """
    flattened = re.sub(r'\s+', ' ', content.casefold())
    tokens = [(m.group(0), m.start(), m.end())
              for m in re.finditer(r'\b[a-z][a-z0-9_]*\b', flattened)]
    required = set(words)
    for i, (word, start, _) in enumerate(tokens):
        if word not in required:
            continue
        for j in range(i, min(len(tokens), i + max(7, len(required) + 2))):
            span_words = {t[0] for t in tokens[i:j + 1]}
            if required.issubset(span_words):
                end = tokens[j][2]
                # Topic words in separate sentences are not one GUI control.
                if re.search(r'[.!?](?:\s|$)', flattened[start:end]):
                    continue
                nearby = flattened[max(0, start - 180): min(len(flattened), end + 180)]
                if _UI_ACTION_WORDS.search(nearby):
                    return True
    return False

def search_ui_guides(db_path, question, limit=5):
    """Find actual documented UI instructions; never substitute random code.

    Select only source documents with an overlapping topic and an actionable UI
    cue. No evidence -> no procedural model answer. Works with existing DBs.
    """
    if not 1 <= limit <= 100:
        raise ValueError("Search limit must be between 1 and 100")
    words = list(dict.fromkeys(w.lower() for w in re.findall(r"[\w]+", question)
                               if len(w) >= 3 and w.lower() not in _UI_GENERIC))
    if not words:
        return []
    with closing(sqlite3.connect(db_path)) as db:
        db.row_factory = sqlite3.Row
        names = _named_repositories(db, question)
        # An explicitly named repository scopes the query; its name need not
        # also appear inside the documentation's body text.
        names_lower = {urlsplit(n).path.rstrip('/').rsplit('/', 1)[-1].lower()
                       for n in names}
        words = [w for w in words if w not in names_lower]
        if not words:
            return []
        query = " OR ".join('"' + w.replace('"', '""') + '"' for w in words[:12])
        scope = (" AND source IN (" + ",".join("?" for _ in names) + ")") if names else ""
        sql = ("SELECT source, location, kind, git_commit, content, "
               "bm25(chunks) AS score FROM chunks WHERE chunks MATCH ? "
               "AND kind = 'document'" + scope + " ORDER BY score LIMIT 250")
        candidates = [dict(row) for row in db.execute(sql, (query, *names))]
    ranked = []
    for hit in candidates:
        path = hit['location'].split(':L', 1)[0].lower()
        if not path.endswith(('.md', '.markdown', '.rst', '.txt', '.html', '.htm', '.pdf', '.docx')):
            continue
        content = hit['content'].lower()
        matching = sum(bool(re.search(r'(?<!\w)' + re.escape(w) + r'(?!\w)', content))
                       for w in words)
        # Two-topic queries must match both topics (e.g. point AND size).
        if matching < len(words) or not _has_focused_ui_instruction(content, words):
            continue
        bonus = 4 if re.search(r'guide|manual|tutorial|how.to|usage|help|walkthrough', path) else 0
        bonus += 2 if path.endswith('readme.md') else 0
        ranked.append((-(matching * 3 + bonus), hit['score'], hit))
    ranked.sort(key=lambda row: row[:2])
    return [hit for _, _, hit in ranked[:limit]]


def _fact_table_exists(db) -> bool:
    return db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='facts'").fetchone() is not None


def _topic_terms(question: str) -> list[str]:
    generic = STOPWORDS | {'repository', 'repositories', 'project', 'projects', 'plugin',
                           'interface', 'user', 'ui', 'gui', 'application', 'software',
                           'increase', 'decrease', 'change', 'configure', 'setting', 'settings',
                           'which', 'show', 'steps', 'operate', 'work', 'works', 'code'}
    return list(dict.fromkeys(w.lower() for w in re.findall(r'[A-Za-z][A-Za-z_0-9]*', question)
                              if len(w) >= 3 and w.lower() not in generic))[:12]


def _topic_overlap(text: str, terms: list[str]) -> int:
    lower = text.lower()
    return sum(bool(re.search(r'(?<!\w)' + re.escape(w) + r'(?!\w)', lower)) for w in terms)


def search_evidence(db_path, question: str, limit: int = 6, *, ui: bool = False) -> list[dict]:
    """Hybrid lexical/relational search across repositories, using one local SQLite file.

    Legacy indexes without a fact table keep working. A fact never becomes an
    assertion of observed runtime behavior: metadata makes its origin visible.
    Each returned passage is cited and short enough for small on-device LLMs.
    """
    if not 1 <= limit <= 30:
        raise ValueError('Evidence limit must be between 1 and 30')
    if ui:
        guides = search_ui_guides(db_path, question, limit=limit)
        # Preserve documentation first, then supplement it with observed GUI
        # controls and connections from source. Neither alone proves a click path.
        baseline: list[dict] = guides
    else:
        baseline = search(db_path, question, limit=max(limit, min(2 * limit, 16)))
    # A broad user question such as "What is the purpose of this charting tool?"
    # needs descriptive documents, not obscure cross-repository symbol edges.
    # Only add the relation graph when the question is *about* architecture or
    # dependencies (UI tasks have their own verified evidence path).
    if not ui and not re.search(
            r"\b(?:architectur\w*|dependenc\w*|integrat\w*|relationship\w*|"
            r"link\w*|connect\w*|implementation|source code|header|class|"
            r"between repositories|across repositories|compare repos|uses?)\b",
            question, re.IGNORECASE):
        return baseline[:limit]
    with closing(sqlite3.connect(db_path)) as db:
        db.row_factory = sqlite3.Row
        if not _fact_table_exists(db):
            return baseline[:limit]
        terms = _topic_terms(question)
        if not terms:
            return baseline[:limit]
        named = _named_repositories(db, question)
        facts = db.execute('''SELECT * FROM facts WHERE predicate IN
                             ('label','title','tooltip','help_text','placeholder',
                              'registered_with','connected_to','signal','callback_invokes','imports_file','references_class')
                             LIMIT 25000''').fetchall()
        candidates = []
        seed_sources = {h['source'] for h in baseline[:max(2, limit // 2)]}
        seed_files = {(h['source'], h['location'].split(':L', 1)[0])
                      for h in baseline[:max(2, limit // 2)]}
        for fact in facts:
            fact = dict(fact)
            is_ui_fact = fact['predicate'] in {
                'label', 'title', 'tooltip', 'help_text', 'placeholder',
                'registered_with', 'connected_to', 'signal', 'callback_invokes'
            }
            if ui and not is_ui_fact:
                continue
            # A precise topic match is required; we never use arbitrary graph
            # connectivity as a reason to include irrelevant code.
            relevant = _topic_overlap(' '.join((fact['subject'], fact['object'],
                                               fact['evidence'])), terms)
            explicit_link = (len(named) >= 2 and fact['source'] in named
                             and fact['target_source'] in named and
                             fact['target_source'] != fact['source'])
            linked_seed = (not ui and bool(fact['target_source']) and
                           (fact['source'], fact['location'].split(':L', 1)[0]) in seed_files)
            if not relevant and not explicit_link and not linked_seed:
                continue
            if named and fact['source'] not in named and fact['target_source'] not in named:
                # Allow related repositories only if they are genuinely connected
                # to a named repository by a resolved cross-repository edge.
                continue
            if ui:
                # Textual UI evidence is allowed, but not a synthetic click-path.
                priority = 10 if fact['predicate'] in {'label', 'title', 'tooltip'} else 5
            else:
                priority = 12 if fact['predicate'] in {'imports_file', 'references_class'} else 4
            if fact['target_source'] and fact['target_source'] != fact['source']:
                priority += 4
            if fact['source'] in seed_sources:
                priority += 3
            priority += relevant * 4 + (10 if explicit_link else 0) + (6 if linked_seed else 0)
            candidates.append((-priority, fact))

        candidates.sort(key=lambda p: (p[0], p[1]['source'], p[1]['location']))
        graph_hits = []
        seen_graph = set()
        for _, fact in candidates:
            key = (fact['source'], fact['location'], fact['subject'], fact['predicate'])
            if key in seen_graph:
                continue
            seen_graph.add(key)
            # Keep exact provenance. Related targets are separate evidence, not
            # implied proof of calling or runtime behavior.
            relation_descriptions = {
                'imports_file': f"The source includes a header named {fact['object']}.",
                'references_class': f"The source mentions a class named {fact['subject']}.",
                'label': f"An interface control has the visible label {fact['object']}.",
                'title': f"An interface section has the visible title {fact['object']}.",
                'tooltip': f"An interface tooltip says {fact['object']}.",
                'help_text': f"The control help text is {fact['object']}.",
                'signal': f"The control connects to signal {fact['object']}.",
                'callback_invokes': f"A callback invokes {fact['object']}.",
            }
            content = (f"Source excerpt from {fact['location']}:\n{fact['evidence']}\n"
                       f"Verified observation: {relation_descriptions.get(fact['predicate'], 'A source-level reference is present.')}")
            if fact['target_source']:
                content += (f"\nUniquely resolved target: {fact['target_source']} "
                            f":: {fact['target_location']}")
            if ui:
                # Describe connected UI behavior using *other observed facts*
                # about the exact same object in the same file, rather than
                # returning a lone property without its signal/handler.
                file_path = fact['location'].split(':L', 1)[0]
                siblings = [row for row in db.execute(
                    "SELECT predicate, object, location FROM facts WHERE source=? AND subject=? "
                    "AND location LIKE ? AND predicate IN "
                    "('label','title','tooltip','registered_with','connected_to','signal','callback_invokes') "
                    "ORDER BY location LIMIT 12",
                    (fact['source'], fact['subject'], file_path + ':L%'))]
                if siblings:
                    content += '\nOther observed properties and connections for this control:\n' + '\n'.join(
                        f"- {r['predicate']}: {r['object']} ({r['location']})"
                        for r in siblings if r['predicate'] != fact['predicate'])
            elif fact['target_source']:
                # Include a small extract from the uniquely resolved target;
                # this is evidence from the second repo, not a guessed link.
                target_file = fact['target_location'].split(':L', 1)[0]
                target = db.execute(
                    'SELECT content, location FROM chunks WHERE source=? AND location LIKE ? LIMIT 1',
                    (fact['target_source'], target_file + ':L%')).fetchone()
                if target:
                    content += f"\nTarget excerpt ({target['location']}):\n{target['content'][:450]}"
            content += (f"\nEvidence confidence: {fact['confidence']}; "
                        'no runtime UI location is implied.')
            graph_hits.append(dict(source=fact['source'], location=fact['location'],
                                   kind='code_relation', content=content,
                                   git_commit='', score=0.0, snippet=content,
                                   target_source=fact['target_source'],
                                   target_location=fact['target_location']))
            if len(graph_hits) >= limit * 3:
                break

        if ui:
            # Give a model both workflow docs *and* the source wiring when
            # available. Never replace documentation with declarations alone.
            result = baseline[:max(1, (limit + 1) // 2)]
            seen = {(h['source'], h['location']) for h in result}
            for hit in graph_hits:
                key = (hit['source'], hit['location'])
                if key not in seen:
                    result.append(hit)
                    seen.add(key)
                if len(result) >= limit:
                    break
            if len(result) < limit:
                for hit in baseline:
                    key = (hit['source'], hit['location'])
                    if key not in seen:
                        result.append(hit)
                        seen.add(key)
                        if len(result) >= limit:
                            break
            return result[:limit]

        # Balance direct source excerpts with cross-file relationships. Include
        # both sides when the graph explicitly resolves a target in another repo.
        result = baseline[:max(1, limit // 2)]
        seen = {(h['source'], h['location']) for h in result}
        for hit in graph_hits:
            key = (hit['source'], hit['location'])
            if key not in seen:
                result.append(hit)
                seen.add(key)
            if len(result) >= limit:
                break
        if len(result) < limit:
            for hit in baseline:
                key = (hit['source'], hit['location'])
                if key not in seen:
                    result.append(hit)
                    seen.add(key)
                    if len(result) >= limit:
                        break
        return result[:limit]


def related_facts(db_path, subject: str, limit: int = 30) -> list[dict]:
    """Inspect the recorded evidence for an exact source symbol or UI object."""
    with closing(sqlite3.connect(db_path)) as db:
        db.row_factory = sqlite3.Row
        if not _fact_table_exists(db):
            return []
        return [dict(row) for row in db.execute(
            'SELECT * FROM facts WHERE subject=? ORDER BY source, location LIMIT ?',
            (subject, min(max(limit, 1), 100)))]
