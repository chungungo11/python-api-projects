from settings import *


def get_asset_info(endpoint):
    title = "Asset Info"
    dashes = (len(title) + 4) * "-"
    print(f"\n{Fore.GREEN}{dashes}\n  {title}  \n{dashes}{Style.RESET_ALL}")

    print(
        "\nINFO: Get information about the assets that are available for deposit, withdrawal, trading and earn."
    )
    print(
        f"\n{Fore.YELLOW}OPTIONAL: Comma delimited list of assets to get info on. Default: all available assets.{Style.RESET_ALL}"
    )
    print("\nEXAMPLE: 'BTC,ETH'")
    asset = input("> ")

    print(
        f"\n{Fore.YELLOW}OPTIONAL: Asset class. Default: 'currency'.{Style.RESET_ALL}"
    )
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
