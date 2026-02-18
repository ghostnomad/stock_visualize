from lib.validate_symbol import get_valid_ticker_set
import sys

#request the ticker from the user
def user_ticker():
    valid_tickers = get_valid_ticker_set()
    
    while True:

        ticker = input("Enter the stock ticker symbol (or type exit to quit): ").upper().strip()
        
        if not ticker:
            print("Input cannot be empty.")
            continue

        if ticker == "EXIT":
            print(f"Exiting......")
            sys.exit(0)

        if ticker in valid_tickers:
            return ticker    
        else:
            print(f"{ticker} is invalid or not tradable.")
            continue