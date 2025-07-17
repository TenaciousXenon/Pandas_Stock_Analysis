"""
Title: *"Volatility and Risk Analysis of Tech Stocks (2020-2023)"*

Tips:
Handle missing data (e.g., data.ffill() for forward-filling stock prices on holidays).
Calculate daily returns (data['Close'].pct_change()) and rolling volatility (.rolling(30).std()).
Use multi-index DataFrames for comparing stocks.

Tasks to Perform:
Data Cleaning, Calculations, Visualization, Advanced
"""
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download stock data
data = yf.download(["AAPL", "MSFT", "GOOGL", "AMZN"], start="2020-01-01", end="2023-12-31")

# Data Cleaning:
# Forward-fill missing values (e.g., for holidays)
data = data.ffill()

# Drop columns with >5% missing values if any remain
null_counts = data.isnull().sum()
threshold = len(data) * 0.05
data = data.dropna(axis=1, thresh=threshold)

# Prepare DataFrame for analysis
df = data['Close'].copy()  # We only need Close prices for this analysis
df = pd.DataFrame(df.stack()).reset_index()
df.columns = ['Date', 'Stock', 'Close']

# Normalize stock prices to a baseline of 100
df['Normalized'] = df.groupby('Stock')['Close'].transform(
    lambda x: 100 * x / x.iloc[0]  # Start each stock at 100
)

# Calculate daily log returns
df['Log_Return'] = df.groupby('Stock')['Close'].apply(
    lambda x: np.log(x / x.shift(1))
)
# Compute annualized volatility for each stock
volatility = df.groupby('Stock')['Log_Return'].std() * np.sqrt(252)
volatility.name = 'Annualized_Volatility'

# Calculate correlation matrix between stocks
returns_pivot = df.pivot(index='Date', columns='Stock', values='Log_Return')
correlation_matrix = returns_pivot.corr()

# Identify the worst single-day drop for each stock
worst_drops = df.loc[df.groupby('Stock')['Log_Return'].idxmin()]

# Plot cumulative returns for all stocks
plt.figure(figsize=(12, 6))
df.pivot(index='Date', columns='Stock', values='Normalized').plot()
plt.title("Normalized Price Performance (Base = 100)")
plt.ylabel("Normalized Price")
plt.grid(True)
plt.show()

# Risk quartile analysis
df = df.merge(volatility, left_on='Stock', right_index=True)

# Bin stocks into quartiles based on volatility
df['Risk_Quartile'] = pd.qcut(
    df['Annualized_Volatility'], 
    q=4, 
    labels=['Q1 (Lowest Risk)', 'Q2', 'Q3', 'Q4 (Highest Risk)']
)

# Backtest equal-weight portfolio by quartile
portfolio_returns = pd.DataFrame()
for quartile in df['Risk_Quartile'].unique():
    stocks = df[df['Risk_Quartile'] == quartile]['Stock'].unique()
    quartile_returns = returns_pivot[stocks].mean(axis=1) / len(df['Risk_Quartile'].unique())
    portfolio_returns[quartile] = quartile_returns

# Calculate cumulative returns
cumulative_returns = (1 + portfolio_returns).cumprod()

# Plot quartile performance
plt.figure(figsize=(12, 6))
cumulative_returns.plot()
plt.title("Equal-Weight Portfolio Performance by Risk Quartile")
plt.ylabel("Cumulative Returns")
plt.grid(True)
plt.show()

# Print key metrics
print("\nAnnualized Volatility by Stock:")
print(volatility)
print("\nCorrelation Matrix:")
print(correlation_matrix)
print("\nWorst Daily Drops:")
print(worst_drops[['Stock', 'Date', 'Log_Return']])