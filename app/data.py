# app/data.py
import sqlite3
import pandas as pd
import os

DB_PATH = "data/history.db"

def _ensure_table():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            amount REAL,
            price REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")

def record_transaction(tx_type, amount, price):
    _ensure_table()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO transactions (type, amount, price) VALUES (?, ?, ?)",
            (tx_type, amount, price),
        )

def get_transaction_history():
    _ensure_table()
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query("SELECT * FROM transactions ORDER BY timestamp DESC", conn)
