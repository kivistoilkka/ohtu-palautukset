class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = {'name': player1_name, 'score': 0}
        self.player2 = {'name': player2_name, 'score': 0}

    def won_point(self, player_name):
        if player_name == self.player1['name']:
            self.player1['score'] += 1
        elif player_name == self.player2['name']:
            self.player2['score'] += 1

    def _score_name(self, score):
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        if score == 3:
            return "Forty"

    def get_score(self):
        if self.player1['score'] == self.player2['score']:
            if self.player1['score'] < 4:
                return self._score_name(self.player1['score'])+"-All"
            else:
                return "Deuce"
        elif self.player1['score'] >= 4 or self.player2['score'] >= 4:
            minus_result = self.player1['score'] - self.player2['score']

            if minus_result == 1:
                return f"Advantage {self.player1['name']}"
            elif minus_result == -1:
                return f"Advantage {self.player2['name']}"
            elif minus_result >= 2:
                return f"Win for {self.player1['name']}"
            else:
                return f"Win for {self.player2['name']}"
        else:
            score = ""
            temp_score = 0
            for i in range(0, 2):
                if i == 0:
                    temp_score = self.player1['score']
                else:
                    score = score + "-"
                    temp_score = self.player2['score']
                score += self._score_name(temp_score)
            return score
