from settings import *


def get_system_status(endpoint):
    title = 'System Status'
    dashes = (len(title) + 4) * '-'
    print(f"\n{Fore.GREEN}{dashes}\n  {title}  \n{dashes}{Style.RESET_ALL}")
    
    print("\nINFO: Get the current system status or trading mode.")
    
    url = BASE_URL + endpoint
    
    return url