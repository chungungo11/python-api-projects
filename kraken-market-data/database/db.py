from dotenv import load_dotenv
import os
import pymysql


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


# connection = pymysql.connect(
#     host=host,
#     user=user,
#     password=password,
#     db=db,
#     charset="utf8mb4",
#     cursorclass=pymysql.cursors.DictCursor,
# )


asset_data = {
    "name": [],
    "aclass": [],
    "altname": [],
    "decimals": [],
    "display_decimals": [],
    "collateral_value": [],
    "status": [],
}


def extract_asset_data(response):
    # convert response into json object
    json_response = response.json()
    result = json_response["result"]

    i = 0
    # loop over all assets in response
    for asset in result:
        # retrieve asset name
        asset_name = list(result)[i]
        asset_data["name"].append(asset_name)
        # asset info properties
        asset_info = json_response["result"][asset_name]

        # loop over all asset info properties
        for key, value in asset_info.items():
            asset_data[key].append(value)
        # ensure collateral value is added if empty in response
        if "collateral_value" not in asset_info.keys():
            asset_data["collateral_value"].append(0)

        i += 1

    return asset_data


# def save_assets_to_db(data):
#     try:
#         with connection.cursor() as cursor:
#             # Create a new record
#             sql = "INSERT INTO `asset_info` (`asset_name`, `aclass`, `altname`, `decimals`, `display_decimals`, `collateral_value`, `status`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#             cursor.execute(
#                 sql,
#                 (
#                     name,
#                     aclass,
#                     altname,
#                     decimals,
#                     display_decimals,
#                     collateral_value,
#                     status,
#                 ),
#             )

#         # Commit changes
#         connection.commit()

#         print("Record inserted successfully")
#     finally:
#         connection.close()
