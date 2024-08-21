from config import BASE_URL


def get_tradable_asset_pairs(endpoint):
    print("\nINFO: Get tradable asset pairs.")
    print("\nOPTIONAL: Asset pair(s) to get data for. Default: all available assets.")
    print("EXAMPLE: 'BTC/USD,ETH/BTC'")
    pair = input("> ")

    print("\nOPTIONAL: Info to retrieve: 'info', 'leverage', 'fees', 'margin'. Default: 'info'.")
    info = input("> ")

    print("\nOPTIONAL: Filter for response to only include pairs available in provided countries/regions. Default: all countries/regions.")
    print("EXAMPLE: 'US:TX,GB,CA'")
    country_code = input("> ")

    # all query params are empty
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
    elif pair == "" and info == "" and country_code != "":
        url = f"{BASE_URL}{endpoint}?country_code={country_code}"
    
    from main import get_response
    get_response(url)