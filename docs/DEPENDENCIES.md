# Граф зависимостей между политиками

Каждая политика в библиотеке имеет `metadata.yml` с полями `depends_on` (что должно быть раньше) и `related_to` (с чем связана горизонтально). Этот документ визуализирует связи.

> **Автогенерация.** Графы в этом файле в перспективе будут автоматически генерироваться из `metadata.yml` всех шаблонов скриптом `tools/generate-dependency-graph.py`. Сейчас — ручной вариант для двух заполненных эталонов.

---

## Условные обозначения

- **Сплошная стрелка** (`-->`) — `depends_on`: должно быть внедрено раньше
- **Пунктирная стрелка** (`-.->`) — `related_to`: связано, но без жёсткого порядка
- Цвет узла отражает домен

---

## Этап 0: Основа

```mermaid
graph TD
    MTA001[POL-MTA-001<br/>Управление политиками]
    GOV001[POL-GOV-001<br/>Политика ИБ]
    MTA002[POL-MTA-002<br/>Управление исключениями]

    MTA001 --> GOV001
    GOV001 --> MTA002

    style MTA001 fill:#fff4e1
    style GOV001 fill:#e1f5ff
    style MTA002 fill:#fff4e1
```

---

## Зонтичная политика → Политика паролей

```mermaid
graph TD
    GOV001[POL-GOV-001<br/>Политика ИБ]
    MTA001[POL-MTA-001<br/>Управление политиками]

    IAM001[POL-IAM-001<br/>Пароли]
    IAM002[POL-IAM-002<br/>MFA]
    IAM003[POL-IAM-003<br/>Управление доступом]
    IAM005[POL-IAM-005<br/>Учётные записи]
    IAM008[POL-IAM-008<br/>Секреты и vault]

    GOV001 --> IAM001
    MTA001 --> IAM001

    IAM001 -.-> IAM002
    IAM001 -.-> IAM003
    IAM001 -.-> IAM005
    IAM001 -.-> IAM008

    style GOV001 fill:#e1f5ff
    style MTA001 fill:#fff4e1
    style IAM001 fill:#e8f5e9
    style IAM002 fill:#e8f5e9
    style IAM003 fill:#e8f5e9
    style IAM005 fill:#e8f5e9
    style IAM008 fill:#e8f5e9
```

---

## Управление доступом — полная картина (планируется)

```mermaid
graph TD
    GOV001[POL-GOV-001<br/>Политика ИБ]

    IAM001[POL-IAM-001<br/>Пароли]
    IAM002[POL-IAM-002<br/>MFA]
    IAM003[POL-IAM-003<br/>Управление доступом]
    IAM004[POL-IAM-004<br/>PAM]
    IAM005[POL-IAM-005<br/>Учётные записи jml]
    IAM006[POL-IAM-006<br/>Just-in-Time]
    IAM007[POL-IAM-007<br/>Access Review]
    IAM008[POL-IAM-008<br/>Секреты]
    IAM009[POL-IAM-009<br/>SSO]
    IAM010[POL-IAM-010<br/>VPN/Удалённый доступ]

    HRM001[POL-HRM-001<br/>AUP]
    HRM002[POL-HRM-002<br/>Onboarding]
    HRM003[POL-HRM-003<br/>Offboarding]

    GOV001 --> IAM003
    IAM003 --> IAM001
    IAM003 --> IAM002
    IAM003 --> IAM004
    IAM003 --> IAM005
    IAM003 --> IAM006
    IAM003 --> IAM007
    IAM003 --> IAM008
    IAM003 --> IAM009
    IAM003 --> IAM010

    IAM005 -.-> HRM002
    IAM005 -.-> HRM003
    HRM001 -.-> IAM003

    style GOV001 fill:#e1f5ff
    style IAM001 fill:#e8f5e9
    style IAM002 fill:#e8f5e9
    style IAM003 fill:#e8f5e9
    style IAM004 fill:#e8f5e9
    style IAM005 fill:#e8f5e9
    style IAM006 fill:#e8f5e9
    style IAM007 fill:#e8f5e9
    style IAM008 fill:#e8f5e9
    style IAM009 fill:#e8f5e9
    style IAM010 fill:#e8f5e9
    style HRM001 fill:#f3e5f5
    style HRM002 fill:#f3e5f5
    style HRM003 fill:#f3e5f5
```

---

## Кластер «Данные»

```mermaid
graph TD
    GOV001[POL-GOV-001<br/>Политика ИБ]

    DAT001[POL-DAT-001<br/>Защита данных]
    DAT002[POL-DAT-002<br/>Резервное копирование]
    DAT003[POL-DAT-003<br/>Обработка ПДн]
    DAT004[POL-DAT-004<br/>Хранение и удаление]
    DAT005[POL-DAT-005<br/>Обработка DSR]
    DAT006[POL-DAT-006<br/>DLP]
    DAT007[POL-DAT-007<br/>Шифрование]

    BCP001[POL-BCP-001<br/>BCP]
    BCP002[POL-BCP-002<br/>DRP]

    GOV001 --> DAT001
    DAT001 --> DAT003
    DAT001 --> DAT004
    DAT003 --> DAT005
    DAT001 --> DAT006
    DAT001 --> DAT007
    DAT002 -.-> BCP002
    BCP001 -.-> BCP002

    style GOV001 fill:#e1f5ff
    style DAT001 fill:#fce4ec
    style DAT002 fill:#fce4ec
    style DAT003 fill:#fce4ec
    style DAT004 fill:#fce4ec
    style DAT005 fill:#fce4ec
    style DAT006 fill:#fce4ec
    style DAT007 fill:#fce4ec
    style BCP001 fill:#f3e5f5
    style BCP002 fill:#f3e5f5
```

---

## Кластер «Разработка ПО»

```mermaid
graph TD
    GOV001[POL-GOV-001<br/>Политика ИБ]

    DEV001[POL-DEV-001<br/>SDLC]
    DEV002[POL-DEV-002<br/>Secure SDLC]
    DEV003[POL-DEV-003<br/>DevSecOps]
    DEV004[POL-DEV-004<br/>Threat Modeling]
    DEV009[POL-DEV-009<br/>Управление кодом]
    DEV014[POL-DEV-014<br/>Зависимости + SBOM]
    DEV015[POL-DEV-015<br/>Безопасность CI/CD]
    DEV008[POL-DEV-008<br/>AI-помощники в разработке]

    SUP018[POL-SUP-018<br/>Supply chain security]

    GOV001 --> DEV001
    DEV001 --> DEV002
    DEV002 --> DEV003
    DEV002 --> DEV004
    DEV001 --> DEV009
    DEV003 --> DEV014
    DEV003 --> DEV015
    DEV014 -.-> SUP018
    DEV009 -.-> DEV008

    style GOV001 fill:#e1f5ff
    style DEV001 fill:#e8f5e9
    style DEV002 fill:#e8f5e9
    style DEV003 fill:#e8f5e9
    style DEV004 fill:#e8f5e9
    style DEV009 fill:#e8f5e9
    style DEV014 fill:#e8f5e9
    style DEV015 fill:#e8f5e9
    style DEV008 fill:#e8f5e9
    style SUP018 fill:#fff4e1
```

---

## Как читать граф

1. **Сверху — фундамент**, снизу — производные
2. **Внедрять снизу вверх по сплошным стрелкам.** Если у политики есть `depends_on` X, без X её внедрять бессмысленно.
3. **Пунктирные стрелки** — это «следует знать о смежной политике», но порядок гибкий.
4. **Цвета доменов** помогают визуально различать области:
   - 🔵 Стратегические — фундамент
   - 🟡 Метаполитики — управление документами
   - 🟢 Управление доступом, разработка
   - 🟣 Персонал, BCP/DRP
   - 🩷 Данные

---

## Полный граф (планируется)

Полный граф для всех 24 доменов будет автоматически генерироваться по мере наполнения библиотеки. Сейчас он бы выглядел слишком разрежённо — большая часть узлов ещё не существует.

См. `tools/generate-dependency-graph.py` для генерации.
