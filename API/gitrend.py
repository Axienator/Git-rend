import requests
from datetime import datetime, timedelta
import sys


main_url = "https://api.github.com/search/repositories"

def git_trend():

    if( 
    len(sys.argv) != 6
    or sys.argv[1] != "trending-repos"
    or sys.argv[2] != "--duration"
    or sys.argv[4] != "--limit"
    ):
        print("Error: Invalid arguments format")
        return
    
    duration = sys.argv[3]
    repo_limit = int(sys.argv[5])

    match duration:
        case "day":
            date_str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        case "week":
            date_str = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        case "month":
            date_str = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        case "year":
            date_str = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
        case _:
            print("Error: Invalid duration value")
            return


    url = f"{main_url}?q=language:python+created:>{date_str}&sort=stars&order=desc&per_page={repo_limit}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error: Request failed with status code:", response.status_code)
        return

    if data:
        for repo in data['items']:
            print(f"Repository Name: {repo['name']}")
            print(f"Username: {repo['owner']['login']}")
            print(f"Stars: {repo['stargazers_count']}")
            print(f"URL: {repo['html_url']}")
            print("-" * 40)
        
git_trend()    

# python main.py trending-repos --duration day --limit 10