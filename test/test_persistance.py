import unittest.mock 
import src.player as player
import src.load as load
import os 

testy = player.Player("Gary McTest", 7, "Both", "Male", False)

class Test_persistance(unittest.TestCase):

    def test_save_load(self):
        # arrange
        filepath = "temp.csv"
        expected_name = "Gary Mctest"
        expected_age = 7
        expected_foot = "Both"
        expected_gender = "Male"
        expected_player = False
        test_list = []
        test_list.append(testy)
        
        # act 
        load.save_player(test_list, filepath)
        actual_output = load.load_players(filepath)

        # assert
        self.assertEqual(expected_name, actual_output[0].name)
        self.assertEqual(expected_age, actual_output[0].age)
        self.assertEqual(expected_foot, actual_output[0].foot)
        self.assertEqual(expected_gender, actual_output[0].gender)
        self.assertEqual(expected_player, actual_output[0].player_status)
        os.remove(filepath)
        