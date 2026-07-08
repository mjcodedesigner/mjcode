# AI Trading Prediction Tool

This tool provides trading recommendations based on technical analysis and real-time news sentiment. It is designed for informational purposes and personal use.

## ⚠️ Important Disclaimer
**Financial trading involves significant risk. This tool does NOT guarantee profits and does NOT provide 100% accuracy. Financial markets are unpredictable. Always do your own research and never invest money you cannot afford to lose. This software is NOT financial advice.**

## Features
- **Technical Analysis**: Uses RSI, MACD, and EMA (Exponential Moving Averages) to identify trends and overbought/oversold conditions.
- **Sentiment Analysis**: Fetches the latest news for a ticker and analyzes the sentiment using Natural Language Processing (NLP).
- **Recommendation Engine**: Combines multiple signals into a simple "Buy/Sell/Hold" recommendation with supporting reasons.

## Installation

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the tool from the command line by providing a ticker symbol (e.g., AAPL, TSLA, BTC-USD):

```bash
python3 main.py AAPL
```

### Example Output
```text
========================================
 TRADING PREDICTION FOR AAPL
========================================
Current Price:  $185.20
Recommendation: BUY
Confidence Score: 2 (Scale: -5 to +5)
----------------------------------------
Technical Analysis:
  - RSI: 45.12
  - News Sentiment: 0.15

Key Factors:
  - MACD is above Signal line (Bullish)
  - Price is above 20 EMA
----------------------------------------

DISCLAIMER: This is NOT financial advice. Trading involves risk. 100% accuracy is impossible.
========================================
```

## Supported Symbols
Most symbols supported by Yahoo Finance should work, including:
- Stocks: `AAPL`, `MSFT`, `TSLA`
- Crypto: `BTC-USD`, `ETH-USD`
- Indices: `^GSPC` (S&P 500)
