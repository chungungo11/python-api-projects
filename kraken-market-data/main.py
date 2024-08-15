import json
import requests


BASE_URL = "https://api.kraken.com/0"

payload = {}
headers = {
  'Accept': 'application/json'
}

public_endpoints = {
    "get_server_time": "/public/Time",
    "get_system_status": "/public/SystemStatus",
    "get_asset_info": "/public/Assets",
    "get_tradable_asset_pairs": "/public/AssetPairs",
    "get_ticker_information": "/public/Ticker",
    "get_ohlc_data": "/public/OHLC",
    "get_order_book": "/public/Depth",
    "get_recent_trades": "/public/Trades",
    "get_recent_spreads": "/public/Spread"
}

def print_endpoints():
    print(f"\n***********************\n* Available endpoints *\n***********************")
    for endpoint in public_endpoints:
        print(f"- {endpoint}")
    get_user_input()

def get_user_input():
    print("\nEnter the endpoint you would like to call (e.g. 'get_asset_info'):")
    user_input = input("> ")
    if validate_user_input(user_input):
        endpoint = public_endpoints[user_input]
        call_endpoint(endpoint)

def validate_user_input(user_input):
    if user_input in public_endpoints:
        return True
    else:
        print("Your input was invalid. Please try again.")
        get_user_input()

def call_endpoint(endpoint):
    url = BASE_URL + endpoint
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

if __name__ == "__main__":
    print_endpoints()