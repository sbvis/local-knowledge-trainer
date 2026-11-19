"""Framework-aware, source-grounded help for *existing* UI actions.

Only the action type, label, tooltip and registration come from the indexed
source. The control affordance mapping is a framework convention, not proof of
where a widget appears in a particular workspace. Never invent menu paths.
"""
from __future__ import annotations

import re
import sqlite3
from contextlib import closing
from pathlib import Path

# A small, auditable adapter. Additional frameworks can add their own mappings.
ACTION_KINDS = {
    'DecimalAction': 'numeric', 'IntegralAction': 'numeric',
    'ToggleAction': 'toggle', 'OptionsAction': 'options',
    'TriggerAction': 'trigger', 'ColorAction': 'color',
    'ColormapAction': 'color', 'FilePickerAction': 'file',
    'DirectoryPickerAction': 'file', 'SelectionAction': 'selection',
    'DimensionPickerAction': 'options', 'GroupAction': 'group',
    'StringAction': 'text',
}


def _symbol_kind(text: str, symbol: str) -> str:
    # Source declarations, not a vague variable-name heuristic.
    expr = re.compile(r'\b(' + '|'.join(map(re.escape, ACTION_KINDS)) +
                      r')\s+\**\s*&?\s*' + re.escape(symbol) + r'\b')
    match = expr.search(text)
    return match.group(1) if match else ''


def resolve_action_type(db_path: Path | str, source: str, symbol: str) -> tuple[str, str]:
    """Return (verified declared type, citation) or empty strings.

    Restricts the lookup to the originating repository to avoid a similarly
    named control in another plugin contaminating the answer.
    """
    if not re.fullmatch(r'[A-Za-z_]\w*', symbol):
        return '', ''
    with closing(sqlite3.connect(db_path)) as db:
        rows = db.execute('''SELECT location, content FROM chunks
                             WHERE source=? AND kind='code' AND content LIKE ?
                             LIMIT 80''', (source, '%' + symbol + '%')).fetchall()
    declared = []
    for location, content in rows:
        kind = _symbol_kind(content, symbol)
        if kind:
            declared.append((kind, location))
            continue
        # A typed signal connection can also identify the framework action
        # class even when the member declaration fell outside the indexed chunk.
        signal = re.search(
            r'\bconnect\s*\(\s*&?' + re.escape(symbol) +
            r'\s*,\s*&(?:[A-Za-z_]\w*::)*(' +
            '|'.join(map(re.escape, ACTION_KINDS)) + r')::[A-Za-z_]\w*',
            re.sub(r'\s+', ' ', content),
        )
        if signal:
            declared.append((signal.group(1), location))
    types = {kind for kind, _ in declared}
    if len(types) != 1:
        return '', ''
    return declared[0]


def interaction_for(kind: str, question: str, label: str) -> str:
    """A generic action suggestion, never a claim of exact screen placement."""
    question = question.lower()
    name = f'**{label}**'
    category = ACTION_KINDS.get(kind)
    if category == 'numeric':
        if re.search(r'\b(increase|enlarge|larger|bigger|grow|raise)\b', question):
            return f'Increase the value of {name}. '
        if re.search(r'\b(decrease|smaller|reduce|shrink|lower)\b', question):
            return f'Decrease the value of {name}. '
        return f'Adjust the numeric value of {name}. '
    if category == 'toggle':
        return f'Turn {name} on or off as needed. '
    if category == 'options':
        return f'Choose the desired option in {name}. '
    if category == 'trigger':
        return f'Activate {name}. '
    if category == 'color':
        return f'Choose the desired color or color map in {name}. '
    if category == 'file':
        return f'Use {name} to choose a file or folder. '
    if category == 'text':
        return f'Enter the desired value in {name}. '
    if category == 'selection':
        return f'Use the {name} selection control. '
    return f'Locate the control labeled {name}. '
