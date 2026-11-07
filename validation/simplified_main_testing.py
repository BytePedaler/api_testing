import requests

def score_request(category, date):
    print("\nInitiating GET request:")
    request = requests.get(f'https://api-web.nhle.com/v1/{category}/{date}', allow_redirects=False, timeout=60)


    return request

def score_parsing(r):
    date_data = r.json()
    
    print(type(date_data))
    
    # dictionary, then a list
    print(len(date_data["games"]))


def main():
    date = '2024-01-15'
    
    try:
        r = score_request("score", date)
        r.raise_for_status()
    except requests.exceptions.Timeout as e:
        print(f"The request timed out: {e}")
        return
    except requests.exceptions.ConnectionError as e:
        print(f"Unable to connect to the server: {e}")
        return
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error raised: {e}")
        return
    
    print("\nBelow is the status of the GET request:")
    print(r.status_code)
    
    if r.status_code == 200:
        print("Request successful.")
        score_parsing(r)
    else:
        print(f"Unexpected status code: {r.status_code}")


if __name__ == "__main__":
    main()