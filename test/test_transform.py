import unittest
from unittest.mock import Mock, patch, call
import src.ETL.transform as t
import src.ETL.customer as custo



class TransformTests(unittest.TestCase):
    print("Transform tests running...")

    def test_title_breaker(self):
        # arrange
        title_mctest = "miss. teri o'person-leary"
        expected = ("Miss", "Teri", "O'Person-Leary")
        # act
        actual = t.name_breaker(title_mctest)

        # assert
        self.assertEqual(expected,actual)

    def test_no_title_breaker(self):
        # arrange
        kein_title = " teri person "
        expected = (None, "Teri", "Person")
        # act
        actual = t.name_breaker(kein_title)

        # assert
        self.assertEqual(expected,actual)
        
    
    @patch("src.ETL.transform.name_breaker",return_value=unittest.mock)
    @patch("src.ETL.transform.card_masker",return_value=unittest.mock)
    def test_process_customers(self, mock_card_masker, mock_name_breaker):
        # arrange 
        test_list = [["name1","dob1", "ccn1"],["name2","dob2", "ccn2"]]
        mock_name_breaker.side_effect = [("title1","first1","last1"), (None,"first2","last2")]
        mock_card_masker.side_effect = ["masked_card1", "masked_card2"]
        customer_one = ("title1","first1","last1", "masked_card1")
        customer_two = (None,"first2","last2", "masked_card2")  
        expected = [customer_one, customer_two]

        #act
        actual = t.process_customers(test_list)
        # assert
        self.assertEqual(mock_name_breaker.call_count, 2)
        mock_name_breaker.assert_has_calls([call("name1"), call("name2")])
        self.assertEqual(mock_card_masker.call_count, 2)
        mock_card_masker.assert_has_calls([call("ccn1"), call("ccn2")])
        self.assertEqual(expected,actual)

    
    def test_card_masker(self):
        # arrange 
        test_card = "1234567891234"
        expected = "XXXXXXXXX1234"

        # act
        actual = t.card_masker(test_card)

        #assert
        self.assertEqual(expected, actual)

    def test_short_card_masker(self):
        # arrange 
        test_card = "2345"
        
        expected = "invalid ccn"

        # act
        actual = t.card_masker(test_card)

        #assert
        self.assertEqual(expected, actual)

# def process_customers(data):
#     customer_list=[]
#     for row in data:
#         arguments = name_breaker(row[0])
#         new_cust = Customer(arguments)
#         customer_list.append(new_cust)
#     return customer_list


if __name__ == "__main__":
    unittest.main()