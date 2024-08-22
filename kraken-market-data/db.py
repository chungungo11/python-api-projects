from settings import *
from mysql.secret import connection
import json
import requests


endpoint = "/public/Assets"


def get_asset_info(endpoint):
    print("\nINFO: Get information about the assets that are available for deposit, withdrawal, trading and earn.")
    print("\nOPTIONAL: Comma delimited list of assets to get info on. Default: all available assets.")
    print("EXAMPLE: 'BTC,ETH'")
    asset = input("> ")

    if asset == "":
        url = BASE_URL + endpoint
    else:
        url = f"{BASE_URL}{endpoint}?asset={asset}"
   
    get_response(url)


def get_response(url):
    print("\nRequest url:" , url)
    response = requests.request("GET", url, headers=headers, data=payload)
    # check if error is returnedß
    if response.json()["error"] != []:
        print_response(response)
        print("\nQuery is invalid. Please check for any typos and try again.")
    else:   
        print_response(response)
        extract_data(response)


def print_response(response):
    pretty_response = json.dumps(response.json(), indent=2)
    print(f"\n------------\n  Response  \n------------\n{pretty_response}")


def extract_data(response):
    data = response.json()
    result = data['result']
    # retrieve asset name
    name = list(result)[0]
    # retrieve asset info
    asset_info = data['result'][name]
    aclass = asset_info.get('aclass')
    altname = asset_info.get('altname')
    decimals = asset_info.get('decimals')
    display_decimals = asset_info.get('display_decimals')
    # check if asset has collateral_value
    if 'collateral_value' in asset_info.keys():
        collateral_value = asset_info.get('collateral_value')
    else:
        collateral_value = 0
    status = asset_info.get('status')
    print("Result:", result)
    print("Asset:", name)
    print("Asset Info:", asset_info)
    print(name, aclass, altname, decimals, display_decimals, collateral_value, status)
    save_to_db(name, aclass, altname, decimals, display_decimals, collateral_value, status)


def save_to_db(name, aclass, altname, decimals, display_decimals, collateral_value, status):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `asset_info` (`name`, `aclass`, `altname`, `decimals`, `display_decimals`, `collateral_value`, `status`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, aclass, altname, decimals, display_decimals, collateral_value, status))

        # Commit changes
        connection.commit()

        print("Record inserted successfully")
    finally:
        connection.close()

get_asset_info(endpoint)