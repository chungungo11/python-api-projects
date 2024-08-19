from main import BASE_URL
from main import get_response

def get_server_time(endpoint):
    print("\nINFO: Get the server's time.")
    url = BASE_URL + endpoint
    get_response(url)