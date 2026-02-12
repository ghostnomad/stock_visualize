import os
# from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, StockTradesRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from dotenv import load_dotenv
from datetime import datetime

symbol = input("Enter the stock ticker symbol: ").upper().strip()

load_dotenv()
api_key = os.getenv("ALPACA_API_KEY")
secret_key = os.getenv("ALPACA_SECRET_KEY")

ta_client = StockHistoricalDataClient(api_key, secret_key)

# add the ability to set the time frame to build the chart

request_params = StockBarsRequest(
    symbol_or_symbols=symbol,
    timeframe=TimeFrame.Day,
    start=datetime(2026, 1, 11), # Start date
    end=datetime(2026, 2, 12)    # End date
)

bars = ta_client.get_stock_bars(request_params)

df = bars.df
#this is just for testing purposes
print(df)

#latest_close = df['close'].iloc[-1]
#print(f"The EOD Close Price for AAPL was: ${latest_close}")
