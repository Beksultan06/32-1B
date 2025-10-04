import sqlite3

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    price REAL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors(id)    
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales(
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(book_id) REFERENCES Books(id)        
)
""")


cursor.executemany("INSERT OR IGNORE INTO Authors VALUES (?, ?)", [
    (1, "Толстой"),
    (2, "Достоевский"),
    (3, "Пушкин"),
])

cursor.executemany("INSERT OR IGNORE INTO Books VALUES (?, ?, ?, ?)", [
    (1, "Война и мир", 500, 1),
    (2, "Анна Каренина", 450, 1),
    (3, "Преступление и наказание", 300, 2),
    (4, "Идиот", 350, 2),
    (5, "Евгений Онегин", 200, 3),
])

cursor.executemany("INSERT OR IGNORE INTO Sales VALUES (?, ?, ?)", [
    (1, 1, 10),
    (2, 2, 5),
    (3, 3, 8),
    (4, 4, 4),
    (5, 5, 12),
])

conn.commit()

cursor.execute("""
SELECT author_id, COUNT(*) AS book_count
FROM Books
GROUP BY author_id
""")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
SELECT author_id, AVG(price) AS avg_price
FROM Books
GROUP BY author_id
""")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
SELECT name FROM Authors
WHERE id = (
    SELECT author_id
    FROM Books
    GROUP BY author_id
    ORDER BY AVG(price) DESC
    LIMIT 1
)
""")
print(cursor.fetchone()[0])

cursor.execute("DROP VIEW IF EXISTS SalesDetails")
cursor.execute("""
CREATE VIEW SalesDetails AS 
SELECT s.id AS sale_id, b.title AS book_title, a.name AS author_name,
       s.quantity,
       b.price
FROM Sales s
JOIN Books b ON s.book_id = .id
JOIN Authors a ON b.author_id = a.id
""")

cursor.execute("SELECT * FROM SalesDetails")
for row in cursor.fetchall():
    print(row)

conn.close()