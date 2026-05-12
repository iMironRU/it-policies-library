# Патч: добавление полного каталога политик в библиотеку

## Что в этом архиве

Изменения относительно ранее выложенного скелета библиотеки.

### Новые файлы
- `docs/CATALOG.md` — **полный каталог из 24 доменов** (~250 пунктов), адаптированный из ранее подготовленного it-policies.md v5. Это карта всех мыслимых политик в IT-периметре. Адаптация: убрана нумерация версий (v5), добавлены ссылки на ROADMAP/MATURITY-LAYERS/DEPENDENCIES, проставлены ✅ на двух уже реализованных шаблонах (POL-GOV-001, POL-IAM-001), секция «Минимальный пакет» заменена ссылкой на `packs/minimum-starter/`, секция «Слои зрелости» сокращена со ссылкой на MATURITY-LAYERS.

### Изменённые файлы
- `README.md` — добавлена четвёртая «дверь» (🗺️ Хочу видеть всю карту целиком) + ссылка в секции «Понимание системы»
- `docs/BY-DOMAIN.md` — добавлена ссылка наверху на CATALOG.md как родительский обзорный документ
- `CHANGELOG.md` — отражены изменения

## Как применить

Распакуйте архив в корень репозитория поверх существующих файлов. Все пути относительны корня:

```bash
cd it-policies-library
tar -xzf it-policies-library-patch.tar.gz
git status   # покажет 4 изменения: 1 новый + 3 модифицированных
git add CHANGELOG.md README.md docs/BY-DOMAIN.md docs/CATALOG.md
git commit -m "docs: add full policy catalog (CATALOG.md)"
```

## Что НЕ изменилось

- Все шаблоны политик (`policies/`)
- Эталоны (POL-GOV-001, POL-IAM-001)
- Метаданные, инструменты, CI
- LICENSE, CLAUDE.md, CONTRIBUTING.md
- packs/, .github/
- ROADMAP.md, MATURITY-LAYERS.md, DEPENDENCIES.md, GLOSSARY.md, BY-USE-CASE.md, BY-REGULATOR.md
