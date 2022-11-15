import requests
from player import Player

def point_order(player):
    return player.goals+player.assists

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []
    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games']
        )

        players.append(player)

    fin_players = [p for p in players if p.nationality == "FIN"]
    print("Players from FIN 2021-2022\n")

    for player in sorted(fin_players, key=point_order, reverse=True):
        print(player)

if __name__ == "__main__":
    main()
