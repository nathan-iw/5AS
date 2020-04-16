import unittest
from unittest.mock import Mock, patch, call
import src.ETL.transform as t
import src.ETL.customer as custo



class TransformTests(unittest.TestCase):
    print("Transform tests running...")

    def test_title_breaker(self):
        # arrange
        title_mctest = "miss. teri person"
        expected = ("Miss", "Teri", "Person")
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
    @patch("src.ETL.customer.Customer",return_value=unittest.mock)
    def test_process_customers(self, mock_customer_class, mock_name_breaker):
        # arrange 
        test_list = [[],["Name"],["name1","dob1"],["name2","dob2"]]
        mock_name_breaker.side_effect = [("title1","first1","last1"), (None,"first2","last2")]
        customer_one = Mock(custo.Customer)
        customer_two = Mock(custo.Customer)    
        mock_customer_class.side_effect = [customer_one, customer_two]
        expected = [customer_one, customer_two]

        #act
        actual = t.process_customers(test_list)
        # assert
        self.assertEqual(mock_name_breaker.call_count, 2)
        mock_name_breaker.assert_has_calls([call("name1"), call("name2")])
        self.assertEqual(mock_customer_class.call_count, 2)
        mock_customer_class.assert_has_calls([call("title1","first1","last1"), call(None,"first2","last2")])
        self.assertEqual(expected,actual)


# def process_customers(data):
#     customer_list=[]
#     for row in data:
#         arguments = name_breaker(row[0])
#         new_cust = Customer(arguments)
#         customer_list.append(new_cust)
#     return customer_list


if __name__ == "__main__":
    unittest.main()