import os
from dotenv import load_dotenv
# from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, StockTradesRequest, StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

load_dotenv()

api_key = os.getenv("ALPACA_API_KEY")
secret_key = os.getenv("ALPACA_SECRET_KEY")

def pull_quotes(ta_client,symbol):
    # add the ability to set the time frame to build the chart

    request_params = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Day,
        start=datetime(2025, 11, 11), # Start date
        end=datetime(2026, 2, 12)    # End date
    )

    return ta_client.get_stock_bars(request_params)
