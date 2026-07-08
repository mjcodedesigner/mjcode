from market_data import get_market_data
from indicators import add_indicators
from sentiment import get_sentiment
from engine import generate_recommendation

def test_engine():
    ticker = "AAPL"
    df = get_market_data(ticker)
    df = add_indicators(df)
    sentiment = get_sentiment(ticker)
    result = generate_recommendation(df, sentiment)

    print(f"--- Prediction for {ticker} ---")
    print(f"Price: {result['ticker_price']:.2f}")
    print(f"Recommendation: {result['recommendation']}")
    print(f"RSI: {result['rsi']:.2f}")
    print(f"Sentiment: {result['sentiment']:.2f}")
    print("Reasons:")
    for reason in result['reasons']:
        print(f"  - {reason}")
    print(f"\n{result['disclaimer']}")

if __name__ == "__main__":
    test_engine()
