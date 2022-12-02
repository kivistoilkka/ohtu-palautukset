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

    def _check_advantage_or_winner(self):
        difference = abs(self.player1['score'] - self.player2['score'])
        leader = max(self.player1, self.player2, key=lambda p: p['score'])
        if difference >= 2:
            return f"Win for {leader['name']}"
        return f"Advantage {leader['name']}"

    def get_score(self):
        if self.player1['score'] == self.player2['score']:
            if self.player1['score'] < 4:
                return self._score_name(self.player1['score'])+"-All"
            return "Deuce"

        if max(self.player1['score'], self.player2['score']) >= 4:
            return self._check_advantage_or_winner()

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
