class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        players_from = [player for player in self.players if player.nationality == nationality]
        return sorted(players_from, key=lambda x: x.goals + x.assists, reverse=True)