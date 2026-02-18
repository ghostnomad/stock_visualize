#import os
from lib.stock_requests import api_key, secret_key, pull_quotes
from lib.plots import show_plots, show_multi_plots
from lib.get_ticker import user_ticker
from lib.timeframe import get_timeframe
from lib.timerange import get_chart_range
from alpaca.data import StockHistoricalDataClient

def main():
    # symbol = input("Enter the stock ticker symbol: ").upper().strip()
    symbol1 = user_ticker()
    symbol2 = user_ticker()

    chart_interval = get_timeframe()
    history_timeframe = get_chart_range()

    ta_client = StockHistoricalDataClient(api_key, secret_key)
    bars1 = pull_quotes(ta_client,symbol1,chart_interval,history_timeframe)
    bars2 = pull_quotes(ta_client,symbol2,chart_interval,history_timeframe)

    show_multi_plots(bars1,bars2, symbol1,symbol2)

    #latest_close = df['close'].iloc[-1]
    #print(f"The EOD Close Price for AAPL was: ${latest_close}")

if __name__ == "__main__":
    main()