import sys
sys.path.append('..')

from unittest import TestCase
import pandas as pd
from pandas.util.testing import assert_frame_equal, assert_dict_equal
from process_data import process_data
from read_data import read_data_from_csv_into_one_dataframe


class DataframeTest(TestCase):

    def setUp(self):
        raw_data_1 = {
            'currency': ['GBP', 'EU', 'PLN', 'GBP', 'EU', 'PLN'],
            'price': [10, 50, 100, 500, 1000, 5000],
            'quantity': [2, 3, 1, 2, 2, 1],
            'matching_id': [1, 3, 2, 3, 2, 1]
        }

        raw_data_2 = {
            'matching_id': [1, 2, 3],
            'top_priced_count': [2, 2, 3]
        }

        dataframe_1 = pd.DataFrame(raw_data_1, columns=['currency', 'price', 'quantity', 'matching_id'])
        dataframe_2 = pd.DataFrame(raw_data_2, columns=['matching_id', 'top_priced_count'])

        dataframe_1.to_csv('test_data_1.csv')
        dataframe_2.to_csv('test_data_2.csv')

        self.TEST_DIR_PATH = '/home/magdalena/SkyGate/Ardigen/tests'

        try:
            self.big_dataframe = read_data_from_csv_into_one_dataframe(self.TEST_DIR_PATH)
        except IOError:
            print('Error: unable to concatenate CSV files')

    def tearDown(self):
        del self.big_dataframe

    def test_process_dataframe(self):
        super(DataframeTest, self).setUp()
        raw_expected_dataframe = {
            'currency': ['PLN', 'EU', 'GBP'],
            'matching_id': [1, 2, 3],
            'total_price': [5000, 2000, 1000],
            'avg_price': [255, 2550, 525]
        }

        expected_dataframe = pd.DataFrame(raw_expected_dataframe, columns=['currency', 'matching_id', 'total_price', 'avg_price'])
        expected_dataframe.to_csv('expected_dataframe.csv', index=False)

        process_data(self.TEST_DIR_PATH)
        processed_data = pd.read_csv('top_products.csv', index_col=False)

        return assert_dict_equal(expected_dataframe.to_dict(), processed_data.to_dict())
