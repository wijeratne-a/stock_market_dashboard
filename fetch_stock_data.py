import yfinance as yf
import pandas as pd

def get_stock_data(ticker, start, end):
    """
    Fetch stock data for the given ticker symbol and date range.
    """
    stock = yf.download(ticker, start=start, end=end)
    return stock

if __name__ == "__main__":
    # Example: Fetch Apple stock data
    data = get_stock_data("AAPL", "2022-01-01", "2023-01-01")
    print(data.head())
