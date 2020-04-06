import unittest.mock
import player


class PlayerTests(unittest.TestCase):

    def test_player(self):
        # Arrange
        expected_outcome = "Name: Gary McTest, Age: 7, Foot: Both, Gender: Male, Playing? False"
        # Act
        actual_outcome = player.player("Gary McTest",7,"Both","Male",False)
        # Assert
        self.assertEqual(expected_outcome,actual_outcome)