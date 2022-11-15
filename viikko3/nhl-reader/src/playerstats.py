class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()
    
    def _point_order(self, player):
        return player.goals+player.assists

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [p for p in self.players if p.nationality == nationality]
        return sorted(filtered_players, key=self._point_order, reverse=True)
