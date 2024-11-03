# StockPredict Midterm Report

# Member: Juling Fan, Ying-Yun Wang, Shangwei Liu, Ruyue Xiao, Junting Lyu

# Goal: 
Our goal is to develop a robust and accurate model for predicting the next day's stock price using historical data. This overarching goal encompasses several specific, measurable, achievable, relevant, and time-bound (SMART) objectives that will guide our project's development and evaluation. In terms of data collection and preprocessing, we aim to gather comprehensive historical stock price data from the past year using Google Finance and Nasdaq. We will develop and implement data preprocessing techniques to handle missing values, remove outliers, and ensure data consistency.

# Data Preprocessing: 
The data processing pipeline begins with downloading historical stock data for different companies from Yahoo Finance, covering the period from January 1, 2020, to January 1, 2024. Using the yfinance library, we retrieve daily price data and select only the 'Date,' 'Close,' and 'Open' columns, which are saved into different CSV files for easy access and storage. Next, to prepare the data for machine learning, we apply Min-Max scaling using the minmaxProcess function. This function normalizes the 'Close' and 'Open' prices independently, scaling each to a range of 0 to 1, ensuring consistency and reducing bias in the model. The scaling process uses MinMaxScaler, which transforms the data and stores the scaling parameters for potential inverse scaling if we need to revert predictions back to the original price range.

After normalization, we structure the data for time series analysis. The create_sequences function generates sequences of a specified length (e.g., 60 days) from the closing prices to form input sequences suitable for time series models like LSTMs. Each sequence comprises 60 consecutive days of closing prices, and the target label is the price on the following day. This process creates two arrays: sequences and labels, where each sequence aligns with its corresponding next-day target value. Finally, the getdata function orchestrates the entire process, reading the CSV data, setting 'Date' as the index, and parsing it as a date. This function calls minmaxProcess for normalization and uses create_sequences to generate the input (X) and output (y) arrays. The X array is reshaped to meet the input format expected by LSTM models, with dimensions (samples, timesteps, features), and y represents the labels for each sequence. The final output includes X, y, and the scaler object, which retains the scaling parameters, facilitating the inverse transformation of predictions back to the original scale.

# Trainning Model:
We plan to use different deep learning models and some basic algorithms to predict the stock prices, including Dual Moving Average Crossover Strategy，LSTM and RNN.
Dual Moving Average Crossover Strategy is a simple yet popular strategy in technical analysis, which involves using two moving averages with different time periods (e.g., 50-day and 200-day moving averages). A buy signal is generated when the shorter moving average crosses above the longer one, indicating an uptrend. 
LSTM (Long Short-Term Memory) is a type of recurrent neural network (RNN) specifically designed to capture long-term dependencies in sequential data. It is widely used in time series forecasting, such as predicting stock prices, because it can learn patterns over time and retain relevant information over long sequences.
RNNs (Recurrent Neural Network) are a class of neural networks designed for sequential data, where the output from previous steps is fed as input to the current step. Hence, they are effective for tasks like time series analysis.


# Visualization:
We will mainly use line plots of Actual vs. Predicted Prices and Residual Plot to compare actual results to our model.

# Test plan: 
We will train on data collected over the past year, past three months, and past month, respectively, and test on data from November to determine the optimal time range for collecting prior data. We also plan to change the input when testing, like using the price of past 3 days or 1 day as the input.


# Potential Extensions: 
If we complete our primary objectives ahead of schedule, we may consider the following extensions:

- Expanding our prediction horizon to weekly or monthly forecasts.
- Incorporating additional data sources, such as sentiment analysis from financial news, to enhance prediction accuracy.

