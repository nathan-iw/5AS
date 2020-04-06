import unittest.mock
import player


class PlayerTests(unittest.TestCase):

    def test_player_unable_to_play(self):
        # Arrange
        expected_outcome = "Gary McTest is male, age 7, both-footed and currently unable to play."
        # Act
        actual_outcome = player.player("Gary McTest",7,"Both","Male",False)
        # Assert
        self.assertEqual(expected_outcome,actual_outcome)

    def test_player_able_to_play(self):
        # Arrange
        expected_outcome = "Gary McTest is male, age 7, both-footed and currently able to play."
        # Act
        actual_outcome = player.player("Gary McTest",7,"Both","Male",True)
        # Assert
        self.assertEqual(expected_outcome,actual_outcome)