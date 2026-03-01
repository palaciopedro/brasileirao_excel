import requests
from config import API_KEY, API_URL

def get_standings():
    

    response = requests.get(API_URL, headers={"X-Auth-Token": API_KEY})

    data = response.json()
    table = data["standings"][0]["table"]

    teams = []

    for team in table:
        teams.append({
            "Name": team["team"]["shortName"],
            "Points": team["points"]
        })
    
    teams_ordered = sorted(teams, key=lambda x: x["Name"])

    return teams_ordered

