import random
import pprint

class Team:
    def __init__(self, id, name=""):
        self.id = id
        self.name = f"Team_{id}" if name == "" else name
        self.wins = 0
        self.losses = 0
    
    def __repr__(self):
        return f"{self.name}, wins: {self.wins}, losses: {self.losses}"
    
class ByeOpponentTeam(Team):
    def __init__(self, id, name=""):
       super().__init__(id, name)
        

"""Shifts the elements of array right, returns a new array"""
def shift_array(arr, steps):
    shifted_array = []

    for i in range(-1 * steps, len(arr) - steps):
        shifted_array.append(arr[i])

    return shifted_array

num_teams = int(input("Enter number of teams: "))
if num_teams <= 0:
    raise Exception("Must be more than 0 teams")

# Round robin match making, "circle" method
teams = [Team(id) for id in range(1, num_teams + 1)]

# Add a dummy team if there's odd number of teams
# Matches against the dummy team are counted as a "bye" - an automatic wins for the opposing team
if num_teams % 2 != 0:
    teams.append(ByeOpponentTeam(num_teams + 1))

hold_team = teams[0]
rounds = {}

for shift in range(0, len(teams[1:])):
    rotated_teams = shift_array(teams[1:], shift)

    all_teams = [hold_team]
    all_teams.extend(rotated_teams)

    first_half = all_teams[:(len(all_teams) // 2)]
    second_half = all_teams[-1:(len(all_teams) // 2) - 1:-1]
    matchups = list(zip(first_half, second_half))

    rounds[shift] = matchups

print(f"{len(rounds.items())} rounds")
print(f"{len(rounds[0])} match per round")

# Decide each match
for all_matches in rounds.values():
    for match in all_matches:
        team_1, team_2 = match
        
        # 0 - team_1 wins
        # 1 - team_2 wins
        outcome = random.randint(0, 1)

        # Handle "bye" games
        if isinstance(team_1, ByeOpponentTeam) or isinstance(team_2, ByeOpponentTeam):
            if isinstance(team_1, ByeOpponentTeam):
                team_1.losses += 1
                team_2.wins += 1
            else:
                team_1.wins += 1
                team_2.losses += 1
        # Normal game
        else:
            if outcome == 0:
                team_1.wins += 1
                team_2.losses += 1
            else:
                team_1.losses += 1
                team_2.wins += 1

# Sort teams by wins
sorted_teams = sorted(teams, key=lambda team: team.wins, reverse=True)
pprint.pprint(sorted_teams[:5])