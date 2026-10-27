# Lab 07 - Database Persistence Layer

Лабораторна робота №7. Варіант 4 — Система банківських рахунків.

## Опис
Проєкт реалізує надійний шар зберігання даних (persistence layer) з використанням:
- **SQLite** та **Python DB-API** (параметризовані запити).
- **SQLAlchemy ORM** (моделі `Client`, `Account`, `Transaction`).
- **Repository Pattern** для відокремлення бізнес-логіки від БД.
- **Транзакцій** (`transfer_money`) із підтримкою `commit` та `rollback` (принципи ACID).
- **Alembic** для міграцій бази даних (додавання поля `account_type`).
- **Pytest** для integration-тестування (in-memory база).

## Структура проєкту
```text
lab7/
├── migrations/      # Міграції Alembic
├── src/bank_app/    # Основний код (database, models, repositories, services)
├── tests/           # Integration тести
└── pyproject.toml