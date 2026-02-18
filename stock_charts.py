import sys
from lib.stock_requests import api_key, secret_key, pull_quotes
from lib.plots import show_plots, show_multi_plots
from lib.get_ticker import user_ticker
from lib.timeframe import get_timeframe
from lib.timerange import get_chart_range
from alpaca.data import StockHistoricalDataClient #type:ignore

def chart_comparisons():
    user_choice = input("Do you want to compare two stock tickers side by side? (Y or N, exit to quit): ").upper().strip()
    match user_choice:
        case "YES" | "Y":
            return True
        case "NO" | "N":
            return False
        case "QUIT" | "Q" | "EXIT" | "E":
            sys.exit(0)
        case _:
            print(f"⚠️  '{user_choice}' is not a valid response.")


def main():
    # symbol = input("Enter the stock ticker symbol: ").upper().strip()
    chart_interval = get_timeframe()
    history_timeframe = get_chart_range()

    if chart_comparisons():
        symbol1 = user_ticker()
        symbol2 = user_ticker()
        
        ta_client = StockHistoricalDataClient(api_key, secret_key)
        
        bars1 = pull_quotes(ta_client,symbol1,chart_interval,history_timeframe)
        bars2 = pull_quotes(ta_client,symbol2,chart_interval,history_timeframe)

        show_multi_plots(bars1,bars2, symbol1,symbol2)
    else:
        symbol = user_ticker()
    
        ta_client = StockHistoricalDataClient(api_key, secret_key)

        bars = pull_quotes(ta_client,symbol,chart_interval,history_timeframe)
    
        show_plots(bars,symbol)


    #latest_close = df['close'].iloc[-1]
    #print(f"The EOD Close Price for AAPL was: ${latest_close}")

if __name__ == "__main__":
    main()