import unittest
from src.advanced_data_structures import ClientDict, ClientMatrix

class TestAdvancedDataStructures(unittest.TestCase):
    def test_client_dict(self):
        dict = ClientDict()
        client = Client('Charlie', 35, 'Chicago')
        dict.add_client(client)
        dict.add_purchase('Charlie', 250)
        self.assertEqual(dict.get_total_purchases('Charlie'), 250)

    def test_client_matrix(self):
        matrix = ClientMatrix()
        client = Client('Alice', 30, 'New York')
        matrix.add_client(client)
        matrix.add_transaction('Alice', 500)
        self.assertEqual(matrix.get_total_transactions('Alice'), 500)

if __name__ == '__main__':
    unittest.main()