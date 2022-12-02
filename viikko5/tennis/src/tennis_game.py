class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = {'name': player1_name, 'score': 0}
        self.player2 = {'name': player2_name, 'score': 0}

    def won_point(self, player_name):
        if player_name == self.player1['name']:
            self.player1['score'] += 1
        elif player_name == self.player2['name']:
            self.player2['score'] += 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1['score'] == self.player2['score']:
            if self.player1['score'] == 0:
                score = "Love-All"
            elif self.player1['score'] == 1:
                score = "Fifteen-All"
            elif self.player1['score'] == 2:
                score = "Thirty-All"
            elif self.player1['score'] == 3:
                score = "Forty-All"
            else:
                score = "Deuce"
        elif self.player1['score'] >= 4 or self.player2['score'] >= 4:
            minus_result = self.player1['score'] - self.player2['score']

            if minus_result == 1:
                score = f"Advantage {self.player1['name']}"
            elif minus_result == -1:
                score = f"Advantage {self.player2['name']}"
            elif minus_result >= 2:
                score = f"Win for {self.player1['name']}"
            else:
                score = f"Win for {self.player2['name']}"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1['score']
                else:
                    score = score + "-"
                    temp_score = self.player2['score']

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
