from settings import *


def get_server_time(endpoint):
    title = "Server Time"
    dashes = (len(title) + 4) * "-"
    print(f"\n{Fore.GREEN}{dashes}\n  {title}  \n{dashes}{Style.RESET_ALL}")

    print("\nINFO: Get the server's time.")

    url = BASE_URL + endpoint

    return url
