import unittest
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

    def test_process_customers(self):
        # arrange [["teri", "01-10-1999"]]
        test_list = [["mr. roy lewis","1922-12-30"],["yvonne peacock","2010-05-23"]]
        expected = [custo.Customer("Mr","Roy","Lewis"),custo.Customer(None,"Yvonne","Peacock")]
        # act
        actual = t.process_customers(test_list)
        # assert
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