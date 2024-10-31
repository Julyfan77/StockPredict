import pandas as pd
from data_preprocess import create_sequences,getdata
from sklearn.preprocessing import MinMaxScaler
from model import getLSTM

def train(X,y,model):
    
    # Train the model
    model.fit(X, y, epochs=100, batch_size=32)

    # Evaluate the model
    train_loss = model.evaluate(X, y, verbose=0)
    #test_loss = model.evaluate(X_test, y_test, verbose=0)
    print(f'Train Loss: {train_loss:.6f}')
    return model
    #print(f'Test Loss: {test_loss:.6f}')
def test(X,y,model):
    test_loss = model.evaluate(X_test, y_test, verbose=0)
    test_loss = model.evaluate(X_test, y_test, verbose=0)
    print(f'Test Loss: {test_loss:.6f}')
    
    
if __name__ == "__main__":
    X,y,scaler=getdata('./yfinance_2020-2024_day.csv')
    # Split the data into training and testing sets
    train_size = int(len(X) * 0.8)
    X_train, y_train = X[:train_size],y[:train_size]
    X_test, y_test = X[train_size:],y[train_size:]
    model=getLSTM((X_train.shape[1], X_train.shape[2]))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model=train(X_train,y_train,model)
    test(X_test,y_test,model)
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)
    
    # Denormalize the predictions
    train_predictions = scaler.inverse_transform(train_predictions)
    y_train_unscaled = scaler.inverse_transform(y_train)
    test_predictions = scaler.inverse_transform(test_predictions)
    y_test_unscaled = scaler.inverse_transform(y_test)
    print(y-y_test)