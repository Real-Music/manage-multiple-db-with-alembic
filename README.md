# manage-multiple-db-with-alembic

How to manage multiple database with alembic

- Have a look at .env.example
- Look at alembic.ini configuration
- Look at config.py
- Look at env.py in both `my_db_one` and `my_db_two`

## create migration for db one

```bash
alembic --name one revision --autogenerate
```

```bash
alembic --name one upgrade head
```

## create migration for db two

```bash
alembic --name two revision --autogenerate
```

```bash
alembic --name two upgrade head
```
