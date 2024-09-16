"""
User-Defined Classes
Coding Exercise: User-Defined Classes
Sim League
"""

#### ---- SETUP ---- ####

import csv
from team import Team

#### ---- LOAD TEAM DATA ---- ####

with open("./team_history.csv") as file:
    data = csv.reader(file)

    teams = []
    for item in data:
        if item[0] != "name":
            item_team = Team(item[0], item[1], item[2])
            teams.append(item_team)

#### ---- SIMULATE SEASON ---- ####

for team in teams:
    print("Simulating The", str(team.name) + "'s home games. \n")
    for i in range(len(teams)):
        competitor = teams[i]
        if competitor != team:
            team.compete(competitor)
    print("")
    print("Hit enter to see the next match's results")
    input("--------------------------------------------------\n")
#### ---- FINAL RESULTS ---- ####

print("FINAL RESULTS: \n")
for team in teams:
    team.display_record()
