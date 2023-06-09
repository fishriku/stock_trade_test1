import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title("Stock Data App")

# 株価コードを入力
stock_code = st.text_input("Enter the stock code: ")  # 例: '9613.T' for NTT Data
interval = st.selectbox("Enter the interval:", ('1d', '1wk', '1mo'))  # '1d', '1wk', or '1mo'

# 開始日と終了日を入力
start_date = st.date_input("Enter the start date")
end_date = st.date_input("Enter the end date")

# データを取得
if st.button('Get Data'):
    with st.spinner('Downloading data...'):
        data = yf.download(stock_code, start=start_date, end=end_date, interval=interval)
    st.success('Downloaded data!')

    # データのプロット
    st.write(f'Closing price of {stock_code} with {interval} interval')
    st.line_chart(data['Close'])
