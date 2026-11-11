from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent          # папка, где лежит этот скрипт

df = pd.read_csv(HERE / "books.csv")  # / склеивает части пути

# print(df.shape)
# print(df.info())

top = df.sort_values("price", ascending=False)
top = top.head(5)

# print(top[["title", "price"]])

# print(df.sort_values("price", ascending=False).head(5)[["title", "price"]])

cheap_top = df[(df["price"] < 20) & (df["rating"] == 5)]

# print(cheap_top.shape[0])

avg_price_by_rating = df.groupby("rating")["price"].mean().round(2)


# print(df["rating"].value_counts().sort_index())

# print(df["url"].is_unique)
# print(df[df["title"].duplicated(keep=False)])

print(df["availability"].value_counts())

df.to_parquet(HERE / "books.parquet", index=False)

