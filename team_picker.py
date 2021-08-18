from numpy import not_equal
from pandas.core.indexes.api import get_objs_combined_axis
import Fpl
from reset_teams_dict import reset_teams

# %%
teams = {'Arsenal': 0, 'Aston Villa': 0, 'Brentford': 0, 'Brighton': 0, 
         'Burnley': 0, 'Chelsea': 0, 'Crystal Palace': 0, 'Everton': 0,
         'Leeds': 0, 'Leicester': 0, 'Liverpool': 0, 'Man City': 0,
         'Man Utd': 0, 'Newcastle': 0, 'Norwich': 0, 'Southampton': 0,
         'Spurs': 0, 'Watford': 0, 'West Ham': 0, 'Wolves': 0}

# %%
def pick_team(amount, budget=1000):
    """[summary]

    Args:
        amount (int): amount of players to call from the df
        budget (int, optional): Total budget for team. Defaults to 1000.

    Returns:
        list: list of best value players
    """

    global teams
    picked_team = []
    budget = budget
    positions = {'Goalkeeper': 2, 'Defender': 5, 'Midfielder': 5, 'Forward': 3}
    best_value_players = dict(list(top_value.items())[0:amount])
    for player, player_stats in best_value_players.items():
        if (budget >= player_stats[3] and player not in picked_team and
            teams[player_stats[0]] < 3 and positions[player_stats[8]] > 0 and
            player_stats[9] > 10):
            
            picked_team.append(player)
            budget -= player_stats[3]
            teams[player_stats[0]] += 1
            positions[player_stats[8]] -= 1
    print(f"Remaining funds: {budget/10} million")
    return picked_team


team = pick_team(400)
print(team)


teams.update({}.fromkeys(teams,0))

# %%


def get_optimial_team(budget=1000):
    """[Retruns a team with 2 star players and best value players]

    Args:
        budget (int, optional): Total budget for team. Defaults to 1000.

    Returns:
        dict: dictionary of optimal players and important stats for each player
    """

    global teams
    picked_team = {}
    budget = budget
    star_player_count = 0
    positions = {'Goalkeeper': 2, 'Defender': 5, 'Midfielder': 5, 'Forward': 3}
    star_players_dict = dict(list(top_points.items())[0:2])
    best_value_players = dict(list(top_value.items())[0:300])
    for player, player_stats in star_players_dict.items():
        if (budget >= player_stats[3] and player not in picked_team and
            teams[player_stats[0]] < 3 and positions[player_stats[8]] > 0 and
            player_stats[9] > 10) and star_player_count < 3:
            
            picked_team[player] = player_stats
            budget -= player_stats[3]
            teams[player_stats[0]] += 1
            positions[player_stats[8]] -= 1
            star_player_count += 1
            
    else:
        for player, player_stats in best_value_players.items():
            if (budget >= player_stats[3] and player not in picked_team and
                teams[player_stats[0]] < 3 and positions[player_stats[8]] > 0 and
                player_stats[9] > 10):

                picked_team[player] = player_stats
                budget -= player_stats[3]
                teams[player_stats[0]] += 1
                positions[player_stats[8]] -= 1
    print(f"Remaining funds: {budget/10} million")
    return picked_team


team = get_optimial_team()
print("Optimal team: \n")
for player, stats in team.items():
    print(player, stats)

teams.update({}.fromkeys(teams,0))
# %%
