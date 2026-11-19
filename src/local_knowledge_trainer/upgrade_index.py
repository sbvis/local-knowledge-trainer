"""Safely enrich a previously exported knowledge.db with source relationships.

Operates on the existing text chunks; retraining and downloading are unnecessary.
For the best graph fidelity, build a fresh package directly from source files.
"""
from __future__ import annotations

import json
import re
import sqlite3
from contextlib import closing
from pathlib import Path

from .analysis import analyze_chunks, graph_summary
from .common import sha256_file, now_utc
from .prepare import Chunk

_LOCATION = re.compile(r'^(.*):L(\d+)-L(\d+)$')


def upgrade_release(release: str | Path) -> dict:
    release = Path(release).expanduser().resolve()
    db_path = release / 'knowledge.db'
    if not db_path.is_file():
        raise FileNotFoundError(f'No knowledge database: {db_path}')
    with closing(sqlite3.connect(db_path)) as db:
        version = db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
        if version is None or version[0] != '1':
            raise ValueError('Expected knowledge index schema v1')
        if db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='facts'").fetchone():
            raise ValueError('Graph already installed. Existing knowledge is unchanged.')
        chunks = []
        for source, loc, kind, content, commit in db.execute(
                'SELECT source, location, kind, content, git_commit FROM chunks'):
            matched = _LOCATION.match(loc)
            if matched:
                chunks.append(Chunk(source, matched.group(1), kind, content,
                                    int(matched.group(2)), int(matched.group(3)), commit))
        if not chunks:
            raise ValueError('No reconstructible source chunks in the index')
        facts = analyze_chunks(chunks)
        # A SQLite backup is more reliable than copying a live WAL file.
        backup_path = release / 'knowledge.pre-graph.db'
        if backup_path.exists():
            raise FileExistsError(f'Backup already exists: {backup_path}')
        with closing(sqlite3.connect(backup_path)) as backup:
            db.backup(backup)
        try:
            with db:
                db.execute('''CREATE TABLE facts (source TEXT NOT NULL, location TEXT NOT NULL,
                           subject TEXT NOT NULL, predicate TEXT NOT NULL, object TEXT NOT NULL,
                           evidence TEXT NOT NULL, target_source TEXT NOT NULL,
                           target_location TEXT NOT NULL, confidence TEXT NOT NULL)''')
                db.executemany('INSERT INTO facts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                               [(f.source, f.location, f.subject, f.predicate, f.object,
                                 f.evidence, f.target_source, f.target_location,
                                 f.confidence) for f in facts])
                db.execute('CREATE INDEX facts_source ON facts(source)')
                db.execute('CREATE INDEX facts_target ON facts(target_source)')
                db.execute('CREATE INDEX facts_subject ON facts(subject)')
        except sqlite3.DatabaseError:
            raise  # backup remains to permit manual recovery
    report = graph_summary(facts)
    (release / 'analysis_summary.json').write_text(json.dumps(report, indent=2) + '\n',
                                                  encoding='utf-8')
    manifest_path = release / 'manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        manifest.setdefault('knowledge_index', {})['relations'] = report['facts']
        manifest['knowledge_index']['method'] = report['method']
        manifest.setdefault('knowledge_updates', []).append({
            'type': 'source relationship analysis', 'created_at_utc': now_utc(),
            'facts': report['facts'], 'trained_model_modified': False})
        manifest_path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    sums_path = release / 'SHA256SUMS.txt'
    if sums_path.exists():
        paths = [line.split('  ', 1)[1] for line in sums_path.read_text().splitlines()
                 if '  ' in line]
        for added in ('analysis_summary.json', 'knowledge.db', 'manifest.json'):
            if added not in paths and (release / added).is_file():
                paths.append(added)
        sums_path.write_text(''.join(f'{sha256_file(release / item)}  {item}\n' for item in paths
                                     if (release / item).is_file()), encoding='utf-8')
    return report
