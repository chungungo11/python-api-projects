from settings import BASE_URL


def get_tradable_asset_pairs(endpoint):
    title = 'Tradable Asset Pairs'
    dashes = (len(title) + 4) * '-'
    print(f"\n{dashes}\n  {title}  \n{dashes}")
    print("\nINFO: Get tradable asset pairs.")
    print("\nOPTIONAL: Asset pair(s) to get data for. Default: all available assets.")
    print("\nEXAMPLE: 'BTC/USD,ETH/BTC'")
    pair = input("> ")

    print("\nOPTIONAL: Info to retrieve: 'info', 'leverage', 'fees', 'margin'. Default: 'info'.")
    info = input("> ")

    print("\nOPTIONAL: Filter for response to only include pairs available in provided countries/regions. Default: all countries/regions.")
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