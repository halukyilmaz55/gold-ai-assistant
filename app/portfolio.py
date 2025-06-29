# app/portfolio.py
import sqlite3
import pandas as pd
from app.nosyapi_client import get_gold_price

DB_PATH = "data/history.db"
INITIAL_BALANCE = 100000  # TL
MONTHLY_TOPUP = 10000     # TL


def calculate_portfolio():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM trades ORDER BY timestamp", conn)
    conn.close()

    if df.empty:
        return {
            "current_balance": INITIAL_BALANCE,
            "total_grams": 0,
            "current_price": get_gold_price(),
            "portfolio_value": 0,
            "total_value": INITIAL_BALANCE,
            "profit": 0,
            "df": df
        }

    current_price = get_gold_price()
    balance = INITIAL_BALANCE
    total_grams = 0
    first_date = pd.to_datetime(df["timestamp"].iloc[0])

    # Her ay bir kere 10k TL ekle
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    latest_date = df["timestamp"].max()
    num_months = (latest_date.year - first_date.year) * 12 + (latest_date.month - first_date.month + 1)
    balance += num_months * MONTHLY_TOPUP

    for _, row in df.iterrows():
        if row["type"].lower() == "al":
            cost = row["amount"] * row["price"]
            balance -= cost
            total_grams += row["amount"]
        elif row["type"].lower() == "sat":
            income = row["amount"] * row["price"]
            balance += income
            total_grams -= row["amount"]

    portfolio_value = total_grams * current_price
    total_value = balance + portfolio_value
    invested = INITIAL_BALANCE + (num_months * MONTHLY_TOPUP)
    profit = total_value - invested

    return {
        "current_balance": balance,
        "total_grams": total_grams,
        "current_price": current_price,
        "portfolio_value": portfolio_value,
        "total_value": total_value,
        "profit": profit,
        "df": df
    }


def display_portfolio():
    st.header("📈 Portföy Durumu")
    result = calculate_portfolio()

    st.metric("💰 Mevcut Bakiye (TL)", f"{result['current_balance']:.2f}")
    st.metric("🥇 Toplam Altın (gram)", f"{result['total_grams']:.2f}")
    st.metric("📈 Güncel Altın Fiyatı", f"{result['current_price']:.2f} TL")
    st.metric("📊 Portföy Değeri (Altın)", f"{result['portfolio_value']:.2f} TL")
    st.metric("🧮 Toplam Varlık Değeri", f"{result['total_value']:.2f} TL")
    st.metric("📈 Kar/Zarar", f"{result['profit']:.2f} TL")

    with st.expander("📜 İşlem Geçmişi"):
        st.dataframe(result['df'])
