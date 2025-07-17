# Pandas Stock Analysis

This repository contains a learning project focused on mastering data analysis with Pandas and other Python libraries through the lens of stock market data.

## Project Overview

This project demonstrates how to download, clean, analyze, and visualize the volatility and risk of major tech stocks (AAPL, MSFT, GOOGL, AMZN) from 2020 to 2023. The analysis covers real-world financial data and introduces practical finance and data science concepts.

## Features

- **Data Acquisition:** Downloads historical stock price data using yfinance.
- **Data Cleaning:** Handles missing values and drops columns with excessive missing data.
- **Return & Volatility Analysis:** Calculates daily log returns and annualized volatility.
- **Correlation Analysis:** Computes correlations between stock returns.
- **Risk Analysis:** Assigns stocks to risk quartiles by volatility.
- **Portfolio Backtesting:** Simulates equal-weighted portfolios by risk quartile.
- **Visualization:** Plots normalized price performance and cumulative portfolio returns.
- **Key Metrics:** Outputs volatility, correlation matrix, and worst daily drops for each stock.

## Notebooks & Code

- **Project5.py:** Main script containing all analysis steps, from data download to visualization and metric reporting.

## Learning Goals

- Master Pandas data manipulation (grouping, pivoting, merging, etc.).
- Apply real-world data cleaning techniques.
- Calculate and interpret financial risk metrics.
- Practice advanced visualization with matplotlib.
- Gain experience with portfolio analysis concepts.

## Requirements

- Python
- pandas
- numpy
- yfinance
- matplotlib

### Install packages with:

```bash
pip install pandas numpy yfinance matplotlib
```

## Usage

- Run the main script:

```bash
python Project5.py
```

## License

- This project is for educational purposes and does not have a license.
