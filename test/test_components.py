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
        expected: {expected}"""

    # def process_customers(data):
    # customer_list=[]
    # for row in data:
    #     if len(row) == 0 or row[0] == "Name": # check for empty rows or rows indicating table headers 
    #         continue # if the above is the case skips that row 
    #     try:
    #         age = age_gen(row[1]) # try to generate an age from the DOB 
    #     except ValueError: # if that fails gives a value error
    #         continue # then skips that row
    #     title, first_name, last_name = name_breaker(row[0]) # assigning the values in the tuple
    #     customer_tuple = (title, first_name, last_name, age, card_masker(row[-1])) # making a new tuple with the age and masked ccn
    #     customer_list.append(customer_tuple) # appending aforementioned tuple to the customer_list
    # return customer_list # returns list 