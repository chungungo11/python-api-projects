from main import BASE_URL
from main import get_response

def get_server_status(endpoint):
    print("\nINFO: Get the current system status or trading mode.")
    url = BASE_URL + endpoint
    get_response(url)