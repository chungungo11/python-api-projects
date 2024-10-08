import json
import pandas as pd
import requests
import time
from api import *
from database import db
from settings import *

# initialize colorama
init()


# main program logic
def main():
    print_available_requests()
    user_input = get_user_input()

    while validate_user_input(user_input) != True:
        user_input = get_user_input()
    else:
        request = user_input
        url = get_endpoint_url(request)
        response = get_response(url)

        while validate_response(response) != True:
            url = get_endpoint_url(request)
            response = get_response(url)
        else:
            print_response(response)
            save_to_json(request, response)
            if request == "get_asset_info":
                db.extract_asset_data(response)
                save_to_csv(db.asset_data)
            prompt_restart()


# print all available public market data requests
def print_available_requests():
    print(
        f"\n{Fore.GREEN}----------------------\n  Available Requests  \n----------------------{Style.RESET_ALL}"
    )
    for request in public_endpoints:
        print(f"- {request}")


# prompt user input for api request
def get_user_input():
    print(
        f"\n{Fore.YELLOW}Enter the endpoint you would like to call (e.g. 'get_asset_info'):{Style.RESET_ALL}"
    )
    user_input = input("> ")
    return user_input


# check if user input is a valid api request
def validate_user_input(user_input):
    if user_input.lower() in public_endpoints:
        return True
    else:
        print(
            f"\n{Fore.RED}Your input was invalid. Please check for any typos and try again.{Style.RESET_ALL}"
        )
        return False


# get full endpoint url based on api request
def get_endpoint_url(request):
    endpoint = public_endpoints[request]
    if request == "get_server_time":
        url = get_server_time.get_server_time(endpoint)
    elif request == "get_system_status":
        url = get_system_status.get_system_status(endpoint)
    elif request == "get_asset_info":
        url = get_asset_info.get_asset_info(endpoint)
    elif request == "get_tradable_asset_pairs":
        url = get_tradable_asset_pairs.get_tradable_asset_pairs(endpoint)
    elif request == "get_ticker_information":
        url = get_ticker_information.get_ticker_information(endpoint)
    elif request == "get_ohlc_data":
        url = get_ohlc_data.get_ohlc_data(endpoint)
    elif request == "get_order_book":
        url = get_order_book.get_order_book(endpoint)
    elif request == "get_recent_trades":
        url = get_recent_trades.get_recent_trades(endpoint)
    elif request == "get_recent_spreads":
        url = get_recent_spreads.get_recent_spreads(endpoint)
    return url


# get response from api request
def get_response(url):
    print(f"\n{Fore.CYAN}Request url:{Style.RESET_ALL}", url)
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


# validate response from api request
def validate_response(response):
    if response.json()["error"] == []:
        return True
    else:
        print_response(response)
        print(
            f"\n{Fore.RED}Query is invalid. Please check for any typos and try again.{Style.RESET_ALL}"
        )
        return False


# pretty print api response
def print_response(response):
    pretty_response = json.dumps(response.json(), indent=2)
    print(
        f"{Fore.GREEN}\n------------\n  Response  \n------------\n{Style.RESET_ALL}\n{pretty_response}"
    )


# save api response to json
def save_to_json(request, response):
    timestamp = int(time.time())
    with open(f"output/{timestamp}-{request}-response.json", "w") as outfile:
        json.dump(response.json(), outfile, indent=2)
    print(
        f"\n{Fore.GREEN}*** Data is saved to 'output/{timestamp}-{request}-response.json' ***{Style.RESET_ALL}"
    )


# save api response to csv
def save_to_csv(data):
    timestamp = int(time.time())
    df = pd.DataFrame(data)
    csv_file_path = f"output/{timestamp}-asset_info.csv"
    df.to_csv(csv_file_path, index=False)
    print(f"\n{Fore.GREEN}*** Data is saved to '{csv_file_path}' ***{Style.RESET_ALL}")


# prompt user to call another endpoint
def prompt_restart():
    print(
        f"\n{Fore.YELLOW}Would you like to call another endpoint? (y/n){Style.RESET_ALL}"
    )
    restart = input("> ")
    if restart.lower() == "y":
        main()
    elif restart.lower() == "n":
        exit(0)
    else:
        print(
            f"\n{Fore.RED}Your input was invalid. Please type 'y' to restart or 'n' to exit.{Style.RESET_ALL}"
        )
        return prompt_restart()


if __name__ == "__main__":
    main()
