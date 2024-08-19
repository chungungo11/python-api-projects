from main import BASE_URL
from main import get_response

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

    get_response(url)