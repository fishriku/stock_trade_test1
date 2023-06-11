import yfinance as yf
import matplotlib.pyplot as plt

# 株価コードを入力
stock_code = input("Enter the stock code: ")  # 例: '9613.T' for NTT Data
interval = input("Enter the interval (1d, 1wk, 1mo): ")  # '1d', '1wk', or '1mo'

# 開始日と終了日を入力
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# データを取得
data = yf.download(stock_code, start=start_date, end=end_date, interval=interval)

# データのプロット
plt.figure(figsize=(14, 7))
plt.plot(data.Close)
plt.title('Closing price of ' + stock_code + ' with ' + interval + ' interval')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid()
plt.show()

