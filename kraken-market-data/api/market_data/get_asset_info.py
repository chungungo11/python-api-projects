from config import BASE_URL


def get_asset_info(endpoint):
    print("\nINFO: Get information about the assets that are available for deposit, withdrawal, trading and earn.")
    print("\nOPTIONAL: Comma delimited list of assets to get info on. Default: all available assets.")
    print("EXAMPLE: 'BTC,ETH'")
    asset = input("> ")
    
    # print("OPTIONAL: Asset class. Default: 'currency'.")

    if asset == "":
        url = BASE_URL + endpoint
    else:
        url = f"{BASE_URL}{endpoint}?asset={asset}"

    from main import get_response    
    get_response(url)