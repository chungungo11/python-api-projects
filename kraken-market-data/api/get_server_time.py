from settings import BASE_URL


def get_server_time(endpoint):
    title = 'Server Time'
    dashes = (len(title) + 4) * '-'
    print(f"\n{dashes}\n  {title}  \n{dashes}")
    print("\nINFO: Get the server's time.")
    url = BASE_URL + endpoint
    
    return url