from settings import *


def get_order_book(endpoint):
    title = "Order Book"
    dashes = (len(title) + 4) * "-"
    print(f"\n{Fore.GREEN}{dashes}\n  {title}  \n{dashes}{Style.RESET_ALL}")

    print("\nINFO: Returns the Order Book.")
    print(f"\n{Fore.YELLOW}REQUIRED: Asset pair to get data for.{Style.RESET_ALL}")
    print("\nEXAMPLE: 'XBTUSD'")
    pair = input("> ")
    while pair == "":
        print(
            f"\n{Fore.RED}Asset pair is required. Please enter an asset pair.{Style.RESET_ALL}"
        )
        pair = input("> ")

    print(
        f"\n{Fore.YELLOW}OPTIONAL: Maximum number of asks/bids. Default value: '100'.{Style.RESET_ALL}"
    )
    print("\nPOSSIBLE VALUES: >= 1 and <= 500")
    count = input("> ")
    while count != "" and int(count) not in range(1, 501):
        print(
            f"\n{Fore.RED}Value is invalid. Please enter a valid number of asks/bids.{Style.RESET_ALL}"
        )
        count = input("> ")

    # pair
    if pair != "" and count == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + count
    elif pair != "" and count != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&count={count}"

    return url
