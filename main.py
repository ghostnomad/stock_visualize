from alpaca.data import StockHistoricalDataClient
from lib.requests import api_key, secret_key, pull_quotes
from lib.plots import show_plots

symbol = input("Enter the stock ticker symbol: ").upper().strip()

ta_client = StockHistoricalDataClient(api_key, secret_key)

# add the ability to set the time frame to build the chart

bars = pull_quotes(ta_client,symbol)
show_plots(bars,symbol)


#latest_close = df['close'].iloc[-1]
#print(f"The EOD Close Price for AAPL was: ${latest_close}")
