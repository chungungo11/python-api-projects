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
    if request == "get_server_time" or request == "get_system_status":
        url = BASE_URL + endpoint
        get_response(url)
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

def get_asset_info(endpoint):
    print("\nOPTIONAL: Comma delimited list of assets to get info on. Default: all available assets.")
    print("\nExample: 'BTC,ETH'")
    asset = input("> ")
    
    # print("OPTIONAL: Asset class. Default: 'currency'.")

    if asset == "":
        url = BASE_URL + endpoint
    else:
        url = f"{BASE_URL}{endpoint}?asset={asset}"
        
    # validate_response(url)
    get_response(url)

def get_tradable_asset_pairs(endpoint):
    print("\nOPTIONAL: Asset pair(s) to get data for. Default: all available assets.")
    print("\nExample: 'BTC/USD,ETH/BTC'")
    pair = input("> ")

    print("\nOPTIONAL: Info to retrieve: 'info', 'leverage', 'fees', 'margin'. Default: 'info'.")
    info = input("> ")

    print("\nOPTIONAL: Filter for response to only include pairs available in provided countries/regions. Default: all countries/regions.")
    print("\nExample: 'US:TX,GB,CA'")
    country_code = input("> ")

    # all query params are empty
    if pair == "" and info == "" and country_code == "":
        url = BASE_URL + endpoint
    # pair
    elif pair != "" and info == "" and country_code == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + info
    elif pair != "" and info != "" and country_code == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&info={info}"
    # pair + country_code
    elif pair != "" and info == "" and country_code != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&country_code={country_code}"
    # info
    elif pair == "" and info != "" and country_code == "":
        url = f"{BASE_URL}{endpoint}?info={info}"
    # info + country_code
    elif pair == "" and info != "" and country_code != "":
        url = f"{BASE_URL}{endpoint}?info={info}&country_code={country_code}"
    elif pair == "" and info == "" and country_code != "":
        url = f"{BASE_URL}{endpoint}?country_code={country_code}"
    
    # validate_response(url)
    get_response(url)

def get_ticker_information(endpoint):
    print("\nOPTIONAL: Asset pair to get data for. Default: all tradeable exchange pairs.")
    print("\nExample: 'XBTUSD'")
    pair = input("> ")

    if pair == "":
        url = BASE_URL + endpoint
    else:
        url = f"{BASE_URL}{endpoint}?pair={pair}"

    # validate_response(url)
    get_response(url)

def get_ohlc_data(endpoint):
    pass

def get_order_book(endpoint):
    pass

def get_recent_trades(endpoint):
    pass

def get_recent_spreads(endpoint):
    pass

def validate_response(url):
    pass

def get_response(url):
    print("\nRequest url:" , url)
    response = requests.request("GET", url, headers=headers, data=payload)
    print_response(response)
    restart_prompt()

def print_response(response):
    pretty_response = json.dumps(response.json(), indent=2)
    print(f"\n------------\n  Response  \n------------\n{pretty_response}")
    
def restart_prompt():
    print("\nWould you like to call another endpoint? (y/n)")
    restart = input("> ")
    if restart.lower() == "y":
        start_program()
    elif restart.lower() == "n":
        exit(0)
    else:
        print("\nYour input was invalid. Please type 'y' to restart or 'n' to exit.")
        return restart_prompt()

if __name__ == "__main__":
    start_program()