import pandas as pd
import pandas_ta as ta

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds technical indicators to the DataFrame.

    Args:
        df: A pandas DataFrame with OHLCV data.

    Returns:
        The DataFrame with added indicators.
    """
    if df.empty:
        return df

    # Ensure we are working with the correct column names for pandas_ta
    # yfinance often returns multi-index columns if only one ticker is fetched
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # RSI
    df['RSI'] = ta.rsi(df['Close'], length=14)

    # MACD
    macd = ta.macd(df['Close'])
    if macd is not None:
        df = pd.concat([df, macd], axis=1)

    # EMA
    df['EMA_20'] = ta.ema(df['Close'], length=20)
    df['EMA_50'] = ta.ema(df['Close'], length=50)

    return df

if __name__ == "__main__":
    from market_data import get_market_data
    test_ticker = "AAPL"
    df = get_market_data(test_ticker)
    if not df.empty:
        df = add_indicators(df)
        print(f"Indicators added for {test_ticker}")
        print(df.tail())
    else:
        print(f"Failed to fetch data for {test_ticker}")
