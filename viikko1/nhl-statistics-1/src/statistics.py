from enum import Enum
from player_reader import PlayerReader
from player import Player

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def sort_by_points(player: Player):
    return player.points

def sort_by_goals(player: Player):
    return player.goals

def sort_by_assists(player: Player):
    return player.assists

class Statistics:
    def __init__(self, reader: PlayerReader):
        self._players = reader.get_players()

    def search(self, name: str):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name: str):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many: int, sort_by: SortBy = SortBy.POINTS):
        if sort_by == SortBy.GOALS:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_goals
            )
        elif sort_by == SortBy.ASSISTS:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_assists
            )
        else:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_points
            )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
