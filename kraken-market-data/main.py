import json
import pandas as pd
import requests
from api.market_data import *
from settings import *


def start_program():
    print(f"\n----------------------\n  Available Requests  \n----------------------")
    for request in public_endpoints:
        print(f"- {request}")
    get_user_input()


def get_user_input():
    print("\nEnter the endpoint you would like to call (e.g. 'get_asset_info'):")
    user_input = input("> ")
    if validate_user_input(user_input):
        request = user_input
        get_endpoint_url(request)


def validate_user_input(user_input):
    if user_input.lower() in public_endpoints:
        return True
    else:
        print("\nYour input was invalid. Please check for any typos and try again.")
        get_user_input()


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
    get_response(url)


def get_response(url):
    print("\nRequest url:" , url)
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.json()["error"] == []:
        print_response(response)
        save_to_json(response)
        prompt_restart()
    else:   
        print_response(response)
        print("\nQuery is invalid. Please check for any typos and try again.")
        get_user_input()


def print_response(response):
    pretty_response = json.dumps(response.json(), indent=2)
    print(f"\n------------\n  Response  \n------------\n{pretty_response}")


def save_to_json(response):
    with open('response.json', 'w') as outfile:
        json.dump(response.json(), outfile, indent=2)
    print('\n*** Data is saved to response.json ***')
    

def prompt_restart():
    print("\nWould you like to call another endpoint? (y/n)")
    restart = input("> ")
    if restart.lower() == "y":
        start_program()
    elif restart.lower() == "n":
        exit(0)
    else:
        print("\nYour input was invalid. Please type 'y' to restart or 'n' to exit.")
        return prompt_restart()


if __name__ == "__main__":
    start_program()