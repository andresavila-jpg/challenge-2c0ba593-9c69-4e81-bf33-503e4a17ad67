import unittest
from src.dataframes import load_dataframe, calculate_average_purchases, filter_dataframe, sort_dataframe
import pandas as pd

class TestDataFrames(unittest.TestCase):
    def test_load_dataframe(self):
        df = load_dataframe('data/clients_complex.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_calculate_average_purchases(self):
        df = load_dataframe('data/clients_complex.csv')
        average = calculate_average_purchases(df)
        self.assertAlmostEqual(average, 200.0)

    def test_filter_dataframe(self):
        df = load_dataframe('data/clients_complex.csv')
        filtered = filter_dataframe(df, 'name', 'Alice')
        self.assertEqual(filtered.shape[0], 1)

    def test_sort_dataframe(self):
        df = load_dataframe('data/clients_complex.csv')
        sorted_df = sort_dataframe(df, 'name')
        self.assertEqual(sorted_df.iloc[0].name, 'Alice')

if __name__ == '__main__':
    unittest.main()