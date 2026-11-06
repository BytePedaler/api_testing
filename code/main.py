from main_deps.api_practice import score_request, score_parsing, roster_request_current, get_vince_dunn
from main_deps.config import TEAMS




def main():
    date = '2024-01-15'
    
    r = score_request("score", date)
    
    print("\nBelow is the status of the GET request:")
    print(r.status_code)
    
    if r.status_code == 200:
        print("Request successful.")
        score_parsing(r)
    elif r.status_code == 404:
        print(f"Error {r.status_code}: Resource not found. Please check for typos in the request.")
    else:
        print(f"Unexpected status code: {r.status_code}")
        
    
    
    #for team in TEAMS:
        #roster_request_current(team)
        
    #get_vince_dunn()
    
    
    
if __name__ == "__main__":
    main()