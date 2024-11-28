class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player):
        if player == self.player1:
            self.increase_player1_score()
        elif player == self.player2:
            self.increase_player2_score()

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.stringify_even_score()
        elif self.player1_score > 40 or self.player2_score > 40:
            score = self.stringify_uneven_score_above_forty()
        else:
            score = self.stringify_uneven_score_at_most_forty()

        return score

    def increase_player1_score(self):
        if self.player1_score < 30:
            self.player1_score += 15
        elif self.player1_score == 30:
            self.player1_score += 10
        else:
            self.player1_score += 1

    def increase_player2_score(self):
        if self.player2_score < 30:
            self.player2_score += 15
        elif self.player2_score == 30:
            self.player2_score += 10
        else:
            self.player2_score += 1

    def stringify(self, score):
        if score == 0:
            return "Love"
        if score == 15:
            return "Fifteen"
        if score == 30:
            return "Thirty"
        if score == 40:
            return "Forty"

    def stringify_even_score(self):
        score = ""
        if self.player1_score < 40:
            score = f"{self.stringify(self.player1_score)}-All"
        else:
            score = "Deuce"
        return score

    def stringify_uneven_score_above_forty(self):
        score = ""
        difference = self.player1_score - self.player2_score
        if difference == 1:
            score = "Advantage player1"
        elif difference == -1:
            score = "Advantage player2"
        elif difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def stringify_uneven_score_at_most_forty(self):
        return f"{self.stringify(self.player1_score)}-{self.stringify(self.player2_score)}"
