# Data Engineering Learning Path

This is my repo where I started to learn data engineering.

## What's inside

- `python_basics/` — simple functions I've written: loops, dictionaries, sorting, reading CSV files, error handling and removing duplicates.
- `sql_basics/` — SQL queries on a small shop database: filtering, aggregation, GROUP BY, JOIN and LEFT JOIN.

## Tools

Python 3.12, uv, DuckDB

## How to run

```bash
cd python_basics
uv run python basics.py
uv run python files_and_cleaning.py

cd ../sql_basics
uv run python setup_shop.py
uv run python sql_practice.py
```