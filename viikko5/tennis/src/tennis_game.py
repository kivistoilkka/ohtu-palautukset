class TennisGame:
    UPPER_LIMIT_OF_FIRST_SERVES = 3

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

    def _check_even_match(self):
        if self.player1['score'] <= TennisGame.UPPER_LIMIT_OF_FIRST_SERVES:
            return self._score_name(self.player1['score'])+"-All"
        return "Deuce"

    def _check_advantage_or_winner(self):
        difference = abs(self.player1['score'] - self.player2['score'])
        leader = max(self.player1, self.player2, key=lambda p: p['score'])
        if difference >= 2:
            return f"Win for {leader['name']}"
        return f"Advantage {leader['name']}"

    def _check_match_in_first_serves(self):
        score = self._score_name(self.player1['score'])
        score += "-" + self._score_name(self.player2['score'])
        return score

    def get_score(self):
        if self.player1['score'] == self.player2['score']:
            return self._check_even_match()
        if max(
            self.player1['score'],
            self.player2['score']
        ) > TennisGame.UPPER_LIMIT_OF_FIRST_SERVES:
            return self._check_advantage_or_winner()
        return self._check_match_in_first_serves()
