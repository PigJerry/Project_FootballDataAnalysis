import requests
import pandas as pd
API_KEY = "b146c6a3dfd146da9480ae0e15857271"

def get_pl_standings(api_key: str) -> pd.DataFrame:
    url = "https://api.football-data.org/v2/competitions/PL/standings"
    headers = {"X-Auth-Token": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    standings_list = data["standings"][0]["table"]

    df = pd.DataFrame(standings_list)

    df = df[["team", "playedGames", "won", "draw", "lost", "points", "goalDifference"]]
    df.rename(columns={
        "team": "球队",
        "playedGames": "场次",
        "won": "胜", 
        "draw": "平",
        "lost": "负",
        "points": "积分",
        "goalDifference": "净胜球"
    }, inplace=True)

    df["球队"] = df["球队"].apply(lambda x: x["name"])

    return df
