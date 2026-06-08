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
    url = (f"{main_url}")
    response = requests.get(url)


    user_choice = sys.argv[2]
    match user_choice:
        case "day":
            print("Day")
        case "week":
            print("Week")
        case "month":
            print("Month")
        case "year":
            print("Year")
 
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: Request failed with status code:", response.status_code)
        

git_trend()    