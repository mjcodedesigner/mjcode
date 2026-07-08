import sys
from market_data import get_market_data
from indicators import add_indicators
from sentiment import get_sentiment
from engine import generate_recommendation

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <TICKER>")
        print("Example: python3 main.py AAPL")
        return

    ticker = sys.argv[1].upper()
    print(f"Fetching data and analyzing {ticker}...")

    # 1. Get Market Data
    df = get_market_data(ticker)
    if df.empty:
        print(f"Error: Could not retrieve data for {ticker}. Please check the symbol.")
        return

    # 2. Add Technical Indicators
    df = add_indicators(df)

    # 3. Get News Sentiment
    sentiment = get_sentiment(ticker)

    # 4. Generate Recommendation
    result = generate_recommendation(df, sentiment)

    # 5. Output Results
    print("\n" + "="*40)
    print(f" TRADING PREDICTION FOR {ticker}")
    print("="*40)
    print(f"Current Price:  ${result['ticker_price']:,.2f}")
    print(f"Recommendation: {result['recommendation']}")
    print(f"Confidence Score: {result['score']} (Scale: -5 to +5)")
    print("-" * 40)
    print(f"Technical Analysis:")
    print(f"  - RSI: {result['rsi']:.2f}")
    print(f"  - News Sentiment: {result['sentiment']:.2f}")
    print("\nKey Factors:")
    for reason in result['reasons']:
        print(f"  - {reason}")
    print("-" * 40)
    print(f"\n{result['disclaimer']}")
    print("="*40)

if __name__ == "__main__":
    main()
