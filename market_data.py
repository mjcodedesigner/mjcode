import yfinance as yf
import pandas as pd

def get_market_data(ticker: str, period: str = "60d", interval: str = "1h") -> pd.DataFrame:
    """
    Fetches historical market data for a given ticker.

    Args:
        ticker: The stock or crypto ticker symbol (e.g., 'AAPL', 'BTC-USD').
        period: The time period to fetch data for.
        interval: The frequency of the data.

    Returns:
        A pandas DataFrame containing the historical data.
    """
    try:
        data = yf.download(ticker, period=period, interval=interval, progress=False)
        if data.empty:
            print(f"Warning: No data found for ticker {ticker}")
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Test run
    test_ticker = "AAPL"
    df = get_market_data(test_ticker)
    if not df.empty:
        print(f"Successfully fetched data for {test_ticker}")
        print(df.head())
    else:
        print(f"Failed to fetch data for {test_ticker}")
