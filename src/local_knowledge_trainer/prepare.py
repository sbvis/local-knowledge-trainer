"""Text extraction, deterministic chunking and modest source-grounded SFT examples."""
import hashlib
import html
import json
import random
import re
import zipfile
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

from .common import dump_json

CODE_EXTS = {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx",
              ".py", ".cs", ".java", ".js", ".ts", ".rs", ".qml", ".swift"}
DOC_EXTS = {".md", ".markdown", ".txt", ".rst", ".html", ".htm", ".pdf", ".docx"}
CONFIG_EXTS = {".cmake", ".json", ".yaml", ".yml", ".toml", ".ini"}
SKIP_DIRS = {".git", ".venv", "node_modules", "build", "dist", "vendor", "third_party",
             "third-party", ".idea", "__pycache__", "target", ".next", "coverage"}
SKIP_NAMES = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "poetry.lock",
              "Cargo.lock", "CMakeCache.txt", "compile_commands.json"}
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_FILES_PER_SOURCE = 2000
MAX_CHUNKS = 12000

@dataclass(frozen=True)
class Chunk:
    source: str
    location: str
    kind: str
    text: str
    start_line: int
    end_line: int
    commit: str = ""


class _TextHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lines = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "footer"):
            self.skip += 1
        if not self.skip and tag in ("h1", "h2", "h3", "p", "br", "li", "pre"):
            self.lines.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer") and self.skip:
            self.skip -= 1
        if not self.skip and tag in ("h1", "h2", "h3", "p", "li", "pre"):
            self.lines.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.lines.append(data)


def extract_text(path):
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise RuntimeError("PDF support needs pypdf (included in requirements-base.txt)") from exc
        reader = PdfReader(str(path))
        return "\n\n".join(f"[Page {n}]\n{page.extract_text() or ''}" for n, page in enumerate(reader.pages, 1))
    if suffix == ".docx":
        with zipfile.ZipFile(path) as file:
            doc = ElementTree.fromstring(file.read("word/document.xml"))
        ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        paragraphs = []
        for paragraph in doc.iter(ns + "p"):
            paragraphs.append("".join(t.text or "" for t in paragraph.iter(ns + "t")))
        return "\n".join(paragraphs)
    data = path.read_text(encoding="utf-8-sig", errors="replace")
    if suffix in (".html", ".htm") or (suffix == "" and "<html" in data[:200].lower()):
        parser = _TextHTML()
        parser.feed(data)
        data = "".join(parser.lines)
    return html.unescape(data).replace("\x00", "")


def iter_source_files(source, *, max_files=None):
    if max_files is None:
        max_files = MAX_FILES_PER_SOURCE
    path = source.path
    if path.is_file():
        yield path
        return
    count = 0
    for candidate in sorted(path.rglob("*")):
        if max_files and count >= max_files:
            break
        if not candidate.is_file() or candidate.is_symlink():
            continue
        rel = candidate.relative_to(path)
        if any(part in SKIP_DIRS or part.startswith(".") for part in rel.parts[:-1]):
            continue
        if candidate.name in SKIP_NAMES or candidate.name.startswith("."):
            continue
        if candidate.suffix.lower() not in (CODE_EXTS | DOC_EXTS | CONFIG_EXTS) and candidate.name not in {"CMakeLists.txt", "Makefile"}:
            continue
        if candidate.stat().st_size > MAX_FILE_BYTES:
            continue
        count += 1
        yield candidate


def _chunks_for_text(text, chunk_lines=36, overlap=5):
    lines = text.splitlines()
    step = chunk_lines - overlap
    for start in range(0, len(lines), step):
        subset = lines[start:start + chunk_lines]
        if not "".join(subset).strip():
            continue
        # Keep manageable even for minified lines.
        # Preserve leading blank lines so extracted fact line numbers remain
        # aligned with the original file. Bound minified lines and token cost.
        content = "\n".join(subset)[:2400].rstrip()
        if len(content.strip()) < 25:
            continue
        actual_end = start + len(content.splitlines())
        yield start + 1, min(actual_end, len(lines)), content


def collect_chunks(sources, *, max_chunks=None, max_files_per_source=None):
    """Round-robin source ingestion prevents one huge repository monopolizing data.

    Per-source file limits still apply. The global limit protects low-memory
    machines; it is an index/training coverage limit, not a download limit.
    """
    from collections import deque
    if max_chunks is None:
        max_chunks = MAX_CHUNKS

    def source_chunks(source):
        for path in iter_source_files(source, max_files=max_files_per_source):
            try:
                content = extract_text(path)
            except (OSError, ValueError, RuntimeError, zipfile.BadZipFile, KeyError) as exc:
                print(f"  Warning: skipping unreadable document {path}: {exc}")
                continue
            relative = path.relative_to(source.path).as_posix() if source.path.is_dir() else path.name
            kind = "code" if path.suffix.lower() in CODE_EXTS else "document"
            for start, end, part in _chunks_for_text(content):
                yield Chunk(source.origin, relative, kind, part, start, end, source.commit)

    active = deque(source_chunks(source) for source in sources)
    chunks = []
    while active and (not max_chunks or len(chunks) < max_chunks):
        iterator = active.popleft()
        try:
            chunks.append(next(iterator))
            active.append(iterator)
        except StopIteration:
            continue
    return chunks


def location_for(chunk):
    return f"{chunk.location}:L{chunk.start_line}-L{chunk.end_line}"


def _heading(text):
    for line in text.splitlines()[:15]:
        line = line.strip()
        if line.startswith("#") and 4 <= len(line) <= 120:
            return line.lstrip("#").strip()
    return ""


def _symbols(text):
    """Conservative symbol finder; declaration/position only, never guessed behavior."""
    seen = set()
    for match in re.finditer(r"\b(?:class|struct|enum(?:\s+class)?)\s+([A-Za-z_]\w*)\b", text):
        seen.add(match.group(1))
    # C/C++ qualified function names before opening parenthesis, one line only.
    for line in text.splitlines():
        if len(line) > 260 or line.strip().startswith(("//", "#", "*", "if ", "for ", "while ")):
            continue
        match = re.search(r"\b([A-Za-z_]\w*(?:::[A-Za-z_~]\w*)+)\s*\([^;{}]{0,150}\)", line)
        if match:
            seen.add(match.group(1))
    return sorted(seen)[:5]


def generated_examples(chunks, limit=1200, *, facts=None, audience="end_user"):
    """Create bounded, evidence-only training examples from documents and code facts.

    The deterministic builder does not invent function behavior. It teaches the
    assistant to synthesize *observed* UI controls and cross-repository links,
    and to say explicitly when runtime behavior is not proven. End-user mode
    avoids source-code modification answers; developer mode remains opt-in.
    High-quality reviewed task-oriented Q&A is still needed for real accuracy.
    """
    if audience not in ("end_user", "developer"):
        raise ValueError("audience must be end_user or developer")
    rows = []
    code_only_safety_examples = []
    for chunk in chunks:
        place = location_for(chunk)
        project = chunk.source.rsplit("/", 1)[-1]
        if Path(chunk.source).suffix.lower() in DOC_EXTS:
            project = Path(chunk.source).stem.replace('-', ' ')
        if chunk.kind == "document":
            from .workflow_search import _clean_line
            if project.startswith('_') or '/tree/' in chunk.source:
                project = Path(chunk.location).stem.replace('-', ' ')
            heading = _heading(chunk.text)
            subject = f"the section '{heading}'" if heading else f"the document at {place}"
            # User-facing examples should not teach the model to output code
            # excerpts as instructions for operating a GUI. Restrict the answer
            # to documentation text; never synthesize click paths here.
            readable_lines = []
            in_frontmatter = chunk.start_line == 1 and chunk.text.startswith('---')
            for offset, line in enumerate(chunk.text.splitlines()):
                if in_frontmatter:
                    if offset and line.strip() == '---':
                        in_frontmatter = False
                    continue
                cleaned = _clean_line(line)
                if (len(cleaned) >= 18 and not line.lstrip().startswith(('```', '#include', '//', '<script', '<style'))
                        and not re.search(r'[{}]|^\w[\w-]*\s*:', cleaned)
                        and not cleaned.lower().startswith(('watch how', 'layout:', 'author:', 'date:'))):
                    readable_lines.append(cleaned)
            readable = ' '.join(readable_lines)[:900]
            if len(readable) >= 65:
                if audience == "end_user":
                    prompt = (f"What does {project} say about {heading}?"
                              if heading else f"What does the {project} documentation explain?")
                    reply = (f"The {project} documentation says: {readable} "
                             f"(Source: {place}).")
                else:
                    prompt = f"Explain what {project} documents about {subject}, citing evidence."
                    reply = f"The documentation describes the following at {place}:\n{chunk.text[:1050]}"
                rows.append({
                    "messages": [{"role": "user", "content": prompt},
                                 {"role": "assistant", "content": reply}],
                    "_source": f"{chunk.source}::{chunk.location}", "_location": place,
                })
        elif audience == "end_user":
            # Small code-only collections still need two source groups for a
            # train/validation split. Add only a *few* truthful negative
            # examples; never teach source editing as an end-user UI task.
            symbols = _symbols(chunk.text)
            if symbols:
                code_only_safety_examples.append({
                    "messages": [
                        {"role": "user", "content": f"How do I operate {project} from its graphical interface?"},
                        {"role": "assistant", "content": "A source-code declaration by itself does not establish a user-interface procedure. "
                         "Look for the application's documented controls; do not edit source code to change "
                         "an existing application setting. The exact steps cannot be verified here."},
                    ],
                    "_source": f"{chunk.source}::{chunk.location}", "_location": place,
                })
        elif audience == "developer":
            for symbol in _symbols(chunk.text):
                matched = next((line.strip() for line in chunk.text.splitlines() if symbol in line), "")
                rows.append({
                    "messages": [
                        {"role": "user", "content": f"What does the source confirm about {symbol} in {project}?"},
                        {"role": "assistant", "content": f"In {place}, the code contains `{matched[:350]}`. This verifies the symbol's occurrence, but not its complete behavior or where it appears in the UI."},
                    ],
                    "_source": f"{chunk.source}::{chunk.location}", "_location": place,
                })

    if audience == "end_user":
        random.Random(73).shuffle(code_only_safety_examples)
        rows.extend(code_only_safety_examples[:max(5, limit // 20)])

    # Documentation questions need to teach complete user tasks, not just
    # summaries of random fragments. Reserve the majority of training space
    # for observed controls and *documented* workflows. Keep source summaries
    # as a small, diverse backup for questions without an explicit procedure.
    from .workflow_training import extract_workflow_examples
    workflows = (extract_workflow_examples(chunks, limit=max(25, limit // 3))
                 if audience == "end_user" else [])
    random.Random(42).shuffle(rows)
    if facts:
        from .analysis import ui_controls
        structured = []
        # Build concise, action-oriented examples from observed interface
        # metadata. These are task examples rather than symbol lookup drills.
        from .ui_semantics import _symbol_kind, interaction_for
        from collections import defaultdict
        source_code = defaultdict(list)
        for chunk in chunks:
            if chunk.kind == 'code':
                source_code[chunk.source].append(chunk.text)
        by_label = defaultdict(list)
        for fact in facts:
            if fact.predicate in {'label', 'title'}:
                by_label[(fact.source, fact.location.split(':L', 1)[0], fact.subject)].append(fact.object)
        for control in ui_controls(facts):
            if len(control['label']) < 3:
                continue
            file = control['file']
            first = control['evidence'][0]
            if audience == "end_user":
                project = control['source'].rstrip('/').split('/')[-1]
                kind = next((_symbol_kind(text, control['object'])
                             for text in source_code[control['source']]
                             if _symbol_kind(text, control['object'])), '')
                if not kind:
                    # Typed Qt signal declarations also establish an action kind.
                    for text in source_code[control['source']]:
                        signal = re.search(r'\bconnect\s*\(\s*&?' +
                            re.escape(control['object']) + r'\s*,\s*&'
                            r'(?:[A-Za-z_]\w*::)*([A-Za-z_]\w*Action)::',
                            re.sub(r'\s+', ' ', text))
                        if signal:
                            kind = signal.group(1)
                            break
                parts = []
                for registered, _ in control['registrations']:
                    parent = registered.split('.', 1)[0]
                    parent_labels = by_label.get((control['source'], file, parent), [])
                    if parent_labels:
                        parts.extend(parent_labels[:1])
                        break
                parts.append(control['label'])
                target = ' → '.join(parts)
                reply = (f"In {project}, locate the {target} control. " +
                         interaction_for(kind, 'change', control['label']).replace('**', '') +
                         "This is grounded in the visible action label and type; "
                         "its exact on-screen location depends on the workspace.")
                if control['hints']:
                    reply += f" Its help text says: {control['hints'][0]}."
                prompt = f"How do I change {control['label']} in {project}?"
            else:
                details = [f"The source defines `{control['object']}` with the visible text "
                           f"`{control['label']}` ({file}; {first[1]})."]
                if control['hints']:
                    details.append(f"Its tooltip/help text is: {control['hints'][0]!r}.")
                if control['registrations']:
                    value, loc = control['registrations'][0]
                    details.append(f"Source code registers the control through `{value}` ({loc}).")
                if control['connections']:
                    value, loc = control['connections'][0]
                    details.append(f"The connection names `{value}` ({loc}).")
                details.append("These are source-level facts; exact runtime screen position is unverified unless documented.")
                reply = ' '.join(details)
                prompt = f"What can the source prove about the '{control['label']}' UI control?"
            structured.append({
                'messages': [
                    {'role': 'user', 'content': prompt},
                    {'role': 'assistant', 'content': reply},
                ],
                '_source': f"relation::{control['source']}::{file}",
                '_location': first[1], '_evidence_type': 'static_ui',
                '_split_group': f"{control['source']}::{file}",
            })
        # Only create cross-repo examples when the target resolves uniquely;
        # never teach the model that an include proves a runtime call path.
        for fact in facts if audience == "developer" else ():
            if fact.predicate not in {'imports_file', 'references_class'} or not fact.target_source:
                continue
            project = fact.source.rstrip('/').split('/')[-1]
            target_project = fact.target_source.rstrip('/').split('/')[-1]
            if fact.predicate == 'imports_file':
                explanation = (f"{project} includes `{fact.object}` at {fact.location}; "
                               f"the referenced file resolves uniquely to {target_project} at {fact.target_location}. "
                               "This establishes a source-level dependency, not an observed runtime workflow.")
            else:
                explanation = (f"{project} references class `{fact.subject}` at {fact.location}; "
                               f"its unique definition is in {target_project} at {fact.target_location}. "
                               "This is source-level evidence and does not establish runtime behavior.")
            structured.append({
                'messages': [
                    {'role': 'user', 'content': f"What verified connection exists between {project} and {target_project}?"},
                    {'role': 'assistant', 'content': explanation},
                ],
                '_source': f'relation::{fact.source}::{fact.location}',
                '_location': fact.location, '_evidence_type': 'cross_repository',
                '_split_group': f"{fact.source}::{fact.location.split(':L', 1)[0]}",
            })
        # Reserve capacity for genuinely connected training examples instead of
        # letting a large README corpus crowd them out.
        rng = random.Random(42)
        rng.shuffle(structured)
        if audience == 'developer':
            keep = min(len(structured), max(40, limit // 2))
            rows = rows[:max(0, limit - keep - len(workflows))] + structured[:keep]

    # Workflow examples are the most actionable supervised targets; keep them
    # intact instead of randomly dropping them after appending more summaries.
    rng = random.Random(42)
    rng.shuffle(rows)
    if audience == 'end_user':
        from .sft_quality import assemble_user_examples
        return assemble_user_examples(workflows, structured if facts else [], rows, limit=limit, chunks=chunks)
    return rows[:limit]


def load_curated(path):
    if not path:
        return []
    rows = []
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        messages = row.get("messages", [])
        if (not isinstance(messages, list) or len(messages) < 2
                or messages[-1].get("role") != "assistant"
                or not any(m.get("role") == "user" for m in messages)):
            raise ValueError(f"Invalid curated QA at {path}:{n}")
        rows.append({"messages": messages, "_source": f"curated::{n}", "_location": str(path)})
    return rows


def write_training_data(rows, data_dir):
    """Group by source to avoid easy train/validation leakage across a file."""
    data_dir = Path(data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    groups = {}
    # Multi-repository examples can use *two* documents. Select the validation
    # split first; never put these auxiliary pairs in validation or include a
    # pair that reads material reserved for validation.
    cross_rows = [r for r in rows if r.get('_training_only')]
    for row in rows:
        if row.get('_training_only'):
            continue
        # A UI or cross-repo example derived from the same file should follow
        # that file into the *same* split as plain source examples.
        groups.setdefault(row.get("_split_group", row["_source"]), []).append(row)
    if len(groups) < 2:
        raise ValueError("Need at least two distinct source files/groups for a meaningful training split. Add documentation or curated QA.")
    keys = sorted(groups)
    # Preserve at least one generated-source validation group when enough files exist;
    # otherwise curated examples would dominate a tiny validation split.
    generated_keys = [key for key in keys if not key.startswith("curated::")]
    curated_keys = [key for key in keys if key.startswith("curated::")]
    cross_references = {key for row in cross_rows
                        for key in row.get('_referenced_groups', ())}
    rng = random.Random(1049)
    rng.shuffle(generated_keys)
    rng.shuffle(curated_keys)
    valid_keys = set()
    if len(generated_keys) >= 2:
        # When spare independent groups exist, reserve them for validation
        # instead of unnecessarily discarding all multi-source examples.
        safe_keys = [key for key in generated_keys if key not in cross_references]
        candidates = safe_keys or generated_keys
        valid_keys.update(candidates[:max(1, min(len(candidates), len(generated_keys) // 10))])
    if len(curated_keys) >= 2:
        valid_keys.update(curated_keys[:max(1, len(curated_keys) // 10)])
    # Never accidentally put *all* documented workflows in validation.
    # One big tutorial is a common case: there may be just one workflow group.
    workflow_keys = {key for key, group in groups.items()
                     if any(row.get('_evidence_type') == 'documented_workflow' for row in group)}
    if workflow_keys and workflow_keys <= valid_keys:
        rescued = sorted(workflow_keys)[0]
        valid_keys.remove(rescued)
        candidates = [key for key in keys if key not in valid_keys and key != rescued]
        candidates.sort(key=lambda key: (key in cross_references, key))
        if not valid_keys and candidates:
            valid_keys.add(candidates[0])
    if len(workflow_keys) >= 2 and not (workflow_keys & valid_keys):
        candidate = sorted(workflow_keys)[-1]
        valid_keys.add(candidate)
    # One README-rich website can coexist with exactly one file containing all
    # typed Qt controls. Do not lose that sole source of UI affordances to the
    # validation split when there are other files available as holdouts.
    ui_keys = {key for key, group in groups.items()
               if any(row.get('_evidence_type') == 'static_ui' for row in group)}
    if len(keys) >= 3 and ui_keys and ui_keys <= valid_keys:
        protected = workflow_keys | ui_keys
        rescued = sorted(ui_keys)[0]
        alternatives = [key for key in keys if key not in protected and key != rescued]
        alternatives.sort(key=lambda key: (key in cross_references, key))
        if valid_keys - {rescued} or alternatives:
            valid_keys.remove(rescued)
            if not valid_keys:
                valid_keys.add(alternatives[0])
    if not valid_keys:
        raise ValueError("Not enough distinct source groups for validation")
    train = [row for key in keys if key not in valid_keys for row in groups[key]]
    valid = [row for key in keys if key in valid_keys for row in groups[key]]
    if not train or not valid:
        raise ValueError("Not enough different sources for training and validation")
    train.extend(row for row in cross_rows
                 if not any(group in valid_keys for group in row.get('_referenced_groups', ())))
    for name, data in (("train", train), ("valid", valid)):
        with (data_dir / f"{name}.jsonl").open("w", encoding="utf-8") as out:
            for row in data:
                out.write(json.dumps({"messages": row["messages"]}, ensure_ascii=False) + "\n")
    from collections import Counter
    training_types = Counter(r.get('_evidence_type', 'general_document_or_safety') for r in train)
    validation_types = Counter(r.get('_evidence_type', 'general_document_or_safety') for r in valid)
    return {'train_examples': len(train), 'validation_examples': len(valid),
            'source_groups': len(keys), 'train_types': dict(training_types),
            'validation_types': dict(validation_types),
            'discarded_multisource_to_prevent_leakage': len(cross_rows) -
                sum(r.get('_evidence_type') == 'multi_source_doc' for r in train)}, valid
