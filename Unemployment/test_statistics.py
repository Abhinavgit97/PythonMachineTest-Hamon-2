import unittest
import csv
from statistics_code import  read_data, calculate_statistic

class TestUnemploymentStats(unittest.TestCase):

    def setUp(self):
        # Create a temporary CSV file for testing
        self.temp_csv = 'test_data.csv'
        with open(self.temp_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Entity', 'Year', 'Unemployment'])
            writer.writerow(['CountryA', '2019', '3.5'])
            writer.writerow(['CountryA', '2020', '4.1'])
            writer.writerow(['CountryA', '2021', '3.8'])
            writer.writerow(['CountryB', '2019', '2.5'])
            writer.writerow(['CountryB', '2020', '2.9'])
            writer.writerow(['CountryB', '2021', '3.2'])
            writer.writerow(['CountryB', '2022', '4.5'])

    def tearDown(self):
        # Remove CSV file after test
        import os
        if os.path.exists(self.temp_csv):
            os.remove(self.temp_csv)

    def test_read_data(self):
        # Test read_data function
        data = read_data(self.temp_csv, 'CountryA', None, None)
        self.assertEqual(len(data), 3)
        self.assertEqual(data, [3.5, 4.1, 3.8])

    def test_filter_data_no_data(self):
        # Test filter_data function for no data found
        filtered = read_data(self.temp_csv, 'France', None, None)
        self.assertEqual(filtered, [])

    def test_calculate_statistics_avg(self):
        # Test average unemployment
        data = read_data(self.temp_csv, 'CountryA', None, None)
        result = calculate_statistic(data, 'avg')
        self.assertAlmostEqual(result, 3.8)

    def test_calculate_statistics_min(self):
        # Test minimum unemployment
        data = read_data(self.temp_csv, 'CountryA', None, None)
        result = calculate_statistic(data, 'min')
        self.assertEqual(result, 3.5)

    def test_calculate_statistics_max(self):
        # Test maximum unemployment with two year range
        data = read_data(self.temp_csv, 'CountryB', 2020, 2022)
        result = calculate_statistic(data, 'max')
        self.assertEqual(result, 4.5)


if __name__ == '__main__':
    unittest.main()

