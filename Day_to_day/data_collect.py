import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

# Download historical price data from Yahoo Finance
ticker = "V"  # Visa stock symbol
start_date = "2020-01-01"
end_date = "2024-01-01"
data = yf.download(ticker, start=start_date, end=end_date)
df = pd.DataFrame(data)

df.reset_index(inplace=True)
df = df[['Date', 'Close', 'Open']]
df.to_csv('./yfinance_2020-2024_day_visa.csv', index=False)


