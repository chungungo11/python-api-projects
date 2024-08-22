from config import *
from secret import mysql_connection
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
    # check if error is returned
    print(response.json())
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
    result = data['result']['BTC']
    aclass = result.get('aclass')
    altname = result.get('altname')
    decimals = result.get('decimals')
    display_decimals = result.get('display_decimals')
    collateral_value = result.get('collateral_value')
    status = result.get('status')
    print(result)
    print(aclass, altname, decimals, display_decimals, collateral_value, status)

# try:
#     with mysql_connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `assets` (`id`, `name`) VALUES (%s, %s)"
#         cursor.execute(sql, ('0', 'BTC'))

#     # Commit changes
#     mysql_connection.commit()

#     print("Record inserted successfully")
# finally:
#     mysql_connection.close()

get_asset_info(endpoint)