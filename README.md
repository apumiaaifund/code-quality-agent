# Code Quality Agent (CQA) — Public Demo

**Встраиваемый offline-анализатор качества кода** для Python, Rust, TypeScript.
0 внешних зависимостей (stdlib Python >= 3.10). Работает офлайн. Не SaaS,
не требует сторонних бинарей — только стандартные компиляторы, если хотите
верификацию.

**Demo materials only. Full source code — available on purchase.**

## Зачем

Большинство SAST-инструментов **молча деградируют**: если тулчейн не установлен,
они просто пропускают проверку — и вы не знаете, что именно не проверено.
CQA устроен иначе: **`Report.errors` явно перечисляет, что не проверено**
(`toolchain:missing`, `scan:timeout`, `scan:size_limit`). Это главное отличие
от Semgrep/Sonar.

## Что проверяется

- **38 правил**: секреты (AWS, GitHub, OpenAI, private key, password, API key),
  `eval`/`exec`/`shell=True`, `unsafe` без `// SAFETY:`, `unwrap`, magic numbers,
  сложность, длина функций, `pub`-видимость, `any`, `console.log`, forbidden
  imports, TODO/FIXME.
- **Компилятор как истина**: `cargo check --message-format=json`, `tsc --noEmit`,
  `compile()` для Python (in-process, без `.pyc`).
- **Циклы импортов** — Tarjan SCC по графу py/rs/ts (TYPE_CHECKING-блоки не считаются).
- **6 слоёв верификации** (опционально): Hypothesis / proptest / fast-check (PBT),
  cargo-fuzz, Kani (model checking), Verus (формальная).
- **ИИ-слой** (опционально, `--ai`): LLM с обязательной верификацией каждой
  гипотезы — `evidence` должен быть в исходнике, иначе REJECTED. Галлюцинации
  не проходят.
- **SARIF 2.1.0** (`--sarif`) — отчёт для GitHub Code Scanning и любого
  CI, который понимает SARIF. Рядом с `report.json` и `report.md`.

## Два режима

1. **CLI** — `python cli.py --project . --fail-on critical`
2. **Модуль** — `CodeQualityAgent(project_dir=Path('.')).scan()` в 3 строки.

## CLI

    # базовый прогон
    python cli.py --project . --fail-on never

    # CI-гейт с максимальной точностью
    python cli.py --project . --precision strict --fail-on critical

    # legacy-проект: принять существующее как baseline
    python cli.py --project . --write-baseline baseline.json
    python cli.py --project . --baseline baseline.json --fail-on critical

    # air-gapped / untrusted code
    python cli.py --project /untrusted --safe-mode --offline --fail-on never

    # SARIF 2.1.0 для GitHub Code Scanning / CI
    python cli.py --project . --fail-on critical --sarif

Exit codes: `0` — успех, `1` — найдены critical (или warning при `--fail-on warning`),
`2` — internal error.

## Что подтверждено прогоном

| Метрика | Значение |
|---|---|
| Тестов | **59**, все ok (`unittest discover`) |
| Правил в реестре | 38 |
| Слоёв верификации | 6 (PBT × 3, fuzz, Kani, Verus) |
| Runtime-зависимостей | **0** (stdlib) |
| Schema контракт | v3, защищён тестом |
| Self-scan CQA | 60 файлов, 0 errors |

## Что честно НЕ закрыто

- Нет taint-анализа, dead code, duplication detection, полной замены Sonar/Semgrep.
- Нет 100% точности (теорема Райса). Максимум — `--precision strict` даёт
  precision ~95% ценой recall ~20–30%.
- `from X import Y` трактуется как зависимость от `X`, а не `X.Y` — ограничение
  детектора циклов.
- AI-слой прогонялся только с MockClient в тестах. `--ai` требует
  Ollama/OpenAI-compatible endpoint, которого в CI нет.
- SARIF содержит абсолютные пути (`artifactLocation.uri`). Для внутреннего
  CI это нормально; для передачи отчёта наружу нужен `--redact-paths` —
  его пока нет (в roadmap).
- **Клиента нет.** Инструмент, не SaaS.

## Что в этой витрине

- `examples/bad_python.py` — демонстрационный файл с 5+ нарушениями
  (eval, shell=True, print, magic number, bad naming, too many args).
- `examples/rules_*.json` — конфиги правил для Python / Rust / TypeScript.
- `LICENSE` — Proprietary. Исходный код — по запросу.

## Цена

| Уровень | Цена | Что |
|---|---|---|
| Non-exclusive license | $1 000–2 000 | Исходник + право использовать в своих проектах |
| С острой болью | $3 000–5 000 | То же + интеграция под ваш CI |

Контакт: [apumiaaifund@gmail.com](mailto:apumiaaifund@gmail.com)

**No synthetic data in production.** Все цифры в этом README подтверждены
прогонами; ничего не придумано.
