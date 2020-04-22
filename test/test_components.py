import unittest
from unittest.mock import Mock, patch, call
import src.ETL.transform as t

class ComponentTest(unittest.TestCase):

    def test_process_customers(self):
        #arrange
        test_list = [["Ms Isatest Face","1999-02-05", "1234567891234"],["dr. Branchy O'test","2020-01-01", "1234567891234"]] # Passing in a nested list to be a mock for the CSV.
        expected = [('Ms', 'Isatest', 'Face', 21, 'XXXXXXXXX1234'), ('Dr', 'Branchy', "O'Test", 0, 'XXXXXXXXX1234')]
        #act
        actual = t.process_customers(test_list)

        #assert        
        assert actual == expected, f""" actual: {actual}
        expected: {expected}"""    #  persistence.save_to_db(clean_customers)
