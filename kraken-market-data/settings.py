# colors in terminal
from colorama import init, Fore, Style


BASE_URL = "https://api.kraken.com/0"

# payload and headers sent in a request
payload = {}
headers = {"Accept": "application/json"}

# all market data endpoints
public_endpoints = {
    "get_server_time": "/public/Time",
    "get_system_status": "/public/SystemStatus",
    "get_asset_info": "/public/Assets",
    "get_tradable_asset_pairs": "/public/AssetPairs",
    "get_ticker_information": "/public/Ticker",
    "get_ohlc_data": "/public/OHLC",
    "get_order_book": "/public/Depth",
    "get_recent_trades": "/public/Trades",
    "get_recent_spreads": "/public/Spread",
}
