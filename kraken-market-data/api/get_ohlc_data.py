from settings import *


def get_ohlc_data(endpoint):
    title = 'OHLC Data'
    dashes = (len(title) + 4) * '-'
    print(f"\n{Fore.GREEN}{dashes}\n  {title}  \n{dashes}{Style.RESET_ALL}")
    
    print("\nINFO: GET OHLC information. The last entry in the OHLC array is for the current, not-yet-committed frame and will always be present, regardless of the value of since.")
    print(f"\n{Fore.YELLOW}REQUIRED: Asset pair to get data for.{Style.RESET_ALL}")
    print("\nEXAMPLE: 'XBTUSD'")
    pair = input("> ")
    if pair == "":
        print("\nAsset pair is required. Please enter an asset pair.")
        get_ohlc_data(endpoint)

    interval_values = [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]
    print(f"\n{Fore.YELLOW}OPTIONAL: Time frame interval in minutes. Default value: '1'.{Style.RESET_ALL}")
    print("\nPOSSIBLE VALUES: [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]")
    interval = input("> ")
    if int(interval) not in interval_values:
        print(f"\n{Fore.RED}Interval value invalid. Please enter a valid interval.{Style.RESET_ALL}")
        get_ohlc_data(endpoint)

    print(f"\n{Fore.YELLOW}OPTIONAL: Return up to 720 OHLC data points since given timestamp.{Style.RESET_ALL}")
    print("\nEXAMPLE: '1548111600'")
    since = input("> ")

    # pair
    if pair != "" and interval == "" and since == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}"
    # pair + interval
    elif pair != "" and interval != "" and since == "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&interval={interval}"
    # pair + since
    elif pair != "" and interval == "" and since != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&since={since}"
    # pair + interval + since
    elif pair != "" and interval != "" and since != "":
        url = f"{BASE_URL}{endpoint}?pair={pair}&interval={interval}&since={since}"
    
    return url