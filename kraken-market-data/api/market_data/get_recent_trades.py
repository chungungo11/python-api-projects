from config import BASE_URL


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

    from main import get_response
    get_response(url)