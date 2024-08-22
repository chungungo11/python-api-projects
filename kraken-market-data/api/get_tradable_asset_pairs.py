from settings import *


def get_tradable_asset_pairs(endpoint):
    title = 'Tradable Asset Pairs'
    dashes = (len(title) + 4) * '-'
    print(f"\n{Fore.GREEN}{dashes}\n  {title}  \n{dashes}{Style.RESET_ALL}")
    
    print("\nINFO: Get tradable asset pairs.")
    print(f"\n{Fore.YELLOW}OPTIONAL: Asset pair(s) to get data for. Default: all available assets.{Style.RESET_ALL}")
    print("\nEXAMPLE: 'BTC/USD,ETH/BTC'")
    pair = input("> ")

    print(f"\n{Fore.YELLOW}OPTIONAL: Info to retrieve: 'info', 'leverage', 'fees', 'margin'. Default: 'info'.{Style.RESET_ALL}")
    info = input("> ")

    print(f"\n{Fore.YELLOW}OPTIONAL: Filter for response to only include pairs available in provided countries/regions. Default: all countries/regions.{Style.RESET_ALL}")
    print("\nEXAMPLE: 'US:TX,GB,CA'")
    country_code = input("> ")

    # no query params
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
    # country_code
    elif pair == "" and info == "" and country_code != "":
        url = f"{BASE_URL}{endpoint}?country_code={country_code}"
    
    return url