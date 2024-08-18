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
    if request == "get_server_time":
        get_server_time(endpoint)
    elif request == "get_system_status":
        get_server_status(endpoint)
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

def get_server_time(endpoint):
    print("\nINFO: Get the server's time.")
    url = BASE_URL + endpoint
    get_response(url)

def get_server_status(endpoint):
    print("\nINFO: Get the current system status or trading mode.")
    url = BASE_URL + endpoint
    get_response(url)

def get_asset_info(endpoint):
    print("\nINFO: Get information about the assets that are available for deposit, withdrawal, trading and earn.")
    print("\nOPTIONAL: Comma delimited list of assets to get info on. Default: all available assets.")
    print("EXAMPLE: 'BTC,ETH'")
    asset = input("> ")
    
    # print("OPTIONAL: Asset class. Default: 'currency'.")

    if asset == "":
        url = BASE_URL + endpoint
    else:
        url = f"{BASE_URL}{endpoint}?asset={asset}"
        
    # validate_response(url)
    get_response(url)

def get_tradable_asset_pairs(endpoint):
    print("\nINFO: Get tradable asset pairs.")
    print("\nOPTIONAL: Asset pair(s) to get data for. Default: all available assets.")
    print("EXAMPLE: 'BTC/USD,ETH/BTC'")
    pair = input("> ")

    print("\nOPTIONAL: Info to retrieve: 'info', 'leverage', 'fees', 'margin'. Default: 'info'.")
    info = input("> ")

    print("\nOPTIONAL: Filter for response to only include pairs available in provided countries/regions. Default: all countries/regions.")
    print("EXAMPLE: 'US:TX,GB,CA'")
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
    print("\nGet ticker information for all or requested markets. To clarify usage, note that:")
    print("- Today's prices start at midnight UTC")
    print("- Leaving the pair parameter blank will return tickers for all tradeable assets on Kraken")
    print("\nOPTIONAL: Asset pair to get data for. Default: all tradeable exchange pairs.")
    print("EXAMPLE: 'XBTUSD'")
    pair = input("> ")

    if pair == "":
        url = BASE_URL + endpoint
    else:
        url = f"{BASE_URL}{endpoint}?pair={pair}"

    # validate_response(url)
    get_response(url)

def get_ohlc_data(endpoint):
    print("\nINFO: GET OHLC information. The last entry in the OHLC array is for the current, not-yet-committed frame and will always be present, regardless of the value of since.")
    print("\nREQUIRED: Asset pair to get data for.")
    print("EXAMPLE: 'XBTUSD'")
    pair = input("> ")
    if pair == "":
        print("\nAsset pair is required! Please enter an asset pair.")
        get_ohlc_data(endpoint)

    interval_values = [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]
    print("\nOPTIONAL: Time frame interval in minutes. Default value: '1'.")
    print("POSSIBLE VALUES: [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]")
    interval = input("> ")
    if int(interval) not in interval_values:
        print("\nInterval value invalid! Please enter a valid interval.")
        get_ohlc_data(endpoint)

    print("\nOPTIONAL: Return up to 720 OHLC data points since given timestamp.")
    print("EXAMPLE: '1548111600'")
    since = input("> ")

    # pair
    if pair != "" and interval == "" and since == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + interval
    elif pair != "" and interval != "" and since == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&interval={interval}"
    # pair + since
    elif pair != "" and interval == "" and since != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&since={since}"
    # pair + interval + since
    elif pair != "" and interval != "" and since != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&interval={interval}&since={since}"
    
    # validate_response(url)
    get_response(url)

def get_order_book(endpoint):
    print("\nINFO: Returns the Order Book.")
    print("\nREQUIRED: Asset pair to get data for.")
    print("EXAMPLE: 'XBTUSD'")
    pair = input("> ")
    if pair == "":
        print("\nAsset pair is required! Please enter an asset pair.")
        get_order_book(endpoint)

    print("\nOPTIONAL: Maximum number of asks/bids. Default value: '100'.")
    print("POSSIBLE VALUES: >= 1 and <= 500")
    count = input("> ")
    if int(count) not in range(1, 501):
        print("\Count value invalid! Please enter a valid interval.")
        get_order_book(endpoint)

    # pair
    if pair != "" and count == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + count
    elif pair != "" and count != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&count={count}"

    # validate_response(url)
    get_response(url)

def get_recent_trades(endpoint):
    print("\nINFO: Returns the last 1000 trades by default.")
    print("\nREQUIRED: Asset pair to get data for.")
    print("EXAMPLE: 'XBTUSD'")
    pair = input("> ")
    if pair == "":
        print("\nAsset pair is required! Please enter an asset pair.")
        get_recent_trades(endpoint)

    print("\nOPTIONAL: Return trade data since given timestamp.")
    print("EXAMPLE: '1616663618'")
    since = input("> ")
    
    print("\nOPTIONAL: Return specific number of trades, up to 1000. Default value: '1000'.")
    print("POSSIBLE VALUES: >= 1 and <= 1000")
    count = input("> ")
    if int(count) not in range(1, 1001):
        print("\Count value invalid! Please enter a valid number of trades.")
        get_recent_trades(endpoint)

    # pair
    if pair != "" and since == "" and count == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + since
    elif pair != "" and since != "" and count == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&since={since}"
    # pair + count
    elif pair != "" and since == "" and count != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&count={count}"
    # pair + since + count
    elif pair != "" and since != "" and count != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&since={since}&count={count}"

    # validate_response(url)
    get_response(url)

def get_recent_spreads(endpoint):
    print("\nINFO: Returns the last ~200 top-of-book spreads for a given pair.")
    print("\nREQUIRED: Asset pair to get data for.")
    print("EXAMPLE: 'XBTUSD'")
    pair = input("> ")
    if pair == "":
        print("\nAsset pair is required! Please enter an asset pair.")
        get_recent_spreads(endpoint)

    print("\nOPTIONAL: Returns spread data since given timestamp. Intended for incremental updates within available dataset (does not contain all historical spreads).")
    print("EXAMPLE: '1678219570'")
    since = input("> ")

    # pair
    if pair != "" and since == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + since
    elif pair != "" and since != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&since={since}"

    # validate_response(url)
    get_response(url)

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