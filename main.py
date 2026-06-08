import requests
import sys

main_url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

def git_trend():
    url = (f"{main_url}&page={sys.argv[1]}")
    
    if response.status_code == 200:
        response = requests.get(url)
        data = response.json()
        return data
    else:
        print("Error: Request failed with status code", response.status_code)
        sys.exit(1)

    