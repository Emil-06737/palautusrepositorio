import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stub = PlayerReaderStub()
        self.players = self.stub.get_players()
        self.player_names = [player.name for player in self.players]
        self.stats = StatisticsService(
            self.stub
        )

    def test_konstruktori_tallentaa_oikeat_pelaajat(self):
        received_player_names = [player.name for player in self.stats._players]
        self.assertEqual(received_player_names, self.player_names)

    def test_search_palauttaa_oikean_pelaajan(self):
        self.assertEqual(self.stats.search("Kurri").name, self.players[2].name)

    def test_search_palauttaa_None_kun_pelaajaa_ei_loydy(self):
        self.assertEqual(self.stats.search("abc"), None)

    def test_team_palauttaa_oikeat_pelaajat(self):
        received_names = [player.name for player in self.stats.team("EDM")]
        EDM_players = [self.players[0].name, self.players[2].name, self.players[4].name]
        self.assertEqual(received_names, EDM_players)

    def test_team_palauttaa_tyhjan_listan_kun_pelaajia_ei_loydy(self):
        self.assertEqual(self.stats.team("HON"), [])

    def test_top_palauttaa_oikean_listan(self):
        received_list = [player.name for player in self.stats.top(4)]
        self.assertEqual(received_list, [self.players[4].name, self.players[1].name, self.players[3].name, self.players[2].name, self.players[0].name])

    def test_top_palauttaa_oikean_listan_kun_valitaan_jarjestys_pisteiden_perusteella(self):
        received_list = [player.name for player in self.stats.top(4, SortBy.POINTS)]
        self.assertEqual(received_list, [self.players[4].name, self.players[1].name, self.players[3].name, self.players[2].name, self.players[0].name])

    def test_top_palauttaa_oikean_listan_kun_valitaan_jarjestys_naalien_perusteella(self):
        received_list = [player.name for player in self.stats.top(4, SortBy.GOALS)]
        self.assertEqual(received_list, [self.players[1].name, self.players[3].name, self.players[2].name, self.players[4].name, self.players[0].name])

    def test_top_palauttaa_oikean_listan_kun_valitaan_jarjestys_syottojen_perusteella(self):
        received_list = [player.name for player in self.stats.top(4, SortBy.ASSISTS)]
        self.assertEqual(received_list, [self.players[4].name, self.players[3].name, self.players[1].name, self.players[2].name, self.players[0].name])