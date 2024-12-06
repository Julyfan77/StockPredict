# StockPredict Midterm Report

# Member: Juling Fan, Ying-Yun Wang, Shangwei Liu, Ruyue Xiao, Junting Lyu

# Midterm Presentation video: 
https://youtu.be/WNl6Qo-JiLw

# Goal: 
Our goal is to develop a robust and accurate model for predicting the next day's stock price using historical data. This overarching goal encompasses several specific, measurable, achievable, relevant, and time-bound (SMART) objectives that will guide our project's development and evaluation. In terms of data collection and preprocessing, we aim to gather comprehensive historical stock price data from the past year using Google Finance and Nasdaq. We will develop and implement data preprocessing techniques to handle missing values, remove outliers, and ensure data consistency.

# Data Preprocessing: 
The data processing pipeline begins with downloading historical stock data for different companies from Yahoo Finance, covering the period from January 1, 2020, to January 1, 2024. Using the yfinance library, we retrieve daily price data and select only the 'Date,' 'Close,' and 'Open' columns, which are saved into different CSV files for easy access and storage. Next, to prepare the data for machine learning, we apply Min-Max scaling using the minmaxProcess function. This function normalizes the 'Close' and 'Open' prices independently, scaling each to a range of 0 to 1, ensuring consistency and reducing bias in the model. The scaling process uses MinMaxScaler, which transforms the data and stores the scaling parameters for potential inverse scaling if we need to revert predictions back to the original price range.

After normalization, we structure the data for time series analysis. The create_sequences function generates sequences of a specified length (e.g., 60 days) from the closing prices to form input sequences suitable for time series models like LSTMs. Each sequence comprises 60 consecutive days of closing prices, and the target label is the price on the following day. This process creates two arrays: sequences and labels, where each sequence aligns with its corresponding next-day target value. Finally, the getdata function orchestrates the entire process, reading the CSV data, setting 'Date' as the index, and parsing it as a date. This function calls minmaxProcess for normalization and uses create_sequences to generate the input (X) and output (y) arrays. The X array is reshaped to meet the input format expected by LSTM models, with dimensions (samples, timesteps, features), and y represents the labels for each sequence. The final output includes X, y, and the scaler object, which retains the scaling parameters, facilitating the inverse transformation of predictions back to the original scale.

# Model Training and Result Analysis:
We have applied LSTM to several stocks including Apple, Amazon, Nvidia and Visa. We trained the model with the first 80% of the data and tested it on the last 20% for each stock.
Upon training, we gradually increased the epoch count to observe how the model fit improves with longer training. To avoid excessive training and potential overfitting, we applied early stopping with a patience setting from tensorflow framework.
We also used MAPE(Mean Square Percentage Error) on both train set and test set to measure the overall accuracy of the prediction. For Apple, Amazon and visa, we have all achieved a test MAPE below 1% with epoch value in range 100-300, which indicates a decent result of prediction.
Also note that for these 3 stocks, the loss and MAPE value of the test set are lower than those of the train set. This is probably because that the test data has less fluctuation than the train data, thus is easier to predict.
As for Nvidia, which shows a strong rising trend in the test period compared to the other stocks, it gives a test MAPE of above 2.5% and a higher test loss than the train loss. This should be the expected result when the test data is harder to generalize compared to the other three.


# Visualization

In the visualization phase of our project, we will use line plots to compare actual vs. predicted prices, allowing us to observe how closely our model’s predictions align with real stock price trends over time. Alongside the line plots, a residual plot will illustrate the differences (residuals) between actual and predicted prices, enabling us to assess the model's consistency and identify any biases or areas for improvement. Additionally, we will display an accuracy rate below each chart, calculated using Mean Absolute Percentage Error (MAPE) and presented as a percentage, providing an immediate summary of the model’s overall reliability for each stock. These visual tools will collectively offer a comprehensive view of our model's performance, helping us evaluate its effectiveness, pinpoint discrepancies, and guide future enhancements.

You can directly access the website at: [https://stock-predict-website.vercel.app/](https://stock-predict-website.vercel.app/). Alternatively, you can run the project locally by cloning the package from GitHub. To run it locally, use the following commands:

```bash
 - cd ./StockPredict_Website
 - python app.py
```
then the website should be available locally at http://127.0.0.1:5000.


# Potential Extensions: 
Since our result showed a potential under-performance with more complex datasets, we considered several plans to improve its performance.

- Extracting data from a shorter time period with a higher frequency in order to avoid the information decay over time and focus more on short term trend.
- Perform cross-validation with a rolling window that shifts forward across the dataset to see if the performance is consistent across different time periods.
- Explore more datasets with different patterns to generalize the training process.
- Incorporating additional data sources, such as sentiment analysis from financial news, to enhance prediction accuracy.

