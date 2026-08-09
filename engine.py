import pandas as pd

def generate_recommendation(df: pd.DataFrame, sentiment_score: float) -> dict:
    """
    Combines technical indicators and sentiment to provide a recommendation.
    """
    if df.empty:
        return {"recommendation": "NEUTRAL", "reason": "No data available"}

    last_row = df.iloc[-1]

    # Technical Signals
    rsi = last_row.get('RSI', 50)
    macd = last_row.get('MACD_12_26_9', 0)
    macd_signal = last_row.get('MACDs_12_26_9', 0)
    ema_20 = last_row.get('EMA_20', last_row['Close'])
    ema_50 = last_row.get('EMA_50', last_row['Close'])
    close = last_row['Close']

    technical_score = 0
    reasons = []

    # RSI logic
    if rsi < 30:
        technical_score += 2
        reasons.append("RSI indicates oversold conditions (Potential Buy)")
    elif rsi > 70:
        technical_score -= 2
        reasons.append("RSI indicates overbought conditions (Potential Sell)")

    # MACD logic
    if macd > macd_signal:
        technical_score += 1
        reasons.append("MACD is above Signal line (Bullish)")
    else:
        technical_score -= 1
        reasons.append("MACD is below Signal line (Bearish)")

    # EMA logic
    if close > ema_20 > ema_50:
        technical_score += 2
        reasons.append("Price is above 20 and 50 EMA (Strong Uptrend)")
    elif close < ema_20 < ema_50:
        technical_score -= 2
        reasons.append("Price is below 20 and 50 EMA (Strong Downtrend)")

    # Sentiment Score integration
    if sentiment_score > 0.2:
        technical_score += 1
        reasons.append(f"Positive news sentiment ({sentiment_score:.2f})")
    elif sentiment_score < -0.2:
        technical_score -= 1
        reasons.append(f"Negative news sentiment ({sentiment_score:.2f})")

    # Final Decision
    if technical_score >= 3:
        rec = "STRONG BUY"
    elif 1 <= technical_score < 3:
        rec = "BUY"
    elif -1 < technical_score < 1:
        rec = "HOLD / NEUTRAL"
    elif -3 < technical_score <= -1:
        rec = "SELL"
    else:
        rec = "STRONG SELL"

    return {
        "ticker_price": float(close),
        "recommendation": rec,
        "score": technical_score,
        "reasons": reasons,
        "rsi": float(rsi),
        "sentiment": float(sentiment_score),
        "disclaimer": "DISCLAIMER: This is NOT financial advice. Trading involves risk. 100% accuracy is impossible."
    }
