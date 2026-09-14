import unittest
from src.data_structures import Client, ClientArray, ClientList

class TestDataStructures(unittest.TestCase):
    def test_client_array(self):
        array = ClientArray()
        client = Client('Alice', 30, 'New York')
        array.add_client(client)
        self.assertEqual(array.find_client_by_name('Alice').name, 'Alice')

    def test_client_list(self):
        list = ClientList()
        client = Client('Bob', 25, 'Los Angeles')
        list.add_client(client)
        self.assertEqual(list.find_client_by_name('Bob').name, 'Bob')

if __name__ == '__main__':
    unittest.main()