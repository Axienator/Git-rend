import requests
from datetime import datetime, timedelta
import sys


main_url = "https://api.github.com/search/repositories"

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
            print(f"Fetching data for the last {user_choice}...\n")
        case _:
            print("Error: Invalid time duration. Please choose 'day', 'week', 'month', or 'year'.")
            return

    url = f"{main_url}{time_filter}&per_page={repo_limit}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error: Request failed with status code:", response.status_code)

    if data:
        for repo in data['items']:
            print(f"Repository Name: {repo['name']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"URL: {repo['html_url']}")
            print("-" * 40)
        
git_trend()    

# python main.py trending-repos --duration day --limit 10