import unittest.mock
from player import Player


class PlayerTests(unittest.TestCase):

    def test_player_unable_to_play(self):
        # Arrange
        expected_outcome = "Gary McTest is male, age 7, both-footed and currently unable to play."
        testy = Player("Gary McTest", 7, "Both", "Male", False)
        # Act
        actual_outcome = testy.get_player_info()
        # Assert
        self.assertEqual(expected_outcome,actual_outcome)

    def test_player_able_to_play(self):
        # Arrange
        expected_outcome = "Gary McTest is male, age 7, both-footed and currently able to play."
        testy = Player("Gary McTest", 7, "Both", "Male", True)
        # Act
        actual_outcome = testy.get_player_info()
        # Assert
        self.assertEqual(expected_outcome,actual_outcome)