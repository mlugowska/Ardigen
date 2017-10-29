from read_data import read_data_from_csv_into_one_dataframe
import pandas as pd


def process_data(CSV_source):
    dataframe = read_data_from_csv_into_one_dataframe(CSV_source)
    dataframe.groupby(['matching_id']).max()

    dataframe['total_price'] = dataframe['price'] * dataframe['quantity']
    products_max = dataframe.loc[dataframe.groupby(['matching_id'])['total_price'].idxmax()]

    PLN = dataframe[dataframe['currency'] == 'PLN']['price'].mean()
    GBP = dataframe[dataframe['currency'] == 'GBP']['price'].mean()
    EU = dataframe[dataframe['currency'] == 'EU']['price'].mean()
    products_max['avg_price'] = [GBP, PLN, EU]

    new_dataframe = pd.concat(
        [
            products_max['currency'],
            products_max['matching_id'],
            products_max['total_price'],
            products_max['avg_price']
         ],
        axis=1,
        keys=['currency', 'matching_id', 'total_price', 'avg_price']
    )

    new_dataframe.to_csv('top_products.csv', sep='\t')

path = '/home/magdalena/Desktop/Ardigen'
process_data(path)