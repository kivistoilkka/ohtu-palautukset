import unittest
from statistics import Statistics, SortBy
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_finds_existing_player(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")

    def test_search_returns_none_if_players_is_not_found(self):
        player = self.statistics.search("Selanne")
        self.assertIsNone(player)

    def test_team_finds_correct_players(self):
        correct_list = [
            "Semenko EDM 4 + 12 = 16",
            "Kurri EDM 37 + 53 = 90",
            "Gretzky EDM 35 + 89 = 124"
        ]
        team = self.statistics.team("EDM")
        str_list = list(map(lambda player: str(player), team))
        self.assertListEqual(str_list, correct_list)

    def test_top_finds_correct_players_with_default_sorting_option(self):
        correct_list = [
            "Gretzky EDM 35 + 89 = 124",
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98"
        ]
        top3 = self.statistics.top(3)
        str_list = list(map(lambda player: str(player), top3))
        self.assertListEqual(str_list, correct_list)

    def test_top_finds_correct_players_by_points(self):
        correct_list = [
            "Gretzky EDM 35 + 89 = 124",
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98"
        ]
        top3 = self.statistics.top(3, SortBy.POINTS)
        str_list = list(map(lambda player: str(player), top3))
        self.assertListEqual(str_list, correct_list)

    def test_top_finds_correct_players_by_goals(self):
        correct_list = [
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98",
            "Kurri EDM 37 + 53 = 90"
        ]
        top3 = self.statistics.top(3, SortBy.GOALS)
        str_list = list(map(lambda player: str(player), top3))
        self.assertListEqual(str_list, correct_list)

    def test_top_finds_correct_players_by_assists(self):
        correct_list = [
            "Gretzky EDM 35 + 89 = 124",
            "Yzerman DET 42 + 56 = 98",
            "Lemieux PIT 45 + 54 = 99"
        ]
        top3 = self.statistics.top(3, SortBy.ASSISTS)
        str_list = list(map(lambda player: str(player), top3))
        self.assertListEqual(str_list, correct_list)