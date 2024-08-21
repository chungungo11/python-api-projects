from config import BASE_URL


def get_server_time(endpoint):
    print("\nINFO: Get the server's time.")
    url = BASE_URL + endpoint
    
    return url