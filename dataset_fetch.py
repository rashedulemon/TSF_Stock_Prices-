import datetime
import yfinance as yf
start_date = datetime.datetime(2022, 10, 1)
end_date = datetime.datetime(2025, 9, 1)
meta = yf.Ticker("AAPL")
data = meta.history(start=start_date, end=end_date)
print(data.to_string())