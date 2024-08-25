from dotenv import load_dotenv
import os
import pymysql


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=db,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


def extract_asset_data(response):
    data = response.json()
    result = data["result"]
    # retrieve asset name
    asset_name = list(result)[0]
    # retrieve asset info
    asset_info = data["result"][asset_name]
    aclass = asset_info.get("aclass")
    altname = asset_info.get("altname")
    decimals = asset_info.get("decimals")
    display_decimals = asset_info.get("display_decimals")
    # check if asset has collateral_value
    if "collateral_value" in asset_info.keys():
        collateral_value = asset_info.get("collateral_value")
    else:
        collateral_value = 0
    status = asset_info.get("status")
    print("Result:", result)
    print("Asset:", asset_name)
    print("Asset Info:", asset_info)
    asset_info_list = [
        asset_name,
        aclass,
        altname,
        decimals,
        display_decimals,
        collateral_value,
        status,
    ]
    print(asset_info_list)
    # save_assets_to_db(asset_info_list)


def save_assets_to_db(asset_info_list):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `asset_info` (`asset_name`, `aclass`, `altname`, `decimals`, `display_decimals`, `collateral_value`, `status`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(
                sql,
                (
                    name,
                    aclass,
                    altname,
                    decimals,
                    display_decimals,
                    collateral_value,
                    status,
                ),
            )

        # Commit changes
        connection.commit()

        print("Record inserted successfully")
    finally:
        connection.close()


def extract_pair_data(response):
    data = response.json()
    result = data["result"]
    # retrieve pair name
    pair_name = list(result)[0]
    # retrieve pair info
    pair_info = data["result"][pair_name]
    altname = pair_info.get("altname")
    wsname = pair_info.get("wsname")
    aclass_base = pair_info.get("aclass_base")
    base = pair_info.get("base")
    aclass_quote = pair_info.get("aclass_quote")
    quote = pair_info.get("quote")
    lot = pair_info.get("lot")
    cost_decimals = pair_info.get("cost_decimals")
    pair_decimals = pair_info.get("pair_decimals")
    lot_decimals = pair_info.get("lot_decimals")
    lot_multiplier = pair_info.get("lot_multiplier")
    fee_volume_currency = pair_info.get("fee_volume_currency")
    margin_call = pair_info.get("margin_call")
    margin_stop = pair_info.get("margin_stop")
    ordermin = pair_info.get("ordermin")
    costmin = pair_info.get("costmin")
    tick_size = pair_info.get("tick_size")
    status = pair_info.get("status")
    long_position_limit = pair_info.get("long_position_limit")
    short_position_limit = pair_info.get("short_position_limit")
    print("Result:", result)
    print("Pair:", pair_name)
    print("Pair Info:", pair_info)
    pair_info_list = [
        pair_name,
        altname,
        wsname,
        aclass_base,
        base,
        aclass_quote,
        quote,
        lot,
        cost_decimals,
        pair_decimals,
        lot_decimals,
        lot_multiplier,
        fee_volume_currency,
        margin_call,
        margin_stop,
        ordermin,
        costmin,
        tick_size,
        status,
        long_position_limit,
        short_position_limit,
    ]
    print(pair_info_list)
    save_pairs_to_db(pair_info_list)


def save_pairs_to_db(pair_info_list):
    pass
