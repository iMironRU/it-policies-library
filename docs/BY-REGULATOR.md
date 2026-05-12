# Индекс по регуляторным требованиям

Сопоставление шаблонов библиотеки с конкретными пунктами стандартов и нормативных актов.

## Принцип

В `metadata.yml` каждого шаблона есть поле `regulatory_refs` со списком ссылок на соответствующие пункты внешних стандартов. Этот индекс — обратный: «по требованию регулятора → какие политики нужны».

> **Дисклеймер.** Маппинг — ориентир, а не юридическая консультация. Для прохождения конкретного аудита привлекайте профильных специалистов.

---

## ISO/IEC 27001:2022

| Annex A контроль | Применимые политики |
|---|---|
| 5.1 Policies for information security | [POL-GOV-001](../policies/01-strategic/information-security-policy/) |
| 5.17 Authentication information | [POL-IAM-001](../policies/02-access-control/password-policy/) |
| ... | (наполняется) |

## NIST CSF 2.0

| Функция / категория | Применимые политики |
|---|---|
| GV.PO (Governance — Policy) | [POL-GOV-001](../policies/01-strategic/information-security-policy/) |
| PR.AA-01 (Identity Management) | [POL-IAM-001](../policies/02-access-control/password-policy/) |
| ... | (наполняется) |

## Российская регуляторика

### Федеральный закон 152-ФЗ «О персональных данных»

| Статья | Применимые политики |
|---|---|
| Ст. 18.1 | [POL-GOV-001](../policies/01-strategic/information-security-policy/) |
| Ст. 19 | [POL-GOV-001](../policies/01-strategic/information-security-policy/), [POL-IAM-001](../policies/02-access-control/password-policy/) |
| ... | (наполняется) |

### Приказ ФСТЭК России от 11.02.2013 № 17

| Мера | Применимые политики |
|---|---|
| ИАФ.1 (Идентификация и аутентификация) | [POL-IAM-001](../policies/02-access-control/password-policy/) |
| ИАФ.4 (Управление средствами идентификации/аутентификации) | [POL-IAM-001](../policies/02-access-control/password-policy/) |
| ... | (наполняется) |

### Приказ ФСТЭК России от 18.02.2013 № 21

| Мера | Применимые политики |
|---|---|
| ИАФ.1 | [POL-IAM-001](../policies/02-access-control/password-policy/) |
| ИАФ.4 | [POL-IAM-001](../policies/02-access-control/password-policy/) |
| ... | (наполняется) |

---

## CIS Controls v8

(наполняется)

## Other

- **GDPR** *(если применимо при трансграничной работе)* — наполняется
- **PCI DSS 4.0** — наполняется
- **СТО БР ИББС / ГОСТ Р 57580** *(для банков)* — наполняется

---

**Помочь наполнить?** Это работа на маппинг — нужны точные ссылки на пункты. Open Issue с тегом `regulatory-mapping`.
