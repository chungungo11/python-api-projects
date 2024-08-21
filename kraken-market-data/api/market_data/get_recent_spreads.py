from config import BASE_URL


def get_recent_spreads(endpoint):
    print("\nINFO: Returns the last ~200 top-of-book spreads for a given pair.")
    print("\nREQUIRED: Asset pair to get data for.")
    print("\nEXAMPLE: 'XBTUSD'")
    pair = input("> ")
    if pair == "":
        print("\nAsset pair is required. Please enter an asset pair.")
        get_recent_spreads(endpoint)

    print("\nOPTIONAL: Returns spread data since given timestamp. Intended for incremental updates within available dataset (does not contain all historical spreads).")
    print("\nEXAMPLE: '1678219570'")
    since = input("> ")

    # pair
    if pair != "" and since == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + since
    elif pair != "" and since != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&since={since}"

    return url