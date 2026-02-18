from alpaca.data import StockHistoricalDataClient
from lib.stock_requests import api_key, secret_key, pull_quotes
from lib.plots import show_plots
from lib.get_ticker import user_ticker
from lib.timeframe import get_timeframe
from lib.timerange import get_chart_range

def main():
    symbol = user_ticker()
    chart_interval = get_timeframe()
    history_timeframe = get_chart_range()

    ta_client = StockHistoricalDataClient(api_key, secret_key)

    # add the ability to set the time frame to build the chart

    bars = pull_quotes(ta_client,symbol,chart_interval,history_timeframe)
    show_plots(bars,symbol)

    #latest_close = df['close'].iloc[-1]
    #print(f"The EOD Close Price for AAPL was: ${latest_close}")

if __name__ == "__main__":
    main()