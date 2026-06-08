import requests
import sys


main_url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

def git_trend():

    duration = {
        "day": "&since=day",
        "week": "&since=weekly",
        "month": "&since=monthly",
        "year": "&since=yearly"
    }

    if len(sys.argv) != 6 or sys.argv[1] != "trending-repos" or sys.argv[2] != "--duration" or sys.argv[4] != "--limit":
        print("Error: Invalid function call. Please use --duration followed by 'day', 'week', 'month', or 'year' and --limit followed by a number.")
        return

    user_choice = sys.argv[3]
    repo_limit = sys.argv[5]

    match user_choice:
        case "day" | "week" | "month" | "year":
            time_filter = duration[user_choice]
            print(f"Fetching data for the last {user_choice}...")
        case _:
            print("Error: Invalid time duration. Please choose 'day', 'week', 'month', or 'year'.")
            return

    url = f"{main_url}{time_filter}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)  
    else:
        print("Error: Request failed with status code:", response.status_code)
        
git_trend()    

# python main.py trending-repos --duration day --limit 10