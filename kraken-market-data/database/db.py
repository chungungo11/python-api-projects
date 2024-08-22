from dotenv import load_dotenv
import os
import pymysql


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

print(host, user, password, db)


connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=db,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


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