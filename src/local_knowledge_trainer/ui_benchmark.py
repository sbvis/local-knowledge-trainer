"""Independently specified end-user acceptance cases, not training-set loss.

Run on a completed release's knowledge.db; the GGUF, GPU and network are not
needed for evidence-first UI answers. A pass is only as credible as the
manually reviewed test cases provided by the evaluator.
"""
from __future__ import annotations

import json
from pathlib import Path

from .ui_help import answer_ui_question


def evaluate_ui(db_path: Path | str, benchmark: Path | str) -> dict:
    db_path = Path(db_path)
    path = Path(benchmark)
    if not db_path.is_file():
        raise FileNotFoundError(f'Knowledge index not found: {db_path}')
    if not path.is_file():
        raise FileNotFoundError(f'Benchmark not found: {path}')
    cases = []
    for number, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith('#'):
            continue
        obj = json.loads(raw)
        question = obj.get('question', '')
        if not isinstance(question, str) or not question.strip():
            raise ValueError(f'Line {number}: nonempty question required')
        for field in ('must_include', 'must_not_include'):
            if field in obj and (not isinstance(obj[field], list)
                                 or not all(isinstance(v, str) for v in obj[field])):
                raise ValueError(f'Line {number}: {field} must be a list of strings')
        expected = obj.get('expected_level')
        if expected is not None and expected not in ('documented', 'control', 'insufficient'):
            raise ValueError(f'Line {number}: invalid expected_level')
        # Never accept source-code editing suggestions for end-user cases.
        answer = answer_ui_question(db_path, question)
        full = answer.answer.casefold()
        failures = []
        if expected and expected != answer.level:
            failures.append(f'expected {expected}, received {answer.level}')
        for term in obj.get('must_include', []):
            if term.casefold() not in full:
                failures.append(f'missing {term!r}')
        for term in obj.get('must_not_include', []):
            if term.casefold() in full:
                failures.append(f'forbidden {term!r}')
        # Distinguish an independent gold-source check from output style checks.
        source = obj.get('expected_source')
        if source is not None and not any(source in ref['source'] for ref in answer.references):
            failures.append(f'expected source absent: {source!r}')
        cases.append({'question': question, 'passed': not failures,
                      'level': answer.level, 'failures': failures,
                      'references': list(answer.references), 'answer': answer.answer})
    if not cases:
        raise ValueError('Benchmark has no test cases')
    passed = sum(c['passed'] for c in cases)
    return {'tested': len(cases), 'passed': passed, 'failed': len(cases) - passed,
            'pass_rate': round(passed / len(cases), 4), 'cases': cases,
            'scope': 'evidence-first offline UI guidance; not GGUF model accuracy'}


def main(argv: list[str] | None = None) -> int:
    import argparse
    parser = argparse.ArgumentParser(description='Benchmark end-user UI answers against reviewed JSONL cases')
    parser.add_argument('release', type=Path)
    parser.add_argument('benchmark', type=Path, help='JSONL: question, expected_level, must_include, must_not_include, expected_source')
    parser.add_argument('--output', type=Path, help='Write detailed JSON report')
    parser.add_argument('--min-pass-rate', type=float, default=1.0)
    args = parser.parse_args(argv)
    if not 0 <= args.min_pass_rate <= 1:
        parser.error('--min-pass-rate must be between 0 and 1')
    result = evaluate_ui(args.release / 'knowledge.db', args.benchmark)
    for case in result['cases']:
        status = 'PASS' if case['passed'] else 'FAIL'
        print(f'{status} [{case["level"]}] {case["question"]}')
        for failure in case['failures']:
            print(f'    {failure}')
    print(f'UI acceptance: {result["passed"]}/{result["tested"]} ({result["pass_rate"]:.1%})')
    print('This is an answer benchmark; it does not measure full GUI runtime accuracy.')
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return 0 if result['pass_rate'] >= args.min_pass_rate else 1


if __name__ == '__main__':
    raise SystemExit(main())
