import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment(ticker: str) -> float:
    """
    Fetches recent news for a ticker and calculates an average sentiment score.

    Args:
        ticker: The ticker symbol.

    Returns:
        Average sentiment score (-1 to 1).
    """
    try:
        t = yf.Ticker(ticker)
        news = t.news
        if not news:
            print(f"No news found for {ticker}")
            return 0.0

        analyzer = SentimentIntensityAnalyzer()
        scores = []

        for article in news:
            # yfinance news structure can vary, try to get title from content if it exists
            content = article.get('content', {})
            title = content.get('title', article.get('title', ''))

            if title:
                score = analyzer.polarity_scores(title)
                scores.append(score['compound'])

        if not scores:
            return 0.0

        return sum(scores) / len(scores)
    except Exception as e:
        print(f"Error fetching sentiment for {ticker}: {e}")
        return 0.0

if __name__ == "__main__":
    test_tickers = ["AAPL", "TSLA", "BTC-USD"]
    for ticker in test_tickers:
        sentiment = get_sentiment(ticker)
        print(f"Average sentiment for {ticker}: {sentiment:.2f}")
