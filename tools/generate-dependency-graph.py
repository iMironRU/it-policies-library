#!/usr/bin/env python3
"""
Генерирует Mermaid-граф зависимостей из всех metadata.yml.

Использование:
    python generate-dependency-graph.py [--output docs/DEPENDENCIES.md]

Stub-версия. Полная реализация — TODO.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)


def main():
    root = Path(__file__).parent.parent
    policies_dir = root / "policies"

    metadata_files = list(policies_dir.rglob("metadata.yml"))
    metadata_files = [f for f in metadata_files if "_TEMPLATE" not in f.parts]

    policies = []
    for f in metadata_files:
        try:
            with open(f, "r", encoding="utf-8") as fp:
                data = yaml.safe_load(fp)
                policies.append(data)
        except Exception as e:
            print(f"WARNING: failed to parse {f}: {e}", file=sys.stderr)

    print(f"Found {len(policies)} policies")
    print()
    print("```mermaid")
    print("graph TD")
    for p in policies:
        pid = p.get("id", "?")
        title = p.get("short_title", p.get("title", "?"))
        print(f'    {pid.replace("-", "_")}[{pid}<br/>{title}]')
    print()
    for p in policies:
        pid = p.get("id", "?")
        for dep in p.get("depends_on", []) or []:
            print(f"    {dep.replace('-', '_')} --> {pid.replace('-', '_')}")
        for rel in p.get("related_to", []) or []:
            print(f"    {pid.replace('-', '_')} -.-> {rel.replace('-', '_')}")
    print("```")

    print("\n[TODO] Эта реализация — stub. Записывать результат в docs/DEPENDENCIES.md, кластеризовать по доменам, добавить стили.", file=sys.stderr)


if __name__ == "__main__":
    main()
