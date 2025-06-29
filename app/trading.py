import streamlit as st
import sqlite3
import datetime
import pandas as pd
from app.nosyapi_client import get_gold_price

DB_PATH = "data/history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            price REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_current_price():
    return get_gold_price()

def save_transaction(tx_type, amount, price):
    timestamp = datetime.datetime.now().isoformat()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO trades (type, amount, price, timestamp) VALUES (?, ?, ?, ?)",
        (tx_type, amount, price, timestamp)
    )
    conn.commit()
    conn.close()

def get_transaction_history():
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query("SELECT * FROM trades ORDER BY timestamp DESC", conn)
    finally:
        conn.close()
    return df

def run_trading_interface():
    st.header("📊 Portföy İşlemi (Simülasyon)")

    init_db()
    tx_type = st.selectbox("İşlem türü", ["Al", "Sat"])
    amount = st.number_input("Miktar (gram)", min_value=0.01, step=0.01)

    if st.button("İşlemi Kaydet"):
        current_price = get_current_price()
        save_transaction(tx_type, amount, current_price)
        st.success(f"✅ {tx_type} işlemi kaydedildi ({amount} gram, {current_price} TL)")

    st.subheader("📜 Geçmiş İşlemler")
    df = get_transaction_history()
    if df is not None and not df.empty:
        st.dataframe(df)
    else:
        st.info("Henüz işlem yapılmamış.")


# import streamlit as st
# import sqlite3
# import datetime
# import pandas as pd  # <-- eksikti

# DB_PATH = "data/history.db"

# def init_db():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS trades (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             type TEXT NOT NULL,
#             amount REAL NOT NULL,
#             price REAL NOT NULL,
#             timestamp TEXT NOT NULL
#         )
#     """)
#     conn.commit()
#     conn.close()

# def get_current_price():
#     # Gerçek zamanlı değil, örnek fiyat
#     return 2450.0

# def save_transaction(tx_type, amount, price):
#     timestamp = datetime.datetime.now().isoformat()
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO trades (type, amount, price, timestamp) VALUES (?, ?, ?, ?)",
#         (tx_type, amount, price, timestamp)
#     )
#     conn.commit()
#     conn.close()

# def get_transaction_history():
#     conn = sqlite3.connect(DB_PATH)
#     try:
#         df = st.session_state.get("df_cache")
#         if df is None:
#             df = pd.read_sql_query("SELECT * FROM trades ORDER BY timestamp DESC", conn)
#             st.session_state["df_cache"] = df
#     except:
#         df = pd.read_sql_query("SELECT * FROM trades ORDER BY timestamp DESC", conn)
#     conn.close()
#     return df

# def run_trading_interface():
#     st.header("📊 Portföy İşlemi (Simülasyon)")

#     init_db()
#     tx_type = st.selectbox("İşlem türü", ["Al", "Sat"])
#     amount = st.number_input("Miktar (gram)", min_value=0.01, step=0.01)

#     if st.button("İşlemi Kaydet"):
#         current_price = get_current_price()
#         save_transaction(tx_type, amount, current_price)
#         st.success(f"✅ {tx_type} işlemi kaydedildi ({amount} gram, {current_price} TL)")

#         # Refresh cache
#         if "df_cache" in st.session_state:
#             del st.session_state["df_cache"]

#     st.subheader("📜 Geçmiş İşlemler")
#     df = get_transaction_history()
#     if df is not None and not df.empty:
#         st.dataframe(df)
#     else:
#         st.info("Henüz işlem yapılmamış.")
