### Stock Market Trading and Prediction Strategies
This project comprises two complementary approaches to aid in stock market trading and investment decisions. The first strategy is a rule-based alert system that leverages real-time exchange data, while the second strategy uses a machine learning model to predict stock prices based on historical trends and technical indicators. Both strategies are designed to provide users with actionable insights and automated alerts for informed decision-making.

## Project Overview
# 1. Rule-Based Strategy with Automated Alerts
This strategy uses real-time data from exchange APIs to identify trade signals. It monitors certain stock parameters, applies predefined trading rules, and sends email alerts when favorable conditions are detected. The strategy has been backtested and performs well under various market conditions.

Core File: main.py
Related Folders:
src: Contains helper scripts for data retrieval, processing, and rule application. These scripts are called by main.py.
data: Lists stock names and stores relevant data required for analysis.
This rule-based strategy allows users to stay updated on potential investment opportunities in real time without manual monitoring.

# 2. Machine Learning-Based Prediction Model
This model applies machine learning techniques to predict equity prices based on historical stock data and technical indicators. Leveraging a combination of past trends and quantitative indicators, this model aims to provide an estimate of future stock prices.

# Core Files:
Jupyter notebook located in the Prediction models folder.
The model uses a Long Short-Term Memory (LSTM) architecture for time series forecasting and Random forest in two seperate approach, trained on past data and technical indicators to learn patterns and generate predictions.

## Getting Started
Prerequisites
Python: Ensure you have Python 3.8+ installed.
Required Libraries: Install dependencies listed in requirements.txt.
Jupyter Notebook (for the Prediction Model): Required to run the machine learning model.
Installation
Clone the repository:

git clone https://github.com/bhartikaran96/stock_prices.git

# Install dependencies:
pip install -r requirements.txt

# Running the Project
Running the Rule-Based Strategy
Execute main.py to start monitoring stock parameters. Remember to do Google Auth to get keys and save it in .pickle file in data folder for email-alerts. Alerts will be automatically sent if trading conditions are met.

python main.py

Running the Prediction Model
Open the Jupyter notebook in the Prediction models folder and run each cell sequentially. The notebook loads historical data, applies technical indicators, and trains an LSTM or random forest model to forecast stock prices.

jupyter notebook
# Project Structure:

main.py: Entry point for the rule-based strategy.

src: Contains scripts for data extraction, processing, and rule evaluation.

data: Stores stock lists and pickle file containing api keys needs to be added.

Prediction models: Prediction Models/Jupyter notebook for the machine learning-based stock price prediction model.
