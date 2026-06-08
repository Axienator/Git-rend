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

    user_choice = sys.argv[2]

    if sys.argv[1] != "--duration":
        print("Error: Invalid function, please use --duration followed by 'day', 'week', 'month', or 'year'")
        return

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
        return data
    else:
        print("Error: Request failed with status code:", response.status_code)
        

git_trend()    
