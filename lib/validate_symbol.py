from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from stock_requests import api_key, secret_key

# 1. Initialize the client (Required for all API interaction)
# Replace with your actual credentials
client = TradingClient(api_key, secret_key, paper=True)

def get_valid_ticker_set():
    # 2. Define search parameters for US Stocks
    search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
    
    # 3. This call hits the Alpaca API and requires authentication
    all_assets = client.get_all_assets(search_params)
    
    # 4. Create a set for lightning-fast lookups
    # We only include active, tradable stocks
    return {a.symbol for a in all_assets if a.status == 'active' and a.tradable}

# Usage
valid_tickers = get_valid_ticker_set()

ticker = "CGNX"
if ticker in valid_tickers:
    print(f"{ticker} is good to go!")
else:
    print(f"{ticker} is invalid or not tradable.")