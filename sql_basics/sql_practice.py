# Days 2-3: SQL basics with DuckDB
# Run setup_shop.py first to create shop.duckdb
import duckdb

con = duckdb.connect("shop.duckdb")


def q(title, sql):
    print(title)
    con.sql(sql).show()


# ---------- Lesson 1: SELECT, WHERE, ORDER BY, LIMIT ----------

q("S1. Names and cities of all clients", """
SELECT name, city
FROM clients
""")

q("S2. Clients from Gdansk", """
SELECT name
FROM clients
WHERE city = 'Gdansk'
""")

q("S3. Orders of client 1", """
SELECT id, client_id, amount
FROM orders
WHERE client_id = 1
""")

q("S4. Orders under 100, cheapest first", """
SELECT id, client_id, amount
FROM orders
WHERE amount < 100
ORDER BY amount
""")

q("S5. Top 3 most expensive orders", """
SELECT id, client_id, amount
FROM orders
ORDER BY amount DESC
LIMIT 3
""")

q("S6. Orders of clients 1 or 3 over 100", """
SELECT id, client_id, amount
FROM orders
WHERE client_id IN (1, 3) AND amount > 100
""")

# ---------- Lesson 2: aggregates and GROUP BY ----------

q("G1. Total number of orders", """
SELECT COUNT(*) AS orders_count
FROM orders
""")

q("G2. Total amount and average order", """
SELECT SUM(amount) AS total, ROUND(AVG(amount), 2) AS avg_amount
FROM orders
""")

q("G3. Orders count and total per client", """
SELECT client_id, COUNT(*) AS orders_count, SUM(amount) AS total_amount
FROM orders
GROUP BY client_id
""")

q("G4. Same as G3, richest client first", """
SELECT client_id, COUNT(*) AS orders_count, SUM(amount) AS total_amount
FROM orders
GROUP BY client_id
ORDER BY total_amount DESC
""")

q("G5. Clients with total over 200", """
SELECT client_id, SUM(amount) AS total
FROM orders
GROUP BY client_id
HAVING SUM(amount) > 200
""")

q("G6. Number of clients per city", """
SELECT city, COUNT(city) AS clients_count
FROM clients
GROUP BY city
""")

# ---------- Lesson 3: JOIN ----------

q("J1. Every order with client name", """
SELECT o.id, c.name, o.amount
FROM orders AS o
JOIN clients AS c ON o.client_id = c.id
""")

q("J2. Orders of clients from Warsaw", """
SELECT o.id, c.name, o.amount, c.city
FROM orders AS o
JOIN clients AS c ON o.client_id = c.id
WHERE c.city = 'Warsaw'
""")

q("J3. Orders count and total per city (INNER JOIN, Krakow is missing)", """
SELECT c.city, COUNT(*) AS orders_count, SUM(o.amount) AS total
FROM orders AS o
JOIN clients AS c ON o.client_id = c.id
GROUP BY c.city
""")

q("J4. Total per client name", """
SELECT c.name, SUM(o.amount) AS total
FROM clients AS c
JOIN orders AS o ON o.client_id = c.id
GROUP BY c.id, c.name
ORDER BY total DESC
""")

# ---------- Lesson 4: LEFT JOIN and NULL ----------

q("L1. Clients without orders (anti-join)", """
SELECT c.name
FROM clients AS c
LEFT JOIN orders AS o ON o.client_id = c.id
WHERE o.client_id IS NULL
""")

q("L2. All clients with orders count, including 0", """
SELECT c.name, COUNT(o.id) AS orders_count
FROM clients AS c
LEFT JOIN orders AS o ON o.client_id = c.id
GROUP BY c.id, c.name
""")

q("L3. All cities with orders count and total, including Krakow", """
SELECT c.city, COUNT(o.client_id) AS orders_count, COALESCE(SUM(o.amount), 0) AS total
FROM clients AS c
LEFT JOIN orders AS o ON o.client_id = c.id
GROUP BY c.city
""")