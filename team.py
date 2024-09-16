"""
User-Defined Classes
Coding Exercise: User-Defined Classes
Team
"""

import random


#### ---- SIMULATE WINNER ---- ####

def simulate_winner(t1_wins, t1_losses, t2_wins, t2_losses):
    rand_num = random.randint(0, 100)
    t1_win_percent = t1_wins / (t1_losses + t1_wins)
    t2_win_percent = t2_wins / (t2_losses + t2_wins)
    t1_win_chance = int(t1_win_percent * 100 / (t1_win_percent + t2_win_percent))

    ## -- Check if team 1 wins -- ##

    if rand_num < t1_win_chance:
        return True
    else:
        return False


#### ---- TEAM CLASS ---- ####

class Team:

    ## -- Init method -- ##

    def __init__(self, name, wins, losses):
        self.name = name
        self._total_wins = int(wins)
        self._total_losses = int(losses)
        self._season_wins = 0
        self._season_losses = 0

    ## -- Compete against team method -- ##

    def compete(self, competitor):

        ## -- Check winner -- ##

        check_winner = simulate_winner(self._total_wins, self._total_losses, competitor._total_wins,
                                       competitor._total_losses)

        ## -- Display game results -- ##

        if check_winner:
            self._season_wins += 1
            competitor._season_losses += 1
            print(self.name, "VS", competitor.name + ":", self.name, "won!")
        else:
            self._season_losses += 1
            competitor._season_wins += 1
            print(self.name, "VS", competitor.name + ":", competitor.name, "won!")
        self._total_wins += self._season_wins
        self._total_losses += self._season_losses

    ## -- Display season results -- ##

    def display_record(self):
        print(self.name)
        print("WINS:", self._season_wins, "LOSSES:", self._season_losses, "\n")
