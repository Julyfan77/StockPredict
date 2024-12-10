# StockPredict Final Report

# Member: Juling Fan, Ying-Yun Wang, Shangwei Liu, Ruyue Xiao, Junting Lyu

# Makefile Explanation

The repository is organized into two main folders, each containing a Makefile to handle tasks specific to that part of the project to ensure tasks remain independent and easy to execute. 


### **1. Day_to_day: Prediction Pipeline**  
The **`Day_to_day`** folder contains the code for predicting next-day stock prices using LSTM models. This includes:  
- **Data preprocessing**  
- **Model training**  
- **Prediction generation**  

**Usage**:  
To execute the pipeline, navigate to the `Day_to_day` folder and run:  
```bash
cd Day_to_day
make install    # Install dependencies
make run        # Run the prediction pipeline
make test       # Run tests
```

---

### **2. StockPredict_Website: Visualization Web Application**  
The **`StockPredict_Website`** folder contains the **Flask-based web application** for visualizing prediction results. It displays:  
- **Line plots** for actual vs predicted stock prices  
- **Residual plots** to highlight prediction errors  
- **Accuracy rates** (MAPE) for each stock  

**Usage**:  
To start the web application, navigate to the `StockPredict_Website` folder and run:  
```bash
cd StockPredict_Website
make install    # Install dependencies
make run        # Start the Flask server
make test       # Run tests
```

Once the server starts, access the application by visiting:  
```
http://127.0.0.1:5000
```

---

# Goal: 
Our goal is to develop a robust and accurate model for predicting the next day's stock price using historical data. This overarching goal encompasses several specific, measurable, achievable, relevant, and time-bound (SMART) objectives that will guide our project's development and evaluation. In terms of data collection and preprocessing, we aim to gather comprehensive historical stock price data from the past year using Google Finance and Nasdaq. We will develop and implement data preprocessing techniques to handle missing values, remove outliers, and ensure data consistency.



# Data Preprocessing: 
The data processing pipeline begins with downloading historical stock data for different companies from Yahoo Finance, covering the period from January 1, 2020, to January 1, 2024. Using the yfinance library, we retrieve daily price data and select only the 'Date,' 'Close,' and 'Open' columns, which are saved into different CSV files for easy access and storage. Next, to prepare the data for machine learning, we apply Min-Max scaling using the minmaxProcess function. This function normalizes the 'Close' and 'Open' prices independently, scaling each to a range of 0 to 1, ensuring consistency and reducing bias in the model. The scaling process uses MinMaxScaler, which transforms the data and stores the scaling parameters for potential inverse scaling if we need to revert predictions back to the original price range.

After normalization, we structure the data for time series analysis. The create_sequences function generates sequences of a specified length (e.g., 60 days) from the closing prices to form input sequences suitable for time series models like LSTMs. Each sequence comprises 60 consecutive days of closing prices, and the target label is the price on the following day. This process creates two arrays: sequences and labels, where each sequence aligns with its corresponding next-day target value. Finally, the getdata function orchestrates the entire process, reading the CSV data, setting 'Date' as the index, and parsing it as a date. This function calls minmaxProcess for normalization and uses create_sequences to generate the input (X) and output (y) arrays. The X array is reshaped to meet the input format expected by LSTM models, with dimensions (samples, timesteps, features), and y represents the labels for each sequence. The final output includes X, y, and the scaler object, which retains the scaling parameters, facilitating the inverse transformation of predictions back to the original scale.


# Model Training and Result Analysis

We applied **LSTM (Long Short-Term Memory)** models to predict the next day's closing stock price for several companies, including **Amazon, Nvidia**, and **Visa**. The dataset was split into two parts:  

- **80% for training**  
- **20% for testing**  

---

### **Training Process**  

#### **Epoch Adjustment**  
- We gradually increased the number of training epochs to observe the model's performance and convergence.  
- Early stopping was applied with a **patience setting** using the TensorFlow framework to prevent overfitting.  

#### **Evaluation Metric**  
- We used **MAPE (Mean Absolute Percentage Error)** to evaluate the accuracy of the predictions on both training and test sets.  

---

### **Observations**  

- **Amazon**:  
  - The model achieved high accuracy with a **test MAPE of 1.52%** and an **accuracy rate of 98.48%**, indicating that the predictions align closely with the actual stock prices.  
  - The lower fluctuation in test data likely contributed to this strong performance.  

- **Visa**:  
  - The model performed exceptionally well with a **test MAPE of 0.83%** and an **accuracy rate of 99.17%**, the highest among all stocks.  
  - Visa's stable and consistent data trends made it easier for the model to generalize effectively.  

- **Nvidia**:  
  - The model achieved a **test MAPE of 3.07%** and an **accuracy rate of 96.93%**, slightly lower than the other stocks due to Nvidia's strong upward trend during the test period.  
  - This trend posed a challenge for the model, as such dynamic patterns are harder to generalize accurately.  

---

### **Results**  

| **Stock**   | **Train MAPE (%)** | **Test MAPE (%)** | **Accuracy Rate (%)** | **Observations**                               |  
|-------------|-------------------|------------------|-----------------------|------------------------------------------------|  
| **Amazon**  | 1.6%              | **1.52%**        | **98.48%**            | High accuracy; predictions align closely.      |  
| **Nvidia**  | 2.9%              | **3.07%**        | **96.93%**            | Slightly higher error due to upward trends.    |  
| **Visa**    | 0.9%              | **0.83%**        | **99.17%**            | Best accuracy; stable and consistent trends.   |  

<img width="676" alt="Screenshot 2024-12-09 at 10 03 12 PM" src="https://github.com/user-attachments/assets/219c7eb5-b517-4c21-a17c-18b6a4e3b20a">
<img width="675" alt="Screenshot 2024-12-09 at 10 02 57 PM" src="https://github.com/user-attachments/assets/2e2c5988-7080-403a-a820-ae1ddf2f2367">
<img width="683" alt="Screenshot 2024-12-09 at 10 02 45 PM" src="https://github.com/user-attachments/assets/10198476-38f1-4d6d-8406-6003dabf7c46">


# Visualization

In the visualization phase of our project, we provide an interactive platform to analyze the model's performance comprehensively.  

### **Features**  

1. **Line Plots**:  
   - Line plots compare actual vs predicted stock prices, allowing users to observe how closely the model’s predictions align with real stock price trends over time.  

2. **Residual Plots**:  
   - Residual plots highlight the differences (residuals) between actual and predicted prices. These plots enable us to assess the model's consistency, identify biases, and pinpoint areas for improvement.  

3. **Accuracy Display**:  
   - The Mean Absolute Percentage Error (MAPE) is calculated and displayed as an accuracy rate below each chart, providing a quick and clear summary of the model’s reliability for each stock.  

4. **Zoom and Pan**:  
   - The platform supports zooming and panning functionalities, allowing users to drill down into daily price details and reset the graph view when needed.  

---

You can directly access the website at: [https://stock-predict-website.vercel.app/](https://stock-predict-website.vercel.app/). Alternatively, you can run the project locally by cloning the package from GitHub. To run it locally, use the following commands:

```bash
 - cd ./StockPredict_Website
 - make install
 - make run

```
then the website should be available locally at http://127.0.0.1:5000.

These visual tools collectively offer a clear and detailed view of our model's performance, helping us evaluate its effectiveness, identify discrepancies, and guide further improvements. The inclusion of residual plots, zooming capabilities, and accuracy displays ensures a comprehensive and interactive user experience.




