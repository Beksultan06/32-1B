


import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        stock INTEGER
    )
""")

def add_product(p):
    cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
    (p.id, p.name, p.price, p.stock))
    conn.commit()

def get_all_products():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()