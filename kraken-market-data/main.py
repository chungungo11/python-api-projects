import json
import requests
from api.market_data import *


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

def start_program():
    print(f"\n-----------------------\n  Available Endpoints  \n-----------------------")
    for endpoint in public_endpoints:
        print(f"- {endpoint}")
    get_user_input()

def get_user_input():
    print("\nEnter the endpoint you would like to call (e.g. 'get_asset_info'):")
    user_input = input("> ")
    if validate_user_input(user_input):
        request = user_input
        call_endpoint(request)

def validate_user_input(user_input):
    if user_input.lower() in public_endpoints:
        return True
    else:
        print("\nYour input was invalid. Please check for any typos and try again.")
        get_user_input()

def call_endpoint(request):
    endpoint = public_endpoints[request]
    if request == "get_server_time":
        get_server_time(endpoint)
    elif request == "get_system_status":
        get_system_status(endpoint)
    elif request == "get_asset_info":
        get_asset_info(endpoint)
    elif request == "get_tradable_asset_pairs":
        get_tradable_asset_pairs(endpoint)
    elif request == "get_ticker_information":
        get_ticker_information(endpoint)
    elif request == "get_ohlc_data":
        get_ohlc_data(endpoint)
    elif request == "get_order_book":
        get_order_book(endpoint)
    elif request == "get_recent_trades":
        get_recent_trades(endpoint)
    elif request == "get_recent_spreads":
        get_recent_spreads(endpoint)

def get_response(url):
    print("\nRequest url:" , url)
    response = requests.request("GET", url, headers=headers, data=payload)
    # check if error is returned
    print(response.json())
    if response.json()["error"] != []:
        print_response(response)
        print("\nQuery is invalid. Please check for any typos and try again.")
    else:   
        print_response(response)
        prompt_restart()

def print_response(response):
    pretty_response = json.dumps(response.json(), indent=2)
    print(f"\n------------\n  Response  \n------------\n{pretty_response}")
    
def prompt_restart():
    print("\nWould you like to call another endpoint? (y/n)")
    restart = input("> ")
    if restart.lower() == "y":
        start_program()
    elif restart.lower() == "n":
        exit(0)
    else:
        print("\nYour input was invalid. Please type 'y' to restart or 'n' to exit.")
        return prompt_restart()

if __name__ == "__main__":
    start_program()