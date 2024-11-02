import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
# def split(data):
    

def minmaxProcess(data):
    # Select closing prices
    scaler = MinMaxScaler(feature_range=(0, 1))
    # 选择 'Close' 列进行归一化
    close_prices = data[['Close']]  # 必须使用双重括号以保持二维输入
    open_prices = data[['Open']]
    data['Close'] = scaler.fit_transform(close_prices)
    data['Open'] = scaler.fit_transform(open_prices)
    return scaler
    
def create_sequences(data, sequence_length=60):
    sequences = []
    labels = []
    for i in range(sequence_length, len(data)):
        sequences.append(data[i-sequence_length:i, 0])  
        labels.append(data[i, 0])
    return np.array(sequences), np.array(labels)

def getdata(path):
    data = pd.read_csv(path, index_col='Date', parse_dates=True)

    # 选择 Close 列并进行归一化
    scaler=minmaxProcess(data)

    # 将 'Close' 列转换为 LSTM 格式
    close_data = data['Close'].values.reshape(-1, 1)
    sequence_length = 30  # 使用60天的窗口
    X, y = create_sequences(close_data, sequence_length)

    # 调整 X 的形状为 [samples, timesteps, features]
    X = X.reshape((X.shape[0], X.shape[1], 1))  # 每个时间步一个特征

    return X,y,scaler
# def getdata(path):
#     data = pd.read_csv(path, index_col='Date', parse_dates=True)
#
#     # Select 'Close' and split data into train and test sets
#     close_prices = data[['Close']].values  # Reshape required for scaler
#     train_size = int(len(close_prices) * 0.8)
#
#     # Fit scaler only on the training data
#     scaler = MinMaxScaler(feature_range=(0, 1))
#     close_prices_train = close_prices[:train_size]
#     close_prices_test = close_prices[train_size:]
#
#     # Scale training and test data
#     close_prices_train_scaled = scaler.fit_transform(close_prices_train)
#     close_prices_test_scaled = scaler.transform(close_prices_test)
#
#     # Prepare sequences for training and test data
#     sequence_length = 30
#     X_train, y_train = create_sequences(close_prices_train_scaled, sequence_length)
#     X_test, y_test = create_sequences(close_prices_test_scaled, sequence_length)
#
#     # Reshape inputs to [samples, timesteps, features]
#     X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
#     X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
#
#     return X_train, y_train, X_test, y_test, scaler

