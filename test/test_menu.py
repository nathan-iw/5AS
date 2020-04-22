import unittest.mock
from unittest.mock import Mock, patch
import menu
from menu import App
from src.player import Player
from src.ETL.persistence import Database

class TestMenu(unittest.TestCase):

    @patch("builtins.input", return_value=unittest.mock)
    def test_add_player(self, mock_input):
        #Arrange
        app = App("Fake DB")
        mock_input.side_effect = ["Lewis","38","Righty","male","Y"]
        expected_name = "Lewis"
        expected_age = 38
        expected_foot = "Righty"
        expected_gender = "male"
        expected_player_status = True


        #Act
        actual_output = app.add_player(menu.players)

        #Assert
        self.assertEqual(expected_name, actual_output.name)
        self.assertEqual(expected_age, actual_output.age)
        self.assertEqual(expected_foot, actual_output.foot)
        self.assertEqual(expected_gender, actual_output.gender)
        self.assertEqual(expected_player_status, actual_output.player_status)
    
class IntegrationTest(unittest.TestCase):


    def test_save_csv_customers(self):
        #Arrange
        db = Mock(Database)
        app = App(db)
        #Act
        app.save_csv_customers(db,"test/test.csv")
        #Assert
        db.save_to_db.assert_called_once_with([('Mr', 'Roy', 'Lewis', 97, 'XXXXXXXX0802')])

# def save_csv_customers(csv_file):
#     dirty_customers = extract.csv_load(csv_file)
#     clean_customers = transform.process_customers(dirty_customers)
#     db.save_to_db(clean_customers)

if __name__ == "__main__":
    
    unittest.main()