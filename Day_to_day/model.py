from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Build the LSTM model
def getLSTM(input_shape):
    model = Sequential([
        LSTM(units=50, input_shape=input_shape),
        Dense(units=1)
    ])
    return model