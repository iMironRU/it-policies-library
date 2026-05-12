#!/usr/bin/env python3
"""
Валидация metadata.yml файлов шаблонов политик.

Использование:
    python validate-metadata.py <path>

Если path — файл: проверяет один файл.
Если path — директория: рекурсивно проверяет все metadata.yml.
"""

import sys
import os
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)


# Обязательные поля
REQUIRED_FIELDS = {
    "id": str,
    "title": str,
    "slug": str,
    "domain": str,
    "version": (str, float, int),
    "status": str,
    "maturity": str,
    "conditional": bool,
    "typical_owner": str,
    "last_reviewed": (str, object),  # date или string
    "review_cycle_months": int,
}

VALID_STATUSES = ["draft", "review", "active", "deprecated"]
VALID_MATURITIES = ["core", "standard", "advanced"]

VALID_DOMAIN_PREFIXES = [
    "GOV", "IAM", "DGV", "DAT", "BCP", "ARC", "OPS", "SVC",
    "NET", "END", "COM", "DEV", "CLD", "SAA", "SUP", "FIN",
    "HRM", "SEC", "FOR", "CMP", "AIG", "EMG", "RUS", "MTA",
]


def validate_file(path: Path) -> list[str]:
    """Возвращает список ошибок (пустой = OK)."""
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"YAML parse error: {e}"]
    except Exception as e:
        return [f"Read error: {e}"]

    if not isinstance(data, dict):
        return ["Root must be a mapping (dict)"]

    # Required fields
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in data:
            errors.append(f"Missing required field: {field}")
            continue
        if not isinstance(data[field], expected_type):
            errors.append(
                f"Field '{field}' must be {expected_type}, got {type(data[field]).__name__}"
            )

    # ID format
    if "id" in data and isinstance(data["id"], str):
        parts = data["id"].split("-")
        if len(parts) != 3 or parts[0] != "POL":
            errors.append(f"ID must match POL-XXX-NNN, got: {data['id']}")
        elif parts[1] not in VALID_DOMAIN_PREFIXES:
            errors.append(
                f"Domain prefix '{parts[1]}' not in valid list. See CLAUDE.md."
            )
        elif not parts[2].isdigit() or len(parts[2]) != 3:
            errors.append(f"ID number must be 3 digits, got: {parts[2]}")

    # Enum values
    if data.get("status") not in VALID_STATUSES:
        errors.append(f"status must be one of {VALID_STATUSES}, got: {data.get('status')}")
    if data.get("maturity") not in VALID_MATURITIES:
        errors.append(f"maturity must be one of {VALID_MATURITIES}, got: {data.get('maturity')}")

    # Slug consistency: должен соответствовать имени родительской папки
    expected_slug = path.parent.name
    if data.get("slug") != expected_slug:
        errors.append(
            f"slug '{data.get('slug')}' must match parent folder name '{expected_slug}'"
        )

    # Domain consistency: должен соответствовать имени папки-домена (на 2 уровня выше)
    expected_domain = path.parent.parent.name
    if data.get("domain") != expected_domain:
        errors.append(
            f"domain '{data.get('domain')}' must match domain folder name '{expected_domain}'"
        )

    return errors


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate-metadata.py <path>")
        sys.exit(1)

    target = Path(sys.argv[1])

    if not target.exists():
        print(f"ERROR: Path not found: {target}")
        sys.exit(1)

    # Соберём список metadata.yml для проверки
    files = []
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = list(target.rglob("metadata.yml"))
        # Исключаем _TEMPLATE
        files = [f for f in files if "_TEMPLATE" not in f.parts]
    else:
        print(f"ERROR: Path is neither file nor directory: {target}")
        sys.exit(1)

    if not files:
        print("No metadata.yml files found.")
        sys.exit(0)

    total_errors = 0
    for f in files:
        errors = validate_file(f)
        if errors:
            print(f"❌ {f}")
            for err in errors:
                print(f"   - {err}")
            total_errors += len(errors)
        else:
            print(f"✅ {f}")

    print(f"\nChecked {len(files)} file(s), found {total_errors} error(s).")
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
