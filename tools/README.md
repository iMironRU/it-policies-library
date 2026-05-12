# Инструменты

Утилиты для работы с библиотекой.

## validate-metadata.py

Проверяет, что `metadata.yml` файлы шаблонов соответствуют схеме.

```bash
# Проверить один файл
python tools/validate-metadata.py policies/02-access-control/password-policy/metadata.yml

# Проверить все
python tools/validate-metadata.py policies/
```

## generate-dependency-graph.py

Генерирует Mermaid-граф зависимостей из metadata.yml всех шаблонов и обновляет `docs/DEPENDENCIES.md`.

```bash
python tools/generate-dependency-graph.py
```

## check-links.py *(planned)*

Проверка ссылок внутри документов.

## Требования

```bash
pip install pyyaml jsonschema
```

Python 3.11+.
