from settings import *


def get_recent_spreads(endpoint):
    title = "Recent Spreads"
    dashes = (len(title) + 4) * "-"
    print(f"\n{Fore.GREEN}{dashes}\n  {title}  \n{dashes}{Style.RESET_ALL}")

    print("\nINFO: Returns the last ~200 top-of-book spreads for a given pair.")
    print(f"\n{Fore.YELLOW}REQUIRED: Asset pair to get data for.{Style.RESET_ALL}")
    print("\nEXAMPLE: 'XBTUSD'")
    pair = input("> ")
    while pair == "":
        print(
            f"\n{Fore.RED}Asset pair is required. Please enter an asset pair.{Style.RESET_ALL}"
        )
        pair = input("> ")

    print(
        f"\n{Fore.YELLOW}OPTIONAL: Returns spread data since given timestamp. Intended for incremental updates within available dataset (does not contain all historical spreads).{Style.RESET_ALL}"
    )
    print("\nEXAMPLE: '1678219570'")
    since = input("> ")

    # pair
    if pair != "" and since == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + since
    elif pair != "" and since != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&since={since}"

    return url
