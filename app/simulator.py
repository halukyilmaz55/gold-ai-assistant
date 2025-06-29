import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt

def run_simulation():
    st.header("🧪 Altın Alım Simülasyonu")
    days = st.slider("📅 Simülasyon süresi (gün)", min_value=7, max_value=180, value=30, step=1)
    monthly_investment = st.number_input("💸 Aylık yatırım tutarı (TL)", min_value=1000, value=10000, step=500)

    initial_price = 4200
    np.random.seed(42)
    daily_returns = np.random.normal(0, 0.012, days)
    prices = [initial_price]
    for r in daily_returns:
        prices.append(prices[-1] * (1 + r))

    dates = pd.date_range(end=dt.datetime.today(), periods=days+1)
    df = pd.DataFrame({'date': dates, 'price': prices})

    total_grams = 0
    portfolio_value = []
    grams_bought = []

    for i, row in df.iterrows():
        if i % 30 == 0:
            grams = monthly_investment / row['price']
            total_grams += grams
            grams_bought.append(grams)
        else:
            grams_bought.append(0)
        portfolio_value.append(total_grams * row['price'])

    df['portfolio_value'] = portfolio_value
    df['total_grams'] = np.cumsum(grams_bought)

    st.subheader("📈 Altın Fiyatı")
    st.line_chart(df.set_index("date")[["price"]])

    st.subheader("💼 Portföy Değeri")
    st.line_chart(df.set_index("date")[["portfolio_value"]])

    st.subheader("🥇 Toplam Alınan Altın (Gram)")
    st.line_chart(df.set_index("date")[["total_grams"]])


# import streamlit as st
# import numpy as np
# import pandas as pd
# import datetime as dt

# def run_simulation():
#     st.header("🧪 Altın Alım Simülasyonu")

#     days = st.slider("📅 Simülasyon süresi (gün)", min_value=7, max_value=180, value=30, step=1)
#     monthly_investment = st.number_input("💸 Aylık yatırım tutarı (TL)", min_value=1000, value=10000, step=500)

#     # Sahte fiyat serisi (NosyAPI geçmiş verisi entegrasyonu sonradan eklenecek)
#     initial_price = 4200
#     np.random.seed(42)
#     daily_returns = np.random.normal(0, 0.012, days)
#     prices = [initial_price]
#     for r in daily_returns:
#         prices.append(prices[-1] * (1 + r))

#     dates = pd.date_range(end=dt.datetime.today(), periods=days+1)
#     df = pd.DataFrame({'date': dates, 'price': prices})

#     total_grams = 0
#     portfolio_value = []
#     grams_bought = []

#     for i, row in df.iterrows():
#         if i % 30 == 0:
#             grams = monthly_investment / row['price']
#             total_grams += grams
#             grams_bought.append(grams)
#         else:
#             grams_bought.append(0)
#         portfolio_value.append(total_grams * row['price'])

#     df['portfolio_value'] = portfolio_value
#     df['total_grams'] = np.cumsum(grams_bought)

#     # Grafikler
#     st.subheader("📈 Altın Fiyatı (Simülasyon)")
#     st.line_chart(df.set_index("date")[["price"]])

#     st.subheader("💼 Portföy Değeri (TL)")
#     st.line_chart(df.set_index("date")[["portfolio_value"]])

#     st.subheader("🥇 Toplam Alınan Altın (Gram)")
#     st.line_chart(df.set_index("date")[["total_grams"]])
