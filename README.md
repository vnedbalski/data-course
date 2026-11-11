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

## scraping/

### Aim
To scrape book data from [books.toscrape.com](https://books.toscrape.com), a website made for scraping practice, clean it and save it as a dataset.

### Tools
requests, BeautifulSoup, pandas, csv, pathlib

### Results
- 1,000 books scraped from 50 pages (1-second pause between requests)
- Fields: url, title, price, availability, rating
- Saved as CSV (145 KB) and Parquet (about 2x smaller)

### Data quality findings
- Two different books have the same title, so the title can't be used as a unique ID. I used the book URL instead.
- The `availability` column is "In stock" for all 1,000 books, so it adds no information.
- Average price barely depends on rating (less than £1 difference between ratings 1 and 5).