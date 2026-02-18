import os
from dotenv import load_dotenv
from alpaca.data import StockBarsRequest # StockHistoricalDataClient, StockTradesRequest
#from alpaca.data.timeframe import TimeFrame
from datetime import datetime

load_dotenv()

api_key = os.getenv("ALPACA_API_KEY")
secret_key = os.getenv("ALPACA_SECRET_KEY")

def pull_quotes(ta_client,symbol,user_timeframe,history_timeframe):
    # add the ability to set the time frame to build the chart

    request_params = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=user_timeframe,
        start=history_timeframe, # Start date
        end=datetime.now()   # End date
    )

    return ta_client.get_stock_bars(request_params)
