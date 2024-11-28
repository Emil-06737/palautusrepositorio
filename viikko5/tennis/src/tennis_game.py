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

        if self.game_is_tied():
            score = self.stringify_tied_score()
        elif self.at_least_one_player_has_above_forty():
            score = self.stringify_nontied_score_above_forty()
        else:
            score = self.stringify_nontied_score_at_most_forty()

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

    def game_is_tied(self):
        return self.player1_score == self.player2_score

    def at_least_one_player_has_above_forty(self):
        return self.player1_score > 40 or self.player2_score > 40

    def stringify_tied_score(self):
        score = ""
        if self.player1_score < 40:
            score = f"{self.stringify_individual_score(self.player1_score)}-All"
        else:
            score = "Deuce"
        return score

    def stringify_nontied_score_above_forty(self):
        score = ""
        difference = self.player1_score - self.player2_score
        if difference == 1:
            score = f"Advantage {self.player1}"
        elif difference == -1:
            score = f"Advantage {self.player2}"
        elif difference >= 2:
            score = f"Win for {self.player1}"
        else:
            score = f"Win for {self.player2}"
        return score

    def stringify_nontied_score_at_most_forty(self):
        return f"{self.stringify_individual_score(self.player1_score)}-{self.stringify_individual_score(self.player2_score)}"

    def stringify_individual_score(self, score):
        if score == 0:
            return "Love"
        if score == 15:
            return "Fifteen"
        if score == 30:
            return "Thirty"
        if score == 40:
            return "Forty"
