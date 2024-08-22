from settings import BASE_URL


def get_ticker_information(endpoint):
    print("\nGet ticker information for all or requested markets. To clarify usage, note that:")
    print("- Today's prices start at midnight UTC")
    print("- Leaving the pair parameter blank will return tickers for all tradeable assets on Kraken")
    print("\nOPTIONAL: Asset pair to get data for. Default: all tradeable exchange pairs.")
    print("\nEXAMPLE: 'XBTUSD'")
    pair = input("> ")

    # no query param
    if pair == "":
        url = BASE_URL + endpoint
    # pair
    else:
        url = f"{BASE_URL}{endpoint}?pair={pair}"

    return url