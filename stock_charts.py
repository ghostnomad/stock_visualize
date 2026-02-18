#import os
from lib.stock_requests import api_key, secret_key, pull_quotes
from lib.plots import show_plots, show_multi_plots
from lib.get_ticker import user_ticker
from lib.timeframe import get_timeframe
# from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient
#from alpaca.data.timeframe import TimeFrame
#from dotenv import load_dotenv
#from datetime import datetime

# symbol = input("Enter the stock ticker symbol: ").upper().strip()
symbol1 = user_ticker()
symbol2 = user_ticker()

chart_interval = get_timeframe()

ta_client = StockHistoricalDataClient(api_key, secret_key)
bars1 = pull_quotes(ta_client,symbol1,chart_interval)
bars2 = pull_quotes(ta_client,symbol2,chart_interval)


#load_dotenv()
#api_key = os.getenv("ALPACA_API_KEY")
#secret_key = os.getenv("ALPACA_SECRET_KEY")
#ta_client = StockHistoricalDataClient(api_key, secret_key)

# add the ability to set the time frame to build the chart

#request_params1 = StockBarsRequest(
#    symbol_or_symbols="AMAT",
 #   timeframe=TimeFrame.Hour,
  #  start=datetime(2026, 1, 11), # Start date
   # end=datetime(2026, 2, 12)    # End date
#)

#request_params2 = StockBarsRequest(
#    symbol_or_symbols="WMT",
#    timeframe=TimeFrame.Hour,
#    start=datetime(2026, 1, 11),
#    end=datetime(2026, 2, 12)
#)

#bars1 = ta_client.get_stock_bars(request_params1)
#bars2 = ta_client.get_stock_bars(request_params2)

show_multi_plots(bars1,bars2, symbol1,symbol2)

#df1 = bars1.df
#df2 = bars2.df
#this is just for testing purposes
# print(bars2.df, "\n", bars1.df)

#latest_close = df['close'].iloc[-1]
#print(f"The EOD Close Price for AAPL was: ${latest_close}")
