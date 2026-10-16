import os
import sqlite3
from flask import g

DB_PATH = os.path.join(os.path.dirname(__file__), "restaurantos.db")

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def init_db():
    # A chamada repetida é segura: CREATE TABLE IF NOT EXISTS não apaga dados.
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.executescript("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL DEFAULT 'Geral',
            stock INTEGER NOT NULL DEFAULT 0,
            min_stock INTEGER NOT NULL DEFAULT 5,
            price REAL NOT NULL DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            total REAL NOT NULL DEFAULT 0,
            status TEXT NOT NULL DEFAULT 'Recebido',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)
    if db.execute("SELECT COUNT(*) FROM products").fetchone()[0] == 0:
        db.executemany(
            "INSERT INTO products (name, category, stock, min_stock, price) VALUES (?, ?, ?, ?, ?)",
            [
                ("Queijo muçarela", "Laticínios", 8, 10, 32.90),
                ("Molho de tomate", "Mercearia", 22, 8, 8.50),
                ("Farinha de trigo", "Mercearia", 16, 10, 6.90),
                ("Refrigerante lata", "Bebidas", 36, 12, 5.50),
                ("Calabresa", "Frios", 5, 8, 24.90),
            ]
        )
    if db.execute("SELECT COUNT(*) FROM orders").fetchone()[0] == 0:
        db.executemany(
            "INSERT INTO orders (table_name, item_name, total, status) VALUES (?, ?, ?, ?)",
            [
                ("Mesa 04", "Pizza calabresa", 49.90, "Em preparo"),
                ("Mesa 02", "Pizza marguerita", 45.90, "Recebido"),
                ("Delivery", "Pizza frango com catupiry", 54.90, "Concluído"),
                ("Mesa 07", "Pizza portuguesa", 52.90, "Recebido"),
            ]
        )
    db.commit()
    db.close()
