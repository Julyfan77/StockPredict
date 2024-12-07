import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

ticker = "V" 
interval = "1h"  # Hourly data
start_date = "2022-12-09"
end_date = "2024-12-07"
data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

df = pd.DataFrame(data)

df.reset_index(inplace=True)
df = df[['Datetime', 'Close', 'Open']]
df.to_csv('./yfinance_2022_2024_hourly_visa.csv', index=False)

