import unittest
from unittest.mock import Mock, patch, call
import src.ETL.transform as t
import src.ETL.customer as custo

class TransformTests(unittest.TestCase): # Ask Lewis: why is this in the class format?
    print("Transform tests running...")
 
    def test_title_breaker(self): # Testing the title breaker in name_breaker function
        # arrange
        title_mctest = "miss. teri o'person-leary" # a fake person who has a title (miss in this case)|
        expected = ("Miss", "Teri", "O'Person-Leary") # what we expect to see when we put our fake person through the name_breaker function
        # act
        actual = t.name_breaker(title_mctest) # what actually happens when you put fake teri into the function. t references the transform module
        # assert
        self.assertEqual(expected,actual) # assert that the expected and actual results are the same. Self relates to the standardised class method?!?!?!?!

    def test_no_title_breaker(self): # Tests the name breaker when input title = None 
        # arrange
        no_title = " teri person " # input w/o title
        expected = (None, "Teri", "Person") # ecpected output 
        # act
        actual = t.name_breaker(no_title) # the actual result given by the real method and test input. t references the transform module
        # assert
        self.assertEqual(expected,actual) # assert that the expected and actual results are the same.
        

    @patch("src.ETL.transform.age_gen") # Decorator to patch in the mock, starts with the content root finishes and returns a mock age_gen value.
    def test_process_customers_bad_dob(self, mock_age): 
        # arrange 
        test_list = [["name1","dob1", "ccn1"]] # This is the list to be fed into the process customer function
        mock_age.side_effect = ValueError() # Mocked error result for the age_gen function
        expected = [] # in event of the value error (above) the expected list should be empty
        #act
        actual = t.process_customers(test_list) # What is the actual outcome when the actual function is used to process the mocks.
        
        # assert
        mock_age.assert_called_once_with("dob1") #asserting that age_gen has been called with "dob1" and "dob2".
        self.assertEqual(expected,actual) # Asserting whether the expected outcome is equal to the actual outcome aka is it doing what you thought it was.


    # patch as in ripping out the named function and replacing it with a 'patch' of a dummy result.
    @patch("src.ETL.transform.name_breaker", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock name_breaker value.
    @patch("src.ETL.transform.card_masker", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock card_masker value.
    @patch("src.ETL.transform.age_gen", return_value=unittest.mock) # Decorator to patch in the mock, starts with the content root finishes and returns a mock age_gen value.
    def test_process_customers(self, mock_age, mock_card_masker, mock_name_breaker): # can be named anything but must be named in reverse order to the lines above ^^^
        # arrange 
        test_list = [["name1","dob1", "ccn1"],["name2","dob2", "ccn2"]] # Passing in a nested list to be a mock for the CSV.
        mock_name_breaker.side_effect = [("title1","first1","last1"), (None,"first2","last2")] # Mocked specific outcomes of putting the names from test_list through name_breaker
        mock_card_masker.side_effect = ["masked_card1", "masked_card2"] # Mocked specific outcomes of putting the card numbers from test_list through card_masker
        mock_age.side_effect = ["age1","age2"] # Mocked specific outcomes of putting the dobs from test_list through age_gen.
        customer_one = ("title1", "first1", "last1", "age1", "masked_card1") # defining the expected outcomes when the first mock goes through the function
        customer_two = (None,"first2", "last2", "age2", "masked_card2")  # defining the expected outcomes when the second mock goes through the function
        expected = [customer_one, customer_two] # defining the expected outcome when the mocks have gone through the function 

        #act
        actual = t.process_customers(test_list) # What is the actual outcome when the actual function is used to process the mocks.
        
        # assert
        assert mock_name_breaker.call_count == 2 # Alternative line to the one below
        self.assertEqual(mock_name_breaker.call_count, 2) # The amount of times the name_breaker function is called is equal to 2? Can be any number at the end.
        mock_name_breaker.assert_has_calls([call("name1"), call("name2")]) # asserting that name_breaker has been called with "name1" and "name2".
        self.assertEqual(mock_card_masker.call_count, 2) # The amount of times the card_masker function is called is equal to 2? Can be any number at the end.
        mock_card_masker.assert_has_calls([call("ccn1"), call("ccn2")]) # asserting that card_masker has been called with "ccn1" and "ccn2".
        self.assertEqual(mock_age.call_count, 2)# The amount of times the age function is called is equal to 2? Can be any number at the end.
        mock_age.assert_has_calls([call("dob1"), call("dob2")]) #asserting that age_gen has been called with "dob1" and "dob2".
        self.assertEqual(expected,actual) # Asserting whether the expected outcome is equal to the actual outcome aka is it doing what you thought it was.

    
    def test_card_masker(self): # testing the card masker function!
        # arrange 
        test_card = "1234567891234" # a dummy card value - over 4 digits long.
        expected = "XXXXXXXXX1234" # what we expect the result to look like after the function has done the business (X out all the digits apart from the last 4)
        # act
        actual = t.card_masker(test_card) # the actual result given by feeding card_masker our test card 
        #assert
        self.assertEqual(expected, actual) # assert that the expected and actual results are the same
        
    def test_short_card_masker(self):
        # arrange 
        test_card = "2345" # a dummy card value - 4 digits long (i.e. too short)
        expected = "invalid ccn" # what we expect the result to look like after the function has done the business (spit out an error message)
        # act
        actual = t.card_masker(test_card) # the actual result given by feeding card_masker our test card 
        #assert
        self.assertEqual(expected, actual) # assert that the expected and actual results are the same


    def test_age_from_dob(self):
        #arrange
        cust1_dob = "1922-12-30" # dummy dob data
        expected = 97 # expected outcome (age)
        #act
        actual = t.age_gen(cust1_dob) # the actual result given by feeding age_gen our raw dob data
        #assert
        self.assertEqual(expected, actual) # assert that the expected and actual results are the same

    
    def test_age_from_dob_after_bday(self):
        #arrange
        cust1_dob = "1987-04-11"
        expected = 33
        #act
        actual = t.age_gen(cust1_dob)
        #assert
        self.assertEqual(expected, actual)

    def test_age_from_dob_broken_date(self):
        #arrange
        cust1_dob = "2000-14-20"
        # act and assert
        self.assertRaises(ValueError, lambda:t.age_gen(cust1_dob)) 


# def process_customers(data):
#     customer_list=[]
#     for row in data:
#         arguments = name_breaker(row[0])
#         new_cust = Customer(arguments)
#         customer_list.append(new_cust)
#     return customer_list


if __name__ == "__main__":
    unittest.main()