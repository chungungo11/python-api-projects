from settings import BASE_URL


def get_asset_info(endpoint):
    title = 'Asset Info'
    dashes = (len(title) + 4) * '-'
    print(f"\n{dashes}\n  {title}  \n{dashes}")
    print("\nINFO: Get information about the assets that are available for deposit, withdrawal, trading and earn.")
    print("\nOPTIONAL: Comma delimited list of assets to get info on. Default: all available assets.")
    print("\nEXAMPLE: 'BTC,ETH'")
    asset = input("> ")
    
    print("\nOPTIONAL: Asset class. Default: 'currency'.")
    print("\nEXAMPLE: 'currency'")
    aclass = input("> ")

    # no query params
    if asset == "" and aclass == "":
        url = BASE_URL + endpoint
    # asset
    elif asset != "" and aclass == "":
        url = f"{BASE_URL}{endpoint}?asset={asset}"
    # aclass
    elif asset == "" and aclass != "":
        url = f"{BASE_URL}{endpoint}?aclass={aclass}"
    # asset + aclass
    elif asset != "" and aclass != "":
        url = f"{BASE_URL}{endpoint}?asset={asset}&aclass={aclass}"
    
    return url