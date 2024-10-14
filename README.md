# StockPredict Proposal

# Member: Juling Fan, Ying-Yun Wang, Shangwei Liu, Ruyue Xiao, Junting Lyu

# Goal: 
Our goal is to develop a robust and accurate model for predicting the next day's stock price using historical data. This overarching goal encompasses several specific, measurable, achievable, relevant, and time-bound (SMART) objectives that will guide our project's development and evaluation. In terms of data collection and preprocessing, we aim to gather comprehensive historical stock price data from the past year using Google Finance and Nasdaq. We will develop and implement data preprocessing techniques to handle missing values, remove outliers, and ensure data consistency.

# Data Collection: 
We will gather historical stock price data of the past 1 year by scraping websites from Google Finance and Nasdaq: 
Besides, we will preprocess it by handling missing values, removing outliers, and ensuring consistency in the format. This will improve the accuracy and reliability of our analysis.

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

