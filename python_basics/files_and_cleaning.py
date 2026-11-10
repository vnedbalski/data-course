# Day 2: reading files, handling errors, removing duplicates
import csv


def read_prices(path):
    prices = []
    try:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    prices.append(float(row["price"]))
                except ValueError:
                    print(f"Skipping row: {row}")
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    return prices


def keep_latest(rows):
    latest = {}
    for row in rows:
        row_id = row["id"]
        if row_id not in latest:
            latest[row_id] = row
        elif row["date"] > latest[row_id]["date"]:
            latest[row_id] = row
    return list(latest.values())


rows = [
    {"id": 1, "date": "2026-10-01", "status": "new"},
    {"id": 2, "date": "2026-10-03", "status": "new"},
    {"id": 1, "date": "2026-10-05", "status": "done"},
]

rows2 = [
    {"id": 1, "date": "2026-10-05", "status": "done"},
    {"id": 2, "date": "2026-10-03", "status": "new"},
    {"id": 1, "date": "2026-10-01", "status": "new"},
]

print(read_prices("prices.csv"))   # [5.5, 4.0, 7.2]
print(read_prices("nope.csv"))     # []
print(keep_latest(rows))           # id 1 -> done
print(keep_latest(rows2))          # id 1 -> done