import requests
import pandas as pd

def get_pl_standings() -> pd.DataFrame:
    url = "https://raw.githubusercontent.com/openfootball/football.json/master/2024-25/en.1.json"
    response = requests.get(url)
    data = response.json()
    matches = data["matches"]

    teams = {}
for m in matches:
        home = m["team1"]
        away = m["team2"]
        score = m.get("score") or {}
        if "ft" not in score:
            continue
        home_goals = score["ft"][0]
        away_goals = score["ft"][1]

        for team in [home, away]:
            if team not in teams:
                teams[team] = {
                    "球队": team, "场次": 0, "胜": 0, "平": 0,
                    "负": 0, "进球": 0, "失球": 0, "积分": 0
                }

        teams[home]["场次"] += 1
        teams[away]["场次"] += 1
        teams[home]["进球"] += home_goals
        teams[home]["失球"] += away_goals
        teams[away]["进球"] += away_goals
        teams[away]["失球"] += home_goals

        if home_goals > away_goals:
            teams[home]["胜"] += 1
            teams[home]["积分"] += 3
            teams[away]["负"] += 1
        elif home_goals < away_goals:
            teams[away]["胜"] += 1
            teams[away]["积分"] += 3
            teams[home]["负"] += 1
        else:
            teams[home]["平"] += 1
            teams[away]["平"] += 1
            teams[home]["积分"] += 1
            teams[away]["积分"] += 1

    df = pd.DataFrame(teams.values())
    df["净胜球"] = df["进球"] - df["失球"]
    df = df[["球队", "场次", "胜", "平", "负", "积分", "净胜球", "失球"]]
    df = df.sort_values("积分", ascending=False).reset_index(drop=True)
    df.insert(0, "排名", range(1, len(df) + 1))
    return df