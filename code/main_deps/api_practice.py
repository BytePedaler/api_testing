import requests


def score_request(category, date):
    print("\nInitiating GET request:")
    request = requests.get(f'https://api-web.nhle.com/v1/{category}/{date}', allow_redirects=False, timeout=60)


    return request


def score_parsing(r):
    date_data = r.json()
    # dictionary, then a list
    print(len(date_data["games"]))

    
def roster_request_current(team):
    print("\nInitiating GET request:")
    # /current is a redirect to 20262027, or whatever the current is so you either have to put the date in or allow redirects
    r = requests.get(f'https://api-web.nhle.com/v1/roster/{team}/current', allow_redirects=True, timeout=1)
    
    r.raise_for_status()
    
    print("\nBelow is the status of the GET request:")
    print(r.status_code)

    return r


def get_vince_dunn():
    print("\nInitiating GET request for specific player:")
    # /current is a redirect to 20262027, or whatever the current is so you either have to put the date in or allow redirects
    r = requests.get(f'https://api-web.nhle.com/v1/roster/SEA/current', allow_redirects=True, timeout=1)
    
    r.raise_for_status()
    
    player_data = r.json()
    
    print(player_data["defensemen"])
    print(player_data["defensemen"][0])
    print(player_data["defensemen"][0]["firstName"])
    
    
    is_this_vince = f"{player_data["defensemen"][0]["firstName"]["default"]} {player_data["defensemen"][1]["lastName"]["default"]}"
    
    print("\nExpecting: Vince Dunn")
    print(f"\nExtracting: {is_this_vince}")

    