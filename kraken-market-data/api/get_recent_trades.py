from settings import *


def get_recent_trades(endpoint):
    title = 'Recent Trades'
    dashes = (len(title) + 4) * '-'
    print(f"\n{Fore.GREEN}{dashes}\n  {title}  \n{dashes}{Style.RESET_ALL}")
    
    print("\nINFO: Returns the last 1000 trades by default.")
    print(f"\n{Fore.YELLOW}REQUIRED: Asset pair to get data for.{Style.RESET_ALL}")
    print("\nEXAMPLE: 'XBTUSD'")
    pair = input("> ")
    if pair == "":
        print(f"\n{Fore.RED}Asset pair is required. Please enter an asset pair.{Style.RESET_ALL}")
        get_recent_trades(endpoint)

    print(f"\n{Fore.YELLOW}OPTIONAL: Return trade data since given timestamp.{Style.RESET_ALL}")
    print("\nEXAMPLE: '1616663618'")
    since = input("> ")
    
    print(f"\n{Fore.YELLOW}OPTIONAL: Return specific number of trades, up to 1000. Default value: '1000'.{Style.RESET_ALL}")
    print("\nPOSSIBLE VALUES: >= 1 and <= 1000")
    count = input("> ")
    if int(count) not in range(1, 1001):
        print(f"\n{Fore.RED}Value is invalid. Please enter a valid number of trades.{Style.RESET_ALL}")
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

    return url