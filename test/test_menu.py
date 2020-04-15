import unittest.mock
from unittest.mock import Mock, patch
import menu
from player import Player

class TestMenu(unittest.TestCase):

    @patch("builtins.input", return_value=unittest.mock)
    def test_add_player(self, mock_input):
        #Arrange
        mock_input.side_effect = ["Lewis","38","Righty","male","Y"]
        expected_name = "Lewis"
        expected_age = 38
        expected_foot = "Righty"
        expected_gender = "male"
        expected_player_status = True

        #Act
        actual_output = menu.add_player(menu.players)

        #Assert
        self.assertEqual(expected_name, actual_output.name)
        self.assertEqual(expected_age, actual_output.age)
        self.assertEqual(expected_foot, actual_output.foot)
        self.assertEqual(expected_gender, actual_output.gender)
        self.assertEqual(expected_player_status, actual_output.player_status)
        
if __name__ == "__main__":
    unittest.main()