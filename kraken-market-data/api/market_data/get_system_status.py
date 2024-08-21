from config import BASE_URL


def get_system_status(endpoint):
    print("\nINFO: Get the current system status or trading mode.")
    url = BASE_URL + endpoint
    
    return url