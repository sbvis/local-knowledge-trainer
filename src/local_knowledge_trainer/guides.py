"""Add verified user guides to an existing release without retraining weights.

The guide is indexed as source evidence, not converted into model weights.
Python standard library only; fully offline. Existing SQLite FTS5 schema is reused.
"""
from __future__ import annotations

import json
import sqlite3
from contextlib import closing
from pathlib import Path

from .common import sha256_file, now_utc
from .prepare import Chunk, _chunks_for_text, extract_text, location_for

GUIDE_EXTENSIONS = {'.md', '.markdown', '.txt', '.rst', '.html', '.htm'}


def add_guide(release: Path, guide_path: Path, source: str | None = None) -> int:
    release = Path(release).expanduser().resolve()
    guide_path = Path(guide_path).expanduser().resolve()
    db_path = release / 'knowledge.db'
    if not db_path.is_file():
        raise FileNotFoundError(f'Knowledge database not found: {db_path}')
    if not guide_path.is_file():
        raise FileNotFoundError(f'User guide not found: {guide_path}')
    if guide_path.suffix.lower() not in GUIDE_EXTENSIONS:
        raise ValueError('add-guide accepts Markdown, text, RST or HTML; convert PDFs to text first')
    origin = source or f'local-guide:{guide_path.stem}'
    if not origin.strip():
        raise ValueError('Guide source name cannot be blank')
    text = extract_text(guide_path)
    parts = [Chunk(origin, guide_path.name, 'document', part, start, end)
             for start, end, part in _chunks_for_text(text)]
    if not parts:
        raise ValueError('User guide is empty or too short to index')
    with closing(sqlite3.connect(db_path)) as db, db:
        version = db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
        if not version or version[0] != '1':
            raise ValueError('Unsupported SQLite knowledge index schema')
        # A source's UI guide is intentionally replaceable and takes precedence
        # during UI retrieval via its filename (guide/manual/tutorial).
        db.execute("DELETE FROM chunks WHERE source=? AND location LIKE ?",
                   (origin, guide_path.name + ':L%'))
        db.executemany('''INSERT INTO chunks (source, location, content, kind, git_commit)
                          VALUES (?, ?, ?, ?, ?)''',
                       [(c.source, location_for(c), c.text, c.kind, '') for c in parts])
        count = db.execute('SELECT count(*) FROM chunks').fetchone()[0]
    manifest_path = release / 'manifest.json'
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        manifest.setdefault('knowledge_index', {})['chunk_count'] = count
        updates = manifest.setdefault('knowledge_updates', [])
        updates.append({'source': origin, 'file': guide_path.name, 'chunks': len(parts),
                        'updated_at_utc': now_utc(), 'guide_sha256': sha256_file(guide_path),
                        'type': 'locally provided user guide (not model fine-tuning)'})
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    # Rehash existing release files, preserving the original list of assets.
    sums_path = release / 'SHA256SUMS.txt'
    if sums_path.is_file():
        listed = []
        for row in sums_path.read_text(encoding='utf-8').splitlines():
            if '  ' in row:
                listed.append(row.split('  ', 1)[1])
        for entry in ('knowledge.db', 'manifest.json'):
            if (release / entry).exists() and entry not in listed:
                listed.append(entry)
        sums_path.write_text(''.join(f'{sha256_file(release / item)}  {item}\n'
                                    for item in listed if (release / item).is_file()),
                             encoding='utf-8')
    return len(parts)
