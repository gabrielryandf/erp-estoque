import sqlite3

con = sqlite3.connect("estoque.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    unidade_medida TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade REAL NOT NULL
)
""")

con.commit()
