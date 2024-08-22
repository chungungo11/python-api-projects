from settings import BASE_URL


def get_order_book(endpoint):
    print("\nINFO: Returns the Order Book.")
    print("\nREQUIRED: Asset pair to get data for.")
    print("\nEXAMPLE: 'XBTUSD'")
    pair = input("> ")
    if pair == "":
        print("\nAsset pair is required. Please enter an asset pair.")
        get_order_book(endpoint)

    print("\nOPTIONAL: Maximum number of asks/bids. Default value: '100'.")
    print("\nPOSSIBLE VALUES: >= 1 and <= 500")
    count = input("> ")
    if int(count) not in range(1, 501):
        print("\nValue is invalid. Please enter a valid interval.")
        get_order_book(endpoint)

    # pair
    if pair != "" and count == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + count
    elif pair != "" and count != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&count={count}"

    return url