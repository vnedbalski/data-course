import duckdb

con = duckdb.connect("shop.duckdb")

con.sql("DROP TABLE IF EXISTS orders")
con.sql("DROP TABLE IF EXISTS clients")

con.sql("""
CREATE TABLE clients (
    id INTEGER,
    name VARCHAR,
    city VARCHAR
)
""")
con.sql("""
INSERT INTO clients VALUES
    (1, 'Anna',  'Warsaw'),
    (2, 'Piotr', 'Gdansk'),
    (3, 'Olga',  'Warsaw'),
    (4, 'Marek', 'Krakow'),
    (5, 'Ivan',  'Gdansk')
""")

con.sql("""
CREATE TABLE orders (
    id INTEGER,
    client_id INTEGER,
    amount DECIMAL(10, 2),
    created_at DATE
)
""")
con.sql("""
INSERT INTO orders VALUES
    (101, 1, 250.00, '2026-10-01'),
    (102, 1,  80.00, '2026-10-03'),
    (103, 2, 120.00, '2026-10-04'),
    (104, 3,  45.50, '2026-10-05'),
    (105, 3, 310.00, '2026-10-07'),
    (106, 2,  99.99, '2026-10-08'),
    (107, 1, 150.00, '2026-10-10'),
    (108, 5,  60.00, '2026-10-11')
""")

con.sql("SELECT * FROM clients").show()
con.sql("SELECT * FROM orders").show()
print("Готово: база shop.duckdb создана")