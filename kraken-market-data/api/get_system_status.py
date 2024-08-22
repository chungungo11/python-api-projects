from settings import BASE_URL


def get_system_status(endpoint):
    title = 'System Status'
    dashes = (len(title) + 4) * '-'
    print(f"\n{dashes}\n  {title}  \n{dashes}")
    print("\nINFO: Get the current system status or trading mode.")
    url = BASE_URL + endpoint
    
    return url